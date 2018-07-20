function scrollTop() {
    return Math.max(
        //chrome
        document.body.scrollTop,
        //firefox/IE
        document.documentElement.scrollTop);
}

//获取页面文档的总高度
function documentHeight() {
    //现代浏览器（IE9+和其他浏览器）和IE8的document.body.scrollHeight和document.documentElement.scrollHeight都可以
    return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
}

//获取页面浏览器视口的高度
function windowHeight() {
    //document.compatMode有两个取值。BackCompat：标准兼容模式关闭。CSS1Compat：标准兼容模式开启。
    return (document.compatMode == "CSS1Compat") ?
        document.documentElement.clientHeight :
        document.body.clientHeight;
}

function waterallowData(page) {
    var inRemainCount = 10;
    $('.waterfllow-loading').addClass('active');
    $.ajax({
        url: '/show/getAllTweets/' + page,
        datatype: 'json',
        type: 'get',
        async: false,
        success: function (data) {
            var html = template("temp", data)
            inRemainCount = data.remainCount
            console.log(inRemainCount)
            $('ol').append(html)
            $('.waterfllow-loading').removeClass('active');
        }
    });
    return inRemainCount
}


$(function () {
    var page = 1;
    var remainCount = 1
    if (remainCount > 0){
        remainCount = waterallowData(page);
    }

        $(window).on('scroll', function () {
        if (scrollTop() + windowHeight() >= (documentHeight() - 50/*滚动响应区域高度取50px*/)) {
            if (remainCount > 0){
            page++;
            remainCount = waterallowData(page);
        }
         }
    });

$("#contentImg").click(function () {
    console.log("点击")
    $(this).toggleClass("maxImg");
    // $(this).removeClass("maxImg")
})

})