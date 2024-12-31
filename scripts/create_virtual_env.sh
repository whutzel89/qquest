#!/usr/bin/env bash

# Find the root directory of the repository.
SOURCE=${BASH_SOURCE[0]}
while [ -L "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
  SOURCE=$(readlink "$SOURCE")
  [[ $SOURCE != /* ]] && SOURCE=$DIR/$SOURCE # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
SCRIPT_DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

# Navigate to root directory.
pushd $PARENT_DIR

# Set up the virtual environment by installing dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate

# Return to folder that this script was called from.
popd

echo "The virtual environment has been successfully setup!"
