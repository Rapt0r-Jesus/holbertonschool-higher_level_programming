#!/usr/bin/python3
"""
Function that generates personalized invitation files
from a template with placeholders and a list of objects.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files
    from a template string and a list of attendee data
    """

    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if (
        not isinstance(attendees, list)
        or not all(isinstance(a, dict) for a in attendees)
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        filled_template = template

    for key in ["name", "event_title", "event_date", "event_location"]:
        value = attendee.get(key, "N/A") or "N/A"
        filled_template = filled_template.replace(f"{{{key}}}", value)

    output_filename = f"output_{i}.txt"

    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(filled_template)
    except Exception as e:
        print(f"Error writing to {output_filename}: {e}")
        continue
