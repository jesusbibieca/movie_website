import media, fresh_tomatoes

toy_story = media.Movie('Toy Story', 'A story of a boy and his toys', 
	'https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg',
	'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar', 'A marine on an alien planet',
	'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
	'https://www.youtube.com/watch?v=5PSNL1qE6VY')

# print avatar.storyline
# avatar.show_trailer()
movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
 