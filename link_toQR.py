import qrcode
import requests


def generate_qr_code(data, file_name):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image locally
    img.save(file_name)


def upload_to_imgur(image_path, client_id):
    url = 'https://api.imgur.com/3/image'
    headers = {'Authorization': f'Client-ID {client_id}'}

    with open(image_path, 'rb') as f:
        payload = {'image': f.read()}

    response = requests.post(url, headers=headers, data=payload)
    data = response.json()

    if response.status_code == 200:
        return data['data']['link']
    else:
        print("Error uploading to Imgur:", data['data']['error'])


# Example usage
data_to_encode = "https://forms.gle/qwRokhxDSNwsQPc96"  # Your data to encode in the QR code
file_name = "qr_code.png"  # File name to save the generated QR code

# Generate QR code
generate_qr_code(data_to_encode, file_name)

# Replace 'YOUR_CLIENT_ID' with your actual Imgur API client ID
client_id = 'YOUR_CLIENT_ID'
imgur_link = upload_to_imgur(file_name, client_id)
print("QR Code Link:", imgur_link)
