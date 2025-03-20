
Sur vmware File -> open -> fichier en .ova
Mettre 4GB de ram et 3 cartes réseau: (1ere carte en NAT custom et les deux autres en Host-Only)

Mettre le clavier en fr et choisir un password.... no et yes puis configurer l'IP etc.
![[Pasted image 20250311134623.png]]
![[Pasted image 20250311140434.png]]




--------------

## **Mettre à jour:**

![[Pasted image 20250311115013.png]]
*Aller dans configuration -> Système -> Maintenance -> Cliquer sur les 3 points et sélectionner le fichier .maj puis cliquer sur "Mettre à jour le firewall"... Vérifier le CLI Stormshield et refresh quand c'est fini*

----------------

## **Appliquer la licence correspondante**:

![[Pasted image 20250311115201.png]]
*Aller dans configuration -> Système -> Licence -> Cliquer sur les 3 points et sélectionner le fichier .licence puis cliquer sur "Installer"*

------------

## Autoriser le PC à se accéder à internet:


D'abord mettre en "(10) Pass all"
![[Pasted image 20250311115402.png]]
![[Pasted image 20250311115435.png]]
*Aller dans configuration -> Politique de Sécurité -> Filtrage et Nat -> Nouvelle règle -> Règle de partage d'adresse source (masquerading) -> État on -> Source: Firewall_out -> Appliquer -> Activer*

----------


