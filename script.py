from database import Database
import functions

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


############## #championship ##############
name,country,start_year,end_year = "Ligue 1 UberEats", "France", 2020, 2021
championship_id = database.insert_table_championships(name,country,start_year,end_year)


############### teams 1 ##############
name,city,coach_name,president,date_creation = "LOSC Lille","Lille","Christophe GALTIER","Olivier Létang",1944
team_id = database.insert_table_teams(name,city,coach_name,president,date_creation)

database.insert_table_participations(team_id,championship_id)

#teams 2 (pour test)
name,city,coach_name,president,date_creation = "Dijon","Dijon","M Dijon","M Dijon",1944
team_id = database.insert_table_teams(name,city,coach_name,president,date_creation)

database.insert_table_participations(team_id,championship_id)




    #players
name,position,birthdate,nationality = "L. Chevalier","Gar.","6/11/01","FRA"    #IL FAUDRA REMETTRE LA COLUMN EN DATETIME
player_id = database.insert_table_players(name,position,birthdate,nationality)


database.insert_table_contracts(player_id,team_id)






############## journey ##############
date,place,rainfall,temperature = "22 Août 2020","Bordeaux",0,0
link_weather = functions.create_link_weather(place, date)
print(link_weather)
#a mettre : scrap météo
match_id = database.insert_table_matches(championship_id,date,place,rainfall,temperature)



city, home, team_goal = "Lille", True, 5
team_id = database.get_team_id(city)
database.insert_table_matches_teams(match_id, team_id, home, team_goal)

city, home, team_goal = "Dijon", False, 0
team_id = database.get_team_id(city)
database.insert_table_matches_teams(match_id, team_id, home, team_goal)


#goals
player_name = "L. Chevalier"
player_id = database.get_player_id(player_name)
goal_type = "Normal"
database.insert_table_goals(player_id, match_id, goal_type)






#goal type juste norm/contre camp ?
#a faire 2 fois pour ext ddom ## teams ##
# dates


#a faire:
#convertion format date db
#api test + transfo
# scraping

#viz corelation$
#model predict