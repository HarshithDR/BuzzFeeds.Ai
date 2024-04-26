from flask import Flask
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = Flask(__name__)

# Path to your service account key file
SERVICE_ACCOUNT_FILE = 'auth.json'

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

@app.route('/')
def list_files():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        return 'No files found.'
    else:
        files = '<ul>'
        for item in items:
            files += f'<li>{item["name"]} ({item["id"]})</li>'
        files += '</ul>'
        return files

if __name__ == '__main__':
    app.run(debug=True)
