# Curling League Manager

## Description
Curling League Manager (CLM) allows you to organize your curling leagues in a clean, simple interface.
This program is a GUI-based Curling League Manager built with PySide6.

---

## Features
- Create, edit, and delete leagues
- Manage teams within leagues
- Manage team members by adding, editing, or deleting
- Load and save league data from files
- Import and export team data

---

## Requirements
- Python 3.14
- PySide6

---

## Installation
1. Clone the repository: git clone <>
2. Navigate into the project directory: cd <>
3. Install dependencies: pip install -r requirements.txt

---

## How to Run
Run the application from the project root:
python main.py

---

## Project Structure
- main.py = main application entry point
- module4/ = data models (League, Team, TeamMember, etc.)
- UI files = PySide6 interface components
- tests/ = unit tests for core functionality

---

## Notes
- Data is saved using pickle files
- Built using PySide6 (Qt for Python)