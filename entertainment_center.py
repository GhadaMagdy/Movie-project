"""This module creates list of movies and show them on web page"""
from media import Movie
import fresh_tomatoes
# create movie instances
TOY_STORY_POSTER = "https://m.media-amazon.com/images/I/618kQqoT2FL._SL500_.jpg"
TOY_STORY_TRAILER = "https://www.youtube.com/watch?v=rNk1Wi8SvNc"
TOY_STORY = Movie.Movie("Toy story", TOY_STORY_POSTER, TOY_STORY_TRAILER)
AVATAR_POSTER = "https://cdn.traileraddict.com/content/20th-century-fox/avatar-6.jpg"
AVATAR_TRAILER = "https://www.youtube.com/watch?v=5PSNL1qE6VY"
AVATAR = Movie.Movie("Avatar", AVATAR_POSTER, AVATAR_TRAILER)
MAMA_COCO_POSTER = "https://ohmy.disney.com/wp-content/uploads/2017/09/Coco_Payoff_IG_Jpeg_v7-1.jpg"
MAMA_COCO_TRAILER = "https://www.youtube.com/watch?v=5sSMRg1X1vg"
MAMA_COCO = Movie.Movie("Mama coco", MAMA_COCO_POSTER, MAMA_COCO_TRAILER)
RATAOUILLE_POSTER = "https://images-na.ssl-images-amazon.com/images/I/71VDlRubWtL._SL1000_.jpg"
RATAOUILLE_TRAILER = "https://www.youtube.com/watch?v=e8GBfNo3IHY"
RATATOUILLE = Movie.Movie("Ratatouille", RATAOUILLE_POSTER, RATAOUILLE_TRAILER)
MIDNIGHT_POSTER = "https://setinparis.com/wp-content/uploads/2014/05/Midnight-in-Paris.jpg"
MIDNIGHT_TRAILER = "https://www.youtube.com/watch?v=x_XMltmF0IM"
MIDNIGHT_IN_PARIS = Movie.Movie("Midnight in paris", MIDNIGHT_POSTER, MIDNIGHT_TRAILER)
HUNGER_POSTER = "http://i.ebayimg.com/00/s/NTAwWDMzNw==/z/~IkAAOxy7nNTVkmT/$_3.JPG?set_id=2"
HUNGER_TRAILER = "https://www.youtube.com/watch?v=FovFG3N_RSU"
HUNGER_GAMES = Movie.Movie("Hunger games", HUNGER_POSTER, HUNGER_TRAILER)
# create movies list
MOVIES_LIST = [TOY_STORY, AVATAR, MAMA_COCO, RATATOUILLE, MIDNIGHT_IN_PARIS, HUNGER_GAMES]
# call open movie page function to render our page with movies list
fresh_tomatoes.open_movies_page(MOVIES_LIST)
