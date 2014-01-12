import requests

def index():
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def login():
    if 'assertion' not in request.vars:
        raise HTTP(404)

    assertion_info = {'assertion' : request.vars.assertion,
            'audience' : 'http://127.0.0.1:8000'}
    resp = requests.post('https://verifier.login.persona.org/verify',
                         data=assertion_info, verify=True)

    if not resp.ok:
        raise HTTP(500)

    data = resp.json()

    if data['status'] == 'okay':
        session.email = data['email']
        return resp.content

def logout():
    session.email = None
    return redirect(URL('index'))
