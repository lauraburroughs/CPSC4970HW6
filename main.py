import sys
import pickle
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QInputDialog, QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from module4.league import League
from module4.team import Team
from module4.team_member import TeamMember


# Laura Burroughs
# CPSC 4970
# 14 April 2026
# Project 6


############################################################
# Main Window
############################################################
class MainWindow(QMainWindow):
    def __init__(self):
        """Initialize the main window"""
        super().__init__()

        self.leagues = []
        self.next_oid = 1

        # Track all open editor windows so they can be closed when loading a new DB
        self.open_windows = []

        loader = QUiLoader()
        base_path = os.path.dirname(__file__)
        ui_file = QFile(os.path.join(base_path, "ui", "main_window.ui"))

        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError("Cannot open UI file")

        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            raise RuntimeError("UI failed to load")

        self.setCentralWidget(self.ui)

        # Button signals
        self.ui.addButton.clicked.connect(self.add_league)
        self.ui.deleteButton.clicked.connect(self.delete_league)
        self.ui.editButton.clicked.connect(self.edit_league)
        self.ui.leagueList.itemDoubleClicked.connect(self.open_league)
        self.ui.saveButton.clicked.connect(self.save_database)
        self.ui.loadButton.clicked.connect(self.load_database)


    def add_league(self):
        """Add a new league"""
        name, ok = QInputDialog.getText(self, "Add League", "League Name:")

        if ok and name:
            league = League(self.next_oid, name)
            self.next_oid += 1

            self.leagues.append(league)
            self.ui.leagueList.addItem(name)

    def delete_league(self):
        """Delete the current league"""
        row = self.ui.leagueList.currentRow()

        if row < 0:
            return

        league = self.leagues[row]

        # Close related windows so they don't reference deleted league data
        for w in self.open_windows[:]:
            if isinstance(w, LeagueEditorWindow) and w.league == league:
                w.close()

        self.leagues.remove(league)
        self.ui.leagueList.takeItem(row)

    def edit_league(self):
        """Edit the current league"""
        row = self.ui.leagueList.currentRow()

        if row < 0:
            return

        league = self.leagues[row]

        new_name, ok = QInputDialog.getText(
            self,
            "Edit League",
            "New League Name:",
            text=league.name
        )

        if ok and new_name:
            league.name = new_name
            self.ui.leagueList.item(row).setText(new_name)

    def open_league(self, item):
        """Open a league"""
        row = self.ui.leagueList.row(item)
        league = self.leagues[row]

        editor = LeagueEditorWindow(league, self)
        self.open_windows.append(editor)
        editor.show()


    # Database actions
    def save_database(self):
        """Save the current database of leagues"""
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save Database",
            "",
            "Database Files (*.db);;All Files (*)"
        )

        if file_name:
            with open(file_name, "wb") as f:
                pickle.dump(self.leagues, f)

    def load_database(self):
        """Load the current database of leagues"""
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Load Database",
            "",
            "Database Files (*.db);;All Files (*)"
        )

        if not file_name:
            return

        # Close all open editor windows before loading new data to clean up references
        for w in self.open_windows:
            w.close()
        self.open_windows.clear()

        try:
            with open(file_name, "rb") as f:
                self.leagues = pickle.load(f)
        except Exception as e:
            print("Error loading database:", e)
            return

        self.ui.leagueList.clear()

        self.next_oid = 1

        for league in self.leagues:
            self.ui.leagueList.addItem(league.name)
            self.next_oid = max(self.next_oid, league.oid + 1)      # Ensures the next league ID is always > any loaded ID




############################################################
# League Editor
############################################################
class LeagueEditorWindow(QMainWindow):
    def __init__(self, league, main_window):
        """Initialize the window"""
        super().__init__()
        self.league = league
        self.main_window = main_window
        self.destroyed.connect(self.remove_from_main)

        loader = QUiLoader()
        base_path = os.path.dirname(__file__)
        ui_file = QFile(os.path.join(base_path, "ui", "league_editor.ui"))

        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError("Cannot open UI file")

        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            raise RuntimeError("UI failed to load")

        self.setCentralWidget(self.ui)

        self.load_teams()

        self.ui.addTeamButton.clicked.connect(self.add_team)
        self.ui.deleteTeamButton.clicked.connect(self.delete_team)
        self.ui.editTeamButton.clicked.connect(self.edit_team)
        self.ui.teamList.itemDoubleClicked.connect(self.open_team)
        self.ui.importButton.clicked.connect(self.import_teams)
        self.ui.exportButton.clicked.connect(self.export_teams)

    def load_teams(self):
        """Load the teams from the database"""
        self.ui.teamList.clear()

        for team in self.league.teams:
            self.ui.teamList.addItem(team.name)

    def add_team(self):
        """Add a new team to the database"""
        name, ok = QInputDialog.getText(self, "Add Team", "Team Name:")

        if ok and name:
            next_id = max([t.oid for t in self.league.teams], default=0) + 1
            team = Team(next_id, name)
            self.league.add_team(team)
            self.load_teams()

    def delete_team(self):
        """Delete a team from the database"""
        row = self.ui.teamList.currentRow()

        if row < 0:
            return

        team = self.league.teams[row]

        try:
            self.league.remove_team(team)
            self.load_teams()
        except ValueError:
            print("Cannot delete team: it is used in a competition")

    def edit_team(self):
        """Edit a team from the database"""
        row = self.ui.teamList.currentRow()

        if row < 0:
            return

        team = self.league.teams[row]

        new_name, ok = QInputDialog.getText(
            self,
            "Edit Team",
            "New Team Name:",
            text=team.name
        )

        if ok and new_name:
            team.name = new_name
            self.ui.teamList.item(row).setText(new_name)

    def open_team(self, item):
        """Open a team from the database"""
        row = self.ui.teamList.row(item)
        team = self.league.teams[row]

        editor = TeamEditorWindow(team, self)
        self.main_window.open_windows.append(editor)
        editor.show()

    def export_teams(self):
        """Export teams to a file"""
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Export Teams",
            "",
            "Team Files (*.teams);;All Files (*)"
        )

        if not file_name:
            return

        try:
            with open(file_name, "wb") as f:
                pickle.dump(self.league.teams, f)
        except Exception as e:
            print("Error exporting teams:", e)

    def import_teams(self):
        """Import teams from a file"""
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Import Teams",
            "",
            "Team Files (*.teams);;All Files (*)"
        )

        if not file_name:
            return

        try:
            with open(file_name, "rb") as f:
                imported_teams = pickle.load(f)
        except Exception as e:
            print("Error importing teams:", e)
            return


        # Reassign team IDs to avoid conflicts with existing teams in that league
        next_id = max([t.oid for t in self.league.teams], default=0) + 1

        for team in imported_teams:
            team.oid = next_id
            next_id += 1
            self.league.add_team(team)

        self.load_teams()

    def remove_from_main(self):
        if self in self.main_window.open_windows:
            self.main_window.open_windows.remove(self)




############################################################
# Team Editor
############################################################
class TeamEditorWindow(QMainWindow):
    def __init__(self, team, league_editor):
        """Initialize the window"""
        super().__init__()
        self.team = team
        self.league_editor = league_editor
        self.main_window = league_editor.main_window
        self.destroyed.connect(self.remove_from_main)

        loader = QUiLoader()
        base_path = os.path.dirname(__file__)
        ui_file = QFile(os.path.join(base_path, "ui", "team_editor.ui"))

        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError("Cannot open UI file")

        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            raise RuntimeError("UI failed to load")

        self.setCentralWidget(self.ui)

        self.load_members()

        self.ui.addMemberButton.clicked.connect(self.add_member)
        self.ui.deleteMemberButton.clicked.connect(self.delete_member)
        self.ui.editMemberButton.clicked.connect(self.edit_member)

    def load_members(self):
        """Load the members from the database"""
        self.ui.memberList.clear()

        for member in self.team.members:
            self.ui.memberList.addItem(f"{member.name} <{member.email}>")

    def add_member(self):
        """Add a new member to the database"""
        name, ok1 = QInputDialog.getText(self, "Add Member", "Member Name:")
        email, ok2 = QInputDialog.getText(self, "Add Member", "Member Email:")

        if ok1 and ok2 and name and email:
            next_id = max([m.oid for m in self.team.members], default=0) + 1
            member = TeamMember(next_id, name, email)
            self.team.add_member(member)
            self.load_members()

    def delete_member(self):
        """Delete a member from the database"""
        row = self.ui.memberList.currentRow()

        if row < 0:
            return

        member = self.team.members[row]
        self.team.remove_member(member)

        self.load_members()

    def edit_member(self):
        """Edit a member from the database"""
        row = self.ui.memberList.currentRow()

        if row < 0:
            return

        member = self.team.members[row]

        new_name, ok1 = QInputDialog.getText(
            self,
            "Edit Member",
            "New Name:",
            text=member.name
        )

        new_email, ok2 = QInputDialog.getText(
            self,
            "Edit Member",
            "New Email:",
            text=member.email
        )

        if ok1 and ok2 and new_name and new_email:
            member.name = new_name
            member.email = new_email
            self.load_members()

    def remove_from_main(self):
        if self in self.main_window.open_windows:
            self.main_window.open_windows.remove(self)



############################################################
# Run the program
############################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())