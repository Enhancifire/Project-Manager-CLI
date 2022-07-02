# Third Party Dependancies
import typer


# Modules
import tasks
import projects

app = typer.Typer()

app.add_typer(tasks.app, name="tasks")
app.add_typer(projects.app, name="projects")


if __name__ == "__main__":

    app()
