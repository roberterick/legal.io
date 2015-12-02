<!DOCTYPE html>

<html>
  <head>
    <title>legal.io--case show legal question submission</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>
  </head>

  <body>
      <h2>legal.io--Show Legal Question Submission</h2>
  
      	%if receivedquestion:
      		%for receivedquestion in receivedquestion:
      			State:{{receivedquestion['State']}}<br>
      			Question:{{receivedquestion['Question']}}<br>
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
