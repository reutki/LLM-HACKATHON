
from video_utils import ensure_output_folder, process_video
import os

def get_config():
    """Return configuration parameters as a dictionary."""
    return {
        'INPUT_FOLDER': "/Users/dcambur/Public/hackathon/videos/track_the_thief/",
        'OUTPUT_FOLDER': "out_letters",
        'FRAME_SKIP': 15,            # process every 20th frame
        'DOWNSCALE': 0.6,            # resize factor
        'MIN_AREA': 40,              # min contour area to treat as car
        'USE_MOG2': True,            # use background subtractor
        'CIRCLE_RADIUS': 1,          # radius of the dot drawn per frame
        'SHOW_PROGRESS': False       # set True for debug preview
    }

def process_all_videos(cfg):
    """Process all videos in the input folder, print results, and run OCR on traces."""
    vids = [v for v in os.listdir(cfg['INPUT_FOLDER'])
            if v.lower().endswith((".mp4", ".avi", ".mov", ".mkv"))]
    vids.sort()
    print(f"Found {len(vids)} videos in {cfg['INPUT_FOLDER']}")
    for i, v in enumerate(vids):
        path = os.path.join(cfg['INPUT_FOLDER'], v)
        out_prefix = f"video_{i+1}"
        
        print(f"[{i+1}/{len(vids)}] Processing {v} ...")
        process_video(path, out_prefix, cfg)

def main():
    cfg = get_config()
    ensure_output_folder(cfg['OUTPUT_FOLDER'])
    process_all_videos(cfg)

if __name__ == "__main__":
    main()
