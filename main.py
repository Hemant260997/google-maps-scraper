from src import Gmaps

love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/'''

queries = [
   "Blue metals in Tamil nadu"
]

Gmaps.places(queries, max=5)
