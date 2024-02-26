import pyrealsense2 as rs
import numpy as np
import cv2

pipeline = rs.pipeline()
config = rs.config()

wrapper = rs.pipeline_wrapper(pipeline)
profile = config.resolve(wrapper)
device = profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))

found_rgb = False
for s in device.sensors:
    if s.get_info(rs.camera_info.name) == 'RGB Camera':
        found_rgb = True
        break
if not found_rgb:
    print("failed color")
    exit(0)

config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

pipeline.start(config)

try:
    while True:

        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            continue

        color_image = np.asanyarray(color_frame.get_data())

        color_colormap_dim = color_image.shape

        cv2.imshow('RealSense', color_image)
        if cv2.waitKey(1) == ord("q"):
            break
finally:
    print("stop streaming.")
    pipeline.stop()
