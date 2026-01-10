import feedparser
import requests
import os

def envoyer_discord(titre, lien, source_nom):
    # On récupère le secret
    webhook_url = os.getenv("DISCORD_WEBHOOK")
    
    # Debug : on vérifie si le secret est chargé
    if not webhook_url:
        print("❌ ERREUR : Le Secret 'DISCORD_WEBHOOK' est vide ou introuvable dans GitHub !")
        return

    payload = {"content": f"✅ **Test de Connexion** : {titre}\n{lien}"}
    response = requests.post(webhook_url, json=payload)
    
    # On affiche le code de réponse (204 = succès chez Discord)
    print(f"Statut Discord : {response.status_code}")

def executer_veille():
    print("--- Démarrage de la vérification ---")
    
    # TEST FORCE : On envoie un message quoi qu'il arrive
    envoyer_discord("Test de configuration", "https://github.com", "Système")
    
    # Le reste de ta veille...
    sources = {"Unity": "https://blog.unity.com/feed"}
    for nom, url in sources.items():
        data = feedparser.parse(url)
        if data.entries:
            envoyer_discord(data.entries[0].title, data.entries[0].link, nom)

if __name__ == "__main__":
    executer_veille()
