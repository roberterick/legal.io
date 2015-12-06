<!DOCTYPE html>

<html>
  <head>
    <title>legal.io--What's my fine results</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>legal.io--What's my fine results</h2>

	%if fines:
	%for fine in fines:
	Title:{{fine['title']}}<br>
	Text:{{fine['entryText']}}<br>
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

