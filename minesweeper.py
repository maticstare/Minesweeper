import bottle, main

@bottle.get('/')
def index():
    return bottle.template('index')


@bottle.post('/instructions/')
def instructions():
    return bottle.template('instructions')


@bottle.post('/game/')
def pokazi_igro():
    return bottle.template('game')



bottle.run(reloader=True, debug=True)