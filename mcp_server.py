from fastmcp import FastMCP
import engine

mcp = FastMCP("Fishing Game")


@mcp.tool()
def play_fishing(command: str) -> str:
    """
    Execute a fishing game command.

    Examples:
    status
    cast
    cast 10
    buy basic_worm 10
    goto reed_river
    """

    return engine.cmd(command)


@mcp.tool()
def new_game(seed: int = 2024) -> str:
    """
    Start a new game.
    """

    return engine.new_game(seed)


if __name__ == "__main__":
    mcp.run()
