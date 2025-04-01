# Googlarr

> A chaotic and deeply unnecessary tool that applies googly eyes to your Plex posters on a schedule.  
> You were warned.

---

## WARNING — THIS PROJECT MAY RUIN YOUR POSTERS

Googlarr uses the Plex API to modify the posters for your Plex media items **in place**. It tries to save and restore the originals, but:

- It might miss a poster
- It might fail to restore properly
- Plex might cache something weird
- You might regret everything

**Use at your own risk. This project is for prank purposes only. I cannot provide support in case of failure.**

---

## What It Does

Googlarr is a scheduled prank daemon that:

1. Scans your Plex libraries for movies and/or shows
2. Detects faces and eye positions in poster images
3. Applies googly eyes using image overlays
4. Swaps the posters on a cron-based schedule
5. Restores the originals after the prank window

---

## Setup

1. Install via Docker Compose (see included `docker-compose.yml`)
2. Configure your `config.yml`
3. `docker compose up -d`
4. Pray

---

## Example Config

```yaml
plex:
  url: http://your.plex.server:32400
  token: your_plex_token
  libraries:
    - Movies
    - TV Shows

paths:
  originals_dir: data/originals
  prank_dir: data/prank

database: "data/googlarr.db"

schedule:
  on: "0 9 * * *"    # Apply prank at 9am daily
  off: "0 17 * * *"  # Restore at 5pm daily

detection:
  face_detection_confidence: 0.5
  landmark_detection_confidence: 0.5
  scale_by_face_size: true
  face_based_eye_scale: 0.35
  use_same_size_for_both_eyes: true
  debug_draw_faces: false
```

## Development

Portions of this project were created with ChatGPT code generation. I am a veteran software engineer however, and have code inspected the output and run extensive testing on multiple libraries.

## License
MIT. See `LICENSE`.

Portions of `overlay.py` and `detector.py` were adapted from MIT-licensed sources. See `LICENSES/` for attribution.
