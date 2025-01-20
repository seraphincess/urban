import time
from time import sleep


class User:
    def __init__(self, nickname: str, password: str, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if None == self.current_user:
            for user in self.users:
                if user.nickname == nickname and hash(password) == hash(user.password):
                    self.current_user = user
        else:
            print('Вы уже авторизованы')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        self.users.append(User(nickname, password, age))
        self.current_user = User(nickname, password, age)

    def log_out(self):
        if None != self.current_user:
            self.current_user = None
        else:
            print('Вы не были авторизованы')

    def add(self, *videos):
        for video in videos:
            for movies in self.videos:
                if movies.title == video.title:
                    return
            self.videos.append(video)

    def get_videos(self, search):
        list_videos = []
        for video in self.videos:
            if search.lower() in video.title.lower():
                list_videos.append(video.title)
        return list_videos

    def watch_video(self, name):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for list in self.videos:
                if list.title == name:
                    if self.current_user.age < 18 and list.adult_mode == True:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for list.time_now in range(list.time_now, list.duration+1):
                            print(list.time_now, end=" ")
                            list.time_now += 1
                            sleep(1)
                        print('Конец видео')



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 2)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2, v3)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')