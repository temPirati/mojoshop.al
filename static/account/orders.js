var order_id = $(this).val();
$("#button_id").on('click', function () {
    $.ajax({
      url: 'http://127.0.0.1:8000/account/orders/recieved/',
      data: {
        csrfmiddlewaretoken: CSRF_TOKEN,
        order_id : order_id
      },
      dataType: 'json',
      success: function (data) {
        if (data.success) {
          alert("ajax call success.");
          
        }else{
          alert("ajax call not success.");
        }
      }
    });
});