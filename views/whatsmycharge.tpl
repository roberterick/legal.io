<html>
  <head>
    <title>legal.io--What's My Charge</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>legal.io--What's My Charge</h2>

    <form action="/dochargelookup" method="POST">

      <b>Enter the charge you want to look up</b><br>
      <input type="text" name="searchTerm" size="60" value="search term"><br>
      <br>
      <b>Enter Your state</b><br>
<select name="state">
	<option value="CA">California</option>
	<option value="OR">Oregon</option>
</select><br><br>

      <input type="submit" value="Submit">

    </form>
  </body>

</html>