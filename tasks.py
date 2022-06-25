import typer
import crud
import rich
import inquirer
from rich.table import Table
from enums import proj_status, task_status, task_tick


app = typer.Typer()


@app.command("new")
def new_task(title: str, project_id: int):
    "Adds a new task to project"

    crud.add_task(title, project_id)
    rich.print("[green]Task Added!")

    proj_tasks(project_id)


@app.command("all")
def tasks():
    "Gets all Tasks regardless of Project"
    tasks = crud.get_all_tasks()

    table = Table()
    table.add_column("")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Status")
    table.add_column("Project")
    table.add_column("Date Created")

    for task in tasks:
        table.add_row(
            f"{task_tick.done.value if task.done else task_tick.not_done.value}",
            f"{task.id}",
            f"{task.title}",
            f"{task.status}",
            f"{task.project}",
            f"{task.date_created}",
        )

    rich.print(table)


@app.command("list")
def proj_tasks(id: int):
    "Gets all Tasks of Project"

    tasks = crud.get_project_tasks(id)

    table = Table()
    table.add_column("")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Status")
    table.add_column("Project")
    table.add_column("Date Created")

    for task in tasks:
        table.add_row(
            f"{task_tick.done.value if task.done else task_tick.not_done.value}",
            f"{task.id}",
            f"{task.title}",
            f"{task.status}",
            f"{task.project}",
            f"{task.date_created}",
        )

    rich.print(table)


@app.command("view")
def view_task(id: int):
    "Shows Detail about Task"
    task = crud.get_task(id)
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
    task = crud.mark_as_done(id)
    rich.print("[green bold]Task Marked as Done")


@app.command("delete")
def delete(id: int):
    "Deletes Task"
    crud.delete_task(id)
    rich.print("[red bold]Task Deleted")


@app.command("update")
def update(id: int):
    "Updates Task"
    task = crud.get_task(id)

    opt = {
        "Status": change_status,
        "Title": (),
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

    crud.update_task_status(id, ans)

    view_task(id)


if __name__ == "__main__":
    app()
