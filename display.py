import cv2


class Display:
    def __init__(self, window_name, window_size):
        self.window_name = window_name
        self.window_size = window_size
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, *window_size)

    def show(self, frame):
        cv2.imshow(self.window_name, frame)

    def wait_key(self, delay):
        return cv2.waitKey(delay) & 0xFF

    def destroy(self):
        cv2.destroyAllWindows()