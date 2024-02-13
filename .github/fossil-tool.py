import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error details: {e}")
        sys.exit(1)

def setup():
    setup_command = "meson setup builddir"
    run_command(setup_command)

def compile():
    compile_command = "meson compile -C builddir -v"
    run_command(compile_command)

def test():
    test_command = "meson test -C builddir -v"
    run_command(test_command)

def main():
    if len(sys.argv) != 2:
        print("Usage: fossil-tool.py [setup|compile|test]")
        sys.exit(1)

    action = sys.argv[1].lower()

    if action == "setup":
        print("Running Meson setup...")
        setup()
    elif action == "compile":
        print("Running Meson compile...")
        compile()
    elif action == "test":
        print("Running Meson test...")
        test()
    else:
        print("Invalid action. Use setup, compile, or test.")
        sys.exit(1)

if __name__ == "__main__":
    main()