#!/bin/bash

set -e

echo "===================================="
echo " Atlas Git Update"
echo "===================================="

git status

echo ""
echo "Staging files..."
git add .

echo ""
read -p "Commit message: " MESSAGE

git commit -m "$MESSAGE"

git push origin $(git branch --show-current)

echo ""
echo "Latest commits:"
git log --oneline --graph --decorate -5
