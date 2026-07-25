from typing import Optional, List, Literal
from mcp.server.fastmcp import FastMCP
from .youtube_service import (
    update_video_metadata,
    upload_caption,
    list_captions,
    list_my_videos,
    get_video,
    get_channel_info,
)

mcp = FastMCP("youtube-own-mcp")

@mcp.tool()
def update_video_metadata_tool(
    video_id: str,
    title: Optional[str] = None,
    description: Optional[str] = None,
    tags: Optional[List[str]] = None,
    category_id: Optional[str] = None,
    privacy_status: Optional[Literal["public", "unlisted", "private"]] = None,
) -> dict:
    """Atualiza título, descrição, tags (palavras-chave), categoria ou privacidade de um vídeo do seu canal."""
    return update_video_metadata(video_id, title, description, tags, category_id, privacy_status)

@mcp.tool()
def upload_caption_tool(
    video_id: str,
    language: str,
    caption_content: str,
    name: str = "",
    format: str = "srt",
    is_draft: bool = False,
) -> dict:
    """Faz upload de legenda (SRT ou VTT) para um vídeo do seu canal."""
    return upload_caption(video_id, language, caption_content, name, format, is_draft)

@mcp.tool()
def list_captions_tool(video_id: str) -> list:
    """Lista as tracks de legenda de um vídeo."""
    return list_captions(video_id)

@mcp.tool()
def list_my_videos_tool(max_results: int = 25) -> list:
    """Lista os vídeos do seu canal (mais recentes primeiro)."""
    return list_my_videos(max_results)

@mcp.tool()
def get_video_tool(video_id: str) -> dict:
    """Obtém detalhes completos de um vídeo (incluindo tags atuais)."""
    return get_video(video_id)

@mcp.tool()
def get_channel_info_tool() -> dict:
    """Informações do seu canal."""
    return get_channel_info()

if __name__ == "__main__":
    mcp.run()
