"""This module creates list of movies and show them on web page"""
from media import Movie
import fresh_tomatoes
# create movie instances
TOY_IMG = "https://m.media-amazon.com/images/I/618kQqoT2FL._SL500_.jpg"
TOY_URL = "https://www.youtube.com/watch?v=rNk1Wi8SvNc"
TOY = Movie.Movie("Toy story", TOY_IMG, TOY_URL)
AVATAR_IMG = "http://www.impawards.com/2009/posters/avatar_ver2.jpg"
AVATAR_URL = "https://www.youtube.com/watch?v=5PSNL1qE6VY"
AVATAR = Movie.Movie("Avatar", AVATAR_IMG, AVATAR_URL)
MAMA_COCO_IMG = "http://www.impawards.com/2017/posters/coco.jpg"
MAMA_COCO_URL = "https://www.youtube.com/watch?v=5sSMRg1X1vg"
MAMACOCO = Movie.Movie("Mama coco", MAMA_COCO_IMG, MAMA_COCO_URL)
RATAOUILLE_IMG = "http://www.impawards.com/2007/posters/ratatouille.jpg"
RATAOUILLE_URL = "https://www.youtube.com/watch?v=e8GBfNo3IHY"
RATATOUILLE = Movie.Movie("Ratatouille", RATAOUILLE_IMG, RATAOUILLE_URL)
MID_IMG = "http://www.impawards.com/2011/posters/midnight_in_paris.jpg"
MID_URL = "https://www.youtube.com/watch?v=x_XMltmF0IM"
MIDNIGHT = Movie.Movie("Midnight in paris", MID_IMG, MID_URL)
HUNGER_IMG = "http://www.impawards.com/2012/posters/hunger_games.jpg"
HUNGER_URL = "https://www.youtube.com/watch?v=FovFG3N_RSU"
HUNGER = Movie.Movie("Hunger games", HUNGER_IMG, HUNGER_URL)
# create movies list
MOVIES_LIST = [TOY, AVATAR, MAMACOCO, RATATOUILLE, MIDNIGHT, HUNGER]
# call open movie page function to render our page with movies list
fresh_tomatoes.open_movies_page(MOVIES_LIST)
