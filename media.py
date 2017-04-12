'''
Defines the class Movie so we can create
Movie objects (in entertainmen_center.py).
'''


class Movie():
    """This class provides a way to store movie related information."""

    '''
    The constructor initializes 4 variables:
    title, storyline, poster image, and Youtube trailer.
    '''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
