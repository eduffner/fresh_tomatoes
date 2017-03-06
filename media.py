import webbrowser

class Media():
	def __init__(self, title):
		self.title = title

class Movie(Media):
	def __init__(self, movie_title, movie_storyline, trailer_youtube_url, poster_image):
		self.title = movie_title
		self.storyline = movie_storyline
		self.trailer_youtube_url = trailer_youtube_url
		self.poster_image_url = poster_image

	def show_trailer(self):
		webbrower.open(self.trailer_url)
