import base64
import requests
#https://oauth.powerbi.com/views/oauthredirect.html?code=XAB11754064138SXItk5ob5k6OjQbziM8EhyAg6kIUAsAb8nAn&state=sandbox-test&realmId=13845050550735405

client_id = "ABpo3n0dY4d2jV71KkDLdTNUMAUQ7GE8VPyC2jYc9TGhnzrHKl"
client_secret = "S8ND1OeVAy4GOwwg2nGvFZ87XyikajNOGoT48Xam"
redirect_uri = "https://oauth.powerbi.com/views/oauthredirect.html"
authorization_code = "XAB11754932869Yjno28bHJJPEFptcZjOrtRgfdOt7GvvFkz57"

# Encode credentials
auth_string = f"{client_id}:{client_secret}"
auth_header = base64.b64encode(auth_string.encode()).decode()

# Headers and body for token request
headers = {
    "Authorization": f"Basic {auth_header}",
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": redirect_uri
}

response = requests.post(
    "https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer",
    headers=headers,
    data=data
)

print(response.status_code)
print(response.json())
