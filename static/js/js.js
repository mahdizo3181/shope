var slideIndex = 1;
var pt;
var items;
slideShow(slideIndex);

function slideShow(n) {
    // console.log('n = ' + n);
    var slides = $('.slide').toArray();
    if (n > slides.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length;
    }
    // console.log('slideIndex  = ' + slideIndex);
    $('.slide').css('display', 'none');
    $(slides[slideIndex - 1]).css('display', 'flex');
    progressbar(slideIndex - 1);
    return slideIndex

}

function move(n) {
    clearInterval(pt);
    items[slideIndex - 1].style.width = '0%';
    slideIndex = slideIndex + n;
    slideShow(slideIndex);

}

function progressbar(slideId) {
    items = document.getElementsByClassName('item-inner');
    var width = 0;
    pt = setInterval(frame, 30);

    function frame() {
        if (width >= 100) {
            clearInterval(pt);
            items[slideId].style.width = '0%';
            slideIndex++;
            slideIndex = slideShow(slideIndex);
        } else {
            width++;
            items[slideId].style.width = width + '%';
        }
    }


}

var lenPdSlide = $('.pdSlide').length
$('.numbertext2').text(lenPdSlide);
// console.log(lenPdSlide)
$('.pdSlide').click(function () {
    var ddd = $(this).find('img').attr('src');
    $('.modal .modal-gallery').attr('src', ddd);
})
for (var i = 0; i < lenPdSlide; i++) {
    var imgPdslide = $('.pdSlide').find('img').eq(i).attr('src');
    var imgsPdSlide = '<div class="gallery-slide-item"><img class="demo" onclick="currentSlide(' + (i + 1) + ')" src="' + imgPdslide + '"></div>';
    $('.gallery-slide').append(imgsPdSlide);
}

var slideIndex2 = 1;
showSlides(slideIndex2);

function plusSlides(n) {
    showSlides(slideIndex2 += n);
}

function currentSlide(n) {
    showSlides(slideIndex2 = n);
}


function showSlides(n) {
    var i;
    var slides2 = $('.pdSlide').toArray();
    var dots = $('.demo').toArray();
    if (n > slides2.length) {
        slideIndex2 = 1
    }
    if (n < 1) {
        slideIndex2 = slides2.length
    }
    $('.pdSlide').css('display', 'none');
    $(slides2[slideIndex2 - 1]).css('display', 'flex');
    $(dots).removeClass('active');
    $(dots[slideIndex2 - 1]).addClass('active');
    $('.numbertext').text(slideIndex2);
}

var dropDownMenu = $('.dropdown-menu');
var dropDownMenuParent = dropDownMenu.parent();
$('.mini-basket__icon').on('click', function () {

    $('.login-register .dropdown-menu').removeClass('is-active');
    $('.mini-basket .dropdown-menu').toggleClass('is-active');
})
$('.login-register').on('click', function () {
    $('.mini-basket .dropdown-menu').removeClass('is-active');
    $('.login-register .dropdown-menu').toggleClass('is-active');
})
$(document).on('click', function (event) {

    if (!$(event.target).closest('.mini-basket__icon, .login-register__icon').length && !$(event.target).closest('.dropdown-menu').length) {
        $('.dropdown-menu').removeClass('is-active');
    }

    if (!$(event.target).closest('.navbar').length && !$(event.target).closest('.navbar-nav').length) {
        $(".navbar-nav").removeClass("is-active");
        $(".overlay").removeClass("is-active");
    }

})
$('.nav-icon').on('click', function () {
    $(this).toggleClass('is-active')
    $('.navbar-nav').toggleClass('is-active')
    $('.overlay').toggleClass('is-active')
})
$(window).scroll(function () {
    if ($(this).scrollTop() >= 200) {
        $('.scrollToTop').fadeIn()
        // $('.navbar').addClass('sticky');
    } else {
        $('.scrollToTop').fadeOut()
        // $('.navbar').removeClass('sticky');

    }
})
$(".scrollToTop").on("click", function () {
    $("html,body").animate({
        scrollTop: 0
    }, 800);
})
$(document).ready(function () {
// Swiper: Slider
    $('.slider').each(function () {
        var swiper = $(this).find('.swiper-container');
        // console.log(swiper);
        var cbox = $(this).find('.c-box');
        var swiper_button_next = cbox.next();
        var swiper_button_prev = swiper_button_next.next();
        new Swiper(swiper, {
            loop: false,
            nextButton: swiper_button_next,
            prevButton: swiper_button_prev,
            slidesPerView: 4,
            paginationClickable: true,
            spaceBetween: 20,
            breakpoints: {
                1920: {
                    slidesPerView: 4,
                    spaceBetween: 30
                },
                1028: {
                    slidesPerView: 3,
                    spaceBetween: 30
                },
                768: {
                    slidesPerView: 2,
                    spaceBetween: 10
                }, 480: {
                    slidesPerView: 1,
                    spaceBetween: 10
                }
            }
        });
    })
});

//plc-dropdown
// $('.plc-dropdown').each(function () {
//     // console.log($(this))
//     var PlcdropDown = $(this);
//     var plcplaceHoler = PlcdropDown.find('span');
//     var plcOptions = PlcdropDown.find('.plc-drop li');
//     var valOptions = plcOptions[0].innerText;
//     plcplaceHoler.text(valOptions)
//     var dataName;
//     // console.log(PlcdropDown.find('.plc-drop li').text())
//     PlcdropDown.find('.plc-drop li').each(function (index) {
//         // console.log(index)
//         // console.log($(this))
//         // console.log($(this).text())
//         var liText = $(this).text();
//         console.log(liText)
//         // $(this).eq(index).attr('data-name', liText);
//         // $('.product-left-container select').append("<option value='" + d3d.dataset.name + "'>" + d3d.innerText + "</option>");
//         $('.product-left-container select').append("<option value='" + liText + "'>" + liText + "</option>");
//
//     })
//
//
//     PlcdropDown.click(function (e) {
//         e.preventDefault();
//         e.stopPropagation();
//         $(this).toggleClass('active');
//     })
//
//     plcOptions.on('click', function () {
//         var opt = $(this);
//         var valOptions = opt.text();
//         // console.log(valOptions);
//         plcplaceHoler.text(valOptions);
//         opt.siblings().removeClass('is-active selected')
//         opt.filter(':contains("' + valOptions + '")').addClass('is-active selected');
//         dataName = opt.data('name');
//         // console.log(dataName)
//         $('.product-left-container select option').removeAttr('selected');
//         var ddd = $('.product-left-container').find('option[value=' + dataName + ']').attr('selected', 'selected').trigger("change");
//         // console.log(ddd);
//
//     });
//
// })
function create_custom_dropdowns() {
    $('select').each(function (i, select) {
        if (!$(this).next().hasClass('dropdown-select')) {
            $(this).after('<div class="dropdown-select wide ' + ($(this).attr('class') || '') + '" tabindex="0"><span class="current"></span><div class="list"><ul></ul></div></div>');
            var dropdown = $(this).next();
            var options = $(select).find('option');
            var selected = $(this).find('option:selected');
            dropdown.find('.current').html(selected.data('display-text') || selected.text());
            options.each(function (j, o) {
                var display = $(o).data('display-text') || '';
                dropdown.find('ul').append('<li class="option ' + ($(o).is(':selected') ? 'selected' : '') + '" data-value="' + $(o).val() + '" data-display-text="' + display + '">' + $(o).text() + '</li>');
            });
        }
    });

    $('.dropdown-select ul').before('<div class="dd-search"><input id="txtSearchValue" autocomplete="off" onkeyup="filter()" class="dd-searchbox" type="text"></div>');
}

$(document).on('click', '.dropdown-select', function (event) {
    if ($(event.target).hasClass('dd-searchbox')) {
        return;
    }
    $('.dropdown-select').not($(this)).removeClass('open');
    $(this).toggleClass('open');
    if ($(this).hasClass('open')) {
        $(this).find('.option').attr('tabindex', 0);
        $(this).find('.selected').focus();
    } else {
        $(this).find('.option').removeAttr('tabindex');
        $(this).focus();
    }
});

$(document).on('click', function (event) {
    if ($(event.target).closest('.dropdown-select').length === 0) {
        $('.dropdown-select').removeClass('open');
        $('.dropdown-select .option').removeAttr('tabindex');
    }
    event.stopPropagation();
});

function filter() {
    var valThis = $('#txtSearchValue').val();
    $('.dropdown-select ul > li').each(function () {
        var text = $(this).text();
        (text.toLowerCase().indexOf(valThis.toLowerCase()) > -1) ? $(this).show() : $(this).hide();
    });
};

$(document).on('click', '.dropdown-select .option', function (event) {
    $(this).closest('.list').find('.selected').removeClass('selected');
    $(this).addClass('selected');
    var text = $(this).data('display-text') || $(this).text();
    $(this).closest('.dropdown-select').find('.current').text(text);
    $(this).closest('.dropdown-select').prev('select').val($(this).data('value')).trigger('change');
});

$(document).on('keydown', '.dropdown-select', function (event) {
    var focused_option = $($(this).find('.list .option:focus')[0] || $(this).find('.list .option.selected')[0]);
    if (event.keyCode == 13) {
        if ($(this).hasClass('open')) {
            focused_option.trigger('click');
        } else {
            $(this).trigger('click');
        }
        return false;
        // Down
    } else if (event.keyCode == 40) {
        if (!$(this).hasClass('open')) {
            $(this).trigger('click');
        } else {
            focused_option.next().focus();
        }
        return false;
        // Up
    } else if (event.keyCode == 38) {
        if (!$(this).hasClass('open')) {
            $(this).trigger('click');
        } else {
            var focused_option = $($(this).find('.list .option:focus')[0] || $(this).find('.list .option.selected')[0]);
            focused_option.prev().focus();
        }
        return false;
        // Esc
    } else if (event.keyCode == 27) {
        if ($(this).hasClass('open')) {
            $(this).trigger('click');
        }
        return false;
    }
});

    create_custom_dropdowns();

$('.product-add-fav').click(function () {
    $(this).toggleClass('is-active');
})
$('.tab-items a').click(function () {

    // console.log(position)
    // console.log(width)
    // alert(index)
    $(".tab-items a").removeClass("active")
    $(this).addClass("active");
    var index = $(this).index();
    // console.log(index)

    $(".tab-sections > section").hide();
    $(".tab-sections > section").eq(index).show();
})

$(document).ready(function(){
    $('.reply-to-comment[href^="#"]').on('click',function (e) {
        e.preventDefault();
        var target = this.hash;
        var $target = $(target);
        $('html, body').stop().animate({
            'scrollTop': $target.offset().top
        }, 900, 'swing', function () {
            // window.location.hash = target;
        });
    });
});
$('.js-box-toggle').on('click', function () {

    var cFilter = $(this).parent().find('.js-box-content');
    if ($(this).hasClass('hide')) {
        $(this).removeClass('hide');
        cFilter.slideDown();
    } else {
        $(this).addClass('hide');
        cFilter.slideUp();

    }
})

function removeCartItem(i) {
    console.log(i)
    var cartItems = $(i).parents('.cart-item').remove();;
    // console.log(pppp)

}