# Project Atlas

> Solutions Delivery Portal (SDP)

Version: 0.1.0-alpha

Status: Active Development

---

# Vision

Project Atlas is a modern web application designed to bridge the gap between Sales and Engineering by providing complete visibility into all pre-sales engineering activities.

Atlas is **not** a Service Desk.

Atlas complements BMC Helix by managing engineering engagements, solution design, quotations, assessments, tenders and customer interactions before implementation.

---

# Mission

Reduce engineering administration.

Improve collaboration.

Standardise solution delivery.

Create an engineering knowledge platform.

---

# Guiding Principles

## Simple

Every screen should be intuitive.

No unnecessary clicks.

No training manuals.

---

## Fast

The portal must feel responsive.

Dashboard loads in under two seconds.

---

## Professional

UI should resemble Microsoft 365, Azure Portal and HPE GreenLake.

---

## Modular

Every feature should be independently maintainable.

---

## Scalable

The architecture must support future integrations without redesign.

---

## API First

Every major feature should eventually expose a REST API.

---

# Out of Scope

Atlas will NEVER replace:

- BMC Helix
- CRM
- ERP
- Active Directory

Atlas integrates with them.

It does not replace them.

---

# Technology Stack

Operating System

- Debian 13

Backend

- Python 3.12
- Flask

Database

- PostgreSQL

ORM

- SQLAlchemy

Frontend

- Bootstrap 5
- Chart.js

Authentication

- Flask Login
- Microsoft Entra ID (Future)

Web Server

- Gunicorn
- Nginx

Version Control

- Git
- GitHub

---

# Development Workflow

main

Production releases only

develop

Integration branch

feature/*

All development

No direct commits to main.

---

# Coding Standards

- PEP8
- Type hints
- Docstrings
- Logging
- Modular services
- Blueprints
- Application Factory

---

# Documentation Standards

Every completed feature includes:

- Documentation
- Installation notes
- Release notes
- Screenshots where appropriate

---

# UI Principles

Clean.

Minimal.

Professional.

Dark mode supported.

Responsive.

Accessible.

---

# Data Principles

PostgreSQL is the source of truth.

Excel is an import/export format.

---

# Security

Secrets never stored in Git.

Environment variables only.

Passwords hashed.

HTTPS only.

Least privilege.

Audit logging.

---

# Roadmap

Sprint 1

Foundation

Sprint 2

Authentication

Sprint 3

Dashboard

Sprint 4

Request Management

Sprint 5

Reporting

Sprint 6

Analytics

Sprint 7

AI Assistant

Sprint 8

Version 1.0 Release

---

# Future Integrations

Microsoft 365

Teams

SharePoint

Graph API

REST API

AI Services

S3 Object Storage

---

# Project Motto

Connecting Sales and Engineering.

---

# Success Criteria

A Sales Manager can see request status in seconds.

An Engineer can manage work without spreadsheets.

Management can understand workload without requesting reports.

Atlas becomes the central engineering workspace.

---

# Project Owner

Christopher Young

Solutions Architect

---

# Development Partner

OpenAI ChatGPT

Project Atlas Engineering Assistant
