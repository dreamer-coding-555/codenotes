import subprocess

def setup_and_compile_project():
    # Step 1: Create a Meson build directory
    subprocess.run(['meson', 'setup', 'builddir'])

    # Step 2: Compile the project
    subprocess.run(['meson', 'compile', '-C', 'builddir'])

if __name__ == "__main__":
    setup_and_compile_project()
