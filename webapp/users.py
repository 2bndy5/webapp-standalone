"""
A module to manage user accounts
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "/login"
login_manager.login_message_category = "warning"

class Remote:
    """A class used for instantiating a user's saved remote control configurations.
    There should be 1 object of this class type per remote control.
    """
    def __init__(self, name, link='/remote'):
        self.name = name
        self.link = link

class User(UserMixin):
    """A class for instantiating saved user accounts.
    There should be 1 object of this class type per user account.
    """
    def __init__(self, name):
        self._id = name
        self._remotes = []
        self._config = {}
        self._load_config()

    __tablename__ = 'users'
    id = DB.Column('user_id', DB.Integer, primary_key=True, index=True)
    username = DB.Column('username', DB.String(20), unique=True)
    password = DB.Column('password', DB.String(20))

    def __init__(self, username, password):
        # Note: The primary key (id) is auto-generated
        self.username = username
        self.password = password
    def _load_config(self):
        """This function will load the information about a user's preferences
        (including account settings and remote control configurations) from the backup json
        file titled with the self._id attribute.
        """
        try:
            with open('backup\\{}.json'.format(self._id), 'r') as acct_file:
                for line in acct_file.readlines():
                    # import from json to self.remotes & self.config
                    print(line)
        except OSError:
            pass # file doesn't exist

    def is_authenticated(self):
        # TODO: This should not always be true
        """ Return true if the user is authenticated. """
        return True

    def is_active(self):
        """ Return true if the user is activated. """
        # TODO: This should not always be true
        return True

    def is_anonymous(self):
        """ Return true if the user is anonymous. """
        return False

    def get_id(self):
        """This class attrubute holds the user account's ID"""
        return str(self.id)

    def __repr__(self):
        return f"<User '{self.username}' of ID {self.id}>"

@login_manager.user_loader
def load_user(user_id):
    """A function wrapper to retreive a user account's object"""
    return User.query.get(int(user_id))
