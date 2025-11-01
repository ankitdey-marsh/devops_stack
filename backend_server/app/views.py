from flask import current_app, render_template, render_template_string

def home():
    return render_template('home.html')

def about():
    return render_template('about.html')

# Optional: simple helper views or HTML endpoints (kept minimal)
def simple_index():
    return render_template_string("<p>Backend server running. Try /api/health or /api/hello</p>")