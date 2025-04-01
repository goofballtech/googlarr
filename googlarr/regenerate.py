import sys
import os
from plexapi.server import PlexServer
from googlarr.config import load_config
from googlarr.prank import (
    initialize_detector_and_overlay,
    generate_prank_poster,
    download_poster
)
from googlarr.db import update_item_status

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m googlarr.regenerate <ratingKey>")
        sys.exit(1)

    rating_key = sys.argv[1]
    config = load_config()
    initialize_detector_and_overlay(config['detection'])
    plex = PlexServer(config['plex']['url'], config['plex']['token'])

    # Find the item by ID
    try:
        item = plex.fetchItem(int(rating_key))
    except Exception as e:
        print(f"Failed to find item with ratingKey {rating_key}: {e}")
        sys.exit(1)

    title = item.title
    item_id = str(item.ratingKey)
    original_path = f"{config['paths']['originals_dir']}/{item_id}.jpg"
    prank_path = f"{config['paths']['prank_dir']}/{item_id}.jpg"

    # Download original if missing
    if not os.path.exists(original_path):
        print(f"Downloading original poster for '{title}'...")
        download_poster(plex, {'title': title}, original_path, config)

    # Regenerate prank
    print(f"Generating prank poster for '{title}'...")
    generate_prank_poster(original_path, prank_path, config)

    print(f"Done. Prank poster saved to {prank_path}")

if __name__ == "__main__":
    main()

