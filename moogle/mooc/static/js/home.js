$(document).ready(function() {
    $(".title-bg").height(
        $(window).height() - $("#top-menu").height());

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
    window.click2("input.main-search", "body", 600);
    window.click2(".to.top", ".title-bg", 600, 70);
    window.click2(".to.jptj", "#jptj", 600, 70);
    window.click2(".to.jckc", "#jckc", 600, 70);
    window.click2(".to.gjjj", "#gjjj", 600, 70);

    // fix daohanglan
    $(window).scroll(function() {
        let sc = $(this).scrollTop();
        if(sc > $(window).height() - $("div.daohanglan").height()) {
            $("div.daohanglan").addClass("fixed");
        } else {
            $("div.daohanglan").removeClass("fixed");
        }
    });

});