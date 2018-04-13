from fresh_tomatoes import open_movies_page
from media import Movie


bottle_rocket = Movie("Bottle Rocket",
    "\"Here are just a few of the key ingredients: dynamite, pole vaulting, laughing gas, choppers...\"",
    "http://rushmoreacademy.com/wp-content/uploads/2011/07/BottleRocketOnline1.jpeg",
    "https://www.youtube.com/watch?v=hspUSez-rYY")

il_posto = Movie("Il Posto",
    "\"A very young college graduate attempts to obtain a position with a large corporation.\"",
    "https://media-cache.cinematerial.com/p/500x/0zkokvl2/il-posto-french-movie-poster.jpg",
    "https://www.youtube.com/watch?v=iYJwm4DlKU0")

dr_strangelove = Movie("Dr. Strangelove",
    "\"An insane general triggers a path to nuclear holocaust that a war room full of politicians and generals frantically tries to stop.\"",
    "https://www.movieruntime.com/wp-content/uploads/2017/09/tviJ68Wj4glQk3CPMvdvExYHxX.jpg",
    "https://www.youtube.com/watch?v=IE9CmX15PYA")

true_stories = Movie("True Stories",
    "\"A small but growing Texas town [...] celebrates its sesquicentennial and converge on a local parade and talent show.\"",
    "https://fiu-assets-2-syitaetz61hl2sa.stackpathdns.com/static/use-media-items/31/30476/full-736x1120/567022c9/53d3394034a8c13d99d755c81879c4ea.jpeg?resolution=0",
    "https://www.youtube.com/watch?v=mhRgCsQf3CU")

la_jetee = Movie("La Jetée",
    "\"The story of a man forced to explore his memories in the wake of World War III's devastation, told through still images.\"",
    "https://intermediodvd.files.wordpress.com/2011/08/la-jetee-poster-2.jpg",
    "https://www.youtube.com/watch?v=9GENscwqjzY")

big_trouble_in_little_china = Movie("Big Trouble in Little China",
    "\"An All-American trucker gets dragged into a centuries-old mystical battle in Chinatown.\"",
    "https://alchetron.com/cdn/Big-Trouble-in-Little-China-images-102f975a-a9d2-4ea4-a7e8-244cc437116.jpg",
    "https://www.youtube.com/watch?v=592EiTD2Hgo")

# Store movie class instances in a list.
movies = [bottle_rocket, il_posto, dr_strangelove, true_stories, la_jetee, big_trouble_in_little_china]

# Open movie website with class list as a passed argument.
if __name__ == '__main__':
    open_movies_page(movies)