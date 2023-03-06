from io import TextIOWrapper
import os
import sys

# Variables


def write_space(file: TextIOWrapper) -> None:
    """Writes to lines to the file

    Args:
    - file (BufferedWriter): File opened with open() func
    """
    file.write("\n")
    file.write("\n")
    return None


def Inquire(Message: str, Options: list[str], Multi_Ans: bool = False) -> str | list[str] | None:
    """Displays a question with multiple options to the user

    Args:
    - Message (str): Message to be displayed for the question
    - Options (list): Options that the user can choose from
    - Multi_Ans (bool, optional): Flag if the question allows multiple answers. Defaults to False.

    Returns:
    - str: If Multi_Ans = False. Returns the option chosen
    - list: If Multi_Ans = True. Returns the options chosen
    """
    def get_input(): return input().strip()

    print(f"[?] {Message}: ")
    for i in range(len(Options)):
        print(f"\t{i}: {Options[i]}")

    if not Multi_Ans:
        answer = get_input()
        return Options[int(answer)]

    print("Enter options separated by a space: ", end="")
    answer = get_input()

    try:
        return [Options[int(ans)] for ans in answer.split(" ")]

    except:
        print("Enter options separated by a space: ", end="")
        answer = get_input()


class Homework:
    """Homework base class"""

    def __init__(self, title: str) -> None:
        """Creates a Homework object

        Args:
        - title (str): Homework's title
        """
        self.title = title

    @property
    def save_path(self) -> str:
        # Save homework on "./[title]"
        return os.path.join(".", self.title)

    @property
    def template(self) -> list[str]:
        header = [
            f'<!-- title: {self.title} -->',
            f'<link rel="stylesheet" href="../../static/style.css">',
            f'<script defer src="../../static/script.js"></script>',
            f"<header>",
        ]

        body = [
            f'<img src="../../static/logo.png">',
            f'# {self.title} <!-- omit in toc -->',
            f"## Universidad Francisco Gavidia | Ingeniería en Ciencias de la Computación <!-- omit in toc -->",
            f"### Date <!-- omit in toc -->",
        ]

        end = [
            f"</header>",
            f"<toc>",
            f"# Índice <!-- omit in toc -->",
            f"</toc>",
            f'# {self.title}',
        ]

        return header + body + end

    def create_homework(self) -> None:
        """Creates the homework directory, copies the static files to there and sets up the main file"""

        try:  # Confirms we can create the homework's directory
            os.mkdir(self.save_path)
        except:  # If not, exits the script
            print("Directory already exists, try another title")
            sys.exit()

        # Creates the main homework file
        with open(
            f"{self.save_path}\\{self.title}.md", "w", encoding="utf-8"
        ) as file:
            for line in self.template:
                file.write(line)
                write_space(file)

    def open_homework(self) -> None:
        """Opens the (save_path)\\(file) directory and (title).md in VScode,
        also starts the directory in explorer"""

        commands = [
            f'code "{self.save_path}"',
            f'code "{self.save_path}\\{self.title}.md"',
            f'explorer "{self.save_path}"',
            "exit",
        ]

        for command in commands:
            os.system(command)

    def main(self) -> None:
        """Main function for created a complete homework
        1. Updates the template
        2. Creates the homework's files
        3. Opens the homework's files
        """
        self.create_homework()
        self.open_homework()
