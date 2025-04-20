from flask import Flask, render_template, send_file, url_for
import os

def create_app():
    app = Flask(__name__)
    app.config['MUSIC_FOLDER'] = os.path.join('static', 'music')

    # Create the music folder if it doesn't exist
    if not os.path.exists(app.config['MUSIC_FOLDER']):
        os.makedirs(app.config['MUSIC_FOLDER'])

    @app.route('/music')
    def index():
        music_files = [f for f in os.listdir(app.config['MUSIC_FOLDER']) if f.endswith(('.mp3', '.wav', '.ogg'))]
        return render_template('index.html', filenames=music_files)


    @app.route('/music/<filename>')
    def serve_music(filename):
        return send_file(os.path.join(app.config['MUSIC_FOLDER'], filename))

    @app.route('/home')
    def home():
        return render_template('home.html')    

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/team')
    def team():
        return render_template('team.html')
    
    @app.route('/')
    def default_route():
        return render_template('home.html')

    return app
    
app = create_app()