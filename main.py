# Third Party Dependancies
import typer

# Modules
import tasks
import projects

app = typer.Typer()

app.add_typer(tasks.app, name="tasks")
app.add_typer(projects.app, name="projects")

# @app.command("")
# def main():
#     choices = {
#         "View Projects": print_projects,
#         "View Project Tree": print_tree,
#         "Open Project": open_project,
#         "All Tasks": print_tasks,
#     }

#     questions = [
#         inquirer.List(
#             "choice", message="Select Option", choices=[choice for choice in choices]
#         )
#     ]

#     ans = inquirer.prompt(questions)["choice"]

#     fun = choices[ans]
#     fun()


if __name__ == "__main__":

    app()
