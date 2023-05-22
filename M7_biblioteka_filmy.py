import random


class Film:
    def __init__(self, title, release_date, film_type, play_counter):
        self.title = title
        self.release_date = release_date
        self.film_type = film_type
        self.play_counter = play_counter

    def play(self):
        self.play_counter += 1

    def __str__(self):
        return f"{self.title} ({self.release_date})"


class Serial(Film):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        if self.season_number >= 10 and self.episode_number >= 10:
            return f"{self.title} S{self.season_number}E{self.episode_number}"
        elif self.season_number >= 10:
            return f"{self.title} S{self.season_number}E0{self.episode_number}"
        elif self.episode_number >= 10:
            return f"{self.title} S0{self.season_number}E{self.episode_number}"
        else:
            return f"{self.title} S0{self.season_number}E0{self.episode_number}"


videos_list = []


def get_movies(videos_list):
    movie_list = []
    for video in videos_list:
        if isinstance(video, Film):
            movie_list.append(video)
    return sorted(movie_list, key=lambda movie: movie.title)


def get_series(videos_list):
    series_list = []
    for video in videos_list:
        if isinstance(video, Serial):
            series_list.append(video)
    return sorted(series_list, key=lambda series: series.title)


def search(videos_list, search_phrase):
    for video in videos_list:
        if video.title == search_phrase:
            return video
    return None


def generate_views(videos_list):
    random_video = random.choice(videos_list)
    random_int = random.randint(1, 100)
    random_video.play_counter += random_int
    print(f"Added {random_int} views to {random_video}")


def generate_views_x10(videos_list):
    for _ in range(10):
        random_video = random.choice(videos_list)
        random_int = random.randint(1, 100)
        random_video.play_counter += random_int
        print(f"Added {random_int} views to {random_video}")


def top_titles(videos_list, content_type, amount_of_videos):
    if content_type == "series":
        series_list = get_series(videos_list)
        sorted_list_series = sorted(series_list, key=lambda series: series.play_counter, reverse=True)
        return sorted_list_series[:amount_of_videos]

    elif content_type == "films":
        films_list = get_movies(videos_list)
        sorted_list_films = sorted(films_list, key=lambda film: film.play_counter, reverse=True)
        return sorted_list_films[:amount_of_videos]


if __name__ == "__main__":
    Avatar = Film(title="Avatar", release_date="19.03.2000", film_type="Film", play_counter=1233210)
    Avatar_Legenda_Anga = Serial(
        episode_number=11, season_number=3, title="Avatar: The Last Airbender", release_date="20.04.2005",
        film_type="Series", play_counter=94500
    )
    videos_list.append(Avatar)
    videos_list.append(Avatar_Legenda_Anga)

    generate_views_x10(videos_list)

