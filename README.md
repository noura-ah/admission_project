#admission
# admission_project

Admission project:
    --- Python Django web application where it provides courses for students. The website also managed by administrators. This web allows for students to register and login. Students can apply to course. Moreover, students can edit their profile and upload their cv. Gust and student can send a message include suggestions or proposals to the admin. Admin can manage students requests for courses via decline or approve . Admin also can add, edit, and delete courses.    He/She also can read and reply messages from both gusts and students.

Admission project link:
    http://50.19.89.100/home

Skills:
    - Web Security
    - Object Relational Mapper(ORM)
    - OOP Design Principals
    - RESTful API Design
    - Deploy web applications via AWS 

Installation requirements:
    1. Install python 
        - Mac: 
            * ~$ brew -v
            * ~$ brew update		    # update homebrew
            * ~$ brew install python3	    # install Python 3
            * ~$ python3 -V         # type this command
        - Windows: To install python, we will download Python directly from Python's website with this link: Python 3.6.4
    2. Create your environment
        -  Mac/Linux: | python3 -m venv djangoPy3Env 
        -  Windows (command prompt): | python -m venv djangoPy3Env
    3. Activate your environment:
        - Mac/Linux: | source djangoPy3Env/bin/activate
        - Windows (command prompt): | call djangoPy3Env\Scripts\activate 
        - Windows (git bash) : | source djangoPy3Env/Scripts/activate  
    4. Install Django:
            pip install Django==2.2.4 | environment must be activated 
    5. Install bcrypt package:
            pip install bcrypt  | environment must be activated 
    6. Install  Mathfilter package :
            pip install django-mathfilters | environment must be activated 

Non-functional requirements:
    - Security 
    - UI Responsiveness
    - Usability 
    - Reliability
Functional requirements:
    - Admin side: 
        * Login
        *  add courses
        * Approved students request
        * Decline students request
        * Edit courses 
        * Display approved students' list of course 
        * Displaying students cv
        * Display messages
        * Reply message 

    - Students side:
        * Login 
        * Apply to course
        * Edit profile
        * Upload cv
        * Display courses 
        * Send a Message to the admin

    - Guest side:
        * Registration
        * Display courses 
        * Send Message to admin
Admission project interface:
    GUST HOME
    ![GUSTHOME!](https://user-images.githubusercontent.com/88772180/177202705-ade6257b-1eca-4cfd-bad5-e5ec331efab5.png)
    ![GUSTHOME!](https://user-images.githubusercontent.com/88772180/177203305-68855ee2-0b63-4c76-be39-02bdd3709e59.png)