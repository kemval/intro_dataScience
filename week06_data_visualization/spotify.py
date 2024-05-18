import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import plotly.express as px

# Set your Spotify API credentials
client_id = '2a4bb94964e24faf8c455c1cb6cfcdd9'
client_secret = 'f6bfc8affd1f461090696be1d2205f7d'

# Initialize Spotipy with your credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Get the top tracks for a specific artist 
artist_name = 'The Neighbourhood'
results = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)

if results['artists']['items']:
    artist_id = results['artists']['items'][0]['id']
    top_tracks = sp.artist_top_tracks(artist_id)['tracks']

    # Create a DataFrame with the Spotify data
    df_spotify = pd.DataFrame({
        'Track': [track['name'] for track in top_tracks],
        'Popularity': [track['popularity'] for track in top_tracks],
        'Release Date': [track['album']['release_date'] for track in top_tracks]
    })

    # Create an interactive bar chart
    fig = px.bar(df_spotify, x='Track', y='Popularity', color='Popularity',
                 hover_data=['Release Date'],
                 title=f'Top Tracks of {artist_name} on Spotify',
                 labels={'Popularity': 'Popularity Score'})

    # Update layout for better interactivity
    fig.update_layout(
        xaxis=dict(title='Track'),
        yaxis=dict(title='Popularity Score'),
        hovermode='x',  # Display closest data point on hover
    )

    # Show the figure
    fig.show()
else:
    print(f"No results found for artist: {artist_name}")
