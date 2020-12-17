# The code below models a spotify playlist using lists and dictionaries

# Create a dictionary to store the playlist information
# This is a more real-world application of how lists and dictionaries are used interchangebly
# A big use for Python is Data Modeling
playlist = {
    'title': 'patagonia bus', 
    'author': 'patrick apgar',
    'songs' : [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
        {'title': 'song2', 'artist': ['garfield'], 'duration': 2.0},
        {'title': 'song3', 'artist': ['green'], 'duration': 2.5},
        {'title': 'song4', 'artist': ['red'], 'duration': 2.45},
        {'title': 'song5', 'artist': ['kitty', 'djcat'], 'duration': 5.25}
    ]
}

total_duration = 0
for song in playlist['songs']:
    total_duration += song['duration']

print(total_duration)