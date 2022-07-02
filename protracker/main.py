# Third Party Dependancies
import typer


# Modules
from .tasks import app as taskapp
from .projects import app as projectapp


def run_app():
    app = typer.Typer()

    app.add_typer(taskapp, name="tasks")
    app.add_typer(projectapp, name="projects")
    app()


if __name__ == "__main__":
    run_app()
