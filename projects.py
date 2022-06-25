# Third Party Dependancies
import typer
import rich
import inquirer
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

        stat = project.status
        if stat == "Planned":
            stat = proj_status.planned.value

        elif stat == "In Progress":
            stat = proj_status.in_progress.value

        elif stat == "Completed":
            stat = proj_status.completed.value

        elif stat == "Under Maintainance":
            stat = proj_status.maintainance.value

        table.add_row(
            f"{project.id}",
            f"{project.name}",
            f"[blue]{stat}",
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


@app.command("view")
def project_details(project_id: int):
    "Gives Project Details"

    project = crud.get_project(project_id)

    stat = project.status

    if stat == "Planned":
        stat = proj_status.planned.value

    elif stat == "In Progress":
        stat = proj_status.in_progress.value

    elif stat == "Completed":
        stat = proj_status.completed.value

    elif stat == "Under Maintainance":
        stat = proj_status.maintainance.value

    rich.print(f"[red]Name:[/red] {project.name}")
    rich.print(f"[red]Status:[/red] {stat}")
    rich.print(f"[red]Date Created:[/red] {project.date_created}")
    rich.print(f"[red]Description:[/red] {project.description}")


@app.command("update")
def update(project_id: int):
    "Updates Project Details"

    opt = {
        "Status": change_status,
        "Update Name": (),
    }

    que = [inquirer.List("opt", message="Property to Update", choices=opt)]

    ans = inquirer.prompt(que)["opt"]

    fun = opt[ans]
    fun(project_id)


def change_status(id: int):
    "Change Status of Project"
    statuses = [
        "Planned",
        "In Progress",
        "Completed",
        "Under Maintainance",
    ]

    que = [inquirer.List("stat", message="Choose Status of Project", choices=statuses)]

    ans = inquirer.prompt(que)["stat"]

    crud.update_project_status(id, ans)

    project_details(id)


if __name__ == "__main__":
    app()
