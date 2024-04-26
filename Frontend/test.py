from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

def service_account_login():
    """Logs into the service account and returns a service object."""
    flow = InstalledAppFlow.from_client_secrets_file('Frontend/credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('drive', 'v3', credentials=creds)
    return service

def upload_file(service, filename, filepath, mimetype):
    """Uploads file to Google Drive."""
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath, mimetype=mimetype)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID:', file.get('id'))

def download_file(service, file_id, filepath):
    """Downloads file from Google Drive."""
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(filepath, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

def list_files(service):
    """Lists all files and folders in the Google Drive."""
    results = service.files().list(pageSize=100, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
# Example usage:
service = service_account_login()
list_files(service)
download_file()