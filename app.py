from flask import Flask, render_template, request, redirect, url_for, send_file, after_this_request
from functions import merge_pdfs, clear_files
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/merge/', methods=['GET', 'POST'])
def merge():
    if request.method == 'POST':
        title = request.form['title']
        f = request.files.getlist('file')
        if len(f) < 1 or len(f) >= 20:
            flash("Please Submit atleast one file, but less than 20")
        else:
            for file in f:
                file.save(f"./files/{file.filename}")

            merge_pdfs(f, title)
            clear_files(f)

            @after_this_request
            def remove_file(response):
                os.remove(f"./files/{title}.pdf")
                return response

            return send_file(f"./files/{title}.pdf", as_attachment=True)

    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)