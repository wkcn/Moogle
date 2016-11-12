$(document).ready(function() {
    $(".title-bg").height(
        $(window).height());

    $(".title-bg").backstretch([
        "/static/img/home-bg-0.jpg",
        "/static/img/home-bg-1.jpg"
        ], {
            duration: 3000,
            fade: 750
        });

    $(".ui.row.main-search").css({
        "margin-top": $(".title-bg").height()/2 - 100
    });

    // change position of search input when page scroll
    $(window).scroll(function() {
        let mt = $(".title-bg").height()/2 + $(this).scrollTop()/2.5 - 100;
        if(mt < $(".title-bg").height() - 100) {
            $(".ui.row.main-search").css({
                "margin-top": mt
            });
        }
    });

    //scroll to top when focus input main-search
    $("input.main-search").click(function() {
        window.scroll2("body", 600);
    });

});