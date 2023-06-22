import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton


class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Create widgets
        self.image_label = QLabel(self)
        self.input_line = QLineEdit(self)
        self.show_button = QPushButton("Show", self)

        # Set the layout
        layout = QVBoxLayout()
        # layout.addWidget(self.input_line)
        layout.addWidget(self.show_button)
        layout.addWidget(self.image_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Connect button click event
        self.show_button.clicked.connect(self.show_image)

    def show_image(self):
        # image_path = self.input_line.text()

        # Load the image using OpenCV
        image = cv2.imread("output.jpg")

        if image is not None:
            # Convert the image from BGR to RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Resize the image to fit the label
            image = cv2.resize(image, (self.image_label.width(), self.image_label.height()))

            # Convert the image to QImage format
            height, width, channel = image.shape
            bytes_per_line = 3 * width
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # Display the image
            self.image_label.setPixmap(QPixmap.fromImage(q_image))
            self.image_label.setScaledContents(True)
            self.input_line.clear()
        else:
            self.image_label.setText("Image not found!")


if __name__ == "__main__":
    import sys
    from PyQt5.QtGui import QImage, QPixmap

    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec_())
