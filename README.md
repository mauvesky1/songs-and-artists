# Songs-and-Artists, QA Devops Project

## Contents

* [Project Brief] (#Project-Brief)
* Design
* Risk Assessment
* The App
* Testing
* Known Issues
* Future Work

## Project Brief

The brief for this project was to design an app with CRUD functionality, storing data in a database. The structure of the database is displayed in the below Entity Relationship Diagram.

## Design

This app allows users to submit artists and songs, and store trivia about the individual songs. Users can then read the information that has been stored, update it and delete it.

## Risk Assessment

Before the project began a risk assessment was carried out.

One of these risks did occur, my internet went down for 6 hours on the first day of the project, Tuesday. I implemented the risk mitigation strategy in the risk assessment, and whilst this did work it could be improved. Specifically, the QA websites would not allow me to log in, and this wouild have been highlighted if the risk mitigation strategy had been tested.

* The App

    The technologies used in this app consist of:

        -Flask
            Flask is a mini web framework, it manges HTTP requests and renders templates. Flask depends upon Jinja.
        -Jinja2
            Jinja is a templating engine allowing python-syntax to be written inside html pages. It also allows a single html page to act as a base and for other files to build upon this.
        -SQL
            Invented by IBM in 1974, SQL is a relational database querying language. It is used here to store data in tables. Queries were written in SQLAlchemy, rather than in straight SQL.
        -Jenkins
            Jenkins is 
        -Pytest
            Testing was acheived with 
* Testing
    When the project is pushed to Github, a hook initiates a testing sequence that generates a report. An example can be seen below

* Known Issues
    The group members are stored in a manner which is not atomic. If I were to improve on this app, I would have a separate table for group members. This would make it possible to search by member as well, as one person could be in multiple groups over time.

* Future Work
    If I were to do the project again, testing the risk mitigation strategies is something I would implement.