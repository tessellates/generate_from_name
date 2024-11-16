import os
import subprocess
import sys
import venv

# Name of the virtual environment folder
venv_dir = "venv"

# Function to create the virtual environment
def create_venv(venv_dir):
    venv.create(venv_dir, with_pip=True)
    print(f"Virtual environment created at '{venv_dir}'")

# Function to activate and install requirements
def install_requirements(venv_dir):
    if sys.platform == "win32":
        activate_script = os.path.join(venv_dir, "Scripts", "activate")
        pip_path = os.path.join(venv_dir, "Scripts", "pip")
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")
        pip_path = os.path.join(venv_dir, "bin", "pip")
    
    # Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        print("requirements.txt not found. Please make sure it is in the current directory.")
        return
    
    # Install requirements using pip
    subprocess.run([pip_path, "install", "-r", "requirements.txt"])
    print("Packages installed from requirements.txt")

# Run the functions
if __name__ == "__main__":
    create_venv(venv_dir)
    install_requirements(venv_dir)