
# YTMusicify by itisFarzin

A script that syncs your Spotify liked songs to a YouTube Music playlist.

## Requirements

- Python 3 (Tested on Python 3.12)
- Install the necessary Python libraries:
  - `ytmusicapi` for interacting with YouTube Music.
  - `spotipy` for interacting with the Spotify API.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/itisFarzin/YTMusicify.git
   cd YTMusicify
   ```

2. **Create a virtual environment** (recommended):
   - If you don’t have `virtualenv` installed, first install it:

     ```bash
     pip install virtualenv
     ```

   - Create a virtual environment:

     ```bash
     virtualenv venv
     ```

   - Activate the virtual environment:
     - On Windows:

       ```bash
       .\venv\Scripts\activate
       ```

     - On macOS/Linux:

       ```bash
       source venv/bin/activate
       ```

3. Set up your environment variables:
   - Copy the example `.env` file to `.env`:

     ```bash
     cp .env.example .env
     ```

   - Open the `.env` file and set the following variables with your credentials:

     ```
     SLEEP_TIME=5
     SPOTIFY_CLIENT_ID=your_spotify_client_id
     SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
     SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
     YOUTUBE_CLIENT_ID=your_oauth_client_secret  # Or use the browser method and set this to empty
     YOUTUBE_CLIENT_SECRET=your_oauth_client_secret  # Or use the browser method and set this to empty
     PROXY=socks5://127.0.0.1:8080  # Optional
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the APIs:
   - Follow the setup guide for [ytmusicapi](https://ytmusicapi.readthedocs.io/en/1.9.0/setup/index.html) to configure access to YouTube Music.
   - Follow the setup guide for [Spotipy](https://spotipy.readthedocs.io/en/2.24.0/#getting-started) to configure access to Spotify.
   - You **must** set "http://localhost:8888/callback" as the redirect uri in your Spotify application.

## Usage

Once the setup is complete, you can run the script to sync your Spotify liked songs to YouTube Music:

```bash
python main.py
```

This will authenticate with both Spotify and YouTube Music APIs and sync your liked songs from Spotify to a YouTube Music playlist. (It will take a while so be pension)

## Proxy (Optional)

If you're using a proxy, ensure the `PROXY` variable is set in your `.env` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
