import os
import requests

def test_robot():
    print("--- APPEL DE LA FONCTION DE TEST ---")
    webhook = os.getenv("DISCORD_WEBHOOK")
    if webhook:
        requests.post(webhook, json={"content": "🚀 TEST : Le robot est enfin à jour !"})
        print("Message envoyé à Discord")
    else:
        print("ERREUR : Secret introuvable")

if __name__ == "__main__":
    test_robot()
