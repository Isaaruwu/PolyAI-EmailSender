from email.mime.image import MIMEImage
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import dotenv_values

ENV = dotenv_values(".env")


def load_template(path: str):
    with open(path, "r", encoding="UTF-8") as file:
        return file.read()


def generate_html(path: str, args: dict):
    content = load_template(path)

    for name, tag_cont in args.items():
        tag = "{" + name + "}"
        content = content.replace(tag, tag_cont)

    return content


def add_images(msg: MIMEMultipart):
    for name, path in json.loads(ENV["EMBEDDED_IMG"]).items():
        with open(path, "rb") as image_file:
            # Create an image MIME object
            image = MIMEImage(image_file.read())

            # Set the image filename
            image.add_header("Content-ID", name)

            # Attach the image to the message
            msg.attach(image)

    return msg


def generate_msg(
    sender: str, receiver: str, subject: str, html_path: str, args: dict
) -> str:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    content = MIMEText(generate_html(html_path, args), "html")

    msg.attach(content)
    msg = add_images(msg)

    return msg.as_string()
