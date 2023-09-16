<!DOCTYPE html>
<html>

<head>
</head>

<body>

<h1><a href="#top">Drowsiness Detection Application</a></h1>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
</ul>

<hr>

<h2 id="introduction">Introduction</h2>

<p>The <strong>Drowsiness Detection</strong> application is a desktop-based solution designed to monitor user
    fatigue levels and ensure their safety, particularly while engaged in tasks that require attentiveness, such as
    driving or operating heavy machinery.</p>

<p>The application features two distinct panels: one for the user and another for the admin. In the user section,
    individuals can log in and activate their camera. The system utilizes facial and eye detection to monitor blinking
    patterns. When a user exhibits signs of drowsiness, the application emits a short beep. If drowsiness persists, an
    alarm will sound to awaken the user. Additionally, a screenshot is captured and stored in an SQL database, allowing
    users to review their past records.</p>

<p>In the admin section, administrators have access to user management and record management functionalities, in
    addition to the standard user features.</p>

<hr>

<h2 id="features">Features</h2>

<ul>
    <li>User-friendly GUI powered by Tkinter for easy interaction.</li>
    <li>Real-time facial and eye detection using OpenCV's Haar cascades.</li>
    <li>Alerts for short and prolonged periods of drowsiness.</li>
    <li>Continuous monitoring and alarm activation to prevent accidents.</li>
    <li>Secure user authentication and record management.</li>
    <li>Screenshot capture and SQL database integration for record storage.</li>
    <li>Intuitive admin panel with user and record management capabilities.</li>
</ul>

<hr>

<h2 id="technologies-used">Technologies Used</h2>

<ul>
    <li>OpenCV</li>
    <li>Haarcascade</li>
    <li>Tkinter</li>
    <li>SQLite</li>
    <li>Pygame</li>
 
</ul>

<hr>

<h2 id="getting-started">Getting Started</h2>

<ol>
    <li>Clone the repository to your local machine.</li>
    <pre><code>git clone https://github.com/hassaanahmed04/drowsiness-detection.git</code></pre>
<li>Install the required dependices using <a href="https://pip.pypa.io/en/stable/">Pip</a></li>
      <pre><code>pip install -r requirements.txt</code></pre>

</ol>

<hr>

<h2 id="usage">Usage</h2>

<ol>
    <li>Navigate to the project directory.</li>
    <pre><code>cd drowsiness-detection</code></pre>
  <li>Launch the application by running the main script.</li>
    <pre><code>python account_system.py</code></pre>
    <li>Create an account.</li>
    <li>Admin Credentials</li>
      <ul>   <li>User Name : admin</li>
      <li>Password : admin</li></ul>
 

    


</ol>

<h2 id="contributing">Contributing</h2>

<p>We welcome contributions from the community and are eager to have more contributors. If you'd like to contribute, please follow these steps:</p>

<ol>
    <li><strong>Fork the Repository:</strong> Click on the "Fork" button on the top right corner of this page.</li>
    <li><strong>Clone the Repository:</strong> Clone the forked repository to your local machine using:</li>
    <pre><code>git clone https://github.com/hassaanahmed04/drowsiness-detection.git</code></pre>
<li><strong>Create a New Branch:</strong> Create a new branch for your contributions:</li>
    <pre><code>cd drowsiness-detection
git checkout -b feature/new-feature</code></pre>
<li><strong>Make Changes:</strong> Make your desired changes and add, commit, and push to your forked repository :</li>
    
   <pre><code>git add .
git commit -m "Added new feature"
git push origin feature/new-feature</code></pre>
<li><strong>Open a Pull Request:</strong> Go to the original repository and click on "New Pull Request". Provide a brief description of your changes and submit the pull request.</li>
</ol>


<p><a href="#top">Back to Top</a></p>

</body>

</html>
