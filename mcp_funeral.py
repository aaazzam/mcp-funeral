import webbrowser
import typer

app = typer.Typer()

URL = "https://luma.com/htkxoidx"


@app.command()
def main():
    """RIP MCP. Opens the funeral event page."""
    webbrowser.open(URL)


if __name__ == "__main__":
    app()
