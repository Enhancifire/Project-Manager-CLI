# Third Party Dependancies
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Table, Date, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# System Dependancies
from datetime import datetime

# Creates base for models
Base = declarative_base()


# Project Class and Table
class Project(Base):
    """Project Class
    Contains Name, Date Created, Description and Status of Project
    """

    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_created = Column(Date, default=datetime.now().date())
    description = Column(Text)
    status = Column(String, default="Planned")

    tasks = relationship("Task", back_populates="project", cascade="all")

    def __repr__(self):
        return f"{self.name}"


# Task Class and Table
class Task(Base):
    """Task Class
    Contains Title, Date Created, Date Completed, Status, Project Id of Task
    Optional: Date Completed, Done, Status"""

    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date_created = Column(Date, default=datetime.now().date())
    date_completed = Column(Date)
    status = Column(String, default="Todo")
    done = Column(Boolean, default=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    project = relationship("Project", back_populates="tasks")

    def __repr__(self):
        return f"{self.title}"

    def change_status(self, status):
        self.status = status

    def mark_as_done(self):
        self.done = True
        self.date_completed = datetime.now().date()
        self.status = "Done"
