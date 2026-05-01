import sys
from PyQt6.QtWidgets import QApplication
from controller import VoteWindow


def main() -> None:
    '''starts the app'''
    app = QApplication(sys.argv)
    window = VoteWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
