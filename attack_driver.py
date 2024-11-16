list = [
"EssenceDrain",
"GhostlyStrike",
"ExecutionSentence",
"Impiety",
"SoulReaver",
"Sacrifice",
"Parry",
"Flèche",
"Bloodshed",
"EssenceBarrage",
"Perforate",
"Impale",
"PreyUpon",
"Skewer",
"Crusify",
"Mirage",
"Sadism",
]

import subprocess
import os

def create_dir(attacks_dir):
    if not os.path.exists(attacks_dir):
        os.makedirs(attacks_dir)

for card in list:
    keyword = card.lower()
    name = f"attacks_original/{keyword}"
    name_png = f"{name}.png"
    name_out = f"attacks/{card}"

    create_dir("attacks")
    create_dir("attacks_original")

    subprocess.run(['python', 'prompt_maker.py', keyword, name])  
    subprocess.run(['python', 'mask_image.py', name_png, "attack_mask.png", name_out])  
