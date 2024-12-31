import os
from setuptools import find_packages, setup

# Filepath Locations,
setup_dir = os.path.dirname(os.path.abspath(__file__))
requirements_file = os.path.join(setup_dir, "requirements.txt")
version_file = os.path.join(setup_dir, "version.txt")


# Helper functions to read text files.
def get_requirements():
    with open(requirements_file, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def get_version():
    with open(version_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"').strip("'")
        return RuntimeError("Error: Version number not found.")


setup(
    name="qquest",
    version=get_version(),
    description="A tool for simulation.",
    packages=find_packages(exclude=["tests*"]),
    python_requires=">=3.11",
    install_requires=get_requirements(),
    include_package_data=False
)
