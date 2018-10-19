def html_string(old_text, new_text, book, chapter, verse, url):
  return """
<!doctype html>
<title>Compare</title>

  
   <iframe src='"""+url+"""' width="100%" style="margin-top:-450px;margin-left:-100px" height="650px"></iframe>
  <h4>"""+book+" "+chapter+":"+verse+"""</h4>

  <p>Old text is:</p>
  <p id="old">"""+old_text+"""</p>
  <a id="delete-old" href='/change_old/"""+book+"/"+chapter+"/"+verse+"""'>delete</a>
  <br>
  <br>

  <p>New text is:</p>
  <p id="new">"""+new_text+"""</p>
  <a id="delete-new" href='/change_new/"""+book+"/"+chapter+"/"+verse+"""'>delete</a>
  <br>
  <br>

  <form action='/change_both/"""+book+"/"+chapter+"/"+verse+"""' method="post">
	  <input type="text" name="user_text" size="150">
	  <input type="submit">
  </form>

  <script>
    // Execute a function when the user releases a key on the keyboard
    document.addEventListener("keyup", function(event) {
      // Cancel the default action, if needed
      event.preventDefault();
      // Number 37 is the "left-arrow" key on the keyboard
      if (event.keyCode === 37) {
        // Trigger the button element with a click
        document.getElementById("delete-old").click();
      }
      // Number 39 is the "right-arrow" key on the keyboard
      if (event.keyCode === 39) {
        // Trigger the button element with a click
        document.getElementById("delete-new").click();
      }
    });
  </script>

        """
