## **Les Menaces**

![[Pasted image 20250120091241.png]]
![[Pasted image 20250120093247.png]]

![[Pasted image 20250120093214.png]]
![[Pasted image 20250120093302.png]]



**Types de cloud public:**
-  **Software as a Service (SaaS)**
	This is a subscription-based model that provides organizations with software that is centrally hosted and accessed by users via a web browser, app or other software. In other words, this is software not stored locally but in the cloud.

- **Platform as a Service (PaaS)**
	This subscription-based model provides a platform that allows an organization to develop, run and manage its applications on the service’s hardware, using tools that the service provides. This platform is accessed via the public cloud.

- **Infrastructure as a Service (IaaS)**
	This subscription-based model provides virtual computing resources such as hardware, software, servers, storage and other infrastructure components over the Internet. An organization will buy access to them and use them via the public cloud.

Menaces du cloud public:
- Data breaches.
- Loss or theft of intellectual property.
- Compromised credentials or account hijacking.
- Social engineering attacks.
- Compliance violation.


**Examples of threats to an organization’s physical facilities domain include:**

- Natural threats such as extreme weather and geological hazards.
- Someone gaining unauthorized access to the premises.
- Power interruptions or outages.
- Social engineering attacks that attempt to find out about an organization’s security policies and procedures.
- Breaches of electronic perimeter defenses.
- Theft.
- An unlocked data center.
- A lack of surveillance on the premises.


**1.1.15 Threats to Applications**

The **application domain** includes all of the critical systems, applications and data used by an organization to support operations. Increasingly, organizations are moving applications such as email, security monitoring and database management to the public cloud.

Common threats to applications include:

- Someone gaining unauthorized access to data centers, computer rooms, wiring closets or systems.
- Server downtime during maintenance periods.
- Network operating system software vulnerabilities.
- Data loss.
- Client-server or web application development vulnerabilities.


**advanced persistent threat (APT)** = *continuous attack that uses elaborate espionage tactics involving multiple actors and/or sophisticated malware to gain access to and analyze a target’s network. (Attackers operate under the radar and remain undetected for a long period of time, with potentially devastating consequences. APTs typically target governments and high-level organizations and are usually well-orchestrated and well-funded.)*


Logiciels de backdoor: Netbus, Back Orifice.

*Cybercriminals typically have authorized users unknowingly run a remote administrative tool program (RAT) on their machine to install a backdoor that gives the criminal administrative control over a target computer. Backdoors grant cybercriminals continued access to a system, even if the organization has fixed the original vulnerability used to attack the system.*


**Rootkit** = *Un rootkit est un type de malware conçu pour modifier le système d'exploitation afin de créer une backdoor permettant aux attaquants d'accéder à l'ordinateur à distance. Exploitant souvent des vulnérabilités logicielles pour obtenir des privilèges élevés, les rootkits modifient des fichiers système et peuvent altérer les outils de surveillance et d'analyse, ce qui les rend particulièrement difficiles à détecter. Dans la plupart des cas, il est nécessaire de réinstaller complètement le système pour éliminer un rootkit.*


**Threat Intelligence Sources:**

- Dark Web

- **Indicator of compromise (IOC)** *IOCs such as malware signatures or domain names provide evidence of security breaches and details about them.*

- **Automated Indicator Sharing (AIS)** *enables the real-time exchange of cybersecurity threat indicators using a standardized and structured language called Structured Threat Information Expression (STIX) and Trusted Automated Exchange of Intelligence Information (TAXII).*

------------
## **Le Social Engineering**



**Types de Social Engineering:**

- Le **pretexting** est une attaque où un individu ment pour accéder à des données sensibles. Par exemple, l'attaquant peut prétendre avoir besoin d'informations personnelles ou financières pour "confirmer" l'identité d'une personne.

- Une attaque **quid pro quo** (quelque chose contre quelque chose) consiste à demander des informations personnelles en échange d'un avantage, comme un cadeau. Par exemple, un email malveillant peut demander des données sensibles en promettant des vacances gratuites.

- L'**identity fraud** (fraude à l'identité) consiste à utiliser l'identité volée d'une personne pour obtenir des biens ou des services par tromperie. Par exemple, un individu peut utiliser vos données pour demander une carte de crédit à votre nom.



Le **shoulder surfing** consiste à espionner une cible, parfois à distance, pour obtenir des informations sensibles comme des codes PIN ou mots de passe. 
Le **dumpster diving** est "la fouille des poubelles" pour récupérer des données précieuses. Détruire les documents sensibles, par exemple en les broyant, permet de s’en protéger.

L'**impersonation** consiste à se faire passer pour quelqu'un d'autre pour manipuler ou nuire, par exemple en exigeant de l'argent sous menace ou en publiant des contenus en ligne pour discréditer une victime.

Un **hoax** (canular) est une tromperie visant à manipuler ou effrayer, pouvant causer autant de perturbations qu'une véritable faille de sécurité. Par exemple, un message avertissant d'une menace de virus inexistante incite les utilisateurs à le partager, propageant une panique inutile via email et réseaux sociaux.



Le **piggybacking** ou **tailgating** se produit lorsqu'un criminel suit une personne autorisée pour accéder à un lieu sécurisé. Cela peut se faire en donnant l'impression d'être accompagné, en rejoignant une foule ou en ciblant une personne négligente. Pour prévenir ce type d'attaque, on utilise des portes doubles, ou **mantrap**, où la porte extérieure se ferme avant d'ouvrir l'intérieur.



Il existe d'autres moyens pour que les attaquants trompent leurs victimes:
- **Fausses factures**
- **Watering hole attack** consistant à infecter des sites fréquemment visités par une organisation
- **Typosquatting** consistant à exploiter les fautes de frappe dans les url pour rediriger vers un autre site malveillant
- **Prepending** consistant à supprimer le tag "externe" des mails utilisés par les organisations, pour leur faire croire que le mail est interne.
- **Influence campaigns** souvent utilisé en "cyber-guerre", propageant les fake news sur les réseaux sociaux.

---------------------

## **Programmes malveillants**

- Un **virus** est un programme qui se réplique en s'attachant à d'autres fichiers. Il peut être inoffensif ou destructeur, modifiant ou supprimant des données. Les virus se propagent via des clés USB, des téléchargements ou des pièces jointes d'emails. Une fois activés, ils infectent d'autres programmes ou ordinateurs et peuvent muter pour éviter la détection, comme le virus Melissa, qui a causé 1,2 milliard de dollars de dégâts en 1999.

- Un **worm (ver)** est un programme malveillant qui se réplique en exploitant indépendamment des vulnérabilités des réseaux. Contrairement à un virus, il n'a pas besoin de programme hôte pour fonctionner et peut se propager rapidement sans interaction de l'utilisateur, ralentissant souvent le réseau. Les vers exploitent des vulnérabilités, se propagent et contiennent un code malveillant pour endommager les systèmes. En 2001, le ver Code Red a infecté plus de 300 000 serveurs en 19 heures.

- Un **cheval de Troie (Trojan Horse)** est un malware qui dissimule ses véritables intentions sous une apparence légitime. Il n'est pas auto-réplicant comme un virus, mais se lie souvent à des fichiers non exécutables (images, audio, vidéo), servant de leurre pour nuire aux systèmes des utilisateurs sans méfiance. Les chevaux de Troie exploitent les privilèges de l'utilisateur qui les exécute.

- Une **bombe logique (logic bomb)** est un programme malveillant qui s'active lorsqu'un déclencheur spécifique se produit. Une fois activée, elle peut endommager des fichiers, des bases de données, ou même détruire des composants matériels en les surchauffant, comme le CPU et les disques durs.

+ Le **ransomware** crypte les données d'un système et demande une rançon pour les déverrouiller, souvent via phishing ou vulnérabilités logicielles.

-------------
## **Attaques DoS (Denial of Service Attacks)**

**Deux types principaux:**

- **Quantité excessive de trafic** : lorsqu'un réseau, un hôte ou une application reçoit trop de données à un rythme qu'il ne peut pas gérer, entraînant un ralentissement, une réponse retardée ou un plantage du service.

- **Paquets formatés malicieusement** : envoyés à un destinataire de manière incorrecte, empêchant ce dernier de les traiter, ralentissant ou faisant planter le dispositif récepteur.
## **Attaques DDoS (Distributed denial of service)**

Les attaques **DDoS** (Distributed Denial of Service) sont similaires aux attaques **DoS** (Denial of Service), mais proviennent de multiples sources coordonnées. Un réseau de machines infectées (**bots**) est utilisé pour saturer un service, le rendant inaccessible.


---------------
## **DNS (Domain Name System)**

- Le **domain reputation** désigne la réputation d'un domaine ou d'une adresse IP dans le **DNS**. Une organisation doit surveiller cette réputation pour se protéger contre les domaines malveillants.

- Le **DNS spoofing** (ou **DNS cache poisoning**) est une attaque où de fausses données sont introduites dans le cache d'un résolveur DNS, redirigeant le trafic d'un domaine vers l'ordinateur de l'attaquant en exploitant une vulnérabilité du logiciel DNS.

- Le **domain hijacking** survient lorsqu'un attaquant prend illégalement le contrôle des informations DNS d'un domaine. Il modifie généralement l'adresse email de l'administrateur via **social engineering** ou en piratant son compte email, souvent accessible via le **WHOIS** public.

- Une **URL** (Uniform Resource Locator) est un identifiant unique pour localiser une ressource sur Internet. Les redirections d'URL sont courantes à des fins légitimes, comme revenir à la page de connexion d'un portail. Cependant, les attaquants peuvent exploiter cette fonctionnalité pour rediriger un utilisateur vers un site malveillant.

----------------
## **Attaques dans le Layer 2**

### Spoofing

- Le **spoofing** exploite une relation de confiance pour usurper des identités. Le **MAC spoofing** masque un appareil comme légitime, l'**ARP spoofing** associe une adresse MAC falsifiée à une IP autorisée, et l'**IP spoofing** falsifie l'adresse source des paquets IP.

### MAC Flooding

- Le **MAC Flooding** consiste à saturer un réseau de fausses adresses MAC, compromettant ainsi la sécurité du **switch** réseau et perturbant la transmission des données.

---------------
## **Man in the Middle**

### Man-in-the-Middle (MitM)

- Une attaque **Man-in-the-Middle (MitM)** se produit lorsqu'un cybercriminel prend le contrôle d'un appareil à l'insu de l'utilisateur. Il peut alors intercepter, manipuler et transmettre de fausses informations entre l'expéditeur et la destination prévue.


### Man-in-the-Mobile (MitMo)

- Le **MitMo** est une variante du **MitM** ciblant les appareils mobiles. Il extrait des informations sensibles et les envoie aux attaquants, comme **ZeuS**, un malware qui capte discrètement les SMS de vérification à deux étapes.

------------
## **Zero-Day Attacks**

- Une attaque **zero-day** exploite des vulnérabilités logicielles avant qu'elles ne soient découvertes ou corrigées par le fournisseur. Les réseaux sont particulièrement vulnérables entre la découverte de l'exploit et la publication du patch. Se protéger contre ces attaques rapides nécessite une approche de sécurité réseau plus sophistiquée et globale.

## **Keyboard Logging**

- Le **keyboard logging** (ou keylogging) enregistre les frappes clavier d'un utilisateur pour collecter des informations sensibles (mots de passe, sites visités). Il peut être détecté et supprimé par certains logiciels anti-spyware.


*Les organisations peuvent se défendre contre diverses attaques en :*

- *Configurant des **firewalls** pour bloquer les paquets internes venant de l'extérieur.*
- *Maintenir les **patches** et mises à jour à jour.*
- *Répartissant la charge de travail sur plusieurs serveurs.*
- *Bloquant les paquets **ICMP** externes avec des firewalls pour prévenir les attaques **DoS** et **DDoS**.*


---------------------

## **Grayware et SMiShing**

- Les **grayware** sont des applications indésirables, non malveillantes, mais potentiellement risquées (suivi de localisation, publicités intrusives). Ces fonctionnalités sont souvent dissimulées dans les conditions d’utilisation.

- Le **SMiShing**, lui, utilise de faux SMS pour inciter à visiter un site malveillant ou appeler un numéro frauduleux, entraînant des risques de vol de données ou d’installation de malware.

## **Rogue Access Points**

Un **Rogue Access Point** est un point d'accès sans fil non autorisé installé sur un réseau sécurisé. Il peut être exploité par des attaquants pour accéder au réseau via des tactiques de **social engineering**. Ces points peuvent servir à des attaques **MitM**.
**evil twin** = un faux point d'accès imite une connexion légitime pour intercepter le trafic réseau et voler des informations.

## **Radio Frequency Jamming**

Les signaux sans fil sont vulnérables aux interférences électromagnétiques (**EMI**), aux interférences radio (**RFI**) et au brouillage intentionnel. Les attaquants exploitent cela en utilisant un brouilleur RF pour empêcher la transmission en égalant la fréquence, la modulation et la puissance du signal cible.

## **Bluejacking et Bluesnarfing**

- Le **bluejacking** utilise le Bluetooth pour envoyer des messages ou images non autorisés à un autre appareil.
- Le **bluesnarfing**, lui, permet à un attaquant de copier des données comme des emails ou contacts via une connexion Bluetooth.

## **Attaques contre les protocoles Wi-Fi**

Le **WEP** et le **WPA** sont des protocoles de sécurité pour réseaux sans fil. Le **WEP**, conçu pour protéger les **WLAN**, chiffrait les données mais souffrait de faiblesses comme un vecteur d’initialisation (**IV**) statique et un manque de gestion des clés, rendant son accès vulnérable. Le **WPA** et le **WPA2** ont été créés pour corriger ces lacunes, offrant un chiffrement plus sécurisé, bien qu’un attaquant puisse toujours analyser le trafic via un outil de capture de paquets.


## **Wi-Fi et défense mobile**

Pour se protéger des attaques sur les réseaux sans fil et appareils mobiles, il est conseillé de :

- Activer les fonctionnalités de sécurité sans fil comme l’authentification et le chiffrement, et modifier les paramètres par défaut.
- Placer les points d’accès hors du pare-feu ou dans une zone démilitarisée (DMZ).
- Utiliser des outils comme **NetStumbler** pour détecter les points d’accès ou postes non autorisés.
- Définir une politique pour l’accès invité au réseau Wi-Fi.
- Préférer une **VPN d'accès distant** pour les connexions WLAN.

-----------

## **Cross-Site Scripting**

**Cross-site scripting (XSS)** est une vulnérabilité courante dans les applications web. Les cybercriminels injectent du code malveillant dans une page web, qui est ensuite chargé par le navigateur de la victime. Ce code peut accéder à des cookies, des jetons de session ou d'autres informations sensibles, permettant au criminel d'usurper l'identité de l'utilisateur.


## **Injection de code**

*Les sites modernes utilisent souvent des bases de données comme SQL ou XML pour gérer leurs données. Les attaques par injection exploitent les failles de ces bases pour accéder ou manipuler les informations.*

- **Une attaque par injection XML** corrompt une base de données XML en manipulant les requêtes pour accéder à des informations sensibles ou modifier un site web.

- **Une attaque par injection SQL** insère une commande SQL malveillante dans un champ de saisie pour exploiter une faille de filtrage, permettant un accès non autorisé à la base de données pour voler, modifier ou détruire des données.

- **L'attaque par injection DLL** consiste à tromper une application pour qu'elle appelle un fichier DLL malveillant, l'exécutant ainsi dans le cadre du processus cible. Cela permet à un cybercriminel d'injecter et d'exécuter du code malveillant dans un programme.

- **L'attaque par injection LDAP** exploite les vulnérabilités de validation des entrées pour injecter et exécuter des requêtes sur les serveurs LDAP, permettant aux cybercriminels d'extraire des informations sensibles depuis le répertoire LDAP d'une organisation.


## **Dépassement de tampon (Buffer overflow)**

Un buffer overflow se produit lorsqu'un programme écrit au-delà de la capacité d'un tampon mémoire, permettant à un attaquant d'accéder à la mémoire d'autres processus et de prendre le contrôle du système.

## **Exécutions de code à distance**

Le **Metasploit Project** est un outil de sécurité informatique utilisé pour tester des vulnérabilités et réaliser des tests de pénétration. Le **Metasploit Framework** permet de développer et exécuter du code exploit contre une cible distante. **Meterpreter**, un composant de **Metasploit**, permet de prendre le contrôle d’un appareil cible via un processus en mémoire, sans laisser de trace sur le disque dur, échappant ainsi aux logiciels antivirus. Il inclut également un module pour contrôler la webcam d'un système distant.

## **Autres attaques d'application**

### Cross-site request forgery (CSRF)

- **CSRF (Cross-Site Request Forgery)** exploite un site web en envoyant des commandes non autorisées depuis le navigateur d'un utilisateur vers une application de confiance, souvent via des images, des formulaires cachés ou JavaScript.

### Race condition attack

- **Une attaque de condition de course (race condition)** se produit lorsqu'un système, conçu pour exécuter des tâches dans un ordre spécifique, est contraint d'effectuer plusieurs opérations simultanément, par exemple lorsque plusieurs threads accèdent et modifient des données partagées en même temps.

### Improper input handling attack

- **Une attaque liée à une gestion incorrecte des entrées** se produit lorsque les données saisies par un utilisateur ne sont pas correctement validées, ce qui peut perturber le flux de données d'un programme et provoquer des vulnérabilités critiques, comme des attaques par dépassement de tampon ou par injection SQL.

### Error handling attack

- **Une attaque par gestion des erreurs** utilise des messages d'erreur pour obtenir des informations sensibles, comme des noms de systèmes, de fichiers ou de bases de données, afin de préparer des attaques comme l'injection SQL.

### Application programming interface (API) attack

- **Une attaque par API** se produit lorsqu'un cybercriminel abuse d'un point de terminaison d'une API, qui relie un utilisateur à un système pour envoyer et recevoir des réponses.

### Replay attack

- **Une attaque par replay** survient lorsqu'un attaquant intercepte, modifie et renvoie une transmission de données valide pour tromper le récepteur et lui faire exécuter une action malveillante.

### Directory traversal attack

- **L'attaque de traversée de répertoire** survient lorsqu'un attaquant parvient à accéder à des fichiers en dehors du répertoire du site web sur le serveur. Cela peut lui permettre de télécharger des fichiers de configuration sensibles, exposer d'autres vulnérabilités ou prendre le contrôle du serveur.

### Resource exhaustion attacks

+ **Les attaques par épuisement de ressources** visent à planter, suspendre ou perturber un programme ou système ciblé. Plutôt que d'envahir la bande passante réseau comme une attaque DoS, elles épuisent les ressources matérielles du serveur cible.

## **Se défendre contre les attaques d'application**

- La première ligne de défense contre une attaque d'application est d'écrire un code solide.
- Une pratique de programmation prudente consiste à traiter et valider toutes les entrées extérieures à une fonction comme si elles étaient hostiles.
- Gardez tous vos logiciels, y compris les systèmes d'exploitation et les applications, à jour.
- Ne ignorez pas les invites de mise à jour.
- N'oubliez pas que tous les programmes ne se mettent pas à jour automatiquement.


------------

## **Attaques dans les mails**

### Spam

- Le **spam**, ou **courrier indésirable**, est un email non sollicité souvent utilisé pour de la publicité ou des arnaques. Il peut contenir des liens malveillants ou des demandes de renseignements personnels. Certains signes indiquent un spam : absence de ligne d'objet, fautes d'orthographe, demandes urgentes ou pièces jointes suspectes.

### Phishing

- Le **phishing** est une technique où un attaquant se fait passer pour une organisation légitime pour tromper l'utilisateur, lui faire installer un malware ou voler ses informations personnelles, comme des mots de passe ou des coordonnées bancaires.

### Spear Phishing

- Le **spear phishing** est une attaque ciblée où un cybercriminel utilise des informations personnelles pour envoyer un e-mail frauduleux et inciter la victime à cliquer sur un lien malveillant.

---------------

## **Vishing, Pharming and Whaling**

### Vishing

- Le **vishing**, ou **phishing vocal**, consiste à utiliser des appels téléphoniques ou des messages enregistrés pour inciter les victimes à divulguer des informations sensibles, comme leurs coordonnées bancaires. Les criminels peuvent usurper des numéros en utilisant la VoIP.

### Pharming

- Le **pharming** redirige les utilisateurs vers une fausse version d'un site officiel. Pensant être sur un site légitime, ils saisissent leurs identifiants sur le site frauduleux.

### Whaling

- Le **whaling** est un type de phishing visant des personnes influentes, comme des cadres supérieurs, des politiciens ou des célébrités.

------------------
## **Autres types d'attaques**


- **Attaques physiques** :  
    Actions visant à endommager ou voler du matériel. Exemples :
    
    - USB infectées par des malwares.
    - Câbles modifiés pour prendre le contrôle des appareils.
    - Clonage de cartes bancaires via des terminaux frauduleux.

- **Attaques sur l’intelligence artificielle** :  
    Exploitation de données falsifiées pour tromper les algorithmes. Exemple : induire en erreur des véhicules autonomes en manipulant les panneaux de signalisation.

- **Attaques sur la chaîne d'approvisionnement** :  
    Compromission de services ou composants tiers. Exemple : modifier les dates de fin de support d’un logiciel pour perturber une entreprise.

- **Attaques sur le cloud** :  
    Exploitation des données sensibles, applications ou infrastructures hébergées dans le cloud.

-----------
## **Perte de données**

- **E-mails et réseaux sociaux** : Les messages interceptés (e-mails ou messagerie instantanée) peuvent révéler des informations confidentielles si elles ne sont pas sécurisées.
    
- **Appareils non chiffrés** : Si un ordinateur portable volé contient des données sensibles et n'est pas chiffré, un voleur peut accéder à ces informations.
    
- **Stockage cloud** : Bien que le stockage dans le cloud présente des avantages, des données sensibles peuvent être perdues si la sécurité de l'accès au cloud est faible.
    
- **Médias amovibles** : Un transfert non autorisé de données vers une clé USB ou la perte d'une clé contenant des informations confidentielles constitue un risque majeur.
    
- **Copies papier** : Les données confidentielles doivent être correctement détruites, par exemple, en les broyant. Sinon, des informations sensibles pourraient être récupérées dans des rapports jetés.
    
- **Contrôle d'accès inadéquat** : Les mots de passe sont essentiels pour protéger les données. Des mots de passe volés ou faibles permettent un accès facile aux données sensibles.

----------

## **Menace, Vulnérabilité, Risque**

- **Menace (Threat)** : Danger potentiel pour un actif (données, réseau).

- **Vulnérabilité (Vulnerability)** : Faiblesse dans un système pouvant être exploitée par une menace.

- **Surface d'attaque (Attack Surface)** : Ensemble des vulnérabilités accessibles à un attaquant.

- **Exploitation (Exploit)** : Mécanisme permettant d'exploiter une vulnérabilité pour compromettre un actif.

- **Risque (Risk)** : Probabilité qu'une menace exploite une vulnérabilité et cause un dommage.


- **Acceptation du risque (Risk Acceptance)** : Le coût des options de gestion du risque dépasse celui du risque lui-même. Le risque est accepté et aucune action n'est entreprise.

- **Évitement du risque (Risk Avoidance)** : Cela consiste à éviter toute exposition au risque en éliminant l'activité ou le dispositif qui le présente. En éliminant l'activité, les bénéfices potentiels sont également perdus.

- **Réduction du risque (Risk Reduction)** : Réduire l'exposition au risque ou l'impact du risque en prenant des mesures pour le diminuer. C'est la stratégie de gestion des risques la plus couramment utilisée, nécessitant une évaluation soignée des coûts, de la stratégie de réduction et des bénéfices associés.

- **Transfert du risque (Risk Transfer)** : Une partie ou la totalité du risque est transférée à un tiers volontaire, comme une compagnie d'assurance.
-----------

## **Indicateurs de menace**

- Les **indicateurs de compromission (IOC)** sont des preuves qu'une attaque a eu lieu, comme des fichiers malveillants ou des adresses IP utilisées. Ils aident à identifier et à prévenir des attaques similaires.

- Les **indicateurs d'attaque (IOA)** se concentrent sur les stratégies des attaquants. Ils permettent de mettre en place une défense proactive pour contrer des attaques futures utilisant les mêmes méthodes.

Les gouvernements, comme la **CISA** aux États-Unis et l'**ENISA** en Europe, promeuvent la cybersécurité. La **CISA** utilise le système **AIS** pour partager des informations sur les menaces et organise des campagnes de sensibilisation comme le **Mois de la cybersécurité**.

----
## **IPv4**

![[Pasted image 20250121095845.png]]

- **Version** : 4 bits indiquant qu'il s'agit d'un paquet IPv4 (0100).

- **Internet Header Length (IHL)** : 4 bits pour la longueur de l'en-tête IP (minimum 20 octets).

- **Differentiated Services (DS)** : 8 bits pour la priorité du paquet, comprenant DSCP et ECN.

- **Total Length** : 2 octets spécifiant la taille totale du paquet (en-tête + données utilisateur).

- **Identification, Flag, Fragment Offset** : Utilisés pour fragmenter et réassembler les paquets si nécessaire.

- **Time-to-Live (TTL)** : 8 bits limitant la durée de vie du paquet, décrémenté par chaque routeur.

- **Protocol** : 8 bits indiquant le type de données du paquet (ex. ICMP, TCP, UDP).

- **Header Checksum** : Calculé pour vérifier les erreurs dans l'en-tête du paquet.

- **Source IPv4 Address** : 32 bits représentant l'adresse IPv4 source.

- **Destination IPv4 Address** : 32 bits représentant l'adresse IPv4 de destination.

- **Options and Padding** : Champ variable, complété par des zéros si nécessaire pour aligner à 32 bits.


## **IPv6**

![[Pasted image 20250121101856.png]]
- **Version** : 4 bits indiquant qu'il s'agit d'un paquet IPv6 (0110).

- **Traffic Class** : 8 bits, équivalent au champ DS d'IPv4, utilisé pour la gestion de la priorité du paquet.

- **Flow Label** : 20 bits suggérant que les paquets avec le même flow label sont traités de la même manière par les routeurs.

- **Payload Length** : 16 bits, indiquant la longueur de la portion de données (payload) du paquet IPv6.

- **Next Header** : 8 bits, équivalent au champ Protocole d'IPv4, indiquant le type de données transportées.

- **Hop Limit** : 8 bits, remplaçant le champ TTL d'IPv4, qui est décrémenté par chaque routeur. Si le compteur atteint 0, le paquet est rejeté et un message ICMPv6 est envoyé.

## **Vulnérabilités des IP**

- **Attaques ICMP** : Utilisation de paquets ICMP pour découvrir des sous-réseaux, générer des attaques par déni de service (DoS) ou modifier les tables de routage des hôtes.
- **Attaques par déni de service (DoS)** : Tentatives d'empêcher les utilisateurs légitimes d'accéder à des informations ou des services.
- **Attaques par déni de service distribué (DDoS)** : Attaque coordonnée simultanée à partir de plusieurs machines sources.
- **Attaques par usurpation d'adresse (Spoofing)** : Usurpation de l'adresse IP source pour réaliser un spoofing aveugle ou non-aveugle.
- **Attaque de l'homme du milieu (MiTM)** : L'attaquant se place entre la source et la destination pour surveiller, capturer ou manipuler la communication.
- **Prise de session (Session Hijacking)** : L'attaquant utilise un MiTM pour prendre le contrôle d'une session après avoir accédé au réseau physique.



## **Attaques ICMP**

- **ICMP echo request et echo reply** : Utilisés pour la vérification des hôtes et les attaques DoS.

- **ICMP unreachable** : Utilisés pour des attaques de reconnaissance et de balayage du réseau.

- **ICMP mask reply** : Utilisés pour cartographier un réseau IP interne.

- **ICMP redirects** : Utilisés pour détourner un hôte cible afin d'envoyer tout son trafic à un appareil compromis, créant ainsi une attaque MiTM.

- **ICMP router discovery** : Utilisés pour injecter de fausses entrées de route dans la table de routage d'un hôte cible.

## **Amplification and Reflection Attacks**

- **Amplification** : L'attaquant envoie des messages ICMP echo request à plusieurs hôtes en utilisant l'adresse IP de la victime comme source.
- **Reflection** : Ces hôtes répondent à l'adresse IP usurpée de la victime, la submergeant avec un grand nombre de réponses.

## **Address Spoofing Attacks**

- **IP Address Spoofing** :
    
    - Création de paquets avec une fausse adresse IP source pour masquer l'identité de l'expéditeur ou se faire passer pour un utilisateur légitime.
    - Souvent utilisé dans des attaques comme les attaques Smurf.
    - **Non-blind spoofing** : L'attaquant voit le trafic entre l'hôte et la cible. Utilisé pour analyser les réponses, prédire les numéros de séquence ou détourner des sessions autorisées.
    - **Blind spoofing** : L'attaquant ne voit pas le trafic entre l'hôte et la cible. Utilisé dans des attaques DoS.

- **MAC Address Spoofing** :
    
    - L'attaquant modifie l'adresse MAC de son appareil pour imiter une adresse connue sur le réseau interne.
    - Le commutateur met à jour sa table CAM avec le nouvel emplacement, redirigeant le trafic destiné à la cible vers l'attaquant.

- **Application/Service Spoofing** :
    
    - Un attaquant peut connecter un faux serveur DHCP pour créer une condition d'homme du milieu (MiTM).

-------

## **Vulnérabilités TCP et UDP**

### Bits de contrôle TCP

![[Pasted image 20250121141007.png]]
- **URG** : Champ pointeur urgent significatif.
- **ACK** : Champ d'accusé de réception significatif.
- **PSH** : Fonction Push.
- **RST** : Réinitialise la connexion.
- **SYN** : Synchronise les numéros de séquence.
- **FIN** : Fin de transmission de données.

### Services TCP

- **Livraison fiable** : Utilise des accusés de réception pour garantir la livraison (ex. HTTP, TLS, FTP).
- **Contrôle de flux** : Réduit le nombre d'accusés de réception en regroupant plusieurs segments.
- **Communication avec état** : Établit une connexion via une **poignée de main en trois étapes (3-way handshake)**.

### Attaques TCP

- **TCP SYN Flood** :
    
    - Exploite la poignée de main en trois étapes.
    - Envoie des paquets SYN avec des adresses IP usurpées.
    - Le serveur répond par SYN-ACK, mais ne reçoit jamais de réponse.
    - Résultat : Connexions TCP semi-ouvertes surchargent le serveur, bloquant les utilisateurs légitimes.

- **TCP Reset Attack** :
    
    - Interrompt une connexion TCP en envoyant un paquet contenant un bit RST.
    - Utilisé pour mettre fin brutalement à une session entre deux hôtes.

- **TCP Session Hijacking** :
    
    - L'attaquant prend le contrôle d'une session TCP existante.
    - Nécessite de prédire le numéro de séquence et de falsifier l'adresse IP d'un hôte authentifié.
    - Permet à l'attaquant d'envoyer des données, mais pas de recevoir.


### Services TCP

1. **Livraison fiable** :
    - Garantit la livraison des données grâce à des accusés de réception.
    - Réémet les données si un accusé de réception n'est pas reçu.
    - Exemples : HTTP, SSL/TLS, FTP, transferts de zones DNS.

1. **Contrôle de flux** :
    - Réduit le nombre d'accusés de réception en regroupant plusieurs segments en un seul accusé.

1. **Communication avec état** :
    - Utilise une **poignée de main en trois étapes (Three-Way Handshake)** :
        1. **Client** demande une session (SYN).
        2. **Serveur** répond en confirmant la demande (SYN-ACK).
        3. **Client** confirme l'établissement de la session (ACK).


### Attaques TCP


1. **Scan de ports** :
    
    - Les acteurs malveillants identifient les services offerts par une cible en scannant les ports TCP ou UDP.
    
2. **Attaque par inondation TCP SYN** :
    
    - Exploite la poignée de main TCP en trois étapes.
    - Envoie de nombreuses requêtes SYN avec des IP usurpées.
    - Le serveur répond avec des SYN-ACK, mais les réponses (ACK) ne sont jamais envoyées.
    - Résultat : le serveur est surchargé par des connexions TCP "semi-ouvertes", empêchant l'accès des utilisateurs légitimes.
    
3. **Attaque par réinitialisation TCP (RST)** :
    
    - Envoie des paquets TCP avec le drapeau RST pour forcer la fermeture immédiate de connexions TCP légitimes.
    
4. **Détournement de session TCP** :
    
    - Le pirate prend le contrôle d'une session TCP active entre deux hôtes.
    - Nécessite de prédire le numéro de séquence TCP et d'usurper une adresse IP.
    - Permet d'envoyer des données au nom de la victime, mais pas d'en recevoir.


### **UDP Segment Header and Operation**

- **Applications courantes** :
    
    - Utilisé par **DNS**, **DHCP**, **TFTP**, **NFS**, **SNMP** et pour des applications en temps réel comme le streaming multimédia ou la VoIP.
- **Caractéristiques principales** :
    
    - **Protocole sans connexion** : Moins de surcharge comparé à TCP.
    - Ne propose pas de fonctionnalités comme la retransmission, la numérotation des segments ou le contrôle de flux.
- **Structure du segment UDP** :
    
    - **Taille totale : 8 octets**, suivis des données de la couche application.
    - Champs :
        - **Source Port** : 16 bits
        - **Destination Port** : 16 bits
        - **Length** : 16 bits (longueur totale du segment UDP)
        - **Checksum** : 16 bits (vérification d’intégrité)
        - **Données de la couche application** : Taille variable.
- **Fiabilité** :
    
    - Bien que UDP soit considéré comme non fiable, cela signifie simplement que la fiabilité n’est pas gérée par le protocole lui-même. Si nécessaire, cette fonction est mise en œuvre à d'autres niveaux.
- **Avantage clé** :
    
    - La faible surcharge rend UDP idéal pour les transactions simples de requêtes/réponses (exemple : DHCP), où la retransmission peut être gérée par l'application en cas d'absence de réponse.


### **Attaques UDP**

UDP, sans chiffrement natif, expose les données à la modification et l'interception.

Les attaques UDP Flood permettent de surcharger les réseaux en envoyant massivement des paquets UDP, provoquant un déni de service (DoS).

---------------------------------

### **ARP Vulnerabilities**

Les **vulnérabilités ARP** permettent à un attaquant d'exploiter le protocole **ARP** en envoyant des réponses **ARP** falsifiées. Cela peut mener à un **empoisonnement ARP**, où l'attaquant associe sa propre adresse MAC à l'adresse IP du passerelle par défaut. Cela crée une attaque de **l'homme du milieu (MiTM)**, où l'attaquant intercepte et manipule le trafic entre les appareils du réseau et l'extérieur, sans que les victimes s'en aperçoivent.


### **Attaques DNS**

#### DNS cache poisoning attacks
Les attaquants envoient des informations falsifiées de ressources DNS à un résolveur DNS, redirigeant ainsi les utilisateurs vers des sites malveillants. Cela se produit lorsque le résolveur utilise un serveur DNS malveillant, influençant ainsi les résolutions DNS.

#### DNS amplification and reflection attacks
Les attaquants exploitent des serveurs DNS ouverts pour envoyer un volume élevé de requêtes vers une cible, masquant ainsi l'origine réelle de l'attaque. Le serveur DNS ouvert répond à n'importe quelle requête, augmentant ainsi l'ampleur de l'attaque.

#### DNS resource utilization attacks
Ces attaques de type DoS consomment les ressources d'un serveur DNS ouvert, entraînant une surcharge qui peut nécessiter un redémarrage ou une interruption des services du serveur DNS.



