from cli.todo_cli import TodoCLI
from services.todo_service import TodoService

def main():
    """
    Main entry point for the Todo CLI application.
    Keeps running in a loop until the user types 'exit' or Ctrl+C.
    """
    service = TodoService()
    cli = TodoCLI(service)

    print("Welcome to Todo CLI! Type 'exit' to quit.\n")

    while True:
        try:
            # Prompt user for input
            user_input = input("todo> ").strip()
            
            # Allow user to quit
            if user_input.lower() in ("exit", "quit"):
                print("Goodbye!")
                break

            # Skip empty input
            if not user_input:
                continue

            # Split input into arguments like sys.argv
            args = user_input.split()
            cli.run(args)

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nExiting...")
            break
        except Exception as e:
            # Catch any other errors without killing the process
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
