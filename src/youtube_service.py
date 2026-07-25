from typing import Optional, List, Literal
from googleapiclient.http import MediaInMemoryUpload
from src.auth import get_youtube_service

def update_video_metadata(
    video_id: str,
    title: Optional[str] = None,
    description: Optional[str] = None,
    tags: Optional[List[str]] = None,
    category_id: Optional[str] = None,
    privacy_status: Optional[Literal["public", "unlisted", "private"]] = None,
):
    service = get_youtube_service()
    current = service.videos().list(part="snippet,status", id=video_id).execute()
    if not current.get("items"):
        raise ValueError(f"Vídeo {video_id} não encontrado ou sem permissão")
    item = current["items"][0]
    snippet = item["snippet"]
    status = item["status"]
    if title is not None:
        snippet["title"] = title
    if description is not None:
        snippet["description"] = description
    if tags is not None:
        snippet["tags"] = tags
    if category_id is not None:
        snippet["categoryId"] = category_id
    if privacy_status is not None:
        status["privacyStatus"] = privacy_status
    body = {"id": video_id, "snippet": snippet, "status": status}
    return service.videos().update(part="snippet,status", body=body).execute()

def upload_caption(
    video_id: str,
    language: str,
    caption_content: str,
    name: str = "",
    format: str = "srt",
    is_draft: bool = False,
):
    service = get_youtube_service()
    body = {
        "snippet": {
            "videoId": video_id,
            "language": language,
            "name": name or f"Caption {language}",
            "isDraft": is_draft,
        }
    }
    mimetype = "text/vtt" if format.lower() == "vtt" else "application/octet-stream"
    media = MediaInMemoryUpload(caption_content.encode("utf-8"), mimetype=mimetype)
    return service.captions().insert(part="snippet", body=body, media_body=media).execute()

def list_captions(video_id: str):
    service = get_youtube_service()
    return service.captions().list(part="snippet", videoId=video_id).execute()

def list_my_videos(max_results: int = 25):
    service = get_youtube_service()
    channels = service.channels().list(part="contentDetails", mine=True).execute()
    if not channels.get("items"):
        return {"items": []}
    uploads = channels["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    return service.playlistItems().list(
        part="snippet,contentDetails", playlistId=uploads, maxResults=max_results
    ).execute()

def get_video(video_id: str):
    service = get_youtube_service()
    return service.videos().list(part="snippet,status,statistics,contentDetails", id=video_id).execute()

def get_channel_info():
    service = get_youtube_service()
    return service.channels().list(part="snippet,statistics,contentDetails", mine=True).execute()
