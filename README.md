# Songs-and-Artists, QA Devops Project

## Contents

* Project Brief
* Design
* Risk Assessment
* The App
* Testing
* Known Issues
* Future Work

## Project Brief

The brief for this project was to design an app with CRUD functionality, storing data in a database. The structure of the database is displayed in the below Entity Relationship Diagram.

![ERD](https://github.com/mauvesky1/songs-and-artists/blob/dev/Images/Improved%20ERD.png)

In the interests of time, the song length field was not implemented

## Design

This app allows users to submit artists and songs, and store trivia about the individual songs. Users can then read the information that has been stored, update it and delete it.

Version Control was achieved with Git and Github. Project Tracking was achieved with Trello, with user stories being assigned story points. The Trello board at the beginning of the project:

## Risk Assessment

Before the project began a risk assessment was carried out.

![Risk](https://github.com/mauvesky1/songs-and-artists/blob/dev/Images/Risk.png)

One of these risks did occur, my internet went down for 6 hours on the first day of the project, Tuesday. I implemented the risk mitigation strategy in the risk assessment, and whilst this did work it could be improved. Specifically, the QA website would not allow me to log in, and this would have been highlighted if the risk mitigation strategy had been tested.

If I were to do the project again, testing the risk mitigation strategies is something I would implement.

## The App

 The technologies used in this app consist of the following:

  ### Flask
   Flask is a mini web framework, it manges HTTP requests and renders templates. Flask depends upon Jinja.

  ### Jinja2
   Jinja is a templating engine allowing python-syntax to be written inside html pages. It also allows a single html page to act as a base and for other files to build upon this.

  ### SQL
  Invented by IBM in 1974, SQL is a relational database querying language. It is used here to store data in tables. Queries were written in SQLAlchemy, rather than in straight SQL.

  ### Jenkins
   Jenkins is an automation server which enables the building, testing and deploying of software. As with the project itself, this was run on an Amazon EC2 instance. An EC2 is a cloud based virtual machine.

  ### Pytest
   Testing was achieved with Pytest, a Python testing module. It is testing integration with the database, as well as the application code. 
   These tests are run to demonstrate that the code achieves the goals it has set out to, and that it continues to do so as the code base is worked on. This way, any additions to the code base that break functionality can be caught by running the test suite.

## Testing
 When the project is pushed to Github, a hook initiates a testing sequence that generates a report. An example can be seen below.


![Tests](https://github.com/mauvesky1/songs-and-artists/blob/dev/Images/Tests.png)

## Known Issues
The group members are stored in a manner which is not fully atomic. 

When an artist is deleted, so are the songs associated with them. However, this is not made obvious to the user.

A song cannot be added unless the artist is already in the database. If this is attempted the program will throw an error rather than stop the request going through.

## Future Work

If I were to improve on this app, I would have a separate table for group members. This would make it possible to search by individual member as well, as one person could be in multiple groups over time. The trivia field could similarly be put into its own table, and the song length field could be implemented.