
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
	int <port>
	switchport mode trunk
OU
	int <port>
	switchport trunk encapsulation dot1q


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