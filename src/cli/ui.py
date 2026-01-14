from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

console = Console()


# =========================
# BANNER
# =========================
def show_banner():
    title = Text("TODO CLI", style="bold white")
    subtitle = Text(
        "Minimal • Fast • Productive task management",
        style="italic bright_black"
    )

    content = Align.center(
        Text.assemble(title, "\n", subtitle),
        vertical="middle"
    )

    console.print(
        Panel(
            content,
            border_style="bright_black",
            padding=(1, 4),
        )
    )


# =========================
# COMMANDS HELP
# =========================
def show_commands():
    commands = Text()

    commands.append("add", style="bold cyan")
    commands.append("        Create a new task\n", style="white")
    commands.append("list", style="bold cyan")
    commands.append("       View all tasks\n", style="white")
    commands.append("update", style="bold cyan")
    commands.append("     Update an existing task\n", style="white")
    commands.append("complete", style="bold cyan")
    commands.append("   Mark task as done\n", style="white")
    commands.append("incomplete", style="bold cyan")
    commands.append(" Mark task as not done\n", style="white")
    commands.append("delete", style="bold cyan")
    commands.append("     Remove a task\n", style="white")
    commands.append("exit", style="bold cyan")
    commands.append("       Exit application\n", style="white")

    console.print(
        Panel(
            commands,
            title="[bold bright_black]Commands[/bold bright_black]",
            border_style="bright_black",
            padding=(1, 2),
        )
    )


# =========================
# TASK TABLE
# =========================
def show_tasks(tasks):
    table = Table(
        title="Tasks",
        title_style="bold white",
        header_style="bold bright_black",
        border_style="bright_black",
        show_lines=False,
    )

    table.add_column("ID", justify="right", style="dim", width=4)
    table.add_column("Status", justify="center", width=10)
    table.add_column("Title", style="white", min_width=20)
    table.add_column("Description", style="bright_black")

    for task in tasks:
        status = (
            "[bold green]DONE[/bold green]"
            if task.completed
            else "[bold yellow]TODO[/bold yellow]"
        )

        table.add_row(
            str(task.id),
            status,
            task.title,
            task.description or "-"
        )

    console.print(table)


# =========================
# FEEDBACK MESSAGES
# =========================
def success(message: str):
    console.print(
        f"[bold green]✔ SUCCESS[/bold green]  {message}"
    )


def error(message: str):
    console.print(
        f"[bold red]✖ ERROR[/bold red]    {message}"
    )
