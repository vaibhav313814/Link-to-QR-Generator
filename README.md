**QR Code Generator**
This project contains Python scripts to generate QR codes from any data and optionally upload the generated QR code image to Imgur.

**Features:**
**~> Generate QR Codes:** Create QR codes from URLs or any text data.
**~> Customize QR Codes:** Adjust QR code version, error correction level, box size, and border.
**~> Save QR Codes:** Save the generated QR code as an image file (PNG format).
**~> Upload to Imgur:** Upload the saved QR code image to Imgur and get a shareable link.

**Usage:**
**1.Generate QR Code:**

Encode your data into a QR code and save it as an image.
**Example:** generate_qr_code(data_to_encode, file_name)

**2.Upload to Imgur:**

Upload the saved QR code image to Imgur using your Imgur API client ID.
**Example:** upload_to_imgur(image_path, client_id)
