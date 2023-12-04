#!/usr/bin/env python
# Ce shebang indique au système d'exploitation d'exécuter ce script avec Python.

from http.server import BaseHTTPRequestHandler, HTTPServer

from manager import QueueClient

# Importe les classes nécessaires pour créer un serveur HTTP.


# Importe la classe QueueClient depuis le module 'manager'. Cette classe n'est pas standard.


class Proxy(QueueClient, BaseHTTPRequestHandler):
    # Crée une nouvelle classe 'Proxy', héritant de QueueClient et BaseHTTPRequestHandler.

    def do_GET(self):
        # Définit la méthode pour gérer les requêtes HTTP GET.

        self.send_response(200)
        # Envoie une réponse HTTP avec le code de statut 200, signifiant "OK".

        self.send_header("Content-type", "application/json")
        # Envoie un en-tête HTTP indiquant que le contenu de la réponse est de type JSON.

        self.end_headers()
        # Termine l'écriture des en-têtes HTTP.

        t = self.task_queue.get()
        # Récupère une tâche de la file d'attente 'task_queue'.

        self.wfile.write(bytes(t.to_json(), "utf-8"))
        # Convertit la tâche en JSON, l'encode en UTF-8, et l'écrit dans le flux de réponse.


def run(server_class=HTTPServer, handler_class=Proxy):
    # Définit une fonction 'run' pour démarrer le serveur. Paramètres par défaut pour la classe du serveur et la classe du gestionnaire.

    server_address = ("", 8000)
    # Définit l'adresse du serveur : écoute sur toutes les interfaces réseau au port 8000.

    httpd = server_class(server_address, handler_class)
    # Crée une instance du serveur HTTP avec l'adresse et la classe de gestionnaire spécifiées.

    httpd.serve_forever()
    # Démarre le serveur, le faisant écouter et répondre aux requêtes indéfiniment.


if __name__ == "__main__":
    # Vérifie si le script est exécuté en tant que programme principal.

    run()
    # Exécute la fonction 'run' pour démarrer le serveur.
