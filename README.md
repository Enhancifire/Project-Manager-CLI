# Project Tracker CLI "Protrack"

A CLI tool built to **manage** Projects and their Tasks.

Uses SQLite3 for the Database and Typer, Rich and Inquirer for Interaction

## Authors
- [@Enhancifire](https://github.com/Enhancifire)

## Features

### Project and Idea Management

Can keep track of the statuses of Projects.

Can be used to keep track of ideas for projects in one single application.

### Task Management

Can keep track of the tasks related to a project. The tasks can have various stasuses in corelation to the stage that they are in.

Primarily built for management of tasks through the CLI instead of relying on a GUI application

## Installation

Install Protrack via pip
```bash
pip install protrack
```

## Usage

You can run the app by typing "protrack" in the terminal

```bash
protrack

protrack --help

protrack tasks --help

protrack projects --help
```

## Requirements
- SqlAlchemy
- Typer
- Rich
- Inquirer
