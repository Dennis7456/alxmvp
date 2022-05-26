@app.route('/')
def index():
    return {'time': time.time()}

@app.route('/time')
def get_current_time():
    return {'time': time.time()}
