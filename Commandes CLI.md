
**créer un vlan:**
	enable
	configure terminal
	vlan <id nombre>
	name <nom>

----------------------------------------------

attribuer des vlan à une rangée de ports

	int range portA-portB (ex fa0/1-12)
	switchport access vlan <id vlan>
	exit

----------------------------------------------

afficher vlan:
	show vlan brief

----------------------------------------------

retirer l'ip d'une interface
	int <port>
	no ip address

----------------------------------------------

faire des sous interfaces:
	int <port.vlan> (exemple: int G0/0.10)
	encapsulation dot1Q <id vlan>
	ip address <gateway> <subnet mask>

----------------------------------------------

 Voir la config:
	 show running-config

----------------------------------------------

lier deux périphériques en mode trunk:
	int <port>vm
	switchport mode trunk
OU pnetlab:
	int <port>
	switchport trunk encapsulation dot1q
	switchport mode trunk

pour voir les trunks actifs:
	show interfaces trunk

pour voir les interfaces:
	show ip interfaces brief
----------------------------------------------

attribuer un vlan à un port:
	int <port>
	switchport mode access
	switchport access vlan <id vlan>

----------------------------------------------

	vtp mode server
	vtp domain <nom>
	vtp password <mdp>


	vtp mode client
	vtp domain <nom>
	vtp password <mdp>

----------------------------------------------

configurer un DHCP:
	ip dhcp pool <nom>
	network <ip réseau> <subnet mask>
	default-router <gateway>
		(pour le dns: dns-server <adresse>)
	exit

----------------------------------------------

Changer le nom d'un appareil:
	enable
	configure terminal
	hostname <nom>

-----------------------------------------------

Activer les VLAN transférées sur le switch + leur donner une IP:
	int vlan <id vlan>
	ip address <gateway> <subnet mask>
	no shutdown

-----------------------------------------------

Voir les IP données aux VLAN + leur état:
	show ip interface brief

-----------------------------------------------

Autoriser le routage inter-VLAN:
	ip routing

-----------------------------------------------

Retirer switchport puis mettre une nvl ip:
	configure terminal
	interface <port>
	no switchport
	ip address <ip> <subnet mask>

-----------------------------------------------

Commande pour rediriger le routeur ailleurs:

	ip route <adresse ip> <subnet mask> <ip destinataire>

(mettre "0.0.0.0 0.0.0.0" pour dire qu'on cherche toutes les ip et subnet mask | ip destinataire = où chercher)

-----------------------------------------------

Routeur:
int <port>
no ip address (ou ip address <IP> <SubnetMask>)
no shutdown

------------------------------------------------

Afficher l'ip sur pnetlab:
Show ip

-------------------------------------------------
Renommer un pc pnetlab:
set pcname <nom>

Attribuer une ip à un vpc Pnetlab:

ip <adresse ip> <subnet mask ou CIDR> <passerelle par défaut>

Sauvegarder:
save

------------------------------------------------

#########################################Sécurité du routeur

Créer un username + mdp:

configure terminal
username <nom> password <mdp>
	(mdp caché:  "secret" au lieu de "password")

Puis l'appliquer en l'ajoutant à la console:
line console 0
login local

-------------
Mettre un mot de passe sans username:

line console 0
password <mdp>
	(pour enlever le mdp: "no password <mdp>)


Mettre un mot de passe au mode "enable":
enable password <mdp>
	(ou "secret" au lieu de "password")

-------------

Mettre une longueur minimum de mot de passe:
security passwords min-length <0-16>

-------------
Encrypter tous les mots de passe (moins sécurisé que la commande "secret"):
service password-encryption

-------------
créer un utilisateur avec tous les droits et mdp crypté:
username <nom> privilege 15 secret <mdp>

Voir le niveau de privilege (plus bas: 0 | plus haut: 15):
show privilege
-------------

Créer un utilisateur et niveau de privilege customisé:
username <nom> privilege <0-15> secret <mdp>
privilege exec level <0-15> <commandes-autorisées>
(ex: privilege exec level 3 show startup-config)

-------------

Déconnecter pour inactivité au bout d'un certain temps:
line console 0
exec-timeout <min> <secs>

-------------
Empêcher le login après un nb d'essais raté:
login block-for <secondes> attempts <nb essais> within <secondes>

-------------
Message router:

avant login:
banner motd &message&

après login:
banner login &message&

----------------------------
Config le telnet:
line vty <1ere ligne> <derniere ligne>
login local (permet d'ajouter les identifiants au telnet)

Se connecter au router depuis un ordinateur:
telnet <gateway>

----------------------------
Config SSH (il faut pas utiliser le hostname par défaut):

ip domain-name <nom>
crypto key generate rsa
line vty <1ere ligne> <derniere ligne>
transport input ssh

Se connecter au router depuis un ordinateur:
ssh -l <username> <gateway>

--------------------------------------------------------
Sécurité Switch:

Dire à quelle adresse mac le port peut être connecté:
int <port>
switchport port-security mac-address <adresse mac>
	ou:
	switchport port-security mac-address sticky
	(ça permet d'enregistrer l'adresse mac du premier appareil connecté au port)

shutdown le port en cas de violation:
switchport post-security violation shutdown

Nb maximum d'adresses mac pour le port:
switchport port-security maximum <1-132>

voir les violations:
show port-security

--------------------------------------------------------
Commandes ACLs



Créer une access-list bloquant un réseau:
	access-list <id/nom> deny <réseau> <wildcard-mask>
	access-list <id/nom> permit any (pour permettre au reste de pouvoir y accéder)

Créer une ACL standard pour whitelist une IP:
	ip access-list standard <id/nom>
	permit host <IP périphérique> (ou permit <IP réseau> <wildcard-mask>)
	deny any
ou
	access-list <id> permit <IP> <wildcard-mask>
	access-list <id> deny any

Placer l'access-list sur un port:
	int <port>
	ip access-group <ID ACL> <in/out>

Pour voir les access-lists:
	show access-lists
	ou
	show access-lists <nombre/nom..>



Voir sur quelles interfaces il y a des ACLs:
	show run | include interface|access

Voir une interface spécifique:
	show ip interface <port>
-------------

Pour supprimer toutes les ACLS / ACL spécifique:
	no access-list
	ou
	no access-list <ID ACL>

Supprimer l'ACL d'un port:
	int <port>
	no ip access-group <ID ACL> <in/out>
-------------

Ajouter une description à une ACL:
	access-list <id/nom> remark <description>

Modifier une ACL standard:
	ip access-list standard <nom>
	<ligne> <commande> (ex: 30 permit any)
	end

Donner l'accès FTP (et ICMP) d'un réseau à un ordinateur:
	access-list <ID> permit tcp <ip-server> <wildcard-mask> host <IP-PC> eq ftp
	access-list <ID> permit icmp <ip-server> <wildcard-mask> host <IP-PC>
	(puis l'appliquer à un port)

Se connecter au serveur FTP depuis un ordinateur:
	ftp <IP>
Pour quitter: quit


Donner l'accès HTTP (et ICMP) à un PC:
	ip access-list extended <nom>
	permit tcp <ip-server> <wildcard-mask> host <IP-PC> eq www
	permit icmp <ip-server> <wildcard-mask> host <IP-PC>

Interdire l'accès HTTP d'un pc à un serveur:
	ip access-list extended <nom/id>
	deny tcp host <IP-PC> host <IP-SERVER> eq 80 (et 443 pour HTTPS)