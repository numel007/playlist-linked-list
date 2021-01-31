from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):

    # Create an object and assign it to new_song
    new_song = Song(title)

    # Capitalize title
    new_song.set_title(title)

    # Move the pointer for the next song to point at the previously new song
    new_song.set_next_song(self.__first_song)

    # Set the first song equal to the new song
    self.__first_song = new_song
    

  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameter, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):

    # Keep track of the index
    index = 0

    # Start tracking from the first song
    current_song = self.__first_song

    # Detect if the playlist is empty and return -1
    if current_song == None:
      return -1

    # Iterate through the song objects while their titles are not the input title
    while current_song.get_title() != str(title):

      # Increase index by 1
      index += 1

      # Set current song to the next song
      current_song = current_song.get_next_song()

      # Return -1 if the end of the list is reached with no matches
      if current_song == None:
        return -1

    # Return the index of the detected song
    return index


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):

    # Keep track of the previous and current song
    previous_song = self.__first_song
    current_song = self.__first_song

    # Detect if the current song is the head
    if current_song.get_title() == title:
      
      # Change the first song in the object list to be the second song, deleting the first song in the process
      self.__first_song = self.__first_song.get_next_song()

      # Immediately exit so now useless below code is not executed
      return


    # Iterate through the linked objects until a match is found, in the cases where the query is not the first object
    while current_song.get_title() != title:

      # Store previous song before advancing current song
      previous_song = current_song

      # Advance current song to next song
      current_song = current_song.get_next_song()

      # If no more objects are detected, return false
      if current_song == None:
        return False

    # When the song is detected, set pointer of previous song to current song's next song
    # 1 --> 2 --> X --> 4 --> 5
    #       |___________^
    # In this scenario, 3 is deleted by telling 2 that 4 is next in line rather than 3
    # Since previous_song.set_next_song() is set to the value after current_song, current_song has effectively been deleted
    previous_song.set_next_song(current_song.get_next_song())


  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):

    # Track length with a counter
    counter = 0

    # Start with the head
    current_song = self.__first_song

    # Detect if there are no song objects
    if current_song == None:
      return 0
    
    # Add 1 to counter until there are no more linked objects
    while current_song.get_title() != None:
      counter += 1
      current_song = current_song.get_next_song()

    return counter


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  def print_songs(self):

    # Use a counter to number each print statement for readability
    counter = 0

    # Start with the head
    current_song = self.__first_song

    # Detect if there are no objects
    if current_song == None:
      return False

    # Iterate through objects, increasing counter by 1 per object
    while current_song.get_title() != None:
      counter += 1
      print(f'{counter}. {current_song.get_title()}')
      current_song = current_song.get_next_song()

      # Kill loop when there are no more linked objects
      if current_song == None:
        break