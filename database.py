import sqlite3
from sqlite3.dbapi2 import connect
import os

# created_at TIMESTAMP
# updated_at_at TIMESTAMP

class Database:
    def __init__(self):
        try:
            os.remove("football.db")
        except:
            pass
        self.connexion = sqlite3.connect("football.db")
        self.c = self.connexion.cursor()

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
            birthdate TEXT,
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
            date TEXT,
            place VARCHAR,
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

    def insert_table_championships(self,name,country,start_year,end_year):
        with self.connexion:
            self.c.execute("INSERT INTO championships (name,country,start_year,end_year) VALUES (?,?,?,?)", (name,country,start_year,end_year))
        return self.c.lastrowid

    def insert_table_teams(self,name,city,coach_name,president,date_creation):
        with self.connexion:
            self.c.execute("INSERT INTO teams (name,city,coach_name,president,date_creation) VALUES (?,?,?,?,?)", (name,city,coach_name,president,date_creation))
        return self.c.lastrowid

    def insert_table_players(self,name,position,birthdate,nationality):
        with self.connexion:
            self.c.execute("""INSERT INTO players (name,position,birthdate,nationality) VALUES (?,?,?,?)""", (name,position,birthdate,nationality))
        return self.c.lastrowid

    def insert_table_participations(self,team_id,championship_id):
        with self.connexion:
            self.c.execute("INSERT INTO participations (team_id,championship_id) VALUES (?,?)", (team_id,championship_id))

    def insert_table_contracts(self,player_id,team_id):
        with self.connexion:
            self.c.execute("INSERT INTO contracts (player_id,team_id) VALUES (?,?)", (player_id,team_id))

    def insert_table_matches(self,championship_id,date,place,rainfall,temperature):
        with self.connexion:
            self.c.execute("INSERT INTO matches (championship_id,date,place,rainfall,temperature) VALUES (?,?,?,?,?)", (championship_id,date,place,rainfall,temperature))
        return self.c.lastrowid

    def insert_table_matches_teams(self,match_id, team_id, home, team_goal):
        with self.connexion:
            self.c.execute("INSERT INTO matches_teams (match_id, team_id, home, team_goal) VALUES (?,?,?,?)", (match_id, team_id, home, team_goal))
        return self.c.lastrowid

    def get_team_id(self,city):
        with self.connexion:
            self.c.execute(f"SELECT * FROM teams where city = '{city}';")
            return self.c.fetchone()[0]

    def insert_table_goals(self,player_id, match_id, goal_type):
        with self.connexion:
            self.c.execute("INSERT INTO goals (player_id, match_id, goal_type) VALUES (?,?,?)", (player_id, match_id, goal_type))

    def get_player_id(self,player_name):
        with self.connexion:
            try:
                self.c.execute(f"SELECT * FROM players where name = '{player_name}';")
                player_id = self.c.fetchone()[0]
            except:
                player_id = -1
            return player_id




