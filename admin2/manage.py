from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template, redirect,  url_for



app = Flask(__name__)




def __init__(self,hg, hb):
        self.hg = hg
        self.hb = hb

def __repr__(self):
        return '<User %r>' % self.hb


@app.route('/')
def vote():
    pw=""
    return render_template('vote.html')
    return pw

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


@app.route('/nps_vote', methods=['POST'])
def post_user():
    vote = Votes(request.form['hg'], request.form['hb'])
    db.session.add(vote)
    db.session.commit()
    return redirect(url_for('thanks'))


@app.route('/nps_results')
def results():
        prithvi=Votes.query.filter(Votes.hb == "prithvi").count()
        tanush=Votes.query.filter(Votes.hb == "tanush").count()
        sneha=Votes.query.filter(Votes.hg == "sneha").count()
        neha=Votes.query.filter(Votes.hg == "neha").count()

        print("Total Voters",(sneha + neha))

        results={"Prithvi":prithvi,"Tanush":tanush,"Sneha":sneha,"Neha":neha}


        return render_template("results.html", results=results)
        #return render_template("result.html",result = result)


if __name__ == "__main__":

    app.run()
