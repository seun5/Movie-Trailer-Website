import media
import fresh_tomatoes

movie = []

# Kingsman 1
movie.append(media.Movie("343668"))
# Starwars 5
movie.append(media.Movie("1891"))
# Darkknight
movie.append(media.Movie("155"))

# Inception
movie.append(media.Movie("27205"))

# Harry Potter
movie.append(media.Movie("671"))
movie.append(media.Movie("672"))
movie.append(media.Movie("673"))
movie.append(media.Movie("674"))
movie.append(media.Movie("675"))

# Midnight_in_Paris
movie.append(media.Movie("59436"))

# Martian
movie.append(media.Movie("286217"))

# LotR
movie.append(media.Movie("120"))
movie.append(media.Movie("121"))
movie.append(media.Movie("122"))

fresh_tomatoes.open_movies_page(movie)
