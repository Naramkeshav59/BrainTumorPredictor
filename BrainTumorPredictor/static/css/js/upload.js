var myForm = document.getElementById('formAjax');  // Our HTML form's ID
var myFile = document.getElementById('fileAjax');  // Our HTML files' ID


myForm.onsubmit = function(event) {
  event.preventDefault();

 
  // Get the files from the form input
  var files = myFile.files;

  // Create a FormData object
  var formData = new FormData();

  // Select only the first file from the input array
  var file = files[0];

  

  // Add the file to the AJAX request
  formData.append("fileAjax", file, img.jpg);

  // Set up the request
  var xhr = new XMLHttpRequest();

  // Open the connection
  xhr.open('POST', '/uploader', true);

  // Set up a handler for when the task for the request is complete
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("outp").innerHTML =
      this.responseText;
    }
  };

  // Send the data.
  xhr.send(formData);
}