Keskustelusovellus

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
- Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
- Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.

Käyttöohjeet:
Kloonaa repositorio ja luo .env-tiedosto samaan hakemistoon sisällöllä:
```
DATABASE_URL=<paikallinen-osoite>
SECRET_KEY=<avain>
```

Siirry hakemistoon, asenna virtuaaliympäristö venv ja muut tarvittavat asennukset:
```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ sudo service postgresql restart
(venv) $ pip install -r ./requirements.txt
(venv) $ psql < schema.sql
(venv) $ flask run
```