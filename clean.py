def normalize_columns(columns):
    return [column.strip().lower().replace(" ", "_") for column in columns]


if __name__ == "__main__":
    columns = ["First Name", "Last Name", "Email Address"]
    print(normalize_columns(columns))
