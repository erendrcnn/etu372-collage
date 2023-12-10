<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/erendrcnn/etu372-collage">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">ETU372 COLLAGE - SCHOOL MANAGEMANT SYSTEM</h3>
  <!--
  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/erendrcnn/etu372-collage"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/erendrcnn/etu372-collage">View Demo</a>
    ·
    <a href="https://github.com/erendrcnn/etu372-collage">Report Bug</a>
    ·
    <a href="https://github.com/erendrcnn/etu372-collage">Request Feature</a>
  </p>
  -->
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

ETU372 is a modern, user-friendly solution developed to meet the diverse needs of schools and educational organizations. The system focuses on providing an efficient and integrated platform to manage various aspects of school administration, including student information, attendance tracking, grade management, and communication between educators, students, and parents.





### Built With

* [![HTML][HTML.com]][HTML-url]
* [![CSS][CSS.com]][CSS-url]
* [![PHP][PHP.com]][PHP-url]
* [![JavaScript][JavaScript.com]][JavaScript-url]
* [![Python][Python.com]][Python-url]






<!-- GETTING STARTED -->
## Getting Started

This section provides instructions on setting up and running the Project372 Django project locally. Follow these steps to get a local copy up and running.

### Prerequisites

Make sure you have the following prerequisites installed on your machine:
* Python - [Download and Install Python](https://www.python.org/downloads/)
* MySQL Command Line Client - [Download and Install MySQL Command Line Client](https://dev.mysql.com/downloads/shell/)

### Installation

1. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   C:\...\Project372\venv\Scripts\activate
2. Install required Python packages:
   ```sh
   pip install django
   pip install mysql
   pip install mysql-connector-python
   ```
3. Clone the repository:
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
4. Navigate to the project directory and install additional dependencies:
   ```sh
   cd Project-Name
   pip install -r requirements.txt
   ```
5. Enter your MySQL database configuration in settings.py:
   ```sh
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'school_management_system',
        'USER': 'school_management_system',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
     }
   }
   ```
6. Run database migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
7. Populate the database by executing the SQL script (DBGenerator_app.sql) using a MySQL client like DBEAVER or MySQL Workbench.
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
8. Start the Django development server:
   ```sh
   python manage.py runserver
   ```
9. Open the following link in your web browser:
  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)




<!-- USAGE EXAMPLES -->
## Usage

ETU372 Collage - School Management System offers a comprehensive set of features to streamline various aspects of school administration. Here are some examples of how to use the system effectively:

1. **Student Information Management:**
   - Manage student information such as student details, attendance records, and grades.
   - Check the weekly program schedule.
   - Request open courses and view the status of the request.

2. **Program Tracking:**
   - Track student attendance and generate reports on attendance trends.
   - Track teacher attendance and generate reports on attendance trends.

3. **Administration Panel:**
   - Manage administrative tasks such as creating and managing user accounts.

4. **Parent Evaluation:**
   - Provide parents with access to the system to view their child's grades and attendance.

5. **User-Friendly Interface:**
   - Navigate through the system's intuitive interface to access various modules easily.
   - Experience a responsive design that adapts to different devices for on-the-go access.

6. **Customization:**
   - Configure system settings and preferences based on the specific needs of the educational institution.
   - Tailor the system to accommodate different grading systems and administrative processes.

7. **Security and Access Control:**
   - Manage user roles and permissions to control access to sensitive information.
   - Ensure data security with features like encrypted communication and secure login.

8. **Reporting and Analytics:**
   - Generate detailed reports on student performance, and other key metrics.
   - Leverage analytics tools to gain insights into school operations.

Feel free to explore and utilize the features of ETU372 Collage - School Management System to enhance the efficiency of your educational institution.




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request





<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.





<!-- CONTACT -->
## Contact

Project Link: [https://github.com/erendrcnn/etu372-collage](https://github.com/erendrcnn/etu372-collage)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/erendrcnn/etu372-collage/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/erendrcnn/etu372-collage/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/erendrcnn/etu372-collage/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/erendrcnn/etu372-collage/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/erendrcnn/etu372-collage/blob/master/LICENSE.txt
<!--
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in
-->
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[HTML.com]: https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white
[HTML-url]: https://html.com
[CSS.com]: https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white
[CSS-url]: https://www.w3.org/Style/CSS/Overview.en.html
[PHP.com]: https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white
[PHP-url]: https://www.php.net
[JavaScript.com]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[JavaScript-url]: https://www.javascript.com
[Python.com]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
