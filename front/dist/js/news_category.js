function NewsCategory() {

};

NewsCategory.prototype.run = function () {
    var self = this;
    self.listenAddCategoryEvent();
    self.listenEditCategoryEvent();
    self.listenDeleteCategoryEvent();
};


$(function () {
    var category = new NewsCategory();
    category.run();
});

NewsCategory.prototype.listenAddCategoryEvent = function(){
    var addBtn = $('#add-btn');
    addBtn.click(function () {
        var name = prompt('请输入分类名字');
         if (name!=null){
             $.post(
                 '/cms/add_news_category/',
                 {
                 'name':name
             });
         }
         location.reload();
    })
};

NewsCategory.prototype.listenEditCategoryEvent = function(){
    var self = this;
    var editBtn = $(".edit-btn");
    editBtn.click(function () {
        var currentBtn = $(this);
        var tr = currentBtn.parent().parent();
        var pk = tr.attr('data-pk');
        var name = tr.attr('data-name');
        var edit = prompt('您当前的分类:' + name);

        $.post('/cms/edit_news_category/',
            {'pk' : pk,  'name': edit},
            function (data,status) {
                alert('haha');
            }
        );
    });
}
NewsCategory.prototype.listenDeleteCategoryEvent = function(){
        var deleteBtn = $('.delete-btn');
        deleteBtn.click(
            function () {
                var currentBtn = $(this);
                var tr = currentBtn.parent().parent();
                var pk = tr.attr('data-pk');
                var delete_data = prompt('输入要删除的数据：')
                $.post('/cms/delete_news_category/',{
                    'pk':pk,
                    name:delete_data
                });
                location.reload();
            }
        );
};



/*function f() {
    swal({
            title: "输入！",
            text: "输入一些有趣的话：",
            type: "input",
            showCancelButton: true,
            closeOnConfirm: false,
            animation: "slide-from-top",
            inputPlaceholder: "输入一些话"
        },
        function (inputValue) {
            if (inputValue === false)
                return false;

            if (inputValue === "") {
                swal.showInputError("你需要输入一些话！");
                return false
            }

            swal("非常好！", "你输入了：" + inputValue, "success");
        });

}*/
