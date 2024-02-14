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

def install_gcc_gpp():
    if platform.system() == 'Linux':
        run_command("sudo apt-get update")
        run_command("sudo apt-get install -y gcc g++")
    elif platform.system() == 'Darwin':  # macOS
        run_command("brew install gcc")
    elif platform.system() == 'Windows':
        run_command("choco install mingw")

def install_rust():
    if platform.system() == 'Linux':
        run_command("sudo apt install -y rustc cargo")
    elif platform.system() == 'Darwin':
        run_command("brew install rust")
    elif platform.system() == 'Windows':
        run_command("choco install rust")

def main():
    print("Installing GCC and G++...")
    install_gcc_gpp()

    print("\nInstalling Rust...")
    install_rust()

    print("\nInstallation completed successfully!")

if __name__ == "__main__":
    main()
