$('.nav-link').each(function(){
    if($(this).prop('href') == window.location.href){
        $(this).css({"color":"white","background-color":"#4169e1","text-decoration":"underline"})
    }
})