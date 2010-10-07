$(document).ready(function(){
     options = {
        dataType:  'json', 
        success:function(data){
            processJson(data)
            $("#form textarea, select, input").attr('disabled','')
            $('#load').hide()
        },
        beforeSubmit: function(){
            $("#form textarea, select, input").attr('disabled','disabled')
            $('#load').show()
        },
        error:function(){
            alert('ajax error')
            $("#edit_person textarea, select, input").attr('disabled','')
            $('#load').hide()
        }
    }

    $("#form form").ajaxForm(options)

function processJson( data) { 
    if (data) {
        if (eval(data.bad)) {
            errors = eval(data.errs);
            $.each(errors, function(fieldname,errmsg)
            {
                id = "#id_" + fieldname;
                $(id).parent().before( errmsg );
                });
            $("#form textarea, select, input").attr('disabled','')

        }else{
            $("#form form").clearForm();
            alert('operation is complited')
        }
    } else {
        alert("Ajax error : no data received. ")
    }
}
   

})
