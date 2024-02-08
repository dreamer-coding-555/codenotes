import subprocess

def setup_and_compile_project():
    # Step 1: Create a Meson build directory
    subprocess.run(['meson', 'setup', 'builddir'])

    # Step 2: Change to the build directory
    subprocess.run(['cd', 'builddir'], shell=True)

    # Step 3: Compile the project
    subprocess.run(['meson', 'compiledir'])

if __name__ == "__main__":
    setup_and_compile_project()
