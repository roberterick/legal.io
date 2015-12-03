<!DOCTYPE html>

<html>
  <head>
    <title>legal.io--statute results</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>legal.io--statutes results</h2>

	%if statutes:
	%for statute in statutes:
	Title:{{statute['title']}}<br>
	Text:{{statute['entryText']}}<br>
	<hr>
	<br>
	%end
	%else:
	No results found.<br><br>
	%end
	%end

	<a href="/">home</a>

  </body>

</html>

