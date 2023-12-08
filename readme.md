<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">


  <h3 align="center">Chitter Challenge</h3>

  <p align="center">
    A Makers Bootcamp project
    <br />

  </p>
</div>



<!-- TABLE OF CONTENTS -->
<!--<details>-->
<!--  <summary>Table of Contents</summary>-->
<!--  <ol>-->
<!--    <li>-->
<!--      <a href="#about-the-project">About The Project</a>-->
<!--      <ul>-->
<!--        <li><a href="#built-with">Built With</a></li>-->
<!--      </ul>-->
<!--    </li>-->
<!--    <li>-->
<!--      <a href="#getting-started">Getting Started</a>-->
<!--      <ul>-->
<!--        <li><a href="#prerequisites">Prerequisites</a></li>-->
<!--        <li><a href="#installation">Installation</a></li>-->
<!--      </ul>-->
<!--    </li>-->
<!--    <li><a href="#usage">Usage</a></li>-->
<!--    <li><a href="#roadmap">Roadmap</a></li>-->
<!--    <li><a href="#contributing">Contributing</a></li>-->
<!--    <li><a href="#license">License</a></li>-->
<!--    <li><a href="#contact">Contact</a></li>-->
<!--    <li><a href="#acknowledgments">Acknowledgments</a></li>-->
<!--  </ol>-->
<!--</details>-->



<!-- ABOUT THE PROJECT -->
## About The Project

[![Chitter]](/Chitter-logged-in.png)

## ***User stories:***

 As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter 

 As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

 As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

 As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter 

 As a Maker
So that only I can post messages on Chitter as me
I want to log in to Chitter

 As a Maker
So that I can avoid others posting messages on Chitter as me
I want to log out of Chitter 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* `pip` (Ensure it is installed or upgrade if needed.)
  ```sh
  python -m ensurepip --upgrade
  ```

### Installation


1. Clone the repo
   ```sh
   git clone git@github.com:soph-em/makers-chitter.git
   ```
2. Create a Database
  * Ensure you have PostgreSQL installed.
  * Create a database using the following command:
   ```sh
   createdb chitter.sql
   ```
3. Initialise the Database
* Navigate to the project directory
* Run the following command to seed the database:
   ```sh
   psql -h 127.0.0.1 chitter < chitter.sql
   ```
4. Pipenv install
   ```sh
   pipenv install
   ```
5. Activate the virtual environment
    ```sh
    pipenv shell
    ```
6. Start the local server
    ```sh
    python app.py
    ```
7. Access the App
Go to http://localhost:5000 in your web browser to use the app
 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

When logged out, users can see a list of 'Peeps', most recent first.

![Chitter website when logged out](/Chitter-logged-out.png)

When logged in, users can write their own 'Peeps' that anybody can then view.

![Chitter website when logged in](/Chitter-logged-in.png)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] MVP fitting user stories
- [ ] Improve styling
- [ ] Add functionality to 'tag' other users in tweets
- [ ] Add functionality to go to user profiles



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
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