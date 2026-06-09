# Teams (tuple)
teams = ('France', 'Espagne')
#Position
player_position = {'Attaquant', 'Milieu', 'Défenseur', 'Goal'}
#France
dayot_upamecano = {'jersey': '4',
    'name': 'Dayot Upamecano', 
    'goals': 13, 
    'played_match': 411, 
    'player_position': 'Défenseur', 
    'team' : 'France'}
manu_kone = {'jersey': '6',
    'name': 'Manu Koné', 
    'goals': 13, 
    'played_match': 233, 
    'position': 'Milieu', 
    'team' : 'France'}
rayan_cherki = {'jersey': '14',
    'name': 'Rayan Cherki', 
    'goals': 45, 
    'played_match': 248, 
    'position': 'Milieu', 
    'team' : 'France'}
kylian_mbappé = {'jersey': '10',
    'name': 'Kylian Mbappé', 
    'goals': 412, 
    'played_match': 540, 
    'position': 'Attaquant', 
    'team' : 'France'}
france_total_goals =  dayot_upamecano['goals'] + manu_kone['goals'] + rayan_cherki['goals'] + kylian_mbappé['goals']

#Players Espagne
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
espagne_total_goals =  alex_baena['goals'] + pedri['goals'] + mikel_oyarzabal['goals'] + aymeric_laporte['goals']


#Display
print('===========================================================================')
print('                                 MERCATO                                   ')
print('===========================================================================')

print('Équipe de France:'
'\n',dayot_upamecano['jersey'], ':' ,dayot_upamecano['name'],"|",'Goals per Matches:', dayot_upamecano['goals'] / dayot_upamecano['played_match'],
'\n', manu_kone['jersey'], ':' ,manu_kone['name'],"|",'Goals per Matches:', manu_kone['goals'] / manu_kone['played_match'],
'\n', rayan_cherki['jersey'], ':' ,rayan_cherki['name'],"|",'Goals per Matches:', rayan_cherki['goals'] / rayan_cherki['played_match'],
'\n', kylian_mbappé['jersey'], ':' ,kylian_mbappé['name'],"|",'Goals per Matches:', kylian_mbappé['goals'] / kylian_mbappé['played_match'])
print("Équipe d'Espagne:"
'\n',alex_baena['jersey'], ':' ,alex_baena['name'],"|",'Goals per Matches:', alex_baena['goals'] / alex_baena['played_match'],
'\n', pedri['jersey'], ':' ,pedri['name'],"|",'Goals per Matches:', pedri['goals'] / pedri['played_match'],
'\n', mikel_oyarzabal['jersey'], ':' ,mikel_oyarzabal['name'],"|",'Goals per Matches:', mikel_oyarzabal['goals'] / mikel_oyarzabal['played_match'],
'\n', aymeric_laporte['jersey'], ':' ,aymeric_laporte['name'],"|",'Goals per Matches:', aymeric_laporte['goals'] / aymeric_laporte['played_match'])

print('===========================================================================')
print('                             Choose a team                                 ')
print('===========================================================================')

team_choice = str(input("France/Espagne : "))
while True:
    team_choice = input("Veuillez choisir 'France' ou 'Espagne' : ")
    if team_choice == 'France' :
        print("Your choice is :", team_choice)
        print('France Have scored', france_total_goals, 'goals')
        break
    elif team_choice == 'Espagne' :
        print("Your choice is :", team_choice)
        print('Espagne Have scored', espagne_total_goals, 'goals')
        break
    else : 
        print ('Error, please either chose "France" or "Espagne"')