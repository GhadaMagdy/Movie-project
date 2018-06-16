"""This module descripes movie variables and methods"""
import webbrowser
class Movie:
    """this class provides way to store movies"""
    # when you define a constant you should write in camel case
    VALID_RATING = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = movie_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
