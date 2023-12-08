import random

class Song:
    def __init__(self, artist, title, duration):
        self.artist = artist
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.duration})"
    

class Playlist:
    def __init__(self, name):
        self.name = name
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
        else:
            print(f"{song.title} is not in playlist.")
    
    def shuffle(self):
        random.shuffle(self.playlist)
    
    def display_playlist(self):
        print(f"playlist: {self.name}")
        for index, song in enumerate(self.playlist, start=1):
            print(f"{index}. {song}")

class MusicPlayer:
    def __init__(self):
        self.current_song = None
        self.playlist = None

    def create_playlist(self, name):
        self.playlist = Playlist(name)
    
    def add_song_to_playlist(self, song):
        if self.playlist:
            self.playlist.add_song(song)
        else:
            print("Create a playlist first.")

    def shuffle_playlist(self):
        if self.playlist:
            self.playlist.shuffle()
            print("Playlist shuffled.")
        else:
            print("Create playlist first.")
    
    def play_song(self, song):
        if self.current_song:
            self.current_song = song
            print(f"Now playing: {self.current_song}")
        else:
            print(f"{song.title} is not in playlist.")
    
    def display_current_song_info(self):
        if self.current_song:
            print(self.current_song)
        else:
            print("No song is currently playing.")

    def repeat_song(self):
        if self.current_song:
            print(f"Repeating: {self.current_song}")
        else:
            print("No song is currently playing.")
    
    def play_random_song(self):
        if self.playlist:
            if self.playlist.playlist:
                random_song = random.choice(self.playlist.playlist)
                self.current_song = random_song
                print(f"Now playing: {self.current_song}")
            else:
                print("The playlist is empty.")
        else:
            print("Create a playlist first.")


# Example usage:
song1 = Song("Shape of You", "Ed Sheeran", "3:53")
song2 = Song("Dance Monkey", "Tones and I", "3:30")
song3 = Song("Someone Like You", "Adele", "4:45")

player = MusicPlayer()
player.create_playlist("My Playlist")
player.add_song_to_playlist(song1)
player.add_song_to_playlist(song2)
player.add_song_to_playlist(song3)

player.playlist.display_playlist()

player.shuffle_playlist()
player.display_current_song_info()

player.play_song(song2)
player.display_current_song_info()

player.play_random_song()
player.display_current_song_info()