
function CMSNewsList() {

}

CMSNewsList.prototype.initDatePicker = function() {
      var startPicker = $('#start-picker');
      var endPicker = $('#end-picker');

      var todayDate = new Date();
      var todayStr = todayDate.getFullYear() + '/' + (todayDate.getMonth()) + '/' + todayDate.getDate();

      var options = {
          'showButtonPanel':true,
          'format':'yyyy/mm/dd',
          'startDate':'2017/6/1',
          'endDate':todayStr,
          'language':'zh-CN',
          'todayBtn':'linked',
          'todayHighlight':true,
          'clearBtn':true,
          'autoclose':true
      };
      startPicker.datepicker(options);
      endPicker.datepicker(options);
};

CMSNewsList.prototype.listenDeleteEvent = function(){
    var deleteBtns = $('.delete-btn');
    deleteBtns.click(function () {
        var btn = $(this); //拿到当前这个按钮
        var news_id = btn.attr('data-news-id');
        $.ajax({
            url:'/cms/delete_news/',
            type: 'POST',
            data:{
                'news_id':news_id
            },
            success:function (result) {
                if(result['code'] === 200){
                    location.reload();
                    console.log('good')
                }
            }
        })

    })
};

CMSNewsList.prototype.run = function () {
    this.initDatePicker();
    this.listenDeleteEvent();
};

$(function () {
    var newsList = new CMSNewsList();
    newsList.run();
});