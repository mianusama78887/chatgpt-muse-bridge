from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ChatGPT-Muse-Bridge")

@mcp.tool()
def send_message(message: str) -> str:
    """Send a message to the bridge."""
    return f"Message received: {message}"

if __name__ == "__main__":
    mcp.run()
