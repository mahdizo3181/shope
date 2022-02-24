    $(document).on("click touchend", ".lblcheckbox,.lblcheckbox .checkmark", function () {
    var self = $(this);
    // console.log(self)
    var pp = self.parents('li');
    var title = pp.find('label').text();
    var dataId = pp.attr('data-id');
    var list = $('.c-listing-options__labels ul');

    var dd = list.find('li[data-id=' + dataId + ']');
    var lenItem = dd.length;
    $('.c-listing-options-labels').css('display', 'block')

    // console.log(lenItem)

    if (lenItem > 0) {
        dd.remove();
    } else {
        var item = '   <li class="dddw" data-id="' + dataId + '" >' +
            '                                                <div class="c-listing-options__label">' +
            '                                                    <button class="js-listing-option-remove" type="button" data-key="brand" data-value="82" onclick="removeItem(this)"></button>' +
            '                                                    <span>' + title + ' </span>' +
            '                                                </div>' +
            '                                            </li>';
        list.append(item);
    }


})


$('.js-listing-options-clear').click(function () {
    var checked = $(this).is(":checked");
    if (!checked) {
        $('.dddw').remove();
        $(".checkboxUl li input").each(function () {
            $(this).prop("checked", false);
        });
    }
    $('.c-listing-options-labels').css('display', 'none')

});


function removeItem(i) {
    var pppp = $(i).parents('li');
    // console.log(pppp)
    pppp.remove();
    var idd = pppp.attr('data-id');
    console.log(idd);
    $('.checkboxUl li[data-id=' + idd + ']').find('input').prop("checked", false);
    console.log($('.c-listing-options__labels ul li').length)
    if ($('.c-listing-options__labels ul li').length == 0) {
        $('.c-listing-options-labels').css('display', 'none')
    }
}