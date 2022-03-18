# Heroes and Villains API
# Learning objective: Build a REST web API in Django REST Framework using multiple apps and foreign key model relationships.

1. CRUD Endpoints for Supers:

    Create: Adds a new super to the database, returns 201 status code
    
    Read:

        1. Gets Super from the database by Id passed as a parameter

        2. If a type query parameter is sent to the function with the value of "hero" - the view function response should be a list of all supers with type "Hero"

        3. If a type query parameter is sent to the function with the value of "villain" - the view function response should be a list of all supers with type "Villain"

        4. If no type query parameter is sent, return a custom object response with a "heroes" key listing all supers with type "Hero" and a "villains" key listing all supers with type "Villains"

    Update: Updates the super by id in the database, returns 201 status code

    Delete: Deletes the super from the database, returns 204 status code

2. CRUD Endpoints for SuperTypes:

    Create: Adds a new super type to the database, returns 201 status code
    
    Read: 
        
        1. Gets all super types from the database

        2. Gets super type by id passed as parameter from the database

    Update: Updates the super type by id in the database, returns 201 status code

    Delete: Deletes super type from the database

Bonus1: 

Create a "Power" model & "powers" many to many field on the supers model that allows association of many powers to a super. 

Create a patch endpoint for the supers app that allows you to add a new Power to a Super by submitting the PK of the hero and the new power as path variables.