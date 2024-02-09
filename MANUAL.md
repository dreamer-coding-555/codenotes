# Tool Updater User Manual

## Overview

The Tool Updater script is a Python-based tool designed to simplify the process of updating and installing Meson and Ninja, two essential build system tools. The script features a graphical user interface (GUI) for user interaction, providing real-time feedback through a terminal-like display.

## Prerequisites

- Ensure you have Python installed on your system.
- Verify that the `pip` package manager is available.

## Running the Script

1. **Download the Script:**
   - Copy the script content into a Python file (e.g., `download.py`).

2. **Open Terminal:**
   - Launch a terminal or command prompt.

3. **Navigate to Script Directory:**
   - Change the directory to where the script is located using the `cd` command.

4. **Run the Script:**
   - Execute the script by entering: `python download.py`.

## GUI Interface

The script opens a GUI window with the following components:

### Meson and Ninja Version Input:

- **Meson Version:** Enter the desired version of Meson.
- **Ninja Version:** Enter the desired version of Ninja.

### Action Buttons:

1. **Update Meson and Ninja:**
   - Upgrades Meson and Ninja to the specified versions.
   - Click this button after entering the desired versions.

2. **Install Meson and Ninja:**
   - Installs Meson and Ninja with the specified versions.
   - Use this button when performing a fresh installation.

3. **Check Meson and Ninja:**
   - Verifies whether Meson and Ninja are currently installed.
   - Click to check the installation status.

4. **Open Info:**
   - Placeholder button for additional actions or information.
   - Modify as needed for specific use cases.

### Progress Bar:

- A horizontal progress bar shows the completion status of update or installation processes.

### Terminal Output:

- The bottom section of the window functions as a terminal, displaying real-time information.
- It has a black background, light blue text, and bold styling for enhanced readability.

## Closing the Application

- Close the GUI window when you have completed the desired actions.
