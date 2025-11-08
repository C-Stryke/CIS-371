#Dictionary Name is the Defending type
#Keys are the type of Attack

AttackBonus = {
    "-6": 2/8,
    "-5": 2/7,
    "-4": 2/6,
    "-3": 2/5,
    "-2": 2/4,
    "-1": 2/3,
    "0": 2/2,
    "1": 3/2,
    "2": 4/2,
    "3": 5/2,
    "4": 6/2,
    "5": 7/2,
    "6": 8/2,
}

Types = [
    "",
    "Normal",
    "Fire",
    "Water",
    "Electric",
    "Grass",
    "Ice",
    "Fighting",
    "Poison",
    "Ground",
    "Flying",
    "Psychic",
    "Bug",
    "Rock",
    "Ghost",
    "Dragon",
    "Dark",
    "Steel",
    "Fairy"
]

TypeDictList = {
"Normal": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 2, "Poison": 1, "Ground": 1, 
          "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 0, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1}
,
"Fire": {"Normal": 1, "Fire": 1/2, "Water": 2, "Electric": 1, "Grass": 1/2, "Ice": 1/2, "Fighting": 1, "Poison": 1, "Ground": 2, 
        "Flying": 1, "Psychic": 1, "Bug": 1/2, "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1/2, "Fairy": 1/2}
,
"FireG1": {"Normal": 1, "Fire": 1/2, "Water": 2, "Electric": 1, "Grass": 1/2, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 2, 
        "Flying": 1, "Psychic": 1, "Bug": 1/2, "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1/2, "Fairy": 1/2}
,
"Water": {"Normal": 1, "Fire": 1/2, "Water": 1/2, "Electric": 2, "Grass": 2, "Ice": 1/2, "Fighting": 1, "Poison": 1, "Ground": 1, 
          "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1/2, "Fairy": 1}
,
"Electric": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1/2, "Grass": 1, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 2, 
          "Flying": 1/2, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1/2, "Fairy": 1}
,
"Grass": {"Normal": 1, "Fire": 2, "Water": 1/2, "Electric": 1/2, "Grass": 1/2, "Ice": 2, "Fighting": 1, "Poison": 2, "Ground": 1/2, 
          "Flying": 1/2, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1/2, "Fairy": 1}
,
"Ice": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1/2, "Fighting": 2, "Poison": 1, "Ground": 1, 
          "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 2, "Fairy": 1}
,
"Fighting": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 1, "Poison": 1, "Ground": 1, 
          "Flying": 2, "Psychic": 2, "Bug": 1/2, "Rock": 1/2, "Ghost": 1, "Dragon": 1, "Dark": 1/2, "Steel": 1, "Fairy": 2}
,
"Poison": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1/2, "Ice": 1, "Fighting": 1/2, "Poison": 1/2, "Ground": 2, 
          "Flying": 1, "Psychic": 2, "Bug": 1/2, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1/2}
,
"PoisonG1": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1/2, "Ice": 1, "Fighting": 1/2, "Poison": 1/2, "Ground": 2, 
          "Flying": 1, "Psychic": 2, "Bug": 2, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1/2}
,
"Ground": {"Normal": 1, "Fire": 1, "Water": 2, "Electric": 0, "Grass": 2, "Ice": 2, "Fighting": 1, "Poison": 1/2, "Ground": 1, 
          "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 1/2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1}
,
"Flying": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 2, "Grass": 1/2, "Ice": 2, "Fighting": 1/2, "Poison": 1, "Ground": 0, 
          "Flying": 1, "Psychic": 1, "Bug": 1/2, "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1}
,
"Psychic": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 1/2, "Poison": 1, "Ground": 1, 
          "Flying": 1, "Psychic": 1/2, "Bug": 2, "Rock": 1, "Ghost": 2, "Dragon": 1, "Dark": 2, "Steel": 1, "Fairy": 1}
,          
"PsychicG1": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 1/2, "Poison": 1, "Ground": 1, 
          "Flying": 1, "Psychic": 1/2, "Bug": 2, "Rock": 1, "Ghost": 0, "Dragon": 1, "Dark": 2, "Steel": 1, "Fairy": 1}
,
"Bug": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 1/2, "Ice": 1, "Fighting": 1/2, "Poison": 1, "Ground": 1/2, 
          "Flying": 2, "Psychic": 1, "Bug": 1, "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1}
,          
"BugG1": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 1/2, "Ice": 1, "Fighting": 1/2, "Poison": 2, "Ground": 1/2, 
          "Flying": 2, "Psychic": 1, "Bug": 1, "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1}
,
"Rock": {"Normal": 1/2, "Fire": 1/2, "Water": 2, "Electric": 1, "Grass": 2, "Ice": 1, "Fighting": 2, "Poison": 1/2, "Ground": 2, 
          "Flying": 1/2, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 2, "Fairy": 1}
,
"Ghost": {"Normal": 0, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 0, "Poison": 1/2, "Ground": 1, 
          "Flying": 1, "Psychic": 1, "Bug": 1/2, "Rock": 1, "Ghost": 2, "Dragon": 1, "Dark": 2, "Steel": 1, "Fairy": 1}
,
"Dragon": {"Normal": 1, "Fire": 1/2, "Water": 1/2, "Electric": 1/2, "Grass": 1/2, "Ice": 2, "Fighting": 1, "Poison": 1, "Ground": 1, 
          "Flying": 1, "Psychic": 1, "Bug": 1, "Rock": 1, "Ghost": 1, "Dragon": 2, "Dark": 1, "Steel": 1, "Fairy": 2}
,
"Dark" : {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 2, "Poison": 1, "Ground": 1, 
          "Flying": 1, "Psychic": 0, "Bug": 2, "Rock": 1, "Ghost": 1/2, "Dragon": 1, "Dark": 1/2, "Steel": 1, "Fairy": 2}
,
"Steel": {"Normal": 1/2, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 1/2, "Ice": 1/2, "Fighting": 2, "Poison": 0, "Ground": 2, 
          "Flying": 1/2, "Psychic": 1/2, "Bug": 1/2, "Rock": 1/2, "Ghost": 1, "Dragon": 1/2, "Dark": 1, "Steel": 1/2, "Fairy": 1/2}
,          
"SteelG2": {"Normal": 1/2, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 1/2, "Ice": 1/2, "Fighting": 2, "Poison": 0, "Ground": 2, 
          "Flying": 1/2, "Psychic": 1/2, "Bug": 1/2, "Rock": 1/2, "Ghost": 1/2, "Dragon": 1/2, "Dark": 1/2, "Steel": 1/2, "Fairy": 1/2}
,
"Fairy": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1, "Fighting": 1/2, "Poison": 2, "Ground": 1, 
          "Flying": 1, "Psychic": 1, "Bug": 1/2, "Rock": 1, "Ghost": 1, "Dragon": 0, "Dark": 1/2, "Steel": 2, "Fairy": 1}
}