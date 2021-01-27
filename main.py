from Playlist import Playlist

# For the purposes of testing, automatically add some test songs to a playlist object
playlist = Playlist()
playlist.add_song('A')
playlist.add_song('B')
playlist.add_song('C')
playlist.add_song('D')
playlist.add_song('E')
playlist.add_song('F')

while True:

  # Prints welcome message and options menu
  print('''

  Welcome to Playlist Maker 🎶  

  =====================================
  Options:
  1: View playlist
  2: To add a new song to playlist
  3: To remove a song from playlist
  4: To search for song in playlist
  5: Return the length of the playlist
  =====================================

  ''')

  # Prints welcome message and options menu
  selection = input('Enter one of the 5 options:  ')

  # Prevent user from entering non-integers
  try:
    user_selection = int(selection)

    # Option 1: View playlist
    if user_selection == 1:

      # Inform the user if they tried to print an empty playlist
      if playlist.print_songs() == False:
        print('No songs in playlist.')


    # Option 2: To add a new song to playlist
    elif user_selection == 2:
      song_title = input('What song do you want to add? ')
      playlist.add_song(song_title)


    # Option 3: To remove a song from playlist
    elif user_selection == 3:
      song_title = input('What song do you want to remove? ')

      # Inform the user if their query failed to match any objects
      if playlist.remove_song(song_title) == False:
        print(f'No match for {song_title} found.')
      else:
        print(f'{song_title} removed.')


    # Option 4: To search for song in playlist
    elif user_selection == 4:

      song_title = input('Which song do you want to find? ')
      index = playlist.find_song(song_title)
      
      # Inform the user if their query failed to match any objects
      if index == -1:
        print(f"The song {song_title} is not in the set list.")

      # Print song name with index+1 for the non comp-sci numbering system oriented folks
      else:
        print(f"The song {song_title} is song number {index+1}")


    # Option 5: Return the length of the playlist
    elif user_selection == 5:
      print(f"This set list has {playlist.length()} songs.")

    # Message for invalid input
    else:
      print('That is not a valid option. Try again.\n')
  
  # Reprimand the user
  except:
    print("Only number inputs are valid. C'mon man, it's not that hard.\n")