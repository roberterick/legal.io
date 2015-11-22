<!DOCTYPE html>

<html>
  <head>
    <title>legal.io--case law lookup results</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>legal.io--case law lookup results</h2>

	%if cases:
	%for case in cases:
	Title:{{case['title']}}<br>
	Text:{{case['entryText']}}<br>
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
