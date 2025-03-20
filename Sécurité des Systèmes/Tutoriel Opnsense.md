**Proxy = intermédiaire**
*Exemple: quand l'utilisateur veut aller sur un site, il demande un proxy, et le proxy va aller lui chercher et lui donner le site.*
*On peut le configurer pour filtrer certains sites*

---------------------

Créer une VM avec l'iso de Opnsense. Mettre le minimum de coeurs, 4096mb de ram.
Dans network type: do not use... (la dernière option)
Disque: 20GB
Settings: 
VMNet0 (Nat)
VMNet10 (Rien)

Démarrer la VM.
Do you want to proceed? yes
login: installer
password: opnsense

clavier French (accent keys) -> Continue...
Install (ZFS)
Stripe
Sélectionner le disque dur (espace) puis OK
Yes

Quand l'install est terminé:
Exit and reboot
Déconnecter le CD Rom (en décochant Connected dans les options de la VM)

login: root
mdp: opnsense

Si en WAN pas d'ip il faut:
1) Assign Interfaces
et inverser Lan et Wan
====

2 Set interface IP Address
Changer le LAN
DHCP: Non
192.168.1.254
Masque: 24
Entrer
ipv6: Non
Ipv6 via DHCP: Non
Ipv6: Entrer
enable the DHCP server on LAN? Yes
IPv4 client address range: 192.168.1.10
end range: 192.168.1.20
HTTPS: Non
Certificate: Non
access details? Non

Aller sur une VM Windows
Settings: VMNet10
Devrait avoir accès à internet

Navigateur internet -> 192.168.1.254 = interface opnsense
Username: root
Mdp: opnsense

mettre en French:
Serveur DNS principal: 8.8.8.8
Fuseau Horaire Europe/Paris
Ne rien changer à l'IP Lan, Suivant
Mdp osef
Puis appliquer

Mettre à jour:
Système -> Firmware -> Mises à jour
Statut -> Vérifier les mises à jour et faire la maj

Création du certificat:
Système -> Gestion des certificats -> Autoritité
Ajouter un certificat (+)
Méthode Créer une autorité de certification interne
Description: Certificat_SSL
Pays France
État Grand-Est
Lieu Metz
Organisation MNS
Sauvegarder...

Télécharger le certificat (symbole de nuage) en tant que "Certificate"
Dossier téléchargements: Renommer le certificat et changer l'extension -> .crt
Ouvrir le certificat et installer le certificat -> Ordinateur local puis Suivant
Placer tous les certificats dans le certificat: "Autorités de certification racine de confiance.."(2eme)
Terminer OK...

Installer le proxy:
Système -> Firmware -> Greffons
Barre de cherche: Squid (os-squid)
Installer en cliquant sur le plus
Une fois installé:
Alimentation -> Redémarrer

Se reconnecter
Services -> Squid Web Proxy -> Administration
Onglet Forward Proxy:
	Interfaces mandataires: LAN
	Port du proxy: laisser par défaut (3128)
	AC à utiliser: Certificat_SSL
	Appliquer
Onglet Réglages Proxy Généraux:
	Cocher Activer le proxy
	Appliquer
Cliquer sur la flèche de l'onglet -> Paramètres Cache Local:
	Cocher "Activer le cache local"
	Appliquer

Pare-Feu -> Règles -> LAN
Ajouter une règle:
	Action: Bloquer
	Protocole: TCP
	Source: LAN net
	Plage de ports de destination: HTTP
	Description: Blocage HTTP pour forcer le PROXY
	Sauvegarder
Dupliquer (3eme bouton):
	Modifier HTTP en HTTPS

L'ordre supérieur est prioritaire:
Faut cocher les 2 règles
Cliquer sur la flèche: déplacer les règles à la place de celle ci (le premier de la liste)
Appliquer les changements
Devrait ne plus avoir accès à internet...


Services -> Squid Web Proxy -> Administration
Onglet Forward Proxy:
	Cocher "Activer le proxy HTTP Transparent"
	Cocher "Activer l'inspection SSL" -> Appuyer sur le i
	Cliquer sur "Add a new Firewall rule" (le lien souligné)
	Rien changer puis Sauvegarder
Appuyer aussi sur le i de "Activer le proxy HTTP Transparent"
	Cliquer sur le lien souligné
	Sauvegarder
On devrait maintenant avoir internet

Onglet Liste de contrôle d'accès distantes:
Ajouter une Blacklist:
	Activée
	Nom de fichier: Blacklist
	URL: http://dsi.ut-capitole.fr/blacklists/download/blacklists.tar.gz
	Description: Blacklist
	Sauvegarder
Cliquer sur Télécharger ACLs

Éditer la liste noire:
Catégories Effacer tout puis sélectionner social_networks
Sauvegarder
Télécharger les ACLs & les Appliquer