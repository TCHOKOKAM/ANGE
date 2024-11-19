import sqlite3 
print(sqlite3.sqlite_version)
connexion=sqlite3.connect("TP3.db")

curseur=connexion.cursor()
curseur.execute('''
create table  if not exists utilisateur(
                id integer primary key autoincrement,
                nom text not null,
                age integer not null,
                email text not null unique
                )''')
print("table utilisateur creer avec succes")
nom="ange"
age=12
email="chjfkddj"
curseur.execute('''
insert into utilisateur(nom,age,email)
values (?,?,?)''' ,(nom, age,email))

print("donnee insere avec succes")

curseur.execute('''
update utilisateur
                set email='hkjkkfj'
                where id = 1''')
#print("donnee mise a jour avec succes")



curseur.execute('select*from utilisateur')
resultat=curseur.fetchall()
#print(resultat)

for ligne in resultat:
    print(ligne)
connexion.commit()



print("base de donnee cree")
connexion.close()