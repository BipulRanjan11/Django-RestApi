# Django-RestApi
Django Assignment
****
This Django-based REST API exposes several endpoints for interacting with the client, artist, and work tables in the database.
Base URL
All endpoints are relative to the base URL of the API, which is:

http://127.0.0.1:8000/app/api

Available Endpoints
Works
This endpoint retrieves all works or a filtered set of works based on work type or artist name.

GET /works - Retrieves all works in the database
GET /works?work_type={work_type} - Retrieves works filtered by work type. Valid values for work_type are 'youtube', 'instagram', or 'other'.
GET /works?artist={artist_name} - Retrieves works filtered by artist name. The value of artist_name should be a string that matches the name of an artist in the database.
Register
This endpoint allows a user to register with the API by providing a username and password.


