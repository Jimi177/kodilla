import random

class Film():
    def __init__(self, title, release_date, type, play_counter):
        self.title = title
        self.release_date = release_date
        self.type = type
        self.play_counter = play_counter

        def play(self):
            self.play_counter += 1

        def __str__(self):
            return f"{self.title}{self.relese_date}"

class Serial(Film):
    def __init__(self,epizode_number,seson_number):
        self.epizod_number = epizode_number
        self.seson_number = seson_number

        def __str__(self):
            return f"{self.title} S0{self.seson_number}E0{self.epizode_number}"

videos_list = []

def get_movies(videos_list):
    movie_list = []
    for video in videos_list:
        if video.seson_number:
            pass
        else:
            movie_list.append(video)

    return sorted(movie_list, key=lambda movie: movie.tilte)

def get_series(videos_list):
    series_list = []
    for video in videos_list:
        if video.seson_number:
            series_list.append(video)

    return sorted(series_list, key=lambda series: series.tilte)

def search(videos_list):
    title = input("Please write tilte of the video: ")
    for video in videos_list:
        if video.tilte == title:
            print(title,"exists in our videos list")

def generate_views(videos_list):
    amount_of_videos = len(videos_list)
    random_video = random.randint(0, amount_of_videos)
    random_int = random.randint(1,100)
    videos_list[random_video].play_counter += random_int
    print(f"Added{random_int}views to{videos_list[random_video]}")

def generate_views_x10(videos_list):
    for _ in range(0,10):
        amount_of_videos = len(videos_list)
        random_video = random.randint(0, amount_of_videos)
        random_int = random.randint(1, 100)
        videos_list[random_video].play_counter += random_int
        print("Added", random_int, "views to ", videos_list[random_video])

def top_titles(videos_list):
    series_list = []
    films_list = []

    amount_of_videos = input("How many top videos")
    content_type = input("List of series or films?: ")
    temp_number = 1

    for video in videos_list:
        if video.seson_number:
            series_list.append(video)
        else:
            films_list.append(video)

    if content_type == "series":
        sorted_list_series = sorted(series_list, key=lambda series: series.play_counter)

        for _ in range(0,amount_of_videos):
            print(temp_number,". ",sorted_list_series[temp_number])
            temp_number+=1
    elif content_type == "films":
        sorted_list_films = sorted(films_list, key=lambda films: films.play_counter)

        for _ in range(0, amount_of_videos):
            print(temp_number, ". ", sorted_list_films[temp_number])
            temp_number += 1

