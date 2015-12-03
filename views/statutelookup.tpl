<!DOCTYPE html>

<html>
  <head>
    <title>legal.io--Statute Look-Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>legal.io--Statute Look-Up</h2>

    <form action="/dostatutelookup" method="POST">

      <b>Search term</b><br>
      <input type="text" name="searchTerm" size="60" value="search term"><br>
      <br>
      <b>Your state</b><br>
<select name="state">
	<option value="CA">California</option>
	<option value="OR">Oregon</option>
</select><br><br>

      <input type="submit" value="Submit">

    </form>
  </body>

</html>
