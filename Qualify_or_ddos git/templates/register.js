<html>
  <head>
    <title>Flask Intro - login page</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="{{url_for('static',filename='css/bootstrap.min.css')}}" rel="stylesheet" media="screen">
  </head>
  <body>
    <div class="container">
      <h1>Please register</h1>
      <br>
      <form action="" method="post"  enctype="multipart/form-data">
        <input type="text" placeholder="Name" name="name" required="required" value="{{
          request.form.name }}"><br>
          <input type="text" placeholder="Username" name="username" required="required" value="{{
            request.form.username }}"><br>
            <input type="email" placeholder="E-mail" name="email" required="required" value="{{
              request.form.email }}"><br>
              <input type="date" placeholder="Date of Birth" name="dob" required="required" value="{{
                request.form.dob }}"><br>
         <input type="password" placeholder="Password" name="password" required="required" value="{{
          request.form.password }}"><br>
          <input type="password" placeholder="Confirm Password" name="cpassword" required="required" value="{{
           request.form.cpassword }}"><br>
         
        <input class="btn btn-success btn-default" type="submit" value="Login">
      </form>
      {% if error %}
        <p class="error"><strong>Error: </strong> {{ error }}
      {% endif %}
    </div>
  </body>
</html>
