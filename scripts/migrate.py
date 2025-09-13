#!/usr/bin/env python3
"""
Migration management script for Feedback API
"""

import os
import sys
import subprocess
from pathlib import Path

# Add app directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

def run_command(command: list[str], description: str):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def upgrade():
    """Run database migrations (upgrade to latest)"""
    return run_command(["alembic", "upgrade", "head"], "Applying migrations")

def downgrade(revision: str = "-1"):
    """Downgrade database by one migration or to specific revision"""
    return run_command(["alembic", "downgrade", revision], f"Downgrading to {revision}")

def create_migration(message: str):
    """Create a new migration with autogenerate"""
    if not message:
        print("❌ Migration message is required")
        return False
    
    return run_command(
        ["alembic", "revision", "--autogenerate", "-m", message],
        f"Creating migration: {message}"
    )

def create_manual_migration(message: str):
    """Create an empty migration file for manual editing"""
    if not message:
        print("❌ Migration message is required")
        return False
    
    return run_command(
        ["alembic", "revision", "-m", message],
        f"Creating manual migration: {message}"
    )

def show_history():
    """Show migration history"""
    return run_command(["alembic", "history", "--verbose"], "Showing migration history")

def show_current():
    """Show current migration revision"""
    return run_command(["alembic", "current", "--verbose"], "Showing current revision")

def main():
    """Main CLI interface"""
    if len(sys.argv) < 2:
        print("""
🗄️  Database Migration Manager for Feedback API

Usage:
  python scripts/migrate.py <command> [options]

Commands:
  upgrade                    - Apply all pending migrations
  downgrade [revision]       - Downgrade by 1 step or to specific revision
  create <message>          - Create new migration with autogenerate
  create-manual <message>   - Create empty migration for manual editing
  history                   - Show migration history
  current                   - Show current migration revision

Examples:
  python scripts/migrate.py upgrade
  python scripts/migrate.py downgrade
  python scripts/migrate.py downgrade base
  python scripts/migrate.py create "Add user_id column to feedbacks"
  python scripts/migrate.py create-manual "Custom data migration"
  python scripts/migrate.py history
  python scripts/migrate.py current
        """)
        return

    command = sys.argv[1].lower()
    
    if command == "upgrade":
        upgrade()
    elif command == "downgrade":
        revision = sys.argv[2] if len(sys.argv) > 2 else "-1"
        downgrade(revision)
    elif command == "create":
        if len(sys.argv) < 3:
            print("❌ Migration message is required")
            return
        message = " ".join(sys.argv[2:])
        create_migration(message)
    elif command == "create-manual":
        if len(sys.argv) < 3:
            print("❌ Migration message is required")
            return
        message = " ".join(sys.argv[2:])
        create_manual_migration(message)
    elif command == "history":
        show_history()
    elif command == "current":
        show_current()
    else:
        print(f"❌ Unknown command: {command}")

if __name__ == "__main__":
    main()