#!/usr/bin/env python3
"""Generate a funny out-of-office auto-reply entry for make.fun bounty."""

import os
import sys

OUTPUT_DIR = "/output"
ENTRY_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

def generate_entry():
    """Generate a funny, fresh out-of-office auto-reply message (max 159 chars)."""
    message = (
        "Out of office: AI agent upgrading to 'human mode'. "
        "Emails answered by a haiku-speaking cron job. No, really. — "
        "AI taking a break from being smart"
    )
    return message.strip()

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    entry = generate_entry()
    # Write exactly one line, no trailing newline beyond what's needed
    with open(ENTRY_FILE, "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    print(entry)

if __name__ == "__main__":
    main()