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

      <b>Attorneys in your county:</b>
      <br>
      <br>
      %if attorneys:
        %for attorney in attorneys:
          Name: {{attorney['name']}}
          <br>
          Phone: {{attorney['phone']}}
          <hr>
          <br>
        %end
      %else:
        No results found.<br><br>
        %end
      %end
      </select>

      <br><br>

      <a href="/">home</a>

  </body>

</html>
