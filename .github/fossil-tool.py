import subprocess
import sys
import platform

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error details: {e}")
        sys.exit(1)

def setup():
    run_command("cd ..")
    run_command("meson setup builddir -v")

def compile():
    if platform.system() != 'Windows':
        # Execute scan-build only if not on Windows
        run_command("cd ..")
        run_command("scan-build meson compile -C builddir -v")
    else:
        # On Windows, execute regular meson compile
        run_command("cd ..")
        run_command("meson compile -C builddir -v")

def test():
    run_command("cd ..")
    run_command("meson test -C builddir -v")

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
