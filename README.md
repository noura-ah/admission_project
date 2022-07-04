#admission


# Admission Project:
        Python Django web application where it provides courses for students. The website 
    also managed by administrators. This web allows for students to register and login.
    Students can apply to course. Moreover, students can edit their profile and upload 
    their cv. Gust and student can send a message include suggestions or proposals to 
    the admin. Admin can manage students requests for courses via decline or approve. 
    Admin also can add, edit, and delete courses.He/She also can read and reply messages 
    from both gusts and students.

# Try It:
    http://50.19.89.100/home

# Project Demo:
    https://youtu.be/cU6KwimPJGU

# Skills:
    - Web Security
    - Object Relational Mapper(ORM)
    - OOP Design Principals
    - RESTful API Design
    - Python - Django
    - Deploy web applications via AWS 

# Installation Requirements:
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
   **OR install Dependencies in one line using : **
  
   > pip install -r requirements.txt
     
# Run The Project:
   make sure that your environment is active and you in the same level with manage.py file and then type: 
   > python manage.py makemigrations 
   
   > python manage.py migrate
   
   > python manage.py runserver 
    
# Non-functional Requirements:
    - Security 
    - UI Responsiveness
    - Usability 
    - Reliability
# Functional Requirements:
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
# Admission project interface:

    GUST HOME
   ![GUSTHOME!](https://user-images.githubusercontent.com/88772180/177202705-ade6257b-1eca-4cfd-bad5-e5ec331efab5.png)
   ![GUSTHOME!](https://user-images.githubusercontent.com/88772180/177203305-68855ee2-0b63-4c76-be39-02bdd3709e59.png)
    ![GUSTHOME!](https://user-images.githubusercontent.com/88772180/177203368-3d07a878-3787-4fd8-8d6b-af7081417d72.png)
    ![GUSTHOME!](https://user-images.githubusercontent.com/88772180/177203435-6ce3fe7d-9f35-4b66-acea-bd9f1fded5ab.png)
    REGISTER/LOGIN
    ![LOGIN!](https://user-images.githubusercontent.com/88772180/177203501-271e71b7-5301-47f9-92b7-e3f1ceb66bac.png)
    ![LOGIN!](https://user-images.githubusercontent.com/88772180/177203836-f5f29be6-be3d-4202-8c34-eb54083a9a38.png)
    ADMIN
    ![ADMIN!](https://user-images.githubusercontent.com/88772180/177204351-b68aca74-eda8-4882-9f83-ecbda13b58aa.png)
    ![ADMIN!](https://user-images.githubusercontent.com/88772180/177204404-0cbacd3d-43b5-4f66-bbab-4d2daf4d8615.png)
    ![ADMIN!](https://user-images.githubusercontent.com/88772180/177204432-ea8fadb3-d734-4b84-bbfd-4885e5a7212d.png)
    ![ADMIN!](https://user-images.githubusercontent.com/88772180/177204471-a78a8d05-89e9-477a-b94a-0a79758e9175.png)
    STUDENT
    ![STUDENT!](https://user-images.githubusercontent.com/88772180/177203628-89fc6f0c-a19d-4b5a-b1b2-760b92857ac5.png)
    ![STUDENT!](https://user-images.githubusercontent.com/88772180/177203979-b8c8513d-7ed2-46af-a32c-35f11b5e346b.png)
    ![STUDENT!](https://user-images.githubusercontent.com/88772180/177204060-c4a4aae7-2853-4f65-9412-b85ef89799cf.png)
    ![STUDENT!](https://user-images.githubusercontent.com/88772180/177204108-8db9afad-ecc8-4e80-b5d0-ba51a44e5d70.png)
    ![STUDENT!](https://user-images.githubusercontent.com/88772180/177204150-bfb54f40-1de5-4682-a896-107890dcd304.png)
    ![STUDENT!](https://user-images.githubusercontent.com/88772180/177204220-eec49f29-2550-4032-bcde-92642c04f26d.png)
    ![STUDENT!](https://user-images.githubusercontent.com/88772180/177204269-fe4d9f67-a96b-4176-88da-aa5ffa393968.png)
    ![STUDENT!](https://user-images.githubusercontent.com/88772180/177204311-caca6642-473f-4118-ae3a-278d2a8f5018.png)

