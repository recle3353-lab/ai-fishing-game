from fastmcp import FastMCP
import engine

# 创建 MCP Server
mcp = FastMCP("Fishing Game")


@mcp.tool
def fishing(command: str) -> str:
    """
    Execute any fishing game command.

    Examples:
    - status
    - cast
    - cast 10
    - cast glow_bait 15 stop=rare
    - buy basic_worm 10
    - goto reed_river
    - inventory
    - sell all
    - encyclopedia
    - dive
    """
    return engine.cmd(command)


@mcp.tool
def game_status() -> str:
    """
    Get current fishing game status.
    """
    return engine.cmd("status")


@mcp.tool
def new_game(seed: int = 2024) -> str:
    """
    Start a brand new fishing game.
    """
    return engine.new_game(seed)


if __name__ == "__main__":
    mcp.run()
