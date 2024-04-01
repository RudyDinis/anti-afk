import keyboard
import time

# Fonction pour simuler la pression sur une touche
def press_key(key):
    keyboard.press(key)
    time.sleep(0.1)  # Délai entre la pression et le relâchement de la touche
    keyboard.release(key)

# Liste des touches à presser
keys_to_press = ['w', 'a', 's', 'd'] #permet de faire deplacer le joueur en carré

while True:
    # Boucle pour presser chaque touche dans l'ordre spécifié
    for key in keys_to_press:
        press_key(key)
        press_key(key)
        press_key(key)
        press_key(key)
        press_key(key)
        press_key(key)
        press_key(key)
        press_key(key)
        # Attendre 10 secondes avant de passer à la prochaine touche
