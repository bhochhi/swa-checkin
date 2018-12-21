
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
        },
        error: function(){
            alert("failure");
        }
     });
     return false;
 });
});


function formattedFormData(data){
    var json = toJson(data);
    json['scheduledDate'] = getUTCDate(json['scheduleDate'])
    return json;
}



function toJson(formArray) {//serialize data function
    var json = formArray.split('&').reduce((json, value, idx) => {
        var obj = value.split('=');
        json[obj[0]] = obj[1];
        return json;
    }, {});

    return json;
}

function getUTCDate(datetime) {
    return moment(unescape(datetime)).format('YYYY-MM-DDTHH:mm:ssZZ');
}


