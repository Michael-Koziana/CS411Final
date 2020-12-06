from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DDL, event
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '57913234348bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from proj import routes

# trig_ddl = DDL("""
#     CREATE TRIGGER tweet_english_checker BEFORE INSERT OR UPDATE
#     ON Tweet
#     FOR EACH ROW EXECUTE PROCEDURE
#     IF new.tweet like '/^[a-z][a-z0-9]*$/i' THEN
#     ELSE
#          new.tweet = ''
#     END IF
# """)
#tbl = db.__table__
#event.listen(tbl, 'after_create', trig_ddl.execute_if(dialect='sqllite'))