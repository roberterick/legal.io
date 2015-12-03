<!DOCTYPE html>

<html>
  <head>
    <title>legal.io--show legal questions</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>
  </head>

  <body>
      <h2>legal.io--Show Legal Question Submission</h2>
  
      	%if receivedquestions:
      		%for receivedquestion in receivedquestions:
      			State:{{receivedquestion['state']}}<br>
      			Question:{{receivedquestion['userquestion']}}<br>
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
