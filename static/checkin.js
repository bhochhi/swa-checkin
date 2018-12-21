
$(document).ready(function() {
   $('#scheduleDate').datetimepicker({
    sideBySide:true,
    format:'YYYY-MM-DDTHH:mm:ssZZ'
   });
//    var input = $(this).find("input[name=scheduleDate]");
//    var picker = $('#scheduleDate').data('datetimepicker');
//    input.val(picker.getLocalDate());

//    $("form-checkin").submit(function(){
//    // Let's find the input to check
//    var input = $(this).find("input[name=scheduleDate]");
//    if (input.val()) {
//            var picker = $('#scheduleDate').data('datetimepicker');
//          alert(input.val());
//            input.val(picker.getLocalDate());
//           }
//    });


 $("form").submit(function(event){
    event.preventDefault();
     $.ajax({
        type: "POST",
        url: $("form").attr('action'),
        data: toJson($('form.form-checkin').serialize()),
        success: function(msg){
             alert(msg);
        },
        error: function(){
            alert("failure");
        }
     });
     return false;
 });
});




function toJson(formArray) {//serialize data function
    var json = formArray.split('&').reduce((json, value, idx) => {
        var obj = value.split('=');
        json[obj[0]] = obj[1];
        return json;

    }, {});

    return json;
}

function getUTCDate(datetime) {
    return moment(datetime).utc().format('YYYY-MM-DDTHH:mm:ssZZ');
}


