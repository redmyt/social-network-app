$("#form1").on( "button", function(event) {
  event.preventDefault();
 // console.log($(this).serializArray());
  path = $(this).data('url');   // вказує на поточну сторінку
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