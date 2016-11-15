$(document).ready(function() {
    $(".title-bg").backstretch("/static/img/home-bg-0.jpg");

    $(".row.title.header").css({
        "margin-top": 125 - $(".row.title.header").height()
    })
})