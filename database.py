import sqlite3

# created_at TIMESTAMP
# updated_at_at TIMESTAMP

class Database:
    def __init__(self):
        connexion = sqlite3.connect("football.db")
        self.c = connexion.cursor()

    def create_table_teams(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            city VARCHAR,
            coach_name VARCHAR,
            president VARCHAR,
            date_creation INTEGER
        );""")

    def create_table_championships(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS championships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            country VARCHAR,
            start_year INTEGER,
            end_year INTEGER
        );""")

    def create_table_players(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            position VARCHAR,
            birthdate DATETIME,
            nationality VARCHAR
        );""")

    def create_table_participations(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS participations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_id INTEGER,
            championship_id INTEGER,
            FOREIGN KEY (team_id)
            REFERENCES teams (id) 
            FOREIGN KEY (championship_id)
            REFERENCES championships(id) 
        );""")

    def create_table_matches(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            championship_id INTEGER,
            date DATETIME,
            place VARCHAR,
            spectators INTEGER,
            rainfall FLOAT,
            temperature FLOAT,
            FOREIGN KEY (championship_id)
            REFERENCES championships(id) 
        );""")

    def create_table_goals(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER,
            match_id INTEGER,
            goal_type VARCHAR,
            FOREIGN KEY (match_id)
            REFERENCES matches(id) 
            FOREIGN KEY (player_id)
            REFERENCES players(id) 
        );""")

    def create_table_contracts(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS contracts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER,
            team_id INTEGER,
            start_date DATETIME,
            end_date DATETIME,
            FOREIGN KEY (player_id)
            REFERENCES players(id) 
            FOREIGN KEY (team_id)
            REFERENCES teams(id) 
        );""")

    def create_table_matches_teams(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS matches_teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_id INTEGER,
            team_id INTEGER,
            home BOOLEAN,
            team_goal INTEGER,
            FOREIGN KEY (match_id)
            REFERENCES matches(id) 
            FOREIGN KEY (team_id)
            REFERENCES teams(id) 
        );""")











