# Step 1: Create the playlist dictionary
playlist = {}

# Step 2: Define the 'add_song' function
def add_song(title, artist, genre):
    """Adds a new song to the playlist."""
    if title in playlist:
        print(f"Error: '{title}' is already in the playlist.")
    else:
        playlist[title] = {'artist': artist, 'genre': genre}
        print(f"Added: '{title}' by {artist} (Genre: {genre})")

# Step 3: Define the 'view_playlist' function
def view_playlist():
    """Displays all songs in the playlist."""
    if not playlist:
        print("\nThe playlist is empty.\n")
    else:
        print("\n--- Your Playlist ---")
        for title, details in playlist.items():
            artist = details.get('artist', 'Unknown Artist')
            genre = details.get('genre', 'Unknown Genre')
            print(f"Title: {title} | Artist: {artist} | Genre: {genre}")
        print("---------------------\n")

# Step 4: Define the 'update_song' function
def update_song(title, artist=None, genre=None):
    """Updates the artist and/or genre of a specific song."""
    if title not in playlist:
        print(f"Error: '{title}' is not in the playlist.")
    else:
        if artist:
            playlist[title]['artist'] = artist
            print(f"Updated artist for '{title}' to {artist}.")
        if genre:
            playlist[title]['genre'] = genre
            print(f"Updated genre for '{title}' to {genre}.")
        if not artist and not genre:
            print("No changes were made. Provide either an artist or a genre to update.")

# Step 5: Define the 'delete_song' function
def delete_song(title):
    """Removes a song from the playlist."""
    if title in playlist:
        del playlist[title]
        print(f"Removed: '{title}' from the playlist.")
    else:
        print(f"Error: '{title}' is not in the playlist.")

# Step 6: Testing the functions
if __name__ == "__main__":
    # Add songs to the playlist
    print("Adding Songs:")
    add_song("Billie Jean", "Michael Jackson", "Pop")
    add_song("In Da Club", "50 Cent", "Hip Hop")
    add_song("Halo", "Beyoncé", "R&B")
    add_song("Billie Jean", "Michael Jackson", "Pop")  # Test duplicate

    # View the playlist
    print("\nViewing Playlist:")
    view_playlist()

    # Update a song
    print("Updating Songs:")
    update_song("Billie Jean", genre="Pop Classic")
    update_song("In Da Club", artist="Curtis Jackson")
    update_song("Nonexistent Song", artist="Unknown")  # Test non-existent song
    update_song("Halo")  # Test no update parameters

    # View the updated playlist
    print("\nViewing Updated Playlist:")
    view_playlist()

    # Delete a song
    print("Deleting Songs:")
    delete_song("In Da Club")
    delete_song("Nonexistent Song")  # Test deleting non-existent song

    # View the final playlist
    print("\nViewing Final Playlist:")
    view_playlist()
