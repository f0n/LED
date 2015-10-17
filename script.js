$(function(){
    $( ".accContainer").hide();
    $( ".accordion:first").next().slideDown();

    $(".accordion").click(function(){
        if( $(this).next().is(":hidden") ) {
            $(".accordion").next().slideUp();
            $(this).next().slideDown();
        }

        return false;
    
    });







});

