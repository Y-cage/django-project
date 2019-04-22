/*
function Banner() {
  //相当于python中的__init__方法
  console.log('init');
  this.person= 'zhidao';
}
//原型琏
Banner.prototype.greet = function() {
  console.log("hello world");
}

var banner = new Banner();

console.log(banner.person);
banner.greet();
*/

function Banner(){
  this.bannerGroup = $('#banner-group');
  this.index = 0;
 // this.listenBannerHover();
  this.bannerUl = $('banner-Ul');
 // this.liList = this.bannerUl.children("li");
  //this.bannerCount = this.liList.length;
}
/*
Banner.prototype.toggleArrow = function(isShow){
  if (isShow){
    $('.left-arrow').show();
    $('.right-arrow').show();
  }else{
    $('.left-arrow').hide();
    $('.right-arrow').hide();
  }
};
*/

Banner.prototype.listenBannerHover = function(){
    var self = this;
    this.bannerGroup.hover(function(){
      //第一个函数是把鼠标移动到banner上会执行的函数
      clearInterval(self.timer);
      //self.toggleArrow(true);
    },function(){
      //第二个函数是把鼠标从banner上移走会执行的函数
      self.loop();
      //self.toggleArrow(false);
    });
};

Banner.prototype.loop = function(){
  var self = this;
  var bannerUl = $('#banner-ul');
  var index = 0;
  this.timer = setInterval(function(){
    if (self.index>=3){
      self.index = 0;
    }else{
      self.index++;
    }
    bannerUl.animate({'left':-770*self.index},500);
  },2000);
};
/*
Banner.prototype.listenArrowClick = function(){
  var self = this;

  self.leftArrow.click(function(){
    if(self.index === 0){
      self.index = self.bannerCount - 1;
    }else{
      self.index--;
    }
    self.bannerUl.animate({"left":-770*self.index},500);
  });

  self.rightArrow.click(function(){
    if(self.index === self.bannerCount - 1){
      self.index = 0;
    }else{
      self.index++;
    }
    self.bannerUl.animate({"left":-770*self.index},500);
  })
};
*/

Banner.prototype.run = function(){
  this.loop();
  //this.listenArrowClick();
};

function Index(){
  var self = this;
  self.page = 2;
  self.categroy_id = 0;
  self.loadBtn = $('#load-more-btn');
}
Index.prototype.listenLoadMoreEvent = function(){
    var self = this;
    var loadBtn = $('#load-more-btn');
    loadBtn.click(function () {
      $.ajax({
        type: 'GET',
        url: '/news/list/',
        data:{
          'p':self.page,
          'category_id': self.categroy_id
        },
        success:function (result) {
          if(result['code'] === 200){
            var newses = result['data'];
            if(newses.length > 0){
                var tpl = template('news-item',{'newses':newses});
                var ul = $('.list-inner-group');
                ul.append(tpl);
                self.page += 1;
              }else{
              loadBtn.hide();
            }

          }
        }
      })

    })

};

Index.prototype.listenCategorySwitchEvent = function(){
  var self = this;
  var tabGroup = $('.list-tab');
  tabGroup.children().click(function () {
      //this代表当前选中的li
      var li = $(this);
      var category_id = li.attr('data-category');
      var page = 1;
      $.ajax({
        type:'GET',
        url:'/news/list/',
        data:{
          'category_id': category_id,
          'p':page,

        },
        success:function (result) {
          if(result['code'] === 200){
            var newses = result['data'];
            var tp1 = template('news-item',{'newses':newses});
            //empty:可以将这个标签下的所有子元素都删掉
            var newsListGroup = $('.list-inner-group');
            newsListGroup.empty();
            newsListGroup.append(tp1);
            self.page = 2;
            self.categroy_id = category_id;
            li.addClass('active').siblings().removeClass('active');
            self.loadBtn.show();
          }
        }
      })
  });
};

Index.prototype.run = function(){
  var self = this;
  self.listenLoadMoreEvent();
  self.listenCategorySwitchEvent();
};

$(function(){
  //等文档加载完毕才执行里面的
  var banner = new Banner();
  banner.run();

  var index = new Index();
  index.run()
});

