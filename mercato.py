# Teams (tuple)
teams = ('France', 'Espagne')
#Position
player_position = {'Attaquant', 'Milieu', 'Défenseur', 'Goal'}
#France
mike_maignan = {'jersey': '16',
    'name': 'Mike Maignan', 
    'goals': 0, 
    'played_match': 383, 
    'player_position': 'Défenseur', 
    'team' : 'France'}
desire_doue= {'jersey': '20',
    'name': 'Désiré Doué', 
    'goals': 40, 
    'played_match': 183, 
    'player_position': 'Attaquant', 
    'team' : 'France'}
ousmane_dembele = {'jersey': '7',
    'name': 'Ousmane Dembélé', 
    'goals': 122, 
    'played_match': 412, 
    'player_position': 'Attaquant', 
    'team' : 'France'}
michael_olise = {'jersey': '11',
    'name': 'Michael Olise', 
    'goals': 70, 
    'played_match': 285, 
    'player_position': 'Milieu', 
    'team' : 'France'}
adrien_rabiot = {'jersey': '14',
    'name': 'Adrien Rabiot', 
    'goals': 68, 
    'played_match': 548, 
    'player_position': 'Milieu', 
    'team' : 'France'}
aurelien_tchouameni = {'jersey': '8',
    'name': 'Aurélien Tchouameni', 
    'goals': 18, 
    'played_match': 359, 
    'player_position': 'Milieu', 
    'team' : 'France'}
theo_hernadez = {'jersey': '19',
    'name': 'Theo Hernández', 
    'goals': 37, 
    'played_match': 390, 
    'player_position': 'Défenseur', 
    'team' : 'France'}
william_saliba = {'jersey': '17',
    'name': 'William Saliba', 
    'goals': 9, 
    'played_match': 329, 
    'player_position': 'Défenseur', 
    'team' : 'France'}
jules_kounde = {'jersey': '5',
    'name': 'Jules Koundé', 
    'goals': 23, 
    'played_match': 435, 
    'player_position': 'Défenseur', 
    'team' : 'France'}
dayot_upamecano = {'jersey': '4',
    'name': 'Dayot Upamecano', 
    'goals': 13, 
    'played_match': 411, 
    'player_position': 'Défenseur', 
    'team' : 'France'}
kylian_mbappé = {'jersey': '10',
    'name': 'Kylian Mbappé', 
    'goals': 412, 
    'played_match': 540, 
    'position': 'Attaquant', 
    'team' : 'France'}
joueurs_france = mike_maignan, desire_doue, ousmane_dembele, michael_olise, adrien_rabiot, aurelien_tchouameni, theo_hernadez, william_saliba, jules_kounde, dayot_upamecano, kylian_mbappé
france_total_goals =  0
for joueurs in joueurs_france :
    france_total_goals += joueurs['goals']

#Players Espagne
fabian_ruiz= {'jersey': '8', 
    'name': 'Fabián Ruiz', 
    'goals': 50, 
    'played_match': 452, 
    'position': 'Milieu', 
    'team' : 'Espagne'}
ferran_torres = {'jersey': '7', 
    'name': 'Fabián Ruiz', 
    'goals': 118, 
    'played_match': 404, 
    'position': 'Attaquant', 
    'team' : 'Espagne'}
rodri= {'jersey': '16', 
    'name': 'Rodri', 
    'goals': 38, 
    'played_match': 487, 
    'position': 'Milieu', 
    'team' : 'Espagne'}
marc_cucurella= {'jersey': '24', 
    'name': 'Marc Cucurella', 
    'goals': 19, 
    'played_match': 394, 
    'position': 'Défenseur', 
    'team' : 'Espagne'}
pau_cubarsi= {'jersey': '22', 
    'name': 'Pau Cubarsí', 
    'goals': 2, 
    'played_match': 133, 
    'position': 'Défenseur', 
    'team' : 'Espagne'}
marcos_llorente= {'jersey': '5', 
    'name': 'Marcos Llorente', 
    'goals': 38, 
    'played_match': 397, 
    'position': 'Milieu', 
    'team' : 'Espagne'}
unai_simon= {'jersey': '23', 
    'name': 'Fabián Ruiz', 
    'goals': 0, 
    'played_match': 334, 
    'position': 'Goal', 
    'team' : 'Espagne'}
alex_baena = {'jersey': '15', 
    'name': 'Álex Baena', 
    'goals': 35, 
    'played_match': 242, 
    'position': 'Milieu', 
    'team' : 'Espagne'}
pedri = {'jersey': '20',
    'name': 'Pedri', 
    'goals': 38, 
    'played_match': 330, 
    'position': 'Milieu', 
    'team' : 'Espagne'}
mikel_oyarzabal = {'jersey': '21',
    'name': 'Mikel Oyarzabal', 
    'goals': 168, 
    'played_match': 514, 
    'position': 'Attaquant', 
    'team' : 'Espagne'}
aymeric_laporte = {'jersey': '14',
    'name': 'Aymeric Laporte', 
    'goals': 22, 
    'played_match': 429, 
    'position': 'Défenseur', 
    'team' : 'Espagne'}
joueurs_espagne = alex_baena, pedri, mikel_oyarzabal, aymeric_laporte, fabian_ruiz, ferran_torres, rodri, marc_cucurella, pau_cubarsi,unai_simon
espagne_total_goals =  0
for joueurs in joueurs_espagne :
    espagne_total_goals += joueurs['goals']

goals_per_match = joueurs['goals'] / joueurs['played_match']
#Display
print('===========================================================================')
print('                                 MERCATO                                   ')
print('===========================================================================')


team_choice = str()
while True:
    team_choice = input("Veuillez choisir 'France' ou 'Espagne' : ").strip().lower()
    print()
    if team_choice == 'france'  :
        print('Équipe de France: ')
        print()
        for joueur in joueurs_france:
            goals_per_match = joueur['goals'] / joueur['played_match']
            print(joueur['jersey'], ':', joueur['name'], '|', 'Goals per matches:', round(goals_per_match, 3))
        print('France Have scored', france_total_goals, 'goals')
        break
    elif team_choice == 'Espagne' :
        print("Équipe d'Espagne: ")
        print()
        for joueur in joueurs_espagne:
            goals_per_match = joueur['goals'] / joueur['played_match']
            print(joueur['jersey'], ':', joueur['name'], '|', 'Goals per matches:', round(goals_per_match, 3))
        print('Espagne Have scored', espagne_total_goals, 'goals')
        break
    else : 
        print ('Error, please either chose "France" or "Espagne"')