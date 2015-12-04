<!DOCTYPE html>

<html>
  <head>
    <title>legal.io--whats my fine results</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>legal.io--whats my fine results</h2>

	%if cases:
	%for case in cases:
	Relevant Case:{{case['title']}}<br>
	Fine:{{case['fine']}}<br>
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
