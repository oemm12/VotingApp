from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
import model


class VoteWindow(QMainWindow):
    def __init__(self):
        '''begins the window and connects the button to the submit function'''
        super().__init__()
        uic.loadUi("voting_app.ui", self)

        self.vote_btn.clicked.connect(self.submit_vote)


        self.update_results()

    def submit_vote(self):
        '''
        gets the candidate and saves the vote then updates the results'''
        candidate = self.candidate_dropdown.currentText()

        if candidate == "Choose a student...":
            QMessageBox.warning(self, "Pick one", "Pick a name first.")
            return

        ok = model.save_vote(candidate)

        if ok:
            QMessageBox.information(self, "Saved", f"Saved for {candidate}.")
            self.update_results()
        else:
            QMessageBox.critical(self, "Oops", "Couldn't save this one right now, try again in a sec.")

    def update_results(self):
        '''gets the vote counts and updates the text label'''
        counts = model.get_vote_counts()
        john = counts.get("John", 0)
        jane = counts.get("Jane", 0)
        total = john + jane
 
        self.results_label.setText(f"John: {john}  |  Jane: {jane}  |  Total: {total}")