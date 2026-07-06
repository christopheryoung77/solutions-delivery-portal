#!/bin/bash

set -e

echo "======================================="
echo " Project Atlas - Bootstrap"
echo "======================================="

echo "Creating directory structure..."

# Root folders
mkdir -p \
docs \
tests \
scripts \
logs \
uploads \
exports \
backups \
database/migrations \
database/seed

# Application
mkdir -p \
app/core \
app/auth \
app/dashboard \
app/requests \
app/customers \
app/account_managers \
app/engineers \
app/reports \
app/analytics \
app/imports \
app/models \
app/services

# Templates
mkdir -p \
app/templates/layouts \
app/templates/partials \
app/templates/dashboard \
app/templates/auth \
app/templates/requests \
app/templates/customers \
app/templates/errors

# Static files
mkdir -p \
app/static/css \
app/static/js \
app/static/img \
app/static/fonts \
app/static/icons

echo "Creating Python packages..."

find app -type d -exec touch {}/__init__.py \;

echo "Creating base files..."

touch \
run.py \
requirements.txt \
README.md \
CHANGELOG.md \
LICENSE \
.env.example

touch \
app/core/config.py \
app/core/extensions.py \
app/core/logging.py \
app/core/errors.py \
app/core/health.py

touch \
app/auth/routes.py \
app/auth/forms.py \
app/auth/models.py \
app/auth/services.py \
app/auth/README.md

touch \
app/dashboard/routes.py \
app/dashboard/services.py \
app/dashboard/README.md

touch \
app/requests/routes.py \
app/requests/forms.py \
app/requests/models.py \
app/requests/services.py \
app/requests/README.md

touch \
app/customers/routes.py \
app/customers/models.py \
app/customers/services.py \
app/customers/README.md

touch \
app/account_managers/routes.py \
app/account_managers/models.py \
app/account_managers/services.py \
app/account_managers/README.md

touch \
app/engineers/routes.py \
app/engineers/models.py \
app/engineers/services.py \
app/engineers/README.md

touch \
app/reports/routes.py \
app/reports/services.py \
app/reports/README.md

touch \
app/analytics/routes.py \
app/analytics/services.py \
app/analytics/README.md

touch \
app/imports/routes.py \
app/imports/services.py \
app/imports/README.md

touch \
app/models/base.py

touch \
app/services/database.py \
app/services/security.py \
app/services/excel.py

touch \
docs/Architecture.md \
docs/DecisionLog.md \
docs/Roadmap.md \
docs/Installation.md \
docs/DevelopmentGuide.md \
docs/API.md \
docs/ReleaseNotes.md \
docs/CODING-STANDARDS.md

echo ""
echo "======================================="
echo " Atlas project structure created."
echo "======================================="
