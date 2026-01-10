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

    # Fonction avec paramètres d'entrée et valeur retournée (booléen)
def est_interessant(titre: str) -> bool: # [cite: 120, 126]
    """Vérifie si l'article contient des sujets qui m'intéressent.""" # [cite: 121]
    mots_cles = ["unity", "unreal", "godot", "engine", "update", "vfx", "devlog"]
    # On met tout en minuscule pour ne pas rater de mots
    titre_min = titre.lower()
    
    for mot in mots_cles:
        if mot in titre_min:
            return True # On retourne Vrai si on trouve un mot [cite: 106]
    return False # Sinon on retourne Faux

    def executer_veille():
    # Dictionnaire de sources variées pour avoir plus de chances d'avoir du contenu
    sources = {
        "Unity Blog": "https://blog.unity.com/feed",
        "Godot Engine": "https://godotengine.org/rss.xml",
        "Unreal Engine": "https://www.unrealengine.com/en-US/rss",
        "GameDev.net": "https://www.gamedev.net/rss/index.xml/",
        "Game Developer": "https://www.gamedeveloper.com/rss.xml"
    }

    print("--- Démarrage de la veille technologique ---")
    
    # On force un message de "Bienvenue" pour vérifier la connexion Discord
    envoyer_discord("Robot de Veille Activé", "Le robot vérifie vos sources...", "Système")

    for nom, url in sources.items(): # On parcourt chaque source [cite: 90]
        data = feedparser.parse(url)
        if data.entries:
            article = data.entries[0]
            # Utilisation de notre fonction de filtrage
            if est_interessant(article.title):
                envoyer_discord(article.title, article.link, nom)
            else:
                print(f"Article ignoré (non pertinent) : {article.title}")
    # Le reste de ta veille...
    sources = {"Unity": "https://blog.unity.com/feed"}
    for nom, url in sources.items():
        data = feedparser.parse(url)
        if data.entries:
            envoyer_discord(data.entries[0].title, data.entries[0].link, nom)

if __name__ == "__main__":
    executer_veille()
