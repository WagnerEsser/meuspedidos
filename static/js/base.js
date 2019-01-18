$(document).ready(function () {

    // ===== MÁSCARAS ===== //
    $('.valor input').mask('00000000000000000,00', {reverse: true});
    $('.somente_numeros input').mask('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', {placeholder: 'Somente números'});

    // ===== ESTILIZAR DROPDOWNS ===== //
    $('select').dropdown();

    $('.ui.dropdown').dropdown();
});
