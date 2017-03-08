import webbrowser

class Media():
	"""
	This class stores media data such as title
	"""
	def __init__(self, title):
		self.title = title

class Movie(Media):
	"""
	This class stores movie data such as storyline, trailer, and movie poster
	"""
	def __init__(self, movie_title, movie_storyline, trailer_youtube_url, poster_image):
		"""
		This method initializes and instance of the class Movie
		"""
		Media.__init__(movie_title)
		self.storyline = movie_storyline
		self.trailer_youtube_url = trailer_youtube_url
		self.poster_image_url = poster_image

	def show_trailer(self):
		"""
		This method opens a movie's trailer in a new browser window
		"""
		webbrower.open(self.trailer_url)
