from flask import Flask
from fronty.html import *
from fronty.css import *
from datetime import date

app = Flask(__name__)

# Basic style using Fronty CSS
def style_css():
    return CSS(
        Selector('*').properties({
            'margin': '0',
            'padding': '0',
            'font-family': 'Arial, sans-serif',
        }),
        Selector('body').properties({
            'background-color': '#f0f0f0',
        }),
        Selector('.container').properties({
            'margin': '80px auto',
            'width': '60%',
            'text-align': 'center',
            'padding': '40px',
            'background-color': '#fff',
            'border-radius': '12px',
            'box-shadow': '0 2px 8px rgba(0,0,0,0.1)',
        }),
        Selector('a').properties({
            'display': 'inline-block',
            'margin-top': '20px',
            'padding': '10px 20px',
            'background-color': '#007BFF',
            'color': '#fff',
            'border-radius': '8px',
            'text-decoration': 'none',
            'font-size': '16px',
        }),
        Selector('a:hover').properties({
            'background-color': '#0056b3',
        }),
    )

# Landing page layout
@app.route('/')
def landing():
    return Html(
        Head(
            Title('Landing Page'),
            Meta(charset='UTF-8'),
            Style(style_css())
        ),
        Body(
            Div(
        
            Element(
                'center',
                Element(
                    'h1',
                    'Welcome'
                ),
                Element(
                    'p',
                    'this is the landing page'
                ),       
        ),
         Anchor('Enter Home Page', href='/home')
    )
            ).class_('container')
        ).render()

# Home page layout
@app.route('/home')
def home():
    return Html(
        Head(
            Title('Home Page'),
            Meta(charset='UTF-8'),
            Style(style_css())
        ),
        Body(
            Div(
                Element(
                'center',
                Element(
                    'h1',
                    'Welcome'
                ),
                Element(
                    'p',
                    'this is the home page'
                ),
                ),
                Anchor('Back to Landing Page', href='/')
            ).class_('container')
        )
    ).render()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
