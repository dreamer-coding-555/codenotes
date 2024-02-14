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
        run_command("/bin/bash -c \"$(curl -fsSL https://sh.rustup.rs)\"")
        run_command("export PATH=\"$HOME/.cargo/bin:$PATH\"")
    elif platform.system() == 'Windows':
        run_command("choco install rust")

def install_gdc():
    if platform.system() == 'Linux':
        run_command("sudo apt-get install -y gdc")
    # Handle other platforms as needed

def install_mono():
    if platform.system() == 'Linux':
        run_command("sudo apt-get install -y mono-devel")
    elif platform.system() == 'Darwin':
        run_command("brew install mono")
    elif platform.system() == 'Windows':
        run_command("choco install mono")

def install_java():
    if platform.system() == 'Linux':
        run_command("sudo apt-get install -y default-jdk")
    # Handle other platforms as needed

def main():
    print("Installing GCC and G++...")
    install_gcc_gpp()

    print("\nInstalling Rust...")
    install_rust()

    print("\nInstalling GDC (D Compiler)...")
    install_gdc()

    print("\nInstalling Mono (C#)...")
    install_mono()

    print("\nInstalling Java...")
    install_java()

    print("\nInstallation completed successfully!")

if __name__ == "__main__":
    main()