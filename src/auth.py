import os
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/youtube.force-ssl",
    "https://www.googleapis.com/auth/youtube",
]

CONFIG_DIR = Path.home() / ".config" / "youtube-own-mcp"
TOKEN_PATH = CONFIG_DIR / "token.json"
CLIENT_SECRET_PATH = Path(os.getenv("YOUTUBE_CLIENT_SECRET", "client_secret.json"))

def get_credentials() -> Credentials:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CLIENT_SECRET_PATH.exists():
                raise FileNotFoundError(
                    f"Coloque client_secret.json em {CLIENT_SECRET_PATH} ou defina YOUTUBE_CLIENT_SECRET"
                )
            flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET_PATH), SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())
            os.chmod(TOKEN_PATH, 0o600)
    return creds

def get_youtube_service():
    creds = get_credentials()
    return build("youtube", "v3", credentials=creds)

if __name__ == "__main__":
    print("Iniciando fluxo OAuth...")
    service = get_youtube_service()
    print("Autenticado com sucesso! Token salvo em", TOKEN_PATH)
