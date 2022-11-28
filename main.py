import requests
import smtplib
from flask import Flask, render_template, request, redirect, url_for
from form import ContactForm
from flask_bootstrap import Bootstrap
import os
from dotenv import load_dotenv


app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)
load_dotenv()

email = os.getenv('email')
password = os.getenv('password')


@app.route('/', methods=["GET", "POST"])
def home():
    form = ContactForm()
    if request.method == "POST":
        cust_name = form.name.data
        cust_email = form.email.data
        cust_message = form.message.data
        # print(cust_name, cust_email, cust_message)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            result = connection.login(email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Subject:SY MANAGEMENT\n\nCustomer Name:{cust_name}\nCustomer Email: {cust_email}\nMessage:{cust_message} "

            )
            return redirect(url_for('home'))

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
