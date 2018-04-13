class Movie:
    """Constructor class that displays movie trailer promo materials.

    Class takes 4 arguments: movie_title, movie_storyline, poster_image, and
     trailer_youtube.

    Args:
    movie_title (str): Movie title name
    movie_storyline (str): Brief description of the movie
    poster_image (str): Image url of movie poster
    trailer_youtube (str): YouTube url of movie trailer

    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
