from app import app
from flask.ext.script import Manager
from app import MigrateCommand

manager = Manager(app)
if __name__ == "__main__":
    manager.add_command('db', MigrateCommand)
    manager.run()
    #app.run(debug=True)