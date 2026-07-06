#!/bin/bash

set -e

if [ $# -lt 3 ]; then
    echo "Usage:"
    echo "./scripts/git-update.sh <type> <scope> <message>"
    echo ""
    echo "Example:"
    echo "./scripts/git-update.sh feat core \"implement application factory\""
    exit 1
fi

TYPE=$1
SCOPE=$2
shift 2
MESSAGE="$*"

echo "===================================="
echo " Atlas Git Update"
echo "===================================="

git status
echo

echo "Staging files..."
git add .

COMMIT="${TYPE}(${SCOPE}): ${MESSAGE}"

echo
echo "Commit:"
echo "$COMMIT"
echo

git commit -m "$COMMIT"

git push origin "$(git branch --show-current)"

echo
echo "Latest commits:"
git log --oneline --graph --decorate -5
