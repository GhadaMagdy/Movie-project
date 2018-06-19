"""This module descripes movie variables and methods"""
import webbrowser


class Movie():
    """this class provides way to store movies"""
    def __init__(self, movie_title, movie_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = movie_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        """show trailer method opens the trailer of mvie on youtupe"""
        webbrowser.open(self.trailer_youtube_url)
