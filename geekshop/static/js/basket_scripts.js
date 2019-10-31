"use strict";

// console.log('hello');

window.onload = function () {
    // let inputQuantity;
    
    // inputQuantity = document.querySelector('div.basket_record input[type="number"]');
    // // console.log(inputQuantity);
    // inputQuantity.onchange = function (evt) {
    //     console.log("событие: " + evt)
    //     // console.log("\ttarget: " + evt.target);
    //     console.log("\ttarget: ", evt.target);
    //     console.log("\ttarget.value: ", evt.target.value);
    // };
    $('.basket_list').on('change', 'input[type="number"]', function (evt) {
        let target = evt.target;
        $.ajax({
            url: "/basket/update/" + target.name + "/" + target.value + "/",
            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });
    });
};

