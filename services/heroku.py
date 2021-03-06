import foauth.providers


class Heroku(foauth.providers.OAuth2):
    # General info about the provider
    provider_url = 'https://heroku.com/'
    docs_url = 'https://devcenter.heroku.com/articles/platform-api-reference'
    category = 'Code'

    # URLs to interact with the API
    authorize_url = 'https://id.heroku.com/oauth/authorize'
    access_token_url = 'https://id.heroku.com/oauth/token'
    api_domain = 'api.heroku.com'

    available_permissions = [
        (None, 'read your account information'),
        ('read', 'read all of your apps and resources, excluding configuration values'),
        ('write', 'write to all of your apps and resources, excluding configuration values'),
        ('read-protected', 'read all of your apps and resources, including configuration values'),
        ('write-protected', 'write to all of your apps and resources, including configuration values'),
        ('global', 'read and write to all of your account, apps and resources'),
    ]
    permissions_widget = 'radio'

    def get_authorize_params(self, redirect_uri, scopes):
        params = super(Heroku, self).get_authorize_params(redirect_uri, scopes)
        params['scope'] = scopes[0] or 'identity'
        return params

    def get_user_id(self, key):
        r = self.api(key, self.api_domain, u'/account')
        return unicode(r.json()[u'id'])
