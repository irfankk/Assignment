from flask import Flask
from flask import render_template, flash, redirect, url_for, session, logging
from flask import request
from flask_sqlalchemy import SQLAlchemy
from login_manager import LoginManager


app = Flask(__name__)
db= SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/expenditure'
login_manager = LoginManager()
login_manager.init_app(app)

class userDtls(db.Model):
     __tablename__ = "usersDtls"
     id = db.Column(db.Integer, autoincrement = True,primary_key = True)
     name = db.Column(db.String, nullable = False)
     username = db.Column(db.String,nullable = False)
     password = db.Column(db.String, nullable = False)
     expence = db.relationship(backref = "userdtl", lazy="dynamic")
     
class cat(db.Model):
     __tablename__ = "cat"
     catId = db.Column(db.Integer, autoincrement = True,primary_key = True)
     category = db.Column(db.String)

class expence(db.Model):
     __tablename__ = "expence"
     id = db.Column(db.Integer,autoincrement = True,primary_key = True)
     day = db.Column(db.Integer, nullable = False)
     month = db.Column(db.String, nullable = False)
     cat = db.Column(db.String, nullable = False)
     disctption = db.Column(db.String, nullable = False)
     amout = db.Column(db.Integer, nullable = False)
     userdtls_id =(db.Column(db.Integer, db.ForeignKey('userdtls_id'))
     


     




#starting           
@app.route('/', methods=["GET", "POST"])
def home():
        return render_template("index.html")

#register form
@app.route('/register', methods=["GET", "POST"])
def register():
     error  = None
     if request.method =="POST":
          username = request.form['username']
          user = userDtls.query.filter_by(username = userName).first()
          if name is None:
               userdtl = userDtls(
                    username = request.form['username'],
                    name = request.form['name'],
                    password = request.form['password'],
                    )
               db.session.add(userdtl)
               db.session.commit()
               login(user)
          flash('the username already exist', 'error')
          return render_template("register.html") 
     return render_template("register.html")

#login form
@app.route('/login', methods=['POST', 'GET'])
def sign():
     error = None
     if request.method == 'POST':
          username = request.form['userNames']
          psd = request.form['password']
          user = userDtls.query.filter_by(username = username).first()
          if user is not None:
               if user.password == psd:
                    login(user)
               flash('Invalid Password', 'error')
          flash('invalid user name or user name is not registered' 'error')
     return render_template("login.html")

#dashboard
@login_required
@app.route('/dashboard', methods=["POST", "GET"])
def dashboard(user):
     cat = cat.query.get(id)
     id = user.id
     dtl = userDtls.query.get('userdtls_id')
     category = dtls.cat
     
     
     
     return render_template("dashboard.html", username = username)


#add expence category and shows all cat datas
@app.route('/addcat', methods=["POST", "GET"])
def addcat():
     newcat = cat.query.all()
     if request.method == "POST":
          category = cat(category = request.form['cat'])
          db.session.add(category)
          db.session.commit()
          
          return redirect(url_for('expence', newcat = newcat))
     return render_template("cat.html", newcat = newcat)

#add expence and shows the expence data in table
@app.route('/expence', methods=["POST", "GET"])
def expence():
     if request.method == "POST":
          expencelist = expence(day = request.form['day'],
                            month = request.form['month'],
                            cat = request.form['cat'],
                            disctption = request.form['discription'],
                            amout = request.form['amout'])
          bd.session.add(expencelist)
          db.session.commit()
          return render_template("expence.html", catone= catone, cat= cat, amout=amout)
     catone = cat.query.all()
     exp = expence.query.all()
     cat = expence.cat
     amout = expence.amout
     return render_template("expence.html", catone = catone, cat= cat, amout=amout)

def login()
     login_user(user)
               flash('you are now login', 'info')
               return redirect(url_for('dashboard', user)
                     
@login_required
def logout():
          logout_user()
                   flash('you are now logout the account', 'info')
                   return redirect(url_for('login'))
                   
     
                                                    


if __name__ == "__main__":
    app.run(debug=True)
