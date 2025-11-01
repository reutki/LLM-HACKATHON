import cv2
import numpy as np
import os

def ensure_output_folder(output_folder):
    """Create the output folder if it doesn't exist."""
    os.makedirs(output_folder, exist_ok=True)

def process_video(path, out_prefix, cfg):
    """Process a single video and return the output image path and the trace image array."""
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print(f"Cannot open: {path}")
        return None, None

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * cfg['DOWNSCALE'])
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * cfg['DOWNSCALE'])
    accum = np.zeros((h, w), dtype=np.uint8)

    if cfg['USE_MOG2']:
        backSub = cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=16, detectShadows=False)
    else:
        ret, prev = cap.read()
        if not ret:
            return None, None
        prev = cv2.resize(prev, (w, h))
        prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_idx += 1
        if frame_idx % cfg['FRAME_SKIP'] != 0:
            continue

        frame = cv2.resize(frame, (w, h))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if cfg['USE_MOG2']:
            fg = backSub.apply(gray)
            _, fg = cv2.threshold(fg, 200, 255, cv2.THRESH_BINARY)
        else:
            diff = cv2.absdiff(gray, prev_gray)
            _, fg = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
            prev_gray = gray

        fg = cv2.medianBlur(fg, 5)
        contours, _ = cv2.findContours(fg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            if cv2.contourArea(c) < cfg['MIN_AREA']:
                continue
            M = cv2.moments(c)
            if M["m00"] > 0:
                cx, cy = int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])
                cv2.circle(accum, (cx, cy), cfg['CIRCLE_RADIUS'], 255, -1)

        if cfg['SHOW_PROGRESS'] and frame_idx % (cfg['FRAME_SKIP']*50) == 0:
            cv2.imshow("trail", accum)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    if cfg['SHOW_PROGRESS']:
        cv2.destroyAllWindows()

    acc_norm = cv2.normalize(accum, None, 0, 255, cv2.NORM_MINMAX)
    _, thresh = cv2.threshold(acc_norm, 20, 255, cv2.THRESH_BINARY)

    base = os.path.join(cfg['OUTPUT_FOLDER'], out_prefix)
    trace_path = base + "_trace.png"
    cv2.imwrite(trace_path, thresh)
    print(f"{out_prefix}: Trace image saved.")
    return trace_path, thresh
