<!DOCTYPE html>

<html>
  <head>
    <title>legal.io--case law lookup</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>legal.io--case law lookup</h2>

    <form action="/docaselawlookup" method="POST">

      <b>Enter a case name you want to look up</b><br>
      <input type="text" name="searchTerm" size="60" value="search term"><br>
      <br>

      <b>Select the state of the case you wish to look up</b><br>
	<select name="state">
	<option value="CA">California</option>
	<option value="OR">Oregon</option>
	</select><br><br>

      <input type="submit" value="Submit">

    </form>
	
	<a href="/">home</a>
	
  </body>

</html>
