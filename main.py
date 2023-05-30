import smtplib
from message_handler import generate_msg
from dotenv import dotenv_values

from data_utils import transform_data


def main(sender_email, sender_password, receiver_email, msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg)

        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))
    finally:
        server.quit()


if __name__ == "__main__":
    env = dotenv_values(".env")

    # Contact Data
    df = transform_data("./data/list_sponsorship.csv", [1, 2, 3, 4, 7, 8, 9, 10])
    print(df)

    sender = env["SENDER"]
    sender_pwrd = env["PASSWORD"]
    subject = "Proposition de commandites pour PolyAI"

    # Third column of df (email)
    receiver = "ismailaarabb@gmail.com"

    dict_args = {
        "name": "meow",  # First column of DF
        "date_event": "meow",
        "company_name": "meow",
        "date_rencontre": "meow",
        "heure_rencontre": "meow",
    }

    msg = generate_msg(sender, receiver, subject, env["HTML"], dict_args)

    main(sender, sender_pwrd, receiver, msg)
