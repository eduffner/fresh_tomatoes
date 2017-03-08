import media
import fresh_tomatoes

shawshank_redemption = media.Movie("Shawshank Redemption",
								   "Fear can hold you prisoner. Hope can set you free.",
								   "https://www.youtube.com/watch?v=6hB3S9bIaco",
								   "http://www.impawards.com/1994/posters/shawshank_redemption_ver2.jpg")

saved = media.Movie("Saved",
					"Got Passion? Get Saved. 5:28",
					"https://www.youtube.com/watch?v=je18yGc6jXk",
					"http://images2.fanpop.com/image/photos/14100000/Movie-Poster-saved-14124914-682-1023.jpg")

brokeback_mountain = media.Movie("Brokeback Mountain",
								 "Love Is A Force Of Nature",
								 "https://www.youtube.com/watch?v=-xuugq7fito",
								 "http://www.impawards.com/2005/posters/brokeback_mountain.jpg")

green_mile = media.Movie("Green Mile",
						 "Walk a mile you'll never forget.",
						 "https://www.youtube.com/watch?v=uDybmxbKf4Ys",
						 "http://www.impawards.com/1999/posters/green_mile_ver3_xlg.jpg")

ten_things_i_hate_about_you = media.Movie("10 Things I Hate About You",
										  "How do I loathe thee? Let me count the ways.",
										  "https://www.youtube.com/watch?v=AWmjzCZr0Jw",
										  "http://abcnews.go.com/images/Entertainment/REX_10_things_cast_jtm_141117.jpg")

finding_nemo = media.Movie("Finding Nemo",
						   "There are 3.7 trillion fish in the ocean. They're looking for one.",
						   "https://www.youtube.com/watch?v=wZdpNglLbt8",
						   "https://d35fkdjhhgt99.cloudfront.net/static/use-media-items/17/16316/full-900x1300/56702cc2/pva6ds.jpeg?resolution=0")

movie_list = [shawshank_redemption, saved, brokeback_mountain, green_mile, ten_things_i_hate_about_you, finding_nemo]
fresh_tomatoes.open_movies_page(movie_list)
