import re


def get_checkbox_status(markdown_text):
    """
    Extracts the status of checkboxes from markdonw text.

    Args:
        markdown_text: A string containing markdown text.

    Returns:
        A list of tuples, where each tuple contains the checkbox (True for checked, False for unchecked).
    """
    checkbox_regex = r"- \[( |x)\] (.*)"
    matches = re.findall(checkbox_regex, markdown_text)

    checkbox_status = []
    for match in matches:
        status = True if match[0] == "x" else False
        text = match[1]
        checkbox_status.append((text, status))
    return checkbox_status


if __name__ == "__main__":
    with open("Genesis/select_date_idea.qmd") as qmd:
        file = qmd.read()
        check_status = get_checkbox_status(file)
        print(check_status)
