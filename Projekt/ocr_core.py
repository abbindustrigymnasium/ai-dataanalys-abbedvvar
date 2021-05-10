try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(
        filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


print(ocr_core('avatar.jpg'))
