import webbrowser

class Movie():
    """Class structure for class Movie"""
    # Movie class constructor
    def __init__(self, movieTitle, movieVideoLink, moviePosterLink):
        """Constructor function for class Movie"""
        self.title = movieTitle
        self.trailer_youtube_url = movieVideoLink
        self.poster_image_url = moviePosterLink

    # Method to play youtube trailer
    def playTrailer(self):
        """Method to play youtube video"""
        webbrowser.open(self.trailer_youtube_url)
