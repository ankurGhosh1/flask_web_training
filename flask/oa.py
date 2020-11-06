import os
from flask import g
from flask_oauthlib.client import OAuth

oauth = OAuth()

github = oauth.remote_app(
    'github',
    consumer_key='86258161130f30f10e95',  #os.getenv('GITHUB_CONSUMER_KEY'),
    consumer_secret= 'dccd0f8ef9636dabaf8ac5a1e56f89c262a0fd67', #os.getenv('GITHUB_CONSUMER_SECRET'),
    request_token_params={"scope": "user:email"},
    base_url='https://api.github.com',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)

@github.tokengetter
def get_github_token():
    if 'access_token' in g:
        return g.access_token