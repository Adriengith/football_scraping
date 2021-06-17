from database import Database

#init
database = Database()

#create tables
#database.create_table_teams()
#database.create_table_championships()
#database.create_table_players()
#database.create_table_participations()
#database.create_table_matches()
database.create_table_goals()
#database.create_table_contracts()
#database.create_table_matches_teams()













"""
 --- ARCHITECTURE ---  (ajouter ligne dans championnat à la main)


=> code à utiliser une fois: ajouter DB tout les clubs (https://www.lequipe.fr/Football/ligue-1/page-classement-equipes/general)
    table teams : name, city, coach_name, president, date_creation
    table players : name, position, birthdate, nationality
    table participations: team_id(Database récupérer l'id), championship_id)
    table contracts : player_id, team_id , start_date , end_date





BOUCLE FOR JOURNEES (https://www.lequipe.fr/Football/ligue-1/page-calendrier-resultats/1re-journee)  (38)
    BOUCLE FOR pour chaque match (https://www.lequipe.fr/Football/match-direct/ligue-1/2020-2021/bordeaux-nantes-live/477156)
        table matches : championship_id(1), date, place, spectators, rainfall(API), temperature(API)
        table matches_teams (pour les 2 teams) : match_id(Database récupérer l'id), team_id(Database récupérer l'id), home, team_goal
        table goals : player_id(Database récupérer l'id), match_id(Database récupérer l'id), goal_type, 









"""