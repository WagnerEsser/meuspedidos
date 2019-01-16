$(document).ready(function () {


    // ===== ESTILIZAR DROPDOWNS ===== //
    $('select').dropdown();

    $('.ui.dropdown').dropdown();
});

$('.message .close').on('click', function () {
    window.history.back();
});