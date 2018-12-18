
$(document).ready(function() {
   $('#scheduleDate').datetimepicker({
    use24hours: true,
   sideBySide:true
   });
});




function getUTCDate() {
    return moment($('#scheduleDate').val()).utc().format('YYYY-MM-DDTHH:mm:ssZZ');
}


