import webbrowser

class Movie():
    #Movie class constructor
    def __init__(self, movieTitle, movieVideoLink, moviePosterLink):
        self.title = movieTitle
        self.trailer_youtube_url = movieVideoLink
        self.poster_image_url = moviePosterLink

    #Method to play youtube trailer
    def playTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
