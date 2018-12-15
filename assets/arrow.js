$(".arrow").on("click", function() {
  $(this).toggleClass("active");
});


$('.filtr-collapse').click(function(){
  $(this).html() == "Méňe" ? $(this).html('Více') : $(this).html('Méňe');
});

$('.text-collapse').click(function(){
  $(this).html() == "Méňe" ? $(this).html('Více') : $(this).html('Méňe');
});
