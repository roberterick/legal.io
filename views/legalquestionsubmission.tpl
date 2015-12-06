<!DOCTYPE html>

<html>
	<head>
		<title>legal.io--Legal Question Submission</title>
		<style type="text/css">
			.label {
				text-align: right;
			}

			.error {
				color: red;
			}
		</style>

	</head>
	<body>
		<h2>legal.io--Legal Question Submission</h2>

		<form action="/dolegalquestionsubmission" method="POST">

				<b>Select the state that your question is relevant to</b><br>
					<select name="state">        
						<option value="CA">California</option>
						<option value="OR">Oregon</option>
					</select><br><br>

				<b>Enter in your question</b><br>
					<p><textarea rows="20" cols="75" input type="text" name="userquestion"></textarea></p>

				<input type="submit" value="Submit">
		</form>
		
		<a href="/">home</a>
		
	</body>
</html>
