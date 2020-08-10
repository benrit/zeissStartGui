import qrcode

import json

qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=4,
)

x = {"name": "BenR",
    "msn": [x+1000 for x in range(200)]
    }

j = json.dumps(x)

qr.add_data(j)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("test1.png")
