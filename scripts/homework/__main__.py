from . import Homework


def main() -> None:
    """Creates a homework, asking for the title first and the type of homework"""

    title = input("Enter the title: ")
    homework = Homework(title)
    homework.main()


if __name__ == "__main__":
    main()
