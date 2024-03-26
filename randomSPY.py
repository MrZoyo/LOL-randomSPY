"""
RandomSPY
Author: MrZoyo
Date: 2024-03-26
----------------
Champions Number: 167
Latest released champion: Smolder
"""

import PySimpleGUI as sg
import random
import io
import os
from PIL import Image

version = 'v0.1.0'
required_folders = ['default', 'champions']
champions_count = len(os.listdir('champions'))

# Define the language settings
LANGUAGES = {
    "English": {
        "folder_error": "Folder {folder} does not exist or is empty, files missing.",
        "random_button": "Random",
        "double_mode": "Double Spy Mode",
        "discord_prompt": "Join BirdGaming Discord:",
        "discord_link": "https://discord.gg/birdgaming",
        "author": "Author: MrZoyo",
        "version": "Version",
        "spy_prefix": "[Spy] ",
        "blue_player": "Blue Player {number}",
        "red_player": "Red Player {number}",
        "window_title": "LOL Spy Generator {version}",
        "help_button": "Help",
        "help_text": """This is a LOL Spy Generator.
Click the random button to generate spies.
You can choose to enable Double Spy mode.
【Common Gameplay】
Custom 5v5 internal games, single or double spies,
Regular players strive for victory, while spies do the opposite,
The regular players of the winning side and the spies of the losing side are the winners.""",
        "help_title": "Help Guide",
        "clash_button": "ARAM 30 RANDOM",
        "red_side": "Red Side",
        "blue_side": "Blue Side",
        "clash_button_tooltip": "Generate 30 random champions for ARAM mode.\n Use self-select mode with this function.",
        "champion_count": f"Champion Count: {champions_count}",
    },
    "中文": {
        "folder_error": "文件夹 {folder} 不存在或为空，文件损坏。",
        "random_button": "随机",
        "double_mode": "双卧底模式",
        "discord_prompt": "游戏组队就来小鸟Discord:",
        "discord_link": "https://discord.gg/birdgaming",
        "author": "作者: MrZoyo",
        "version": "版本",
        "spy_prefix": "[卧底] ",
        "blue_player": "蓝色方-玩家{number}",
        "red_player": "红色方-玩家{number}",
        "window_title": "LOL卧底生成器 {version}",
        "help_button": "帮助",
        "help_text": """这是一个LOL卧底生成器。
点击随机按钮来生成卧底。
可以选择是否开启双卧底模式。
【常用玩法】
内战自定义房间5v5，单卧底或者双卧底，
正常玩家努力寻求胜利，卧底则相反，
获胜方的正常玩家和失败方的卧底为胜利者。""",
        "help_title": "帮助指南",
        "clash_button": "乱斗随机30个",
        "red_side": "红色方",
        "blue_side": "蓝色方",
        "clash_button_tooltip": "为乱斗内战随机30个英雄。\n 使用自选模式配合此功能。",
        "champion_count": f"英雄数量: {champions_count}",
    },
    "Deutsch": {
        "folder_error": "Ordner {folder} existiert nicht oder ist leer, Dateien fehlen.",
        "random_button": "Zufällig Generieren",
        "double_mode": "Doppel-Undercover-Mod",
        "discord_prompt": "Für Spielteams suchen: BirdGaming Discord:",
        "discord_link": "https://discord.gg/birdgaming",
        "author": "Autor: MrZoyo",
        "version": "Version",
        "spy_prefix": "[Undercover] ",
        "blue_player": "Blauer Spieler {number}",
        "red_player": "Roter Spieler {number}",
        "window_title": "LOL Undercover Generator {version}",
        "help_button": "Hilfe",
        "help_text": """Dies ist ein LOL Undercover Generator.
Klicke auf den Zufällig-Button, um Undercover zu generieren.
Du kannst wählen, ob der Doppel-Undercover-Modus aktiviert sein soll.
【Übliche Spielweise】
Benutzerdefiniertes 5v5 internes Spiel, einzelner oder doppelter Undercover,
Normale Spieler streben nach dem Sieg, während Undercover das Gegenteil tun,
Die normalen Spieler der gewinnenden Seite und die Undercover der verlierenden Seite sind die Gewinner.""",
        "help_title": "Hilfeleitfaden",
        "clash_button": "ARAM 30 Zufällige",
        "red_side": "Roter Team",
        "blue_side": "Blauer Team",
        "clash_button_tooltip": "30 Champions für ARAM. \n Verwenden Sie den Selbstauswahlmodus mit dieser Funktion.",
        "champion_count": f"Champion Anzahl: {champions_count}",
    }
}

# Set the default language
current_language = "中文"


def load_image(path, size=(100, 100)):
    """Adjust the size of the image and return the data for display."""
    image = Image.open(path)
    image = image.resize(size, Image.Resampling.LANCZOS)
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    return bio.getvalue()


def check_folders(language):
    for folder in required_folders:
        if not os.path.exists(folder) or not os.listdir(folder):
            sg.popup_error(LANGUAGES[language]["folder_error"].format(folder=folder))
            exit()


def load_champions():
    """Load the images of the champions and return a list of tuples with the path and name of the champion."""
    champions_path = os.path.join('champions')
    all_champions = os.listdir(champions_path)
    random_champions = random.sample(all_champions, 30)  # Select 30 random champions
    return [(load_image(os.path.join(champions_path, champ)), champ.split('.')[0]) for champ in random_champions]


def create_clash_window(selected_champions, language):
    """Create a window with the selected champions."""
    layout = []
    layout.append([sg.Text(LANGUAGES[language]["blue_side"], font=("SimHei", 20), text_color='blue')])
    for i in range(0, 15, 5):  # Blue side
        row_images = [sg.Image(data=champ[0], size=(100, 100)) for champ in selected_champions[i:i + 5]]
        row_names = [sg.Text(champ[1], size=(9, 1), font=("Helvetica", 14)) for champ in selected_champions[i:i + 5]]
        layout.append(row_images)
        layout.append(row_names)
    layout.append([sg.Text('_' * 100)])  # Separator
    layout.append([sg.Text(LANGUAGES[language]["red_side"], font=("SimHei", 20), text_color='red')])
    for i in range(15, 30, 5):  # Red side
        row_images = [sg.Image(data=champ[0], size=(100, 100)) for champ in selected_champions[i:i + 5]]
        row_names = [sg.Text(champ[1], size=(9, 1), font=("Helvetica", 14)) for champ in selected_champions[i:i + 5]]
        layout.append(row_images)
        layout.append(row_names)
    return sg.Window('ARAM Clash Random', layout, modal=True)


def create_spy_window(players, double_mode, language):
    layout = [
        [
            sg.Text(LANGUAGES[language]["discord_prompt"]),
            sg.InputText(LANGUAGES[language]["discord_link"], size=(30, 2), key='-READONLY-', readonly=True,
                         enable_events=True)
        ],
    ]
    blue_spys = random.sample(range(5), 2 if double_mode else 1)
    red_spys = random.sample(range(5), 2 if double_mode else 1)

    for i in range(5):
        blue_text = f"{LANGUAGES[language]['spy_prefix'] if i in blue_spys else ''}{players[i][0]}"
        red_text = f"{LANGUAGES[language]['spy_prefix'] if i in red_spys else ''}{players[i][1]}"

        row = [
            sg.Image(
                data=load_image('./default/wolf_blue.png' if i in blue_spys else './default/human_blue.png')),
            sg.InputText(blue_text, size=(20, 1), disabled=True,
                         text_color='red' if i in blue_spys else 'black'),
            sg.VSeparator(),
            sg.InputText(red_text, size=(20, 1), disabled=True, text_color='red' if i in red_spys else 'black'),
            sg.Image(data=load_image('./default/wolf_red.png' if i in red_spys else './default/human_red.png'))
        ]
        layout.append(row)

    window = sg.Window(LANGUAGES[language]["window_title"].format(version=version), layout, modal=True)
    return window


def create_window(language):
    player_input_layout = [
        [sg.Image(data=load_image('./default/human_blue.png')),
         sg.InputText(LANGUAGES[language]["blue_player"].format(number=i + 1), key=f'BLUE_{i}', size=(15, 1)),
         sg.VSeparator(),
         sg.InputText(LANGUAGES[language]["red_player"].format(number=i + 1), key=f'RED_{i}', size=(15, 1)),
         sg.Image(data=load_image('./default/human_red.png'))]
        for i in range(5)
    ]

    layout = [
        [sg.Button(LANGUAGES[language]["random_button"], key="-Random-", size=(15, 2), font=("Helvetica", 30)),
         ],
        [sg.Button(LANGUAGES[language]['clash_button'], key='-ARAM-', size=(16, 2), font=("Helvetica", 12),
                   tooltip=LANGUAGES[language]['clash_button_tooltip']),
         sg.Checkbox(LANGUAGES[language]["double_mode"], default=False, key='DOUBLE_MODE')],
        [
            sg.Text(LANGUAGES[language]["discord_prompt"]),
            sg.InputText(LANGUAGES[language]["discord_link"], size=(30, 2), key='-READONLY-', readonly=True,
                         enable_events=True)
        ],
        [
            sg.Image(data=load_image('./default/LANG.png', size=(30, 30))),
            sg.Combo(list(LANGUAGES.keys()), default_value=language, key='-LANG-', enable_events=True),
            sg.Button(LANGUAGES[language]["help_button"], key="-HELP-", size=(8, 1), font=("Helvetica", 10)),
        ],
        *player_input_layout,
        [sg.Text(LANGUAGES[language]["author"]),
         sg.Text(f'{LANGUAGES[language]["version"]}: {version}'),
         sg.Text(LANGUAGES[language]["champion_count"]),
         ],

    ]

    return sg.Window(LANGUAGES[language]["window_title"].format(version=version), layout)


def main():
    global current_language
    check_folders(current_language)

    sg.theme('Light Grey 1')
    window = create_window(current_language)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == '-Random-':
            players = [(values[f'BLUE_{i}'], values[f'RED_{i}']) for i in range(5)]
            double_mode = values['DOUBLE_MODE']
            spy_window = create_spy_window(players, double_mode, current_language)
            spy_window.read()
            spy_window.close()
        elif event == '-LANG-':
            current_language = values['-LANG-']
            window.close()
            main()  # Restart the program with the new language

        elif event == "-HELP-":
            sg.popup(LANGUAGES[current_language]["help_text"], title=LANGUAGES[current_language]["help_title"])

        elif event == '-ARAM-':
            selected_champions = load_champions()
            clash_window = create_clash_window(selected_champions, current_language)
            clash_window.read()
            clash_window.close()

    window.close()


if __name__ == '__main__':
    main()
