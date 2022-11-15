from utilities.config import env
from src.services.gintruderService import GintruderService

from typing import Optional, List

import typer

app = typer.Typer(add_completion=env["menu_config"]["add_completion"])
gintruderService = GintruderService()

@app.command()
def menu(
    path: str = typer.Argument(
        ...,
        help="PATH of your local repository"
    ),
    search_word: Optional[List[str]] = typer.Option(
        None,
        "--search-word",
        "-sw",
        help="search words in all history repository, example: -sw word1"
    ),
    search_file: Optional[List[str]] = typer.Option(
        None,
        "--search-file",
        "-sf",
        help = "search files in all history repository, example: -sf file1"
    ),
    show_remote_repositories: Optional[bool] = typer.Option(
        False,
        "--show-remote-repo",
        "-sr",
        help = "show remote repositories"
    ),
    show_branches: Optional[bool] = typer.Option(
        False,
        "--show-branches",
        "-sb",
        help="show all branches of the repository"
    ),
    show_users: Optional[bool] = typer.Option(
        False,
        "--show-users",
        "-su",
        help="show the reposity's users"
    ),
    add_completion=env["menu_config"]["add_completion"],
) -> None:
    gintruderService.manageMenuOptions([
        search_word,
        search_file,
        show_remote_repositories,
        show_branches,
        show_users
    ], path)


def main():
    app()

if __name__ == '__main__':
    main()