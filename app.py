from flask import Flask, redirect, jsonify, json, request, current_app
from flask import render_template, url_for
import os
import stripe

app = Flask(__name__)

stripe.api_key = 'sk_test_68QUFQZxlmORTdF0xqbfYEj3'
stripe.api_version = '2020-08-27'

YOUR_DOMAIN = 'http://localhost:4242'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/membership")
def membership():
    return render_template("membership.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/contributors")
def contributors():
    return render_template("contributors.html")

@app.route("/currentmembers")
def currentmembers():
    return render_template("currentmembers.html")

@app.route("/donate")
def donate():
    return render_template("donate.html")

@app.route("/equipment")
def equipment():
    return render_template("equipment.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/cancel")
def cancel():
    return render_template("cancel.html")

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # 'price': prices.data[0].id,
                    'price': 'price_1IXBRvG0vtiIDHhMN2S998RT',
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=YOUR_DOMAIN +
            '/success.html',
            # '/success.html?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        print(e)
        return "Server error", 500

@app.route('/create-checkout-session-associate', methods=['POST'])
def create_checkout_session_associate():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # 'price': prices.data[0].id,
                    'price': 'price_1IXBSsG0vtiIDHhM7Tu7capF',
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=YOUR_DOMAIN +
            '/success.html',
            # '/success.html?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        print(e)
        return "Server error", 500

@app.route('/create-checkout-session-student', methods=['POST'])
def create_checkout_session_student():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # 'price': prices.data[0].id,
                    'price': '01',
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=YOUR_DOMAIN +
            '/success.html',
            # '/success.html?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        print(e)
        return "Server error", 500

@app.route('/create-checkout-session-keyfob', methods=['POST'])
def create_checkout_session_keyfob():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # 'price': prices.data[0].id,
                    'price': 'price_1Kd2uSG0vtiIDHhMmm4h2KQo',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN +
            '/success.html',
            # '/success.html?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        print(e)
        return "Server error", 500