# **Challenge** 

## **Esercizio 1**

Script che date due stringe ed una cartella, verifica se il nome di ogni file presente all'interno della stessa contiene la prima stringa. Se lo contiene, rinomina il file sostituendo la prima stringa alla seconda.

Comando:
```
./exercise1.sh {FIRST_STRING} {SECOND_STRING} {DIR}
```

## **Esercizio 2**

Script Python che conta il numero di file script all'interno di una cartella (passata come parametro) suddividendoli in base all'interpete shebang.

Comando:
```
python3 exercise2.py --folder {folder}
```

## **Esercizio 3**

Script che permette di aggiungere un cronjob con un comando attraverso l'utilizzo di crontab. Il comando utilizza rsync per effettuare il backup di una cartella specifica (/home/user) e inviare lo stesso in ssh ad un server remoto.
In particolare: il backup viene effettuato ogni domenica alle 23:00 ed inviato a user@192.168.1.100

Comando:
```
./exercise3.sh
```

## **Esercizio 4** 

Progetto Ansible che effettua l'installazione ed il setup di Wordpress.

OS utilizzato: Fedora

## Albero dei file:
```
├── files
│   └── httpd.conf
├── inventory.txt
├── playbook.yml
├── roles
│   ├── apache
│   │   └── tasks
│   │       └── main.yml
│   ├── firewall
│   │   └── tasks
│   │       └── main.yml
│   ├── mariadb
│   │   └── tasks
│   │       └── main.yml
│   ├── php
│   │   └── tasks
│   │       └── main.yml
│   └── wordpress
│       └── tasks
│           └── main.yml
└── vars
    ├── default.yml
    └── secrets.yml
```

### Descrizione del contenuto

| File             		| Descrizione 							|
| :---------------------------: | :-----------------------------------------------------------: |
| inventory.txt			| Informazioni del targetNode necessarie per la connessione ssh |
| files/httpd.conf 		| Configurazione virtual host Apache				|
| playbook.yml			| File principale che include ruoli e variabili da creare 	|
| apache/tasks/main.yml 	| Installazione e configurazione di Apache nel TargetNode	|
| firewall/tasks/main.yml 	| Configurazione Firewall e disabilitazione SELinux		|
| php/tasks/main.yml 		| Installazione e configurazione di Php-7.4 nel TargetNode	|
| mariadb/tasks/main.yml 	| Installazione e configurazione di MariaDB nel TargetNode	|
| wordpress/tasks/main.yml 	| Installazione e configurazione di Wordpress nel TargetNode	|
| vars/default.yml		| variabili necessarie per le diverse installazioni		|
| vars/secrets.yml		| variabili con valori sensibili criptati con ansible-vault (password, nome-utente etc)	|



### comando

```
ansible-playbook playbook.yml -i inventory.txt --ask-vault-pass -e "ansible_sudo_pass={password}"

```






