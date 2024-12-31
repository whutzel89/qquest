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

# Activate the virtual environment.
source .venv/bin/activate

# Return to folder that this script was called from.
popd
