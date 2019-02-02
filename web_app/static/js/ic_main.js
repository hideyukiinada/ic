Dropzone.options.myAwesomeDropzone = {

  init: function() {
    this.on("success", function(file, serverResponse) { // Called after the file successfully uploaded.

    // Populate classification fields
    $('#classification').show();

    $("#name1").text(serverResponse["name"][0]);
    $("#name2").text(serverResponse["name"][1]);
    $("#name3").text(serverResponse["name"][2]);
    $("#prob1").text(serverResponse["probability"][0]);
    $("#prob2").text(serverResponse["probability"][1]);
    $("#prob3").text(serverResponse["probability"][2]);

    });
  }
};

$(document).ready(function(){

    $('#classification').hide();

    // Clear button event handler
    $('#clear').click(function() {

        $('#classification').hide();

        // Clear all fields that contain name and prob in id field.
        $("[id*=name]").text("");
        $("[id*=prob]").text("");
        Dropzone.forElement("#myAwesomeDropzone").removeAllFiles(true);
    });
});
