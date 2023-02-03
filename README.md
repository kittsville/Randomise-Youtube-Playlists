# Randomise YouTube Playlists

I needed to randomly order the videos in a large YouTube playlist. I'd made a playlist with videos from various creators but didn't want to watch blocks all from the same creator.

Why not just shuffle? This would change the order every time, which both fails to allow me to pick up from where I left off and would result in repeated videos. I need to re-order the playlist itself randomly and only once.

It seems like a simple tool that would exist but I couldn't find one, so I made one.

## Requirements

Python 3 + `pip install -r requirements.txt`

## Usage

```bash
python randomise.py $CLIENT_ID $CLIENT_SECRET $PLAYLIST_ID
```
