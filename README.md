Kurssimateriaalissa ehdotettu keskusteluketju- ja viestintäsovellus.
Sovelluksen halutut ominaisuudet:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
- Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
- Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
- Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. Käyttäjä voi myös poistaa ketjun tai viestin.
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
- Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
- Ylläpitäjä voi luoda salaisen alueen ja määrittää, keillä käyttäjillä on pääsy alueelle.


Eteneminen 7.4.
- Kolme valittua aihetta näkyvät etusivulla linkkeinä ja jokaiseen aiheeseen pystyy lähettämään viestejä.
- Viestiä lähettäessä valitaan aihe, jolloin viesti näkyy vain tämän aiheen sivulla.
- Itselläni ainakin vaati "sudo service postgresql restart" -komentoa jostakin syystä, kun aloitin työskentelyn uudelleen.
- Olen jo laatinut pienehkön schema-tiedoston, johon on tarkoitus lisätä ajan myötä.
- Tajusin vasta commitin tehtyäni, etten laatinut hyviä kuvauksia. Pahoittelut tästä. Pyrin seuraavalla palautuksella parempaan.

Eteneminen 21.4.
- Viestien sijaan näkyy ketjut mutta en saanut vielä linkattua ketjujen sisälle. 
- Tarvittavia tiedostoja on lisätty, kuten laajempi schema.sql sekä requirements.txt.
- Tauluihin lisätty käyttäjät ja ketjut, joita pitää vielä parantaa huomattavasti.
- Uusia templaatteja, kuten login ja register, vaikkakin käyttäjäsessiot eivät ole vielä kunnossa.
- En ole välttämättä edennyt yhtä pitkälle kuin pitäisi tässä vaiheessa kurssia. Sovelluksesta puuttuu vielä monia olennaisia toimintoja.

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