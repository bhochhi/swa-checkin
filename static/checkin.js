
$(document).ready(function() {
   $('#scheduleDate').datetimepicker({
    sideBySide:true,
    format:'MM/DD/YYYY HH:mm:ss'
   });


 $("form").submit(function(event){
    event.preventDefault();
     $.ajax({
        type: "POST",
        url: $("form").attr('action'),
        data: formattedFormData($('form.form-checkin').serialize()),
        success: function(msg){
             alert(unescape(msg));
             $("form.form-checkin")[0].reset()

        },
        error: function(err){
            alert("failure!! ",err);
           $("form.form-checkin")[0].reset()
        }
     });
     return false;
 });
});


function formattedFormData(data){
    var json = toJson(data);
    json['scheduleDate'] = getUTCDate(json['scheduleDate'])
    return json;
}



function toJson(formArray) {
    var json = formArray.split('&').reduce((json, value, idx) => {
        var obj = value.split('=');
        json[obj[0]] = obj[1];
        return json;
    }, {});
    console.log('returning....',json)
    return json;
}

function getUTCDate(datetime) {
    return moment(unescape(datetime)).format('YYYY-MM-DDTHH:mm:ssZZ');
}


