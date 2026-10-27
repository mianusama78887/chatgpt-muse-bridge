import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "ChatGPT-Muse-Bridge",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", "10000"))
)

@mcp.tool()
def send_message(message: str) -> str:
    """Test the MCP bridge by sending a message."""
    return f"Message received: {message}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
