from video_capture import VideoCapture
from object_detection import ObjectDetector
from video_writer import VideoWriter
from display import Display
import cv2
import datetime

def main():
    cap = VideoCapture()
    detector = ObjectDetector()
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # 原始视频的输出文件路径和名称
    original_output_file = f"C:/Users/86187/Desktop/视觉识别/原视频_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.avi"
    original_writer = VideoWriter(original_output_file, fourcc, 30.0, (640, 480))

    # 目标检测后视频的输出文件路径和名称
    output_file = f"C:/Users/86187/Desktop/视觉识别/检测后视频_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.avi"
    writer = VideoWriter(output_file, fourcc, 30.0, (640, 480))
    display = Display('Annotated Frame', (640, 480))

    while True:
        success, frame = cap.read()
        if success:
            # 写入原始视频帧
            original_writer.write(frame)
            # 进行目标检测
            annotated_frame = detector.detect(frame)
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cv2.putText(annotated_frame, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            writer.write(annotated_frame)
            display.show(annotated_frame)
            if display.wait_key(1) == ord('q'):
                break
        else:
            break

    cap.release()
    original_writer.release()
    writer.release()
    display.destroy()

if __name__ == '__main__':
    main()
