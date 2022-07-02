import typer
from .crud import (
    add_task,
    get_all_tasks,
    get_project_tasks,
    get_task,
    mark_as_done,
    delete_task,
    update_task_status,
    update_task_title,
)
import rich
import inquirer
from rich.table import Table
from .enums import proj_status, task_status, task_tick


app = typer.Typer()


@app.command("new")
def new_task(title: str, project_id: int):
    "Adds a new task to project"

    add_task(title, project_id)
    rich.print("[green]Task Added!")

    proj_tasks(project_id)


@app.command("all")
def tasks():
    "Gets all Tasks regardless of Project"
    tasks = get_all_tasks()

    table = Table()
    table.add_column("")
    table.add_column("[red bold]ID")
    table.add_column("[red bold]Title")
    table.add_column("[red bold]Status")
    table.add_column("[red bold]Project")
    table.add_column("[red bold]Date Created")

    for task in tasks:
        stat = task.status

        if stat == "Todo":
            stat = task_status.todo.value

        elif stat == "Doing":
            stat = task_status.doing.value

        elif stat == "Done":
            stat = task_status.done.value

        elif stat == "Stalled":
            stat = task_status.stalled.value

        table.add_row(
            f"{task_tick.done.value if task.done else task_tick.not_done.value}",
            f"{task.id}",
            f"{task.title}",
            f"{stat}",
            f"{task.project}",
            f"{task.date_created}",
        )

    rich.print(table)


@app.command("list")
def proj_tasks(id: int):
    "Gets all Tasks of Project"

    tasks = get_project_tasks(id)

    table = Table()
    table.add_column("")
    table.add_column("[red bold]ID")
    table.add_column("[red bold]Title")
    table.add_column("[red bold]Status")
    table.add_column("[red bold]Date Created")

    for task in tasks:
        stat = task.status

        if stat == "Todo":
            stat = task_status.todo.value

        elif stat == "Doing":
            stat = task_status.doing.value

        elif stat == "Done":
            stat = task_status.done.value

        elif stat == "Stalled":
            stat = task_status.stalled.value

        table.add_row(
            f"{task_tick.done.value if task.done else task_tick.not_done.value}",
            f"{task.id}",
            f"{task.title}",
            f"{stat}",
            f"{task.date_created}",
        )

    rich.print(table)


@app.command("view")
def view_task(id: int):
    "Shows Detail about Task"
    task = get_task(id)
    stat = task.status

    if stat == "Todo":
        stat = task_status.todo.value

    elif stat == "Doing":
        stat = task_status.doing.value

    elif stat == "Done":
        stat = task_status.done.value

    elif stat == "Stalled":
        stat = task_status.stalled.value

    rich.print(f"[blue]Title:[/blue] {task.title}")
    rich.print(f"[blue]Status:[/blue] {stat}")
    rich.print(
        f"Done: {task_tick.done.value if task.done else task_tick.not_done.value}"
    )
    rich.print(f"Date Created: {task.date_created}")
    rich.print(f"Date Completed: {task.date_completed}")
    rich.print(f"[red]Project:[/red] {task.project}")


@app.command("complete")
def done(id: int):
    task = mark_as_done(id)
    rich.print("[green bold]Task Marked as Done")


@app.command("delete")
def delete(id: int):
    "Deletes Task"
    delete_task(id)
    rich.print("[red bold]Task Deleted")


@app.command("update")
def update(id: int):
    "Updates Task"

    opt = {
        "Status": change_status,
        "Title": change_title,
        "Completion": (),
    }

    que = [inquirer.List("opt", message="Property to Update", choices=opt)]

    ans = inquirer.prompt(que)["opt"]

    fun = opt[ans]
    fun(id)


def change_status(id: int):
    statuses = [
        "Todo",
        "Doing",
        "Done",
        "Stalled",
    ]

    que = [inquirer.List("stat", message="Choose Status of Task", choices=statuses)]

    ans = inquirer.prompt(que)["stat"]

    update_task_status(id, ans)

    view_task(id)


def change_title(id: int):
    new_title = input("Enter a new title: ")

    update_task_title(id, new_title)

    view_task(id)


if __name__ == "__main__":
    app()
