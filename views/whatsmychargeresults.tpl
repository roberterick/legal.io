<!DOCTYPE html>

<html>
  <head>
    <title>legal.io--What's my charge results</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>legal.io--What's my charge results</h2>

	%if charges:
	%for charge in charges:
	Title:{{charge['title']}}<br>
	Text:{{charge['entryText']}}<br>
	<hr>
	<br>
	%end
	%else:
	No results found.<br><br>
	%end
	%end

	<a href="/">home</a>

  </body>

</html><!DOCTYPE html>

