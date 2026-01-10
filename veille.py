import feedparser # [cite: 19]
import requests   # [cite: 19]
import os         # [cite: 19]

# --- FONCTION 1 : ENVOI DISCORD ---
def envoyer_discord(titre, lien, source_nom):
    """Envoie un message formaté au Webhook Discord""" # [cite: 121]
    webhook_url = os.getenv("DISCORD_WEBHOOK")
    
    if not webhook_url:
        print("❌ ERREUR : Le Secret 'DISCORD_WEBHOOK' est introuvable !")
        return # [cite: 106]

    payload = {"content": f"✅ **{source_nom}** : {titre}\n{lien}"}
    response = requests.post(webhook_url, json=payload)
    print(f"Statut Discord : {response.status_code}")

# --- FONCTION 2 : FILTRAGE DES ARTICLES ---
def est_interessant(titre: str) -> bool: # [cite: 120, 126]
    """Vérifie si l'article contient des sujets qui m'intéressent.""" # [cite: 121]
    mots_cles = ["unity", "unreal", "godot", "engine", "update", "vfx", "devlog"]
    titre_min = titre.lower()
    
    for mot in mots_cles:
        if mot in titre_min:
            return True # [cite: 106, 117]
    return False

# --- FONCTION 3 : LOGIQUE DE VEILLE ---
def executer_veille():
    print("--- Démarrage de la veille technologique ---")
    
    # 1. Test de connexion systématique au lancement
    envoyer_discord("Robot de Veille Activé", "Le robot vérifie vos sources...", "Système")

    # 2. Liste des sources (Dictionnaire)
    sources = {
        "Unity Blog": "https://blog.unity.com/feed",
        "Godot Engine": "https://godotengine.org/rss.xml",
        "Unreal Engine": "https://www.unrealengine.com/en-US/rss",
        "GameDev.net": "https://www.gamedev.net/rss/index.xml/",
        "Game Developer": "https://www.gamedeveloper.com/rss.xml"
    }

    # 3. Boucle de parcours des sources [cite: 90]
    for nom, url in sources.items():
        print(f"Vérification de : {nom}...")
        data = feedparser.parse(url)
        
        if data.entries:
            article = data.entries[0]
            # Utilisation de la fonction de filtrage
            if est_interessant(article.title):
                envoyer_discord(article.title, article.link, nom)
            else:
                print(f"Article ignoré : {article.title}")

# --- POINT D'ENTRÉE DU PROGRAMME ---
if __name__ == "__main__":
    executer_veille() # Appel de la fonction principale [cite: 74]
