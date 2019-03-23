import webbrowser
"""
             This Creating Class Making Own
             HTML to Display the list of videos 
     
"""

# Creating Class:

class Movie():

    def __init__(self,song_name,movie_name,movie_release_date,movie_image,youtube_url):
        self.song_name = song_name
        self.movie_name = movie_name
        self.releasedate = movie_release_date
        self.image = movie_image
        self.song_url = youtube_url


    def show_song(self):
        webbrowser.open(self.song_url)

    def movie_release_date(self):
        print(self.releasedate)

    def movie_name():
        print(self.movie_name)

    def song_name():
        print(self.song_name)
    
