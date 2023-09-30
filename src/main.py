import argparse
from config import get_api_credentials
from utility import setup_logger, get_music_folder_path
from savify import Savify
from savify.types import Type, Format, Quality
from savify.utils import PathHolder

def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(description='Spotify song downloader')
    parser.add_argument('song_url', help='URL of the Spotify song')
    parser.add_argument('--format', choices=['MP3', 'AAC', 'FLAC', 'M4A', 'OPUS', 'VORBIS', 'WAV'],
                        default='FLAC', help='Download format (default: FLAC)')
    parser.add_argument('--new-credentials', action='store_true',
                        help='Force to input new Spotify API credentials')

    args = parser.parse_args()

    client_id, client_secret = get_api_credentials()

    s = Savify(api_credentials=(client_id, client_secret),
               quality=Quality.BEST, download_format=getattr(Format, args.format),
               path_holder=PathHolder(downloads_path=get_music_folder_path()), logger=logger)

    s.download(args.song_url, query_type=Type.TRACK)

if __name__ == "__main__":
    main()
