import feedparser # Bibliothèque pour lire les flux RSS [cite: 19]
import requests   # Bibliothèque pour envoyer des messages [cite: 37]
import os         # Bibliothèque pour lire les secrets (sécurité)

# Définition de la fonction d'envoi [cite: 120]
def envoyer_discord(titre, lien):
    """Envoie un article sur Discord""" # Docstring [cite: 83]
    webhook_url = os.getenv("DISCORD_WEBHOOK")
    payload = {"content": f"📢 **News :** {titre}\n{lien}"}
    requests.post(webhook_url, json=payload)

# Définition de la fonction principale [cite: 110]
def executer_veille():
    # Liste des sources (les ingrédients) 
    flux_rss = "https://blog.unity.com/feed" 
    
    print("Vérification du flux...")
    data = feedparser.parse(flux_rss)
    
    if data.entries:
        # On prend le premier article (le plus récent)
        article = data.entries[0]
        envoyer_discord(article.title, article.link) # Appel de la fonction [cite: 74]

# Lancement du programme
if __name__ == "__main__":
    executer_veille()
def executer_veille():
    # ... (garde ton code précédent) ...
    
    # AJOUTE CECI POUR TESTER LA CONNEXION :
    print("Envoi d'un test de connexion direct...")
    envoyer_discord("Test de configuration", "Si vous voyez ce message, le bot est bien connecté !", "Système")
