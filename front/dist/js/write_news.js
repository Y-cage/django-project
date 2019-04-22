
function News() {

}


News.prototype.run = function () {
    var self = this;
    self.listenUploadFileEvent();
    self.listenSubmitEvent();
};

$(function (){
    var news = new News();
    news.run();
});

News.prototype.listenUploadFileEvent = function (){
    var uploadBtn = $('#thumbnail-btn');
    uploadBtn.change(function () {
       var file = uploadBtn[0].files[0];    //取到第一个uploadBtn按钮，的所有文件的第一个文件
       var formData = new FormData(); //文件存储在FormData中
       formData.append('file',file); //字段名
       $.ajax({
           type: 'POST',
           url:'/cms/upload_file/',
           data:formData,
           contentType: false, //默认使用文件形式
           processData: false, //不需要jqurey再处理了

           success:function (result) {
               if (result['code'] === 200){
                   var url = result['data']['url'];
                   var thumbnailInput = $('#thumbnail-form');
                   thumbnailInput.val(url);
               }
           }
       });
    });
};

News.prototype.listenSubmitEvent = function() {
    var submitBtn = $('#submit-btn');
    submitBtn.click(function (event) {
        event.preventDefault();

        var btn = $(this);
        var pk = btn.attr('data-news-id');


        var title = $('input[name="title"]').val();
        var category = $('select[name="category"]').val();
        var desc = $('input[name="desc"]').val();
        var thumbnail = $('input[name="thumbnail"]').val();
        var content = $('textarea[name="content"]').val();
        var url = '';

        if(pk){
            url = '/cms/edit_news/';
        }else{
            url = '/cms/write_news/';
        }
        $.ajax({
            type: "POST",
            dataType: "json",
            url: url,
            data: {
                'title':title,
                'category':category,
                'desc':desc,
                'thumbnail':thumbnail,
                'content':content,
                'pk': pk
            },
            success:function (result) {
               if (result['code'] === 200){
                   location.reload();
               }else{

               }
            }
        });

    });
};