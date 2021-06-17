from database import Database

#init
database = Database()

#create tables
database.create_table_championships()

database.create_table_teams()
database.create_table_players()
database.create_table_participations()
database.create_table_contracts()

database.create_table_matches()
database.create_table_matches_teams()
database.create_table_goals()


#insert
name,country,start_year,end_year = "Ligue 1 UberEats", "France", 2020, 2021
database.insert_table_championships(name,country,start_year,end_year)

name,city,coach_name,president,date_creation = "LOSC Lille","Lile","Christophe GALTIER","Olivier Létang",1944
database.insert_table_teams(name,city,coach_name,president,date_creation)


# name,position,birthdate,nationality = "L. Chevalier","Gar.","6/11/01","FRA"    #IL FAUDRA REMETTRE LA COLUMN EN DATETIME
# database.insert_table_players(name,position,birthdate,nationality)


# team_id,championship_id = 1,1
# database.insert_table_participations(team_id,championship_id)





# database.insert_table_contracts()

# database.insert_table_matches()
# database.insert_table_matches_teams()
# database.insert_table_goals()










