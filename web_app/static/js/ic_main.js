
// Dropzone.autoDiscover = false;

$(document).ready(function(){

    $('#clear').click(function() {
        $("#name1").text("");
        $("#name2").text("");
        $("#name3").text("");
        $("#prob1").text("");
        $("#prob2").text("");
        $("#prob3").text("");

        Dropzone.forElement("#myAwesomeDropzone").removeAllFiles(true);
    });
});
