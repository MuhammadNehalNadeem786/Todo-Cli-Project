from cli.todo_cli import TodoCLI
from services.todo_service import TodoService
from cli.ui import show_banner, show_commands
from rich.console import Console

console = Console()

def main():
    service = TodoService()
    cli = TodoCLI(service)

    show_banner()
    show_commands()

    while True:
        try:
            user_input = console.input("\n[bold cyan]todo > [/bold cyan]").strip()

            if user_input.lower() in ("exit", "quit"):
                console.print("[bold yellow]Goodbye! 👋[/bold yellow]")
                break

            if not user_input:
                continue

            args = user_input.split()
            cli.run(args)

        except KeyboardInterrupt:
            console.print("\n[bold red]Exiting...[/bold red]")
            break
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
