# Third Party Dependancies
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# User Modules
from .database import Base, Project, Task

# Creates engine for connection to database
engine = create_engine(
    url="sqlite:///db.sqlite3",
)

# Creates missing tables and columns
Base.metadata.create_all(engine)

# Creates database connection session
session = Session(engine)


# Projects Section
def get_projects():
    "Returns List of All Projects"
    return session.query(Project).all()


def add_project(title: str):
    "Adds New Project and Returns Project Object"
    new_project = Project(name=title)

    session.add(new_project)
    session.commit()
    return new_project


def get_project(id: int):
    "Returns Project"
    return session.query(Project).get(id)


def delete_project(id: int):
    "Deletes Project"
    proj = session.query(Project).get(id)
    session.delete(proj)
    session.commit()


def update_project_status(id: int, status: str):
    "Updates Status of Project"

    proj = session.query(Project).get(id)
    proj.status = status
    session.commit()


# Tasks Section
def get_all_tasks():
    "Returns List of All Tasks"
    return session.query(Task).all()


def get_project_tasks(project_id: int):
    "Returns List of Task Related to Current Project"
    return session.query(Task).where(Task.project_id == project_id)


def get_task(task_id: int):
    "Returns Task"
    return session.query(Task).get(task_id)


def add_task(title: str, project_id: int):
    "Adds Task to Project and Returns Task Object"
    new_task = Task(title=title, project_id=project_id)

    session.add(new_task)
    session.commit()
    return new_task


def mark_as_done(task_id: int):
    "Marks Task as Done and Returns Task Object"
    task = session.query(Task).get(task_id)
    task.mark_as_done()
    session.add(task)
    session.commit()
    return task


def delete_task(task_id: int):
    "Deletes Task"
    task = session.query(Task).get(task_id)
    session.delete(task)
    session.commit()


def update_task_status(id: int, status: str):
    "Updates Status of Task"

    task = session.query(Task).get(id)
    task.status = status
    session.commit()


def update_task_title(id: int, title: str):
    "Updates Title of Task"

    task = session.query(Task).get(id)
    task.title = title
    session.commit()
