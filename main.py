"""
main application that runs the voting app
"""
 
import sys
from PyQt6.QtWidgets import QApplication
from controller import VoteWindow
 
 
def main() -> None:
    """
    Start the app, show the main window, and run the event loop
    
    """
    app = QApplication(sys.argv)
    window = VoteWindow()
    window.show()
    sys.exit(app.exec())
 
 
if __name__ == "__main__":
    main()