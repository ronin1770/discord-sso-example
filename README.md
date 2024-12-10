# discord-sso-example

In order to better understand this code base / example, please checkout our blog at: [FAMRO Blog - How to build Discord SSO application in Python](https://famro-llc.com/how-to-build-discord-sso-application-in-python.html)

## Prequisites ##
- Python 3.x
- PIP3 installer
- Flask Pypi library
- Web server
- Domain name
- SSL certificate

## Set Environment Variables ##

On Linux you can use the following set of commands:

```
export CLIENT_ID=<DISCORD Application Client ID>
export CLIENT_SECRET=<DISCORD Application Client Secret>
export REDIRECT_URI=<DISCORD Application Redirect URL>
export DISCORD_API_BASE_URL=https://discord.com/api
```

## Executing the Code ##

```python3 app.py ```
