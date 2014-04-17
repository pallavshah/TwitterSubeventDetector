<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../assets/ico/favicon.ico">

    <title>Blog Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="blog.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy this line! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="blog-masthead">
      <div class="container">
        <nav class="blog-nav">
          <a class="blog-nav-item active" href="#">HOME</a>
        </nav>
      </div>
    </div>

    <div class="container">

      <div class="blog-header">
        <h1 class="blog-title">Sub Event Detection</h1>
        <p class="lead blog-description">Make a timeline/summary of events fom tweets.</p>
      </div>

      <div class="row">

        <div class="col-sm-3 blog-sidebar">
          <h2>Run Code</h2>
          <div class="sidebar-module sidebar-module-inset">
            <h4>Sub-Event Detection</h4>
            <?php if (isset($_POST['detection'])) { exec('test.pl'); } ?>
            <form action="" method="post">
                <button class="btn btn-danger" type="submit" name="detection">Run</button>
            </form>
          </div>

          <div class="sidebar-module sidebar-module-inset">
            <h4>Summarisation</h4>
            <?php if (isset($_POST['summary'])) { exec('test.pl'); } ?>
            <form action="" method="post">
                <button class="btn btn-danger" type="submit" name="summary">Run </button>
            </form>
          </div>
          <!--
          <div class="sidebar-module">
            <h4>Archives</h4>
            <ol class="list-unstyled">
              <li><a href="#">January 2014</a></li>
              <li><a href="#">December 2013</a></li>
              <li><a href="#">November 2013</a></li>
              <li><a href="#">October 2013</a></li>
              <li><a href="#">September 2013</a></li>
              <li><a href="#">August 2013</a></li>
              <li><a href="#">July 2013</a></li>
              <li><a href="#">June 2013</a></li>
              <li><a href="#">May 2013</a></li>
              <li><a href="#">April 2013</a></li>
              <li><a href="#">March 2013</a></li>
              <li><a href="#">February 2013</a></li>
            </ol>
          </div>
        -->
          <div class="sidebar-module">
            <h4>Code Base</h4>
            <ol class="list-unstyled">
              <li><a href="https://github.com/dreamrulez07/SubEventDetectionIRE">GitHub</a></li>
            </ol>
          </div>
        </div><!-- /.blog-sidebar -->

        <div class="col-sm-8 blog-main">

          <div class="blog-post">
            <h2 class="blog-post-title">US Presidential Elections</h2>
            <p class="blog-post-meta">Data collected in 2012 from <a href="#">Twitter</a></p>

            <h3>Sub-Events:</h3>
            </br>
            <?php
            $xml=simplexml_load_file("summary.xml");
            foreach ($xml->children() as $subevent) {
                echo "<h4>";
                echo $subevent->heading;
                echo " </h4>";
                echo "<pre>";
		            echo "<ol>";
	              foreach ($subevent->tweet as $tweet) {
		                echo "<li>";
                    echo $tweet;
		                echo "</li>";
		                echo "</br>";
                }
		            echo "</ol>";
                echo "</pre>";
            }
            ?>

            
            
          </div><!-- /.blog-post -->

          
          
        </div><!-- /.blog-main -->

        

      </div><!-- /.row -->

    </div><!-- /.container -->

    <div class="blog-footer">
      <p>IRE Project on Sub-Event Detection <a href="https://github.com/dreamrulez07/SubEventDetectionIRE">Code</a> by <a href="https://twitter.com/mdo">@mdo</a>.</p>
      <p>
        <a href="#">Back to top</a>
      </p>
    </div>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
