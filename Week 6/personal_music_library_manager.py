songs = []
genre_count = {}

print ("Welcome to Music Library Manager")

ans=True
while ans:
    print("\nMusic Library Menu:")
    print("1. Make a new Music Library")
    print("2. View My Music Library")
    print("3. View Genre Statistics")
    print("4. Exit")

    ans=input("Enter your choice: ")

    if ans == '1':
        for i in range(1, 6):
            print(f"Enter Song {i}:")
            song_title = input(" Song Title: ")
            genre = input(" Genre: ")
            artist = input(" Artist: ")
            print()
            song_library = (song_title, genre, artist)
            songs.append(song_library)
            genre_count[genre] = genre_count.get(genre, 0) + 1
    if ans == '2':
        print('===YOUR MUSIC LIBRARY===')
        for index, (song_title, genre, artist) in enumerate(songs, start=1):
            print(f'{index}. {song_title}, by {artist}, ({genre})')
    if ans == '3':
        print('===GENRE STATISTICS===')
        print(f'Most popular genre: {max(genre_count, key=genre_count.get)}')
    elif ans == '4':
        print("\nExiting...")
        break
