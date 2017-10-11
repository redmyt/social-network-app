$("#form1").on( "button", function(event) {
  event.preventDefault();
 // console.log($(this).serializArray());
<<<<<<< HEAD
  path = $(this).data('url');   // вказує на поточну сторінку
=======
  path = $(this).data('url');  
>>>>>>> origin/US04_3
  $.ajax({
        type: "POST",
        url: path,
        data: $(this).serializeArray(),
        cache: false,
        headers: {
          'X-CSRFToken': csrftoken
        }
    });
});