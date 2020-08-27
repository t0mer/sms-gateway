$(document).ready(function () {
    $('#send').click(function (e) {
        
        $.ajax({
            type: "POST",
            url: '/send',
            data: { message: $('#message').val(), phone: $('#phone').val() },
            success: function (data) {
            console.log(data)
            },
            error: function (data) {
                // console.log(data)
            },
            // dataType: 'json'
          });
    });
});

