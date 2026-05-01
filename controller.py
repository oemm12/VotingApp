from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
import model


class VoteWindow(QMainWindow):
    def __init__(self) -> None:
        '''sets up the window'''
        super().__init__()
        uic.loadUi("voting_app.ui", self)

        self.vote_btn.clicked.connect(self.submit_vote)
        self.update_results()

    def submit_vote(self) -> None:
        '''saves the vote for whoever was picked'''
        candidate = self.candidate_dropdown.currentText()

        if candidate == "Choose a student...":
            QMessageBox.warning(self, "Error", "gotta pick someone before voting")
            return

        ok = model.save_vote(candidate)

        if ok:
            QMessageBox.information(self, "Nice", f"You're voting for {candidate}")
            self.update_results()
        else:
            QMessageBox.critical(self, "Error", "You need to pick someone before voting.")

    def update_results(self) -> None:
        '''reads the csv and updates the label'''
        counts = model.get_vote_counts()
        john = counts.get("John", 0)
        jane = counts.get("Jane", 0)
        total = john + jane

        self.results_label.setText(f"John: {john}  |  Jane: {jane}  |  Total: {total}")
