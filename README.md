# Casting Agency - Full Stack Capstone Project

Simple casting agency software to manage actors and movies based on accessed user role and permissions.

This mini-project has the purpose to show the ability to set up a DB with sqlalchemy, use JWT token with roles and abilities (provided in this case by Auth0), check permission during routing in a Flask App and project/write RESTful APIs.


## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment,

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### Database Setup
To set up empty DB run alembic upgrade
```bash
flask db upgrade
```

With Postgres running and to run tests, restore a database using the casting-agency-test.psql file provided. From the folder in terminal run:
```bash
psql casting-agency-test < casting-agency-test.psql
```


## User Abilities

### Actors
- **create:actor**: Ability to permit creation of a new actor to insert into the DB
- **read:actor**: Ability to permit retrieving actors infos
- **update:actor**: Ability to permit edit an actor infos
- **delete:actor**: Ability to remove an actor from the DB

### Movies
- **create:movie**: Ability to permit creation of a new movie to insert into the DB
- **read:movie**: Ability to permit retrieving movies infos
- **update:movie**: Ability to permit edit a movie infos
- **delete:movie**: Ability to remove a movie from the DB


## User Roles
- **assistant**: Help casting director to analyze actors and movies info. Has following abilities:
    - read:actor
    - read:movie
- **director**: Take decisions about actors and can update movies data. Abilities:
    - create:actor
    - read:actor
    - update:actor
    - delete:actor
    - read:movie
    - update:movie
- **executive-producer**: Can manage everything. Abilities:
    - create:actor
    - read:actor
    - update:actor
    - delete:actor
    - create:movie
    - read:movie
    - update:movie
    - delete:movie


## API Endpoints

### Actors
- #### **POST /actors**
    Endpoint to add a new actor in the DB. You need **_create:actor_** ability.
    
    JSON parameters:
    - **name**: Name of the actor
    - **age**: Age of the actor
    - **gender**: Gender of the actor. Admitted values are "male", "female" or "other"
    
    Example JSON request:
    ```
    {
        "id": 1,
        "name": "Jack Brown",
        "age": 34,
        "gender: "male",
        "movies":[]
    }
    ```
- #### **GET /actors**
    Endpoint to get list of actors. You need **_read:actor_** ability.
    
    Query parameters:
    - **search_term**: String to filter actors by their name. Search is case insensitive
    - **page**: As the result is paginated, this parameter specify the page to retrieve
    - **per_page**: As the result is paginated, this specify how many items get per page (max 50)
    
    Example JSON response:
    ```
    {
        "items": [
            {
                "id": 1,
                "name": "Jack Brown",
                "age": 34,
                "gender: "male",
                "movies":[]
            },
            {
                "id": 2,
                "name": "Optimus Prime",
                "age": 120,
                "gender: "other",
                "movies": [
                    {
                        "id": 1,
                        "title": "Transformers",
                        "release_date": "2007-09-21"
                    }
                ]
            },
            ...,
        ],
        "total_items": 25,
        "page": 1,
        "pages": 3
    }
    ```
- #### **GET /actors/:actor_id**
    Endpoint to get a specific actor. You need **_read:actor_** ability.
    
    URL parameters:
    - **actor_id**: Id of actor to retrieve
  
    Example JSON response:
    ```
     {
        "id": 2,
        "name": "Optimus Prime",
        "age": 120,
        "gender: "other",
        "movies": [
            {
                "id": 1,
                "title": "Transformers",
                "release_date": "2007-09-21"
            }
        ]
    }
    ```
- #### **PATCH /actors/:actor_id**
    Endpoint to edit an actor data. You need **_update:actor_** ability.
    
    URL parameters:
    - **actor_id**: Id of actor to edit
    
    JSON parameters:
    - **name**: New name of the actor
    - **age**: New age of the actor
    - **gender**: New gender of the actor. Admitted values are "male", "female" or "other"
    
    Example JSON request:
    ```
    {
        "Name "Mary Brown",
        "gender": "female",
    }
    ```
  
    Example JSON response:
    ```
    {
        "id": 1,
        "name": "Mary Brown",
        "age": 34,
        "gender": "female",
    }
    ```
- #### **DELETE /actors/:actor_id**
    Endpoint to remove an actor from the DB. You need **_delete:actor_** ability.
    
    URL parameters:
    - **actor_id**: Id of actor to delete

### Movies
- #### **POST /movies**
    Endpoint to add a new movie in the DB. You need **_create:movie_** ability.
    
    JSON parameters:
    - **title**: Title of the movie
    - **release_date**: Date of release
    
    Example JSON request:
    ```
    {
        "title "Transformers",
        "release_date": "2007-09-21",
    }
    ```
  
    Example JSON response:
    ```
    {
        {
            "id": 1,
            "title": "Transformers",
            "release_date": "2007-09-21",
            "actors": []
        }
    }
    ```
- #### **GET /movies**
    Endpoint to get list of movies. You need **_read:movie_** ability.
    
    Query parameters:
    - **search_term**: String to filter movies by their title. Search is case insensitive
    - **page**: As the result is paginated, this parameter specify the page to retrieve
    - **per_page**: As the result is paginated, this specify how many items get per page (max 50)
    
    Example JSON request:
    ```
    {
        "items": [
            {
                "id": 1,
                "title": "Transformers",
                "release_date": "2007-09-21",
                "actors": [
                    {
                        "id": 2,
                        "name": "Optimus Prime",
                        "age": 120,
                        "gender: "other"
                    }
                ]
            },
            ...,
        ],
        "total_items": 12,
        "page": 1,
        "pages": 2
    }
    ```
- #### **GET /movies/:movie_id**
    Endpoint to get a specific movie. You need **_read:movie_** ability.
    
    URL parameters:
    - **movie_id**: Id of movie to retrieve
    
    Example JSON response:
    ```
    {
        "id": 1,
        "title": "Transformers",
        "release_date": "2007-09-21",
        "actors": [
            {
                "id": 2,
                "name": "Optimus Prime",
                "age": 120,
                "gender: "other"
            }
        ]
    }
    ```
- #### **PATCH /movies/:movie_id**
    Endpoint to edit an movie data. You need **_update:movie_** ability.
    
    URL parameters:
    - **movie_id**: Id of movie to edit
    
    JSON parameters:
    - **title**: New title fo the movie
    - **release_date**: New release date of the movie
    
    Example JSON request:
    ```
    {
        "title "Transformer - 2",
        "release_date": "3299-01-01",
    }
    ```
  
    Example JSON response:
    ```
    {
        "id": 1,
        "title": "Transformer - 2",
        "release_date": "3299-01-01",
    }
    ```
- #### **DELETE /movies/:movie_id**
    Endpoint to remove an movie from the DB. You need **_delete:movie_** ability.
    
    URL parameters:
    - **movie_id**: Id of movie to delete