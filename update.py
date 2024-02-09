import os

def update_meson_build_script(directory):
    with open('meson.build', 'a') as build_file:
        build_file.write(f"subdir('{directory}')\n")

def should_skip_directory(directory):
    skip_list = ['.github', '.vscode', 'subprojects']
    return any(directory.startswith(skip_item) for skip_item in skip_list)

def main():
    for entry in os.listdir('.'):
        if os.path.isdir(entry) and entry[0].isdigit() and not should_skip_directory(entry):
            update_meson_build_script(entry)

if __name__ == "__main__":
    main()
