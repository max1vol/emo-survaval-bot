import re


def update_total_time(journal_path="Journal.md"):
    """
    Reads a journal file, calculates the total time spent from entries,
    and updates the total time spent in the file.
    """
    try:
        with open(journal_path, "r") as f:
            content = f.read()

        # Find all "Spent" entries and sum the hours
        spent_times = re.findall(r"> Spent: ([\d.]+)h", content)
        total_hours = sum(float(t) for t in spent_times)

        # Format the total hours to be an integer if it's a whole number
        if total_hours.is_integer():
            display_hours = int(total_hours)
        else:
            display_hours = total_hours

        # Update the "Total time spent" line
        new_content = re.sub(
            r"Total time spent: [\d.]+h",
            f"Total time spent: {display_hours}h",
            content,
        )

        # Write the updated content back to the file
        with open(journal_path, "w") as f:
            f.write(new_content)

        print(f"Successfully updated total time to {display_hours}h in {journal_path}")

    except FileNotFoundError:
        print(f"Error: The file {journal_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    update_total_time()
