import feedparser
import requests
import os

# --- FONCTION 1 : ENVOI VERS DISCORD ---
def envoyer_discord(titre, lien, source_nom):
    """Envoie un message au Webhook Discord"""
    webhook_url = os.getenv("DISCORD_WEBHOOK")
    
    if not webhook_url:
        print("❌ ERREUR : Le Secret 'DISCORD_WEBHOOK' est introuvable !")
        return

    payload = {"content": f"✅ **{source_nom}** : {titre}\n{lien}"}
    response = requests.post(webhook_url, json=payload)
    # Ce print permet de voir si Discord accepte le message dans les logs [cite: 23]
    print(f"Statut Discord : {response.status_code}")

# --- FONCTION 2 : FILTRAGE ---
def est_interessant(titre: str) -> bool:
    """Vérifie les mots-clés dans le titre [cite: 120]"""
    mots_cles = ["unity", "unreal", "godot", "engine", "update", "vfx", "devlog"]
    titre_min = titre.lower()
    for mot in mots_cles:
        if mot in titre_min:
            return True # On retourne une valeur booléenne [cite: 106]
    return False

# --- FONCTION 3 : LOGIQUE PRINCIPALE ---
def executer_veille():
    # Ce message nous confirmera que c'est bien la NOUVELLE version qui tourne
    print("--- Démarrage de la veille technologique ---")
    
    # TEST DE CONNEXION : S'affichera sur Discord quoi qu'il arrive
    envoyer_discord("Robot de Veille Activé", "Le robot vérifie vos sources...", "Système")

    sources = {
        "Unity Blog": "https://blog.unity.com/feed",
        "Godot Engine": "https://godotengine.org/rss.xml",
        "Unreal Engine": "https://www.unrealengine.com/en-US/rss",
        "Game Developer": "https://www.gamedeveloper.com/rss.xml"
    }

    for nom, url in sources.items():
        data = feedparser.parse(url)
        if data.entries:
            article = data.entries[0]
            if est_interessant(article.title):
                envoyer_discord(article.title, article.link, nom)

if __name__ == "__main__":
    # Appel de la fonction principale [cite: 74]
    executer_veille()
