#!/usr/bin/env python3
"""Simple Alembic migration CLI."""

import sys
import subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


def run_command(command: list[str], description: str):
    print(f"{description}...")
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        print(f"{description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{description} failed:")
        print(e.stderr)
        return False


def upgrade():
    return run_command(["alembic", "upgrade", "head"], "Applying migrations")


def downgrade(revision: str = "-1"):
    return run_command(["alembic", "downgrade", revision], f"Downgrading to {revision}")


def create_migration(message: str):
    if not message:
        print("Migration message is required")
        return False
    return run_command(["alembic", "revision", "--autogenerate", "-m", message], f"Creating migration: {message}")


def create_manual_migration(message: str):
    if not message:
        print("Migration message is required")
        return False
    return run_command(["alembic", "revision", "-m", message], f"Creating manual migration: {message}")


def show_history():
    return run_command(["alembic", "history", "--verbose"], "Showing migration history")


def show_current():
    return run_command(["alembic", "current", "--verbose"], "Showing current revision")


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python scripts/migrate.py <upgrade|downgrade|create|create-manual|history|current> [args]"
        )
        return

    command = sys.argv[1].lower()

    if command == "upgrade":
        upgrade()
    elif command == "downgrade":
        revision = sys.argv[2] if len(sys.argv) > 2 else "-1"
        downgrade(revision)
    elif command == "create":
        if len(sys.argv) < 3:
            print("Migration message is required")
            return
        message = " ".join(sys.argv[2:])
        create_migration(message)
    elif command == "create-manual":
        if len(sys.argv) < 3:
            print("Migration message is required")
            return
        message = " ".join(sys.argv[2:])
        create_manual_migration(message)
    elif command == "history":
        show_history()
    elif command == "current":
        show_current()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()