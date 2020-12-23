# movieapi

To create a movie type like Series and Clip:
{
"category": 
}  /api/add_movie/

To create a media description for a Series:
{
"movie_name": ,
"genre": ,
"cast": ,
"season": 
}  /api/movies/{id}/add_media/

To create a media description for a Clip:
{
"movie_name": ,
"genre": ,
"cast": 
}  /api/movies/{id}/add_media/

To create videos for a Series(user can add as much videos):
{
"episode": ,
"description": ,
"thumbnail": ,
"video": 
}  /api/movies/{id}/medias/{media_pk}/add_video/

To create video for a Clip:
{
"description": ,
"thumbnail": ,
"video": 
}  /api/movies/{id}/medias/{media_pk}/add_video/


Other endpoints to view each details can be found in:
/api/v1/


#contributions

To contribute to the project:
1. Install Python (You can skip if you have python already)
2. pip install virtualenv
3. run virtualenv env
4. the env folder will be created then run "env\scripts\activate" You can skip steps 2-4 if you know how to run django already
5. pip install -r requirements.txt
6. now you can run the server, python manage.py runserver

You can fork the repo and 
