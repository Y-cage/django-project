function PubCourse() {

}

PubCourse.prototype.listenSubmitEvent = function(){
    var submitBtn = $('#submit-btn');
    submitBtn.click(function () {
        var title = $('#title-input').val();
        var category_id = $('#category-input').val();
        var teacher_id = $('#teacher-input').val();
        var video_url = $('#video-input').val();
        var pict_url = $('#pict-input').val();
        var price = $('#price-input').val();
        var duration = $('#duration-input').val();
        var profile = $('#context-input').val();

        $.ajax({
            type: 'POST',
            url: '/cms/pub_course/',
            data:{
                'title':title,
                'category_id': category_id,
                'teacher_id': teacher_id,
                'video_url':video_url,
                'pict_url': pict_url,
                'price': price,
                'duration': duration,
                'profile':profile
            },
            success:function (result) {
                if(result['code'] === 200){
                    location.reload();
                    console.log('ok')
                }
            }
        })
    })
};


PubCourse.prototype.run = function () {
    this.listenSubmitEvent();
};


$(function () {
   var course = new PubCourse();
   course.run()
});