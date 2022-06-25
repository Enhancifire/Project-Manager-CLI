import enum


class proj_status(enum.Enum):
    planned = "[pink]Planned"
    in_progress = "[yellow]In Progress"
    completed = "[green]Completed"
    maintainance = "[orange]Under Maintainance"


class task_status(enum.Enum):
    todo = "[blue]Todo[/blue]"
    doing = "[yellow]Doing[/yellow]"
    done = "[green]Done[/green]"
    stalled = "[red bold]Stalled[/red /bold]"


class task_tick(enum.Enum):
    done = ":white_check_mark:"
    not_done = ":x:"
