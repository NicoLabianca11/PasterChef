## **PasterChef**

![Logo PasterChef](images/pasticccere.png)

## 🍰 Cos'è PasterChef?
PasterChef è una **Web App** innovativa che trasforma l'arte della pasticceria in un gioco. L'obiettivo non è solo fornire ricette, ma renderti un vero Maestro Pasticcere attraverso un percorso di apprendimento basato sulla **gamification**. Impara le tecniche, conosci gli ingredienti e mettiti alla prova divertendoti.

## 🏆 Perché usare PasterChef
Abbiamo rivoluzionato il modo di imparare a cucinare dolci. Ecco i nostri punti di forza:

* **🎮 50 Livelli Interattivi:** Un percorso strutturato che ti guida dalle basi fino alle tecniche più complesse.
* **🧩 Coinvolgimento Totale:** Ogni livello include mini-giochi e quiz per testare le tue abilità prima di passare ai fornelli.
* **🌍 Classifiche Globali:** Scala la vetta! Confronta i tuoi punteggi con aspiranti pasticceri di tutto il mondo e conquista il titolo di Chef Supremo.

---

## ⚙️ Requisiti e Installazione
### ⚠️ Prerequisiti Software

* **Git:** Per scaricare il progetto.
* **Docker Desktop:** (Consigliato) Per avviare tutto senza configurazioni manuali.
* **Python 3.10+:** (Solo se non usi Docker) Per eseguire il backend manualmente.
* **Web Browser:** Qualsiasi browser moderno (Chrome, Firefox, Safari) per giocare.

---

### 📥 Come iniziare
Apri il terminale (o Prompt dei Comandi) e scarica la repository:

```bash
git clone https://github.com/Nicola-perhub/PasterChef.git
```
Una volta scaricato, entra nella cartella del progetto:
```bash
cd .\PasterChef\.git\
```
Infine questo comando scaricherà le dipendenze, compilerà il progetto e avvierà il server(c'è bisogno che docker sia già in esecuzione):
```bash
docker-compose up --build
```

---

## 🆘 Problemi all'avvio? (Troubleshooting)

Se l'applicazione non parte o Docker ti dà errori sul file `users.json`, ecco come risolvere in un attimo.

### 🟢 Soluzione Rapida (Consigliata)
**Fai "Tabula Rasa":**
1. Vai nella cartella del progetto.
2. **Cancella** manualmente il file `users.json`.
3. Riavvia l'app.

*Perché funziona?* Eliminando il file "bloccato", Docker ne creerà uno nuovo e pulito automaticamente all'avvio.

---

### 🟠 Soluzione Avanzata (Per mantenere i dati)
Se non vuoi cancellare il file perché contiene dati importanti, devi sbloccare i permessi:

* **Su Windows:** Chiudi tutto e riapri Docker/Terminale facendo **Tasto Destro → Esegui come amministratore**.
* **Su Mac/Linux:** Apri il terminale nella cartella ed esegui questo comando per sbloccare il file:

```bash
sudo chmod 777 users.json
```

---


## 🔮 Sviluppi Futuri (Roadmap)
Il viaggio di PasterChef è appena iniziato. Ecco le funzionalità pianificate per le prossime versioni:

* **⚔️ Modalità Duello (PvP):** La sfida definitiva 1vs1! Gareggia in tempo reale contro altri utenti per vedere chi decora la torta nel minor tempo possibile.
* **🛍️ Negozio Virtuale:** Un sistema di reward che permette di utilizzare i punti guadagnati nei livelli per personalizzare l'avatar del proprio chef o acquistare utensili da cucina virtuali.
* **🍰 Espansione Contenuti:** Aggiunta di nuove "ere" e moduli didattici specifici, come la *Pasticceria Francese* e l'arte della *Cioccolateria*.
* **🤝 Gilde di Pasticceri:** Funzionalità social che permetterà di creare squadre (Gilde) per collaborare e partecipare a sfide di gruppo contro altre pasticcerie virtuali.

---


## 📘 Documentazione & Demo
Vuoi scoprire tutti i dettagli del progetto e vedere l'app in azione?
Scarica la presentazione qui sotto per approfondire l'architettura e guardare la **demo operativa**.

[📥 Scarica la presentazione completa (.pptx)](ProgettoGamification.pptx)
