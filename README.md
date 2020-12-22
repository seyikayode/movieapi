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

