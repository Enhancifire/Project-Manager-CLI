# Third Party Dependancies
import typer
import rich
from rich.tree import Tree
from rich.table import Table

# User Modules
from enums import proj_status, task_status, task_tick
import crud


app = typer.Typer()


@app.command("new")
def new_project(title: str):
    "Adds New Project"
    crud.add_project(title)

    rich.print("[green]Project Added")


@app.command("all")
def print_projects():
    "Prints Table of All Projects"
    projects = crud.get_projects()

    table = Table()
    table.add_column("[red bold]Id")
    table.add_column("[red bold]Project")
    table.add_column("[red bold]Status")
    table.add_column("[red bold]Date Created")

    for project in projects:
        table.add_row(
            f"{project.id}",
            f"{project.name}",
            f"[blue]{project.status}",
            f"{project.date_created}",
        )

    rich.print(table)


@app.command("tree")
def print_tree():
    "Prints Projects and Tasks in Tree View"
    projects = crud.get_projects()
    mtree = Tree("[blue bold]Projects")
    for project in projects:
        tree = Tree(f"[green]{project.name}")
        for task in project.tasks:
            tree.add(
                f"{task_tick.done.value if task.done == True else task_tick.not_done.value} {task.title}"
            )

        mtree.add(tree)

    rich.print(mtree)


@app.command("detail")
def project_details(project_id: int):
    "Gives Project Details"

    project = crud.get_project(project_id)
    rich.print(project)


if __name__ == "__main__":
    app()
