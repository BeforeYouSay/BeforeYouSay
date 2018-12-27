from flask_failsafe import failsafe

@failsafe
def create_app():
    # note that the import is *inside* this function so that we can catch
    # errors that happen at import time
    from app import app
    return app

if __name__ == "__main__":
    from os import path
    import os
    extra_dirs = ['.','templates','static']
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in os.walk(extra_dir):
            for filename in files:
                filename = path.join(dirname, filename)
                if path.isfile(filename):
                    extra_files.append(filename)
    create_app().run(host='0.0.0.0', extra_files=extra_files, debug=True)
