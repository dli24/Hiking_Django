$('.nav-link').each(function(){
    if($(this).prop('href') == window.location.href){
        $(this).addClass('activeNav');
    }
})
