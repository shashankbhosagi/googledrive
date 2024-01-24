from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID ='1WeQjbGZ9TZJIFmlZBBwVY0mqf63osX78'

def authenticate():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload(file_path):
    creds = authenticate();
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': file_path,
        'parents': [PARENT_FOLDER_ID]
    }
    file = service.files().create(
        body=file_metadata,
        media_body=file_path,
        ).execute()
    print('File ID: %s' % file.get('id'))
    print("File uploaded successfully")

upload('test.txt')