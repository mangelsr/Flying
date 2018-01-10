$(document).ready(function(){

    $('#form').on('submit', function(event){
        event.preventDefault();
        
        let tipo;
        if ($('#tipo0').is(':checked'))
            tipo = '0';
        else
            tipo = '1';
        
        let data =  {
            origen: $('#id_origen').val(),
            destino: $('#id_destino').val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            tipo: tipo
        };
        
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: data,
            success: function(data){
                console.log(data);
                $('#result').hide().html(data.content).fadeIn('slow');
            },
            error: function (jqXHR, exception) {
                var msg = '';
                if (jqXHR.status === 0) {
                    msg = 'Not connect.\n Verify Network.';
                } else if (jqXHR.status == 404) {
                    msg = 'Requested page not found. [404]';
                } else if (jqXHR.status == 500) {
                    msg = 'Internal Server Error [500].';
                } else if (exception === 'parsererror') {
                    msg = 'Requested JSON parse failed.';
                } else if (exception === 'timeout') {
                    msg = 'Time out error.';
                } else if (exception === 'abort') {
                    msg = 'Ajax request aborted.';
                } else {
                    msg = 'Uncaught Error.\n' + jqXHR.responseText;
                }
                alert(msg);
            },
        });
    });
});