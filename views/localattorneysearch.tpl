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
    <h2>legal.io--Local Attorney Search</h2>

    <form action="/dolocalattorneysearch" method="POST">

      <b>Your state</b><br>
	<select name="state">
	<option value="CA">California</option>
	<option value="OR">Oregon</option>
	</select><br><br>

      <b>Your county</b><br>
	<select name="county">
	<option value="Linn">Linn</option>
	<option value="Benton">Benton</option>
	</select><br><br>

      <input type="submit" value="Submit">

    </form>
  </body>

</html>
