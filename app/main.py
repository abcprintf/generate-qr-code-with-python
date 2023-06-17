import qrcode
import os
from dotenv import load_dotenv
from PIL import Image
from datetime import datetime

# get .env file
load_dotenv()

# get current date and time
current_date_time = datetime.now().strftime("%Y-%m-%d_%H%M%S")

# image logo
logo = Image.open(os.environ.get('IMAGE_LOGO_PATH'))

# resize logo
width = 50
width_percent = (width / float(logo.size[0]))
height_size = int((float(logo.size[1]) * float(width_percent)))
logo = logo.resize((width, height_size), Image.Resampling.LANCZOS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# url link
url = os.environ.get('LINK_URL')
QRcode.add_data(url)
QRcode.make()

QRcolor = os.environ.get('COLOR_LOGO')
QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')

pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save QR code
QRimg.save("app/output/QRcode"+ current_date_time +".png")

print("QR code generated successfully")