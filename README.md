Prérequis : Installer Python et le client Symfony sur sa machine

Pour setup la plateforme de monitoring :

1) Se rendre dans le dossier front
2) Entrer la commande "symfony server:start" pour lancer le serveur php
3) Entrer la commande "php bin/console doctrine:database:create" pour créer la base de données
4) Entrer le commande "php bin/console doctrine:schema:update --force" pour créer les entités de la base de données

Pour lancer la plateforme de monitoring :

Dans le dossier front, entrer la commande "symfony server:start" pour lancer le serveur php

Avant de lancer le virus, il faut lancer la plateforme de monitoring.

Pour lancer le virus, se rendre dans le dossier virus et entrer la commande "python infestation.py"

Pour arrêter la propagation du virus, appuyer sur la touche "q" de son clavier

Chaque attaque sera visible depuis la plateforme de monitoring, d'où la nécessité de la lancer avant de procéder à des attaques
