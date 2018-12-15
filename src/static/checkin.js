
function validateForm(event){
//    console.log(document.forms)
//    document.forms["form-checkin"]["scheduleDate"].value = new Date()
    return true;
}

window.onload = function(){
    document.getElementById("scheduleDate").defaultValue = Date.now()
}