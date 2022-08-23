#app.py
from flask import Flask, render_template
 
app = Flask(__name__)
   
@app.route('/')
def google_pie_chart():
    data = {'Task' : 'Hours per Day', 'Work' : 22, 'Eat' : 4, 'Commute' : 6, 'Watching TV' : 5, 'Sleeping' : 15}
    return render_template('chart.html', data=data)
 
if __name__ == "__main__":
    app.run()
