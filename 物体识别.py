import cv2
from ultralytics import YOLO
import datetime
import time

def main():
   cap = cv2.VideoCapture(0)
   cv2.namedWindow('Annotated Frame', cv2.WINDOW_NORMAL)
   cv2.resizeWindow('Annotated Frame', 640, 480)
   model = YOLO("yolov8n.pt")
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   output_file = f"C:/Users/86187/Desktop/视觉识别/output_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.avi"
   out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))
   last_write_time = time.time()
   while True:
    current_time = time.time()
    if current_time - last_write_time > 60:  # 如果已经过了一分钟
        out.release()  # 释放之前的视频写入对象
        out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))  # 创建新的视频写入对象
        last_write_time = current_time
    success, frame = cap.read()
    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        annotated_frame = results[0].plot()
        cv2.putText(annotated_frame, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        out.write(annotated_frame)
        cv2.imshow('Annotated Frame', annotated_frame)  # 显示预测结果
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
   cap.release()
   out.release()
   cv2.destroyAllWindows()
if __name__ == '__main__':
    main()