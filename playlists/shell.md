from playlists.models import Playlist
from videos.models import Video

# Create your tests here.

video_a = Video.objects.create(title='My Title', video_id='abc123')
playlist_a = Playlist.objects.create(title='This is my title', video=video_a)
