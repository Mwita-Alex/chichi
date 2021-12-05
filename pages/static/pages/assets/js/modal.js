$(document).ready(function() {

  
    $('[data-toggle="collapse"]').click(function() {
      $(this).toggleClass( "active" );
      if ($(this).hasClass("active")) {
        $(this).text("Hide text");
      } else {
        $(this).text("Read More");
      }
    });
      
      
    // document ready  
    });