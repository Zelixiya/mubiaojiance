import cv2
import datetime
import psutil

class VideoWriter:
    def __init__(self, output_path, fourcc, fps, frame_size):
        self.output_path = output_path
        self.fourcc = fourcc
        self.fps = fps
        self.frame_size = frame_size
        self.out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)
        self.last_write_time = datetime.datetime.now()

    def write(self, frame):
        current_time = datetime.datetime.now()
        if (current_time - self.last_write_time).seconds > 60:
            # 检测磁盘可用空间
            disk_usage = psutil.disk_usage(self.output_path)
            if disk_usage.free < 4 * 1024 * 1024 * 1024:  # 4GB in bytes
                self.out.release()
                self.out = cv2.VideoWriter(self.output_path, self.fourcc, self.fps, self.frame_size)
            self.last_write_time = current_time
        self.out.write(frame)

    def release(self):
        self.out.release()


