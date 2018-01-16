import requests

# These are global variables(strings) that are needed to get the tMDB API response
api_main =  'https://api.themoviedb.org/3/movie/'
api_video = 'https://www.youtube.com/watch?v='
api_image = 'http://image.tmdb.org/t/p/w342///'
api_key = '?api_key=80555f22c7835f1b06f5da898a041d5e'


class Movie():
    """This class provides a way to store movie database automatically as long we have the movie ID"""
    def __init__(self, movie_id):
        #URL to extract movie data using movie_id
        url = api_main + movie_id + api_key
        #Video URL to extract movie youtube link
        video_url = api_main + movie_id + "/videos" + api_key
        #Movie Data in JSON format
        json_data = requests.get(url).json()
        json_trailer = requests.get(video_url).json()
        #Get official(original) movie Title, Poster
        self.title = json_data['original_title']
        self.poster_image_url = api_image + json_data["poster_path"]
        #Since there are multiple trailers available,just choose the first one that was brought in
        self.trailer_youtube_url = api_video + json_trailer["results"][0]["key"]

