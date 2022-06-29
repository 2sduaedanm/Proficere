function LaunchVideoModal(identifier){
    var modal = document.getElementById("videoModal-"+$(identifier).data('id')); 
    modal.style.display = "block";
}
function CloseVideoModal(identifier){
    var modal = document.getElementById("videoModal-"+$(identifier).data('id')); 
    modal.style.display = "none";
    $(modal).find('video')[0].pause();
}

// Hints Video Modal
//   When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if ($(event.target).hasClass('videoModal')) {
        $(event.target).find('video')[0].pause();
        var modal = document.getElementById(event.target.id); 
        modal.style.display = "none";
    }
}