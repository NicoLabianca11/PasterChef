from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import json
import os
import uuid
from datetime import datetime
from quiz_data import get_quiz, calculate_score

# ==================== STORAGE CONFIGURATION ====================
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')

def ensure_data_dir():
    """Assicura che la directory dati e il file utenti esistano"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump({"users": []}, f)

ensure_data_dir()

app = Flask(__name__)
app.secret_key = 'pasterchef_secret_key_2024'

# ==================== DATABASE STRUCTURE ====================

BADGES = {
    "apprentice": {"name": "Apprendista", "min_level": 1, "max_level": 10, "icon": "🌟"},
    "pastry_cook": {"name": "Pastry Cook", "min_level": 11, "max_level": 20, "icon": "⭐"},
    "sous_chef": {"name": "Sous Chef", "min_level": 21, "max_level": 30, "icon": "🌠"},
    "chef_patissier": {"name": "Chef Pâtissier", "min_level": 31, "max_level": 40, "icon": "💫"},
    "maestro": {"name": "Maestro Stellato", "min_level": 41, "max_level": 50, "icon": "✨"}
}

RECIPES = [
    # LIVELLO 1-10: BASE
    {"id": 1, "name": "Biscotti Base", "difficulty": 1, "xp": 100, "ingredients_count": 5,
     "ingredients": ["300g Farina 00", "150g Zucchero", "100g Burro", "1 Uovo", "Vanillina"],
     "steps": ["Mescola farina e zucchero in una ciotola.", "Aggiungi il burro freddo a cubetti.", "Incorpora l'uovo e la vanillina.", "Impasta fino ad ottenere un composto omogeneo.", "Stendi e taglia i biscotti.", "Inforna a 180°C per 12-15 minuti."],
     "images": ["https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=600", "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=600"]},
    
    {"id": 2, "name": "Muffin Magici", "difficulty": 1, "xp": 120, "ingredients_count": 7,
     "ingredients": ["250g Farina", "150g Zucchero", "2 Uova", "100ml Latte", "80g Burro", "Lievito", "Gocce cioccolato"],
     "steps": ["Preriscalda il forno a 180°C.", "Mescola gli ingredienti secchi.", "Unisci uova, latte e burro fuso.", "Combina i due composti.", "Aggiungi le gocce di cioccolato.", "Versa negli stampini.", "Cuoci per 20-25 minuti."],
     "images": ["https://images.unsplash.com/photo-1607958996333-41aef7caefaa?w=600", "https://images.unsplash.com/photo-1558303926-f5d503126de7?w=600"]},
    
    {"id": 3, "name": "Crostata Croccante", "difficulty": 1, "xp": 140, "ingredients_count": 6,
     "ingredients": ["300g Farina", "150g Burro", "100g Zucchero", "2 Tuorli", "Marmellata", "Sale"],
     "steps": ["Prepara la frolla sabbiando burro e farina.", "Aggiungi zucchero e tuorli.", "Riposa in frigo 30 minuti.", "Stendi e fodera la teglia.", "Aggiungi la marmellata.", "Decora e cuoci a 180°C per 35 minuti."],
     "images": ["https://images.unsplash.com/photo-1464305795204-6f5bbfc7fb81?w=600", "https://images.unsplash.com/photo-1519915028121-7d3463d20b13?w=600"]},
    
    {"id": 4, "name": "Tiramisù Tradizionale", "difficulty": 2, "xp": 160, "ingredients_count": 6,
     "ingredients": ["500g Mascarpone", "4 Uova", "100g Zucchero", "Caffè", "Savoiardi", "Cacao"],
     "steps": ["Prepara il caffè e lascia raffreddare.", "Monta tuorli e zucchero.", "Incorpora il mascarpone.", "Monta gli albumi a neve.", "Alterna strati di savoiardi e crema.", "Riposa in frigo 4 ore."],
     "images": ["https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=600", "https://images.unsplash.com/photo-1586040140378-b5634cb4c8fc?w=600"]},
    
    {"id": 5, "name": "Profiteroles Pazzi", "difficulty": 2, "xp": 180, "ingredients_count": 8,
     "ingredients": ["125g Farina", "100g Burro", "4 Uova", "250ml Acqua", "Panna", "Cioccolato", "Zucchero", "Sale"],
     "steps": ["Prepara la pasta choux.", "Forma i bignè.", "Cuoci a 200°C per 25 minuti.", "Prepara la crema.", "Farcisci i bignè.", "Ricopri con cioccolato fuso."],
     "images": ["https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=600", "https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc?w=600"]},
    
    {"id": 6, "name": "Cannoli Creativi", "difficulty": 2, "xp": 200, "ingredients_count": 9,
     "ingredients": ["300g Farina", "30g Strutto", "Marsala", "Ricotta", "Zucchero a velo", "Pistacchi", "Cioccolato", "Cannella", "Uovo"],
     "steps": ["Prepara l'impasto con farina, strutto e marsala.", "Riposa 30 minuti.", "Taglia e arrotola sui tubi.", "Friggi in olio caldo.", "Prepara la crema di ricotta.", "Farcisci e decora."],
     "images": ["https://images.unsplash.com/photo-1551024506-0bccd828d307?w=600", "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600"]},
    
    {"id": 7, "name": "Babà al Rum", "difficulty": 2, "xp": 220, "ingredients_count": 7,
     "ingredients": ["250g Farina", "15g Lievito", "4 Uova", "100g Burro", "Rum", "Zucchero", "Acqua"],
     "steps": ["Prepara l'impasto lievitato.", "Lascia lievitare 2 ore.", "Cuoci a 180°C.", "Prepara la bagna al rum.", "Immergi i babà.", "Servi con panna."],
     "images": ["https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=600", "https://images.unsplash.com/photo-1464305795204-6f5bbfc7fb81?w=600"]},
    
    {"id": 8, "name": "Torta Sacher", "difficulty": 3, "xp": 250, "ingredients_count": 8,
     "ingredients": ["200g Cioccolato", "150g Burro", "150g Zucchero", "6 Uova", "100g Farina", "Marmellata albicocche", "Panna", "Vaniglia"],
     "steps": ["Fondi cioccolato e burro.", "Monta tuorli e zucchero.", "Incorpora il cioccolato.", "Aggiungi farina e albumi montati.", "Cuoci a 170°C per 50 minuti.", "Farcisci e glassa."],
     "images": ["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600", "https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=600"]},
    
    {"id": 9, "name": "Macaron Mignon", "difficulty": 3, "xp": 280, "ingredients_count": 6,
     "ingredients": ["125g Farina mandorle", "200g Zucchero a velo", "3 Albumi", "30g Zucchero", "Colorante", "Ganache"],
     "steps": ["Setaccia mandorle e zucchero a velo.", "Monta gli albumi con lo zucchero.", "Macronage delicato.", "Forma i dischetti.", "Cuoci a 150°C per 14 minuti.", "Farcisci con ganache."],
     "images": ["https://images.unsplash.com/photo-1569864358642-9d1684040f43?w=600", "https://images.unsplash.com/photo-1558326567-98ae2405596b?w=600"]},
    
    {"id": 10, "name": "Torta della Nonna", "difficulty": 2, "xp": 300, "ingredients_count": 9,
     "ingredients": ["Pasta frolla", "500ml Latte", "4 Tuorli", "120g Zucchero", "40g Amido", "Pinoli", "Limone", "Vaniglia", "Zucchero a velo"],
     "steps": ["Prepara la pasta frolla.", "Cuoci la crema pasticcera.", "Fodera la teglia.", "Versa la crema.", "Copri con altra frolla.", "Aggiungi pinoli e zucchero a velo.", "Cuoci a 180°C per 40 minuti."],
     "images": ["https://images.unsplash.com/photo-1519915028121-7d3463d20b13?w=600", "https://images.unsplash.com/photo-1464305795204-6f5bbfc7fb81?w=600"]},
    
    # LIVELLO 11-20: INTERMEDIO
    {"id": 11, "name": "Millefoglie Classica", "difficulty": 3, "xp": 320, "ingredients_count": 7,
     "ingredients": ["Pasta sfoglia", "Crema pasticcera", "Panna", "Zucchero a velo", "Vaniglia", "Fragole", "Cioccolato"],
     "steps": ["Cuoci la sfoglia a 200°C.", "Prepara la crema.", "Monta la panna.", "Alterna strati.", "Decora con fragole.", "Spolvera con zucchero a velo."],
     "images": ["https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600", "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600"]},
    
    {"id": 12, "name": "Cheesecake New York", "difficulty": 2, "xp": 340, "ingredients_count": 8,
     "ingredients": ["300g Biscotti digestive", "100g Burro", "600g Philadelphia", "200g Zucchero", "3 Uova", "Panna", "Vaniglia", "Limone"],
     "steps": ["Trita i biscotti.", "Mescola con burro fuso.", "Pressa nella teglia.", "Mescola formaggio e zucchero.", "Aggiungi uova e panna.", "Cuoci a bagnomaria.", "Raffredda lentamente."],
     "images": ["https://images.unsplash.com/photo-1524351199678-941a58a3df50?w=600", "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=600"]},
    
    {"id": 13, "name": "Éclair al Cioccolato", "difficulty": 3, "xp": 360, "ingredients_count": 9,
     "ingredients": ["Pasta choux", "Crema pasticcera", "Cioccolato fondente", "Panna", "Burro", "Zucchero", "Uova", "Farina", "Sale"],
     "steps": ["Prepara la pasta choux.", "Forma gli éclair.", "Cuoci a 200°C.", "Prepara la crema cioccolato.", "Farcisci gli éclair.", "Glassa con cioccolato lucido."],
     "images": ["https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc?w=600", "https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=600"]},
    
    {"id": 14, "name": "Panna Cotta Frutti Bosco", "difficulty": 1, "xp": 380, "ingredients_count": 6,
     "ingredients": ["500ml Panna", "80g Zucchero", "Gelatina", "Vaniglia", "Frutti di bosco", "Zucchero per coulis"],
     "steps": ["Scalda panna e zucchero.", "Aggiungi gelatina ammollata.", "Versa negli stampini.", "Riposa in frigo 4 ore.", "Prepara il coulis.", "Sforma e servi."],
     "images": ["https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600", "https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc?w=600"]},
    
    {"id": 15, "name": "Paris-Brest", "difficulty": 4, "xp": 400, "ingredients_count": 10,
     "ingredients": ["Pasta choux", "Crema mousseline", "Pralinato nocciole", "Burro", "Uova", "Farina", "Mandorle", "Zucchero a velo", "Panna", "Zucchero"],
     "steps": ["Forma un anello di choux.", "Cospargi di mandorle.", "Cuoci a 190°C.", "Prepara crema mousseline.", "Aggiungi pralinato.", "Farcisci generosamente.", "Spolvera con zucchero."],
     "images": ["https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=600", "https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc?w=600"]},
    
    {"id": 16, "name": "Torta Caprese", "difficulty": 2, "xp": 420, "ingredients_count": 5,
     "ingredients": ["250g Cioccolato", "250g Burro", "250g Zucchero", "5 Uova", "250g Mandorle"],
     "steps": ["Fondi cioccolato e burro.", "Monta uova e zucchero.", "Incorpora il cioccolato.", "Aggiungi le mandorle.", "Cuoci a 160°C per 45 minuti.", "Lascia raffreddare."],
     "images": ["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600", "https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=600"]},
    
    {"id": 17, "name": "Sfogliatella Riccia", "difficulty": 4, "xp": 450, "ingredients_count": 11,
     "ingredients": ["500g Farina", "200g Strutto", "Semola", "Ricotta", "Zucchero", "Canditi", "Cannella", "Vaniglia", "Uova", "Sale", "Acqua"],
     "steps": ["Prepara la pasta.", "Stendi sottilissima.", "Spalma lo strutto.", "Arrotola strettamente.", "Riposa in frigo.", "Prepara il ripieno.", "Forma le sfogliatelle.", "Friggi o cuoci al forno."],
     "images": ["https://images.unsplash.com/photo-1551024506-0bccd828d307?w=600", "https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=600"]},
    
    {"id": 18, "name": "Crème Brûlée", "difficulty": 2, "xp": 470, "ingredients_count": 5,
     "ingredients": ["500ml Panna", "5 Tuorli", "100g Zucchero", "Vaniglia", "Zucchero di canna"],
     "steps": ["Scalda panna e vaniglia.", "Monta tuorli e zucchero.", "Unisci i composti.", "Cuoci a bagnomaria 160°C.", "Raffredda in frigo.", "Caramella lo zucchero."],
     "images": ["https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc?w=600", "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600"]},
    
    {"id": 19, "name": "Torta Mimosa", "difficulty": 3, "xp": 500, "ingredients_count": 10,
     "ingredients": ["Pan di spagna", "Crema pasticcera", "Panna", "Ananas", "Zucchero", "Uova", "Farina", "Limone", "Vaniglia", "Bagna"],
     "steps": ["Prepara il pan di spagna.", "Cuoci la crema.", "Monta la panna.", "Taglia il pan di spagna.", "Alterna strati.", "Ricopri di cubetti.", "Decora a mimosa."],
     "images": ["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600", "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600"]},
    
    {"id": 20, "name": "Cassata Siciliana", "difficulty": 4, "xp": 550, "ingredients_count": 12,
     "ingredients": ["Pan di spagna", "Ricotta", "Zucchero", "Gocce cioccolato", "Canditi", "Pistacchi", "Pasta reale", "Glassa", "Ciliegine", "Scorza arancia", "Liquore", "Vaniglia"],
     "steps": ["Prepara la crema di ricotta.", "Fodera lo stampo.", "Alterna strati.", "Riposa in frigo.", "Prepara la pasta reale.", "Ricopri la cassata.", "Glassa e decora."],
     "images": ["https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600", "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600"]},
    
    # LIVELLO 21-30: AVANZATO
    {"id": 21, "name": "Saint-Honoré", "difficulty": 5, "xp": 600, "ingredients_count": 12,
     "ingredients": ["Pasta sfoglia", "Pasta choux", "Crema chiboust", "Caramello", "Panna", "Uova", "Zucchero", "Farina", "Burro", "Vaniglia", "Gelatina", "Latte"],
     "steps": ["Cuoci base sfoglia.", "Prepara i bignè.", "Cuoci la crema chiboust.", "Monta la meringa.", "Incorpora alla crema.", "Glassa i bignè.", "Monta la struttura."],
     "images": ["https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=600", "https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc?w=600"]},
    
    {"id": 22, "name": "Opera Cake", "difficulty": 5, "xp": 650, "ingredients_count": 14,
     "ingredients": ["Biscuit joconde", "Ganache cioccolato", "Crema al burro caffè", "Glassa cioccolato", "Mandorle", "Uova", "Zucchero", "Farina", "Burro", "Caffè", "Cioccolato", "Panna", "Sciroppo", "Oro alimentare"],
     "steps": ["Prepara il biscuit.", "Cuoci la ganache.", "Prepara crema al caffè.", "Bagna gli strati.", "Alterna crema e ganache.", "Glassa con cioccolato.", "Decora con oro."],
     "images": ["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600", "https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=600"]},
    
    {"id": 23, "name": "Tarte Tatin", "difficulty": 3, "xp": 580, "ingredients_count": 6,
     "ingredients": ["Pasta sfoglia", "1kg Mele", "150g Zucchero", "80g Burro", "Cannella", "Vaniglia"],
     "steps": ["Prepara il caramello.", "Disponi le mele.", "Cuoci sul fuoco.", "Copri con sfoglia.", "Inforna a 200°C.", "Capovolgi e servi."],
     "images": ["https://images.unsplash.com/photo-1519915028121-7d3463d20b13?w=600", "https://images.unsplash.com/photo-1464305795204-6f5bbfc7fb81?w=600"]},
    
    {"id": 24, "name": "Charlotte Royale", "difficulty": 4, "xp": 620, "ingredients_count": 10,
     "ingredients": ["Biscuit roulé", "Mousse frutti bosco", "Gelatina", "Panna", "Zucchero", "Uova", "Farina", "Frutti di bosco", "Marmellata", "Bagna"],
     "steps": ["Prepara il biscuit.", "Spalma la marmellata.", "Arrotola e affetta.", "Fodera lo stampo.", "Prepara la mousse.", "Versa e refrigera.", "Sforma e decora."],
     "images": ["https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600", "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600"]},
    
    {"id": 25, "name": "Croquembouche", "difficulty": 5, "xp": 700, "ingredients_count": 11,
     "ingredients": ["Pasta choux", "Crema pasticcera", "Caramello", "Zucchero filato", "Uova", "Farina", "Burro", "Latte", "Vaniglia", "Sale", "Mandorle"],
     "steps": ["Prepara i bignè.", "Farcisci con crema.", "Prepara il caramello.", "Costruisci la piramide.", "Decora con caramello.", "Aggiungi zucchero filato."],
     "images": ["https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=600", "https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc?w=600"]},
    
    {"id": 26, "name": "Torta Setteveli", "difficulty": 5, "xp": 750, "ingredients_count": 15,
     "ingredients": ["Dacquoise nocciole", "Mousse cioccolato", "Croccante", "Crema gianduia", "Glassa specchio", "Cioccolato", "Panna", "Nocciole", "Uova", "Zucchero", "Burro", "Gelatina", "Pralinato", "Glucosio", "Cacao"],
     "steps": ["Prepara la dacquoise.", "Cuoci il croccante.", "Prepara la mousse.", "Monta la crema gianduia.", "Assembla gli strati.", "Refrigera bene.", "Glassa a specchio."],
     "images": ["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600", "https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=600"]},
    
    {"id": 27, "name": "Fraisier", "difficulty": 4, "xp": 680, "ingredients_count": 11,
     "ingredients": ["Génoise", "Crema mousseline", "Fragole", "Pasta di mandorle", "Burro", "Uova", "Zucchero", "Farina", "Latte", "Vaniglia", "Bagna"],
     "steps": ["Prepara la génoise.", "Cuoci la crema.", "Emulsiona col burro.", "Fodera con fragole.", "Alterna strati.", "Copri con mandorle.", "Decora con fragole."],
     "images": ["https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600", "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600"]},
    
    {"id": 28, "name": "Torta Foresta Nera", "difficulty": 4, "xp": 700, "ingredients_count": 10,
     "ingredients": ["Pan di spagna cacao", "Ciliegie", "Kirsch", "Panna", "Cioccolato", "Uova", "Zucchero", "Farina", "Cacao", "Scaglie cioccolato"],
     "steps": ["Prepara il pandispagna.", "Scola le ciliegie.", "Prepara la bagna al kirsch.", "Monta la panna.", "Alterna strati.", "Decora con scaglie.", "Aggiungi le ciliegie."],
     "images": ["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600", "https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=600"]},
    
    {"id": 29, "name": "Mousse al Cioccolato", "difficulty": 3, "xp": 550, "ingredients_count": 5,
     "ingredients": ["300g Cioccolato fondente", "6 Uova", "50g Zucchero", "Panna", "Caffè"],
     "steps": ["Fondi il cioccolato.", "Separa le uova.", "Monta tuorli e zucchero.", "Monta gli albumi.", "Incorpora delicatamente.", "Refrigera 4 ore."],
     "images": ["https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=600", "https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc?w=600"]},
    
    {"id": 30, "name": "Zuppa Inglese", "difficulty": 3, "xp": 600, "ingredients_count": 9,
     "ingredients": ["Pan di spagna", "Crema pasticcera", "Crema cioccolato", "Alchermes", "Rum", "Uova", "Zucchero", "Farina", "Latte"],
     "steps": ["Prepara il pan di spagna.", "Cuoci le due creme.", "Taglia il pan di spagna.", "Bagna con i liquori.", "Alterna strati.", "Decora con panna.", "Refrigera."],
     "images": ["https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600", "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600"]},
    
    # LIVELLO 31-40: ESPERTO
    {"id": 31, "name": "Torta Dobos", "difficulty": 5, "xp": 800, "ingredients_count": 10,
     "ingredients": ["6 strati biscotto", "Crema cioccolato", "Caramello", "Uova", "Zucchero", "Farina", "Burro", "Cioccolato", "Vaniglia", "Nocciole"],
     "steps": ["Prepara i 6 strati.", "Cuoci singolarmente.", "Prepara crema cioccolato.", "Alterna strati e crema.", "Prepara il caramello.", "Glassa lo strato finale.", "Taglia prima che indurisca."],
     "images": ["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600", "https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=600"]},
    
    {"id": 32, "name": "Torta Margherita Farcita", "difficulty": 3, "xp": 650, "ingredients_count": 8,
     "ingredients": ["6 Uova", "200g Zucchero", "200g Fecola", "Crema", "Fragole", "Panna", "Vaniglia", "Limone"],
     "steps": ["Monta uova e zucchero.", "Incorpora la fecola.", "Cuoci a 170°C.", "Lascia raffreddare.", "Farcisci con crema.", "Decora con fragole."],
     "images": ["https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600", "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600"]},
    
    {"id": 33, "name": "Pastiera Napoletana", "difficulty": 4, "xp": 750, "ingredients_count": 12,
     "ingredients": ["Pasta frolla", "Grano cotto", "Ricotta", "Zucchero", "Uova", "Canditi", "Acqua di fiori", "Cannella", "Vaniglia", "Latte", "Burro", "Scorza arancia"],
     "steps": ["Cuoci il grano.", "Prepara la frolla.", "Mescola ricotta e zucchero.", "Aggiungi uova e aromi.", "Incorpora il grano.", "Fodera e versa.", "Cuoci a 180°C."],
     "images": ["https://images.unsplash.com/photo-1519915028121-7d3463d20b13?w=600", "https://images.unsplash.com/photo-1464305795204-6f5bbfc7fb81?w=600"]},
    
    {"id": 34, "name": "Bûche de Noël", "difficulty": 4, "xp": 780, "ingredients_count": 11,
     "ingredients": ["Biscuit roulé", "Ganache", "Crema al burro", "Cioccolato", "Panna", "Uova", "Zucchero", "Farina", "Cacao", "Meringhe", "Frutti rossi"],
     "steps": ["Prepara il biscuit.", "Spalma la crema.", "Arrotola stretto.", "Prepara la ganache.", "Ricopri il tronco.", "Decora con forchetta.", "Aggiungi meringhe."],
     "images": ["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600", "https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=600"]},
    
    {"id": 35, "name": "Tarte au Citron", "difficulty": 3, "xp": 700, "ingredients_count": 9,
     "ingredients": ["Pasta frolla", "Limoni", "Uova", "Zucchero", "Burro", "Panna", "Amido", "Meringa", "Vaniglia"],
     "steps": ["Cuoci la frolla in bianco.", "Prepara la crema limone.", "Versa nella base.", "Prepara la meringa.", "Decora con sac à poche.", "Brucia con cannello."],
     "images": ["https://images.unsplash.com/photo-1519915028121-7d3463d20b13?w=600", "https://images.unsplash.com/photo-1464305795204-6f5bbfc7fb81?w=600"]},
    
    {"id": 36, "name": "Entremets Exotic", "difficulty": 5, "xp": 850, "ingredients_count": 14,
     "ingredients": ["Biscotto cocco", "Mousse mango", "Inserto passion fruit", "Glassa specchio", "Gelatina", "Panna", "Zucchero", "Cocco rapé", "Uova", "Burro", "Mango", "Passion fruit", "Glucosio", "Bianco cioccolato"],
     "steps": ["Prepara il biscotto.", "Cuoci l'inserto.", "Monta la mousse.", "Assembla in cerchio.", "Congela completamente.", "Prepara glassa.", "Glassa e decora."],
     "images": ["https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600", "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600"]},
    
    {"id": 37, "name": "Croissant", "difficulty": 4, "xp": 800, "ingredients_count": 8,
     "ingredients": ["500g Farina", "10g Sale", "80g Zucchero", "20g Lievito", "300ml Latte", "280g Burro", "1 Uovo", "Miele"],
     "steps": ["Prepara l'impasto base.", "Riposa in frigo.", "Incorpora il burro.", "Piega 3 volte.", "Riposa tra le pieghe.", "Taglia e arrotola.", "Lievita e cuoci."],
     "images": ["https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=600", "https://images.unsplash.com/photo-1530610476181-d83430b64dcd?w=600"]},
    
    {"id": 38, "name": "Torta Red Velvet", "difficulty": 3, "xp": 720, "ingredients_count": 11,
     "ingredients": ["Farina", "Cacao", "Colorante rosso", "Buttermilk", "Uova", "Zucchero", "Olio", "Aceto", "Bicarbonato", "Vaniglia", "Frosting"],
     "steps": ["Mescola ingredienti secchi.", "Combina i liquidi.", "Unisci i composti.", "Cuoci in 2 teglie.", "Prepara il frosting.", "Assembla gli strati.", "Decora."],
     "images": ["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600", "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600"]},
    
    {"id": 39, "name": "Meringata", "difficulty": 3, "xp": 680, "ingredients_count": 6,
     "ingredients": ["6 Albumi", "350g Zucchero", "Panna", "Frutti di bosco", "Vaniglia", "Limone"],
     "steps": ["Monta gli albumi.", "Aggiungi zucchero.", "Forma i dischi.", "Cuoci a 100°C.", "Monta la panna.", "Assembla e decora."],
     "images": ["https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600", "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600"]},
    
    {"id": 40, "name": "Torta Tre Latti", "difficulty": 3, "xp": 750, "ingredients_count": 10,
     "ingredients": ["Pan di spagna", "Latte condensato", "Latte evaporato", "Panna", "Uova", "Zucchero", "Farina", "Vaniglia", "Cannella", "Caramello"],
     "steps": ["Prepara il pan di spagna.", "Mescola i tre latti.", "Buca la torta.", "Versa i latti.", "Lascia assorbire.", "Copri con panna.", "Decora con caramello."],
     "images": ["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600", "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600"]},
    
    # LIVELLO 41-50: MAESTRO
    {"id": 41, "name": "Wedding Cake 3 Piani", "difficulty": 5, "xp": 900, "ingredients_count": 15,
     "ingredients": ["3 torte diverse", "Ganache", "Fondant", "Pasta di zucchero", "Fiori", "Coloranti", "Crema burro", "Supporti", "Pirottini", "Perle zucchero", "Nastri", "Glassa reale", "Alcol alimentare", "Oro", "Argento"],
     "steps": ["Prepara le 3 basi.", "Livella le torte.", "Applica crumb coat.", "Ricopri di fondant.", "Monta i piani.", "Crea le decorazioni.", "Assembla finale."],
     "images": ["https://images.unsplash.com/photo-1535254973040-607b474cb50d?w=600", "https://images.unsplash.com/photo-1464349153735-7db50ed83c84?w=600"]},
    
    {"id": 42, "name": "Pièce Montée", "difficulty": 5, "xp": 950, "ingredients_count": 13,
     "ingredients": ["Pasta choux", "Crema", "Caramello", "Nougat", "Zucchero tirato", "Fiori zucchero", "Uova", "Burro", "Farina", "Vaniglia", "Mandorle", "Miele", "Coloranti"],
     "steps": ["Prepara centinaia di bignè.", "Farcisci tutti.", "Prepara il caramello.", "Costruisci la piramide.", "Crea decorazioni zucchero.", "Aggiungi fiori.", "Presenta maestosamente."],
     "images": ["https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=600", "https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc?w=600"]},
    
    {"id": 43, "name": "Torta Moderna Art", "difficulty": 5, "xp": 880, "ingredients_count": 12,
     "ingredients": ["Mousse assortite", "Inserti gel", "Glassa specchio", "Decorazioni 3D", "Cioccolato", "Gelatina", "Panna", "Coloranti", "Acetato", "Stampi silicone", "Azoto", "Oro alimentare"],
     "steps": ["Crea le mousse.", "Congela gli inserti.", "Assembla gli strati.", "Congela profondo.", "Prepara glasse colorate.", "Glassa con tecnica.", "Decora avanguardia."],
     "images": ["https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600", "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600"]},
    
    {"id": 44, "name": "Petit Fours Assortiti", "difficulty": 5, "xp": 870, "ingredients_count": 20,
     "ingredients": ["Génoise", "Marzapane", "Fondant", "Cioccolato", "Frutta candita", "Crema", "Glasse colorate", "Noci", "Mandorle", "Pistacchi", "Caffè", "Liquori", "Coloranti", "Oro", "Argento", "Perle", "Fiori", "Foglie", "Stampi", "Acetato"],
     "steps": ["Prepara diverse basi.", "Taglia in quadratini.", "Farcisci varietà.", "Ricopri di marzapane.", "Glassa in colori.", "Decora singolarmente.", "Presenta in scatola."],
     "images": ["https://images.unsplash.com/photo-1558326567-98ae2405596b?w=600", "https://images.unsplash.com/photo-1569864358642-9d1684040f43?w=600"]},
    
    {"id": 45, "name": "Scultura Cioccolato", "difficulty": 5, "xp": 1000, "ingredients_count": 8,
     "ingredients": ["3kg Cioccolato", "Stampi silicone", "Termometro", "Pistola calore", "Coloranti liposolubili", "Pennelli", "Acetato", "Supporto"],
     "steps": ["Tempera il cioccolato.", "Crea gli elementi.", "Assembla la struttura.", "Salda con cioccolato.", "Aggiungi dettagli.", "Dipingi effetti.", "Esponi capolavoro."],
     "images": ["https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=600", "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600"]},
    
    {"id": 46, "name": "Torta Decostruita", "difficulty": 5, "xp": 920, "ingredients_count": 14,
     "ingredients": ["Elementi scomposti", "Gel texture", "Sferificazioni", "Crumble", "Mousse", "Sorbetto", "Fiori edibili", "Microgreens", "Polveri", "Aria", "Agar", "Alginato", "Calcio", "Azoto"],
     "steps": ["Prepara ogni elemento.", "Crea le texture.", "Sferifica i sapori.", "Prepara arie e gel.", "Componi il piatto.", "Posiziona con pinzette.", "Presenta l'arte."],
     "images": ["https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600", "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600"]},
    
    {"id": 47, "name": "Torta Gravity", "difficulty": 4, "xp": 850, "ingredients_count": 11,
     "ingredients": ["Base torta", "Struttura interna", "Caramelle", "M&M's", "Smarties", "Cioccolato", "Crema burro", "Paglia decorativa", "Supporto nascosto", "Colla alimentare", "Coloranti"],
     "steps": ["Prepara la torta.", "Installa il supporto.", "Ricopri la torta.", "Crea l'effetto gravity.", "Fissa le caramelle.", "Nascondi la struttura.", "Sorprendi tutti!"],
     "images": ["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600", "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600"]},
    
    {"id": 48, "name": "Number Cake", "difficulty": 3, "xp": 780, "ingredients_count": 10,
     "ingredients": ["Pasta sablée", "Crema diplomate", "Frutta fresca", "Fiori edibili", "Macaron", "Meringhe", "Cioccolatini", "Oro alimentare", "Template", "Panna"],
     "steps": ["Disegna i numeri.", "Taglia la sablée.", "Cuoci i numeri.", "Prepara la crema.", "Monta con panna.", "Farcisci a sac à poche.", "Decora lussuosamente."],
     "images": ["https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600", "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600"]},
    
    {"id": 49, "name": "Semifreddo Strati", "difficulty": 4, "xp": 830, "ingredients_count": 12,
     "ingredients": ["Biscotto", "Mousse vaniglia", "Mousse cioccolato", "Mousse frutti", "Croccante", "Panna", "Uova", "Zucchero", "Cioccolato", "Frutti rossi", "Gelatina", "Bagna"],
     "steps": ["Prepara il biscotto.", "Crea tre mousse.", "Assembla a strati.", "Aggiungi croccante.", "Congela profondo.", "Glassa o decora.", "Taglia e servi."],
     "images": ["https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc?w=600", "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600"]},
    
    {"id": 50, "name": "Il Capolavoro Finale", "difficulty": 5, "xp": 1500, "ingredients_count": 25,
     "ingredients": ["Tutto ciò che hai imparato", "Creatività", "Passione", "Tecnica", "Decorazioni", "Cioccolato", "Mousse", "Biscotti", "Creme", "Frutta", "Glasse", "Fondant", "Pasta reale", "Fiori", "Oro", "Perle", "Nastri", "Zucchero tirato", "Isomalt", "Stampi", "Pennelli", "Colori", "Cuore", "Anima", "Amore"],
     "steps": ["Pianifica la tua opera.", "Prepara tutti gli elementi.", "Lavora con amore.", "Cura ogni dettaglio.", "Assembla con precisione.", "Decora con arte.", "Presenta il tuo capolavoro.", "Sei un MAESTRO!"],
     "images": ["https://images.unsplash.com/photo-1535254973040-607b474cb50d?w=600", "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600"]}
]

# Default user profile
DEFAULT_USER = {
    "name": "Chef Pasticcere",
    "level": 1,
    "total_xp": 0,
    "completed_recipes": [],  # Lista di ID ricette completate
    "quiz_completed": [],     # Lista di ID ricette con quiz completato
    "quiz_scores": {}         # Dizionario {recipe_id: score}
}

# Configurazione per la persistenza degli utenti
USERS_FILE = 'users.json'
XP_PER_LEVEL = 100 # XP necessari per salire di livello

# ==================== STORAGE HELPERS ====================

def load_users_data():
    """Carica i dati degli utenti dal file JSON"""
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"users": []}

def save_users_data(data):
    """Salva i dati degli utenti nel file JSON"""
    with open(USERS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_persistent_user(user_id):
    """Trova un utente per ID"""
    data = load_users_data()
    for u in data['users']:
        if u['id'] == user_id:
            return u
    return None

def create_persistent_user(name, user_id=None):
    """Crea un nuovo utente persistente"""
    if not user_id:
        user_id = uuid.uuid4().hex
        
    user = DEFAULT_USER.copy()
    user.update({
        "id": user_id,
        "name": name,
        "created_at": datetime.now().isoformat(),
        "last_active": datetime.now().isoformat()
    })
    
    data = load_users_data()
    data['users'].append(user)
    save_users_data(data)
    return user

def update_persistent_user(user_data):
    """Aggiorna i dati di un utente esistente"""
    data = load_users_data()
    updated = False
    for i, u in enumerate(data['users']):
        if u['id'] == user_data.get('id'):
            # Aggiorna last_active
            user_data['last_active'] = datetime.now().isoformat()
            data['users'][i] = user_data
            updated = True
            break
    
    if updated:
        save_users_data(data)

def get_leaderboard(top=10):
    """Ritorna la top N utenti per XP"""
    data = load_users_data()
    # Ordina per XP decrescente
    users = sorted(data['users'], key=lambda x: x.get('total_xp', 0), reverse=True)
    return users[:top]

def get_user_rank(user_id):
    """Ritorna la posizione in classifica dell'utente"""
    data = load_users_data()
    users = sorted(data['users'], key=lambda x: x.get('total_xp', 0), reverse=True)
    for i, u in enumerate(users, 1):
        if u['id'] == user_id:
            return i
    return None

def get_user_profile():
    if 'user' not in session:
        session['user'] = DEFAULT_USER.copy()
    return session['user']

def get_badge_for_level(level):
    for badge_id, badge in BADGES.items():
        if badge["min_level"] <= level <= badge["max_level"]:
            return badge
    return BADGES["maestro"]

def calculate_level(xp):
    # Every 100 XP = 1 level, roughly
    return min(50, max(1, xp // 100 + 1))


def check_milestone(old_level, new_level):
    milestones = [10, 20, 30, 40, 50]
    for m in milestones:
        if old_level < m <= new_level:
            return m
    return None

# ==================== QUIZ LOGIC (NUOVO) ====================

import random

def get_all_ingredients():
    """Raccoglie tutti gli ingredienti unici da tutte le ricette"""
    all_ingredients = set()
    for recipe in RECIPES:
        for ing in recipe.get('ingredients', []):
            # Estrae solo il nome dell'ingrediente (senza quantità)
            clean_ing = ing.split(' ', 1)[-1] if any(c.isdigit() for c in ing.split()[0]) else ing
            all_ingredients.add(clean_ing)
    return list(all_ingredients)

def generate_quiz_questions(recipe_id):
    """Genera 5 domande quiz con distrattori intelligenti"""
    recipe = next((r for r in RECIPES if r['id'] == recipe_id), None)
    if not recipe:
        return []
    
    recipe_ingredients = recipe.get('ingredients', [])
    difficulty = recipe.get('difficulty', 1)
    
    # Trova ingredienti da ricette con difficoltà simile (±1) per i distrattori
    similar_recipes = [r for r in RECIPES if abs(r.get('difficulty', 1) - difficulty) <= 1 and r['id'] != recipe_id]
    distractor_pool = set()
    for r in similar_recipes:
        for ing in r.get('ingredients', []):
            clean_ing = ing.split(' ', 1)[-1] if any(c.isdigit() for c in ing.split()[0]) else ing
            distractor_pool.add(clean_ing)
    
    # Rimuovi ingredienti che sono anche nella ricetta corrente
    recipe_ing_clean = set()
    for ing in recipe_ingredients:
        clean_ing = ing.split(' ', 1)[-1] if any(c.isdigit() for c in ing.split()[0]) else ing
        recipe_ing_clean.add(clean_ing)
    
    distractor_pool = list(distractor_pool - recipe_ing_clean)
    
    # Se non abbiamo abbastanza distrattori, usa tutti gli ingredienti
    if len(distractor_pool) < 15:
        distractor_pool = list(set(get_all_ingredients()) - recipe_ing_clean)
    
    # Seleziona 5 ingredienti casuali dalla ricetta per le domande
    selected_ingredients = random.sample(recipe_ingredients, min(5, len(recipe_ingredients)))
    
    questions = []
    for i, correct_ingredient in enumerate(selected_ingredients):
        # Pulisci l'ingrediente corretto
        correct_clean = correct_ingredient.split(' ', 1)[-1] if any(c.isdigit() for c in correct_ingredient.split()[0]) else correct_ingredient
        
        # Seleziona 3 distrattori casuali
        available_distractors = [d for d in distractor_pool if d != correct_clean]
        distractors = random.sample(available_distractors, min(3, len(available_distractors)))
        
        # Crea le opzioni e mescola
        options = [correct_clean] + distractors
        random.shuffle(options)
        
        # Trova l'indice della risposta corretta
        correct_index = options.index(correct_clean)
        
        questions.append({
            "id": i + 1,
            "question": f"Quale di questi ingredienti serve per {recipe['name']}?",
            "options": options,
            "correct": correct_index
        })
    
    return questions

# Emoji per gli ingredienti
INGREDIENT_EMOJIS = {
    "farina": "🌾", "zucchero": "🍬", "burro": "🧈", "uovo": "🥚", "uova": "🥚",
    "latte": "🥛", "panna": "🥛", "cioccolato": "🍫", "cacao": "🍫", "vaniglia": "🌸",
    "mandorle": "🥜", "nocciole": "🌰", "pistacchi": "🥜", "noci": "🌰",
    "fragole": "🍓", "limone": "🍋", "arancia": "🍊", "mele": "🍎", "frutti": "🫐",
    "marmellata": "🍯", "miele": "🍯", "cannella": "✨", "sale": "🧂",
    "lievito": "🫧", "ricotta": "🧀", "mascarpone": "🧀", "philadelphia": "🧀",
    "caffè": "☕", "rum": "🥃", "marsala": "🍷", "liquore": "🍾",
    "gelatina": "💎", "colorante": "🎨", "oro": "✨", "default": "🥄"
}

def get_ingredient_emoji(ingredient):
    """Ritorna un emoji appropriato per l'ingrediente"""
    ing_lower = ingredient.lower()
    for key, emoji in INGREDIENT_EMOJIS.items():
        if key in ing_lower:
            return emoji
    return INGREDIENT_EMOJIS["default"]

# ==================== ROUTES ====================

@app.route('/')
def index():
    # Gestione Sessione Utente Persistente
    user_id = session.get('user_id')
    user = None
    
    if user_id:
        user = get_persistent_user(user_id)
        
    # Se utente non esiste o non ha ID, mandalo al welcome
    if not user:
        if not user_id:
            user_id = uuid.uuid4().hex
            session['user_id'] = user_id
        return redirect(url_for('welcome'))
    
    # Aggiorna sessione con dati freschi
    session['user'] = user
    
    # Calcola livello e progressi
    user_level = calculate_level(user['total_xp'])
    badge = get_badge_for_level(user_level)
    
    # Leaderboard Data
    leaderboard = get_leaderboard(10)
    user_rank = get_user_rank(user['id'])
    
    # Arricchisci le ricette con lo stato (bloccato/sbloccato/completato)
    recipes_with_status = []
    completed_ids = user.get('completed_recipes', [])
    quiz_completed_ids = user.get('quiz_completed', []) # Se vuoi visualizzare anche stato quiz
    
    for recipe in RECIPES:
        # Sbloccato se ID <= user level
        is_unlocked = recipe['id'] <= user_level
        status = "unlocked" if is_unlocked else "locked"
        completed = recipe['id'] in completed_ids
        
        # Aggiungiamo info se il quiz è fatto per mostrarlo nella UI eventualmente
        quiz_done = recipe['id'] in quiz_completed_ids
        
        recipes_with_status.append({
            **recipe,
            "status": status,
            "completed": completed,
            "quiz_done": quiz_done
        })
    
    # Logica roadmap progress
    xp_for_next = XP_PER_LEVEL * user_level
    xp_progress = (user['total_xp'] % XP_PER_LEVEL) / XP_PER_LEVEL * 100
    
    return render_template('index.html', 
                         recipes=recipes_with_status,
                         user=user,
                         user_level=user_level,
                         badge=badge,
                         xp_for_next=xp_for_next,
                         xp_progress=xp_progress,
                         leaderboard=leaderboard,
                         user_rank=user_rank)

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:
             return render_template('welcome.html', error="Inserisci un nome!")
             
        user_id = session.get('user_id') or uuid.uuid4().hex
        session['user_id'] = user_id
        
        # Crea e salva utente
        user = create_persistent_user(username, user_id)
        session['user'] = user
        
        return redirect(url_for('index'))
    
    return render_template('welcome.html')

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    user = get_user_profile()
    user_level = calculate_level(user['total_xp'])
    badge = get_badge_for_level(user_level)
    
    recipe_data = next((r for r in RECIPES if r['id'] == recipe_id), None)
    if not recipe_data:
        return "Ricetta non trovata", 404
    
    if recipe_id > user_level:
        return "Ricetta bloccata! Completa le ricette precedenti.", 403
    
    user_notes = user.get('notes', {}).get(str(recipe_id), '')
    completed = recipe_id in user.get('completed_recipes', [])
    
    return render_template('recipe.html', 
                         recipe=recipe_data, 
                         user=user,
                         user_level=user_level,
                         badge=badge,
                         user_notes=user_notes,
                         completed=completed)

# ==================== QUIZ ROUTES (NUOVO) ====================

@app.route('/quiz/<int:recipe_id>')
def quiz(recipe_id):
    """Pagina quiz per una ricetta"""
    user = get_user_profile()
    user_level = calculate_level(user['total_xp'])
    badge = get_badge_for_level(user_level)
    
    # DEBUG
    print(f"DEBUG: Quiz per ricetta {recipe_id}")
    print(f"DEBUG: User level: {user_level}")
    
    recipe_data = next((r for r in RECIPES if r['id'] == recipe_id), None)
    if not recipe_data:
        return "Ricetta non trovata", 404
    
    if recipe_id > user_level:
        return "Ricetta bloccata! Completa le ricette precedenti.", 403
    
    # Usa le domande predefinite da quiz_data.py
    questions_raw = get_quiz(recipe_id)
    
    print(f"DEBUG: Domande trovate: {len(questions_raw)}")
    
    # Formatta le domande per il template
    questions = []
    for i, q in enumerate(questions_raw):
        questions.append({
            'id': i + 1,
            'question': q['question'],
            'options': q['options'],
            'correct': q['correct'],
            'explanation': q['explanation'],
            'options_with_emoji': [
                {'text': opt, 'emoji': get_ingredient_emoji(opt)}
                for opt in q['options']
            ]
        })
    
    # Controlla se il quiz è già stato completato
    quiz_already_done = recipe_id in user.get('quiz_completed', [])
    best_score = user.get('quiz_scores', {}).get(str(recipe_id), 0)
    
    return render_template('quiz.html',
                         recipe=recipe_data,
                         user=user,
                         user_level=user_level,
                         badge=badge,
                         quiz_already_done=quiz_already_done,
                         best_score=best_score)

@app.route('/api/get-quiz/<int:recipe_id>')
def get_quiz_api(recipe_id):
    """API per ottenere le domande del quiz"""
    questions_raw = get_quiz(recipe_id)
    
    questions = []
    for i, q in enumerate(questions_raw):
        questions.append({
            'id': i + 1,
            'question': q['question'],
            'options': q['options'],
            'correct': q['correct'],
            'explanation': q['explanation'],
            'options_with_emoji': [
                {'text': opt, 'emoji': get_ingredient_emoji(opt)}
                for opt in q['options']
            ]
        })
    return jsonify({
        "questions": questions,
        "totalQuestions": len(questions)
    })

@app.route('/api/submit-quiz', methods=['POST'])
def submit_quiz():
    """API per inviare le risposte del quiz"""
    try:
        data = request.json
        recipe_id = data.get('recipe_id')
        answers = data.get('answers', [])  # Lista di indici delle risposte selezionate
        
        print(f"DEBUG: Submit quiz {recipe_id}, Answers: {answers}")
        
        recipe_data = next((r for r in RECIPES if r['id'] == recipe_id), None)
        if not recipe_data:
            return jsonify({"error": "Ricetta non trovata"}), 404
        
        # Usa le domande predefinite da quiz_data.py
        questions_raw = get_quiz(recipe_id)
        
        # Gestione caso array answers sparso (es. [0, null, 1])
        # Assicuriamoci che abbia la lunghezza giusta riempiendo i buchi con -1
        processed_answers = []
        for i in range(len(questions_raw)):
            val = answers[i] if i < len(answers) and answers[i] is not None else -1
            processed_answers.append(val)
        
        # Calcola il punteggio
        correct_count = 0
        results = []
        for i, (q, user_answer) in enumerate(zip(questions_raw, processed_answers)):
            is_correct = user_answer == q['correct']
            if is_correct:
                correct_count += 1
            results.append({
                "question_id": i + 1,
                "user_answer": user_answer,
                "correct_answer": q['correct'],
                "is_correct": is_correct,
                "explanation": q['explanation']
            })
        
        print(f"DEBUG: Result {correct_count}/{len(questions_raw)}")
        
        # Calcola XP usando la funzione da quiz_data.py
        xp_earned = calculate_score(correct_count)
        passed = correct_count >= 3  # Minimo 3/5 per superare
        
        user = get_user_profile()
        old_level = calculate_level(user['total_xp'])
        
        # Inizializza i campi quiz se non esistono
        if 'quiz_completed' not in user:
            user['quiz_completed'] = []
        if 'quiz_scores' not in user:
            user['quiz_scores'] = {}
        
        # Assegna XP solo se è la prima volta che completa il quiz
        # NOTA: Usiamo il dizionario user caricato da session/storage
        first_time = recipe_id not in user.get('quiz_completed', [])
        
        if first_time and passed:
            # Aggiorna liste
            completed_list = user.get('quiz_completed', [])
            if recipe_id not in completed_list:
                completed_list.append(recipe_id)
                user['quiz_completed'] = completed_list
                
            user['total_xp'] = user.get('total_xp', 0) + xp_earned
        
        # Aggiorna il best score
        scores = user.get('quiz_scores', {})
        current_best = scores.get(str(recipe_id), 0)
        if correct_count > current_best:
            scores[str(recipe_id)] = correct_count
            user['quiz_scores'] = scores
        
        # AGGIORNAMENTO PERSISTENTE
        user_id = session.get('user_id')
        # Se per caso non c'è user_id (sessione scaduta o test), usiamo l'ID dentro user se c'è
        if not user_id and 'id' in user:
            user_id = user['id']
            
        if user_id:
            # Assicuriamoci che l'oggetto user abbia l'id
            user['id'] = user_id
            update_persistent_user(user)
            session['user'] = user # Aggiorna sessione
        
        new_level = calculate_level(user['total_xp'])
        milestone = check_milestone(old_level, new_level) if (first_time and passed) else None
        new_badge = get_badge_for_level(new_level) if milestone else None
        
        # Messaggi motivazionali
        if correct_count == 5:
            message = "🎉 Perfetto! Sei un vero esperto degli ingredienti!"
        elif correct_count >= 4:
            message = "🌟 Ottimo lavoro! Conosci bene questa ricetta!"
        elif correct_count >= 3:
            message = "👍 Bene! Hai superato il quiz!"
        elif correct_count >= 2:
            message = "💪 Ci sei quasi! Riprova per migliorare!"
        else:
            message = "📚 Studia un po' gli ingredienti e riprova!"
        
        return jsonify({
            "success": True,
            "correct_count": correct_count,
            "total_questions": len(questions_raw),
            "xp_earned": xp_earned if (first_time and passed) else 0,
            "total_xp": user['total_xp'],
            "passed": passed,
            "first_time": first_time,
            "message": message,
            "results": results,
            "new_level": new_level,
            "milestone": milestone,
            "new_badge": new_badge
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/api/complete-recipe', methods=['POST'])

def complete_recipe():
    data = request.json
    recipe_id = data.get('recipe_id')
    
    recipe_data = next((r for r in RECIPES if r['id'] == recipe_id), None)
    if not recipe_data:
        return jsonify({"error": "Ricetta non trovata"}), 404
    
    user = get_user_profile()
    old_level = calculate_level(user['total_xp'])
    
    # Add XP if not already completed
    if recipe_id not in user['completed_recipes']:
        user['completed_recipes'].append(recipe_id)
        user['total_xp'] += recipe_data['xp']
        session['user'] = user
    
    new_level = calculate_level(user['total_xp'])
    milestone = check_milestone(old_level, new_level)
    new_badge = get_badge_for_level(new_level) if milestone else None
    
    return jsonify({
        "success": True,
        "xp_earned": recipe_data['xp'],
        "total_xp": user['total_xp'],
        "new_level": new_level,
        "milestone": milestone,
        "new_badge": new_badge
    })

@app.route('/api/save-notes', methods=['POST'])
def save_notes():
    data = request.json
    recipe_id = str(data.get('recipe_id'))
    notes = data.get('notes', '')
    
    user = get_user_profile()
    if 'notes' not in user:
        user['notes'] = {}
    user['notes'][recipe_id] = notes
    session['user'] = user
    
    return jsonify({"success": True})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '').lower()
    recipe_id = data.get('recipe_id')
    
    # Context-aware responses
    responses = {
        "tempo": "Il tempo di cottura dipende dal forno. Controlla sempre il colore dorato!",
        "temperatura": "Preriscalda sempre il forno. La temperatura giusta è fondamentale!",
        "impasto": "L'impasto deve essere lavorato ma non troppo. La pazienza è la chiave!",
        "crema": "Per una crema perfetta, mescola sempre sul fuoco basso e non smettere mai!",
        "uova": "Le uova devono essere a temperatura ambiente per montare meglio.",
        "burro": "Il burro deve essere freddo per la frolla, morbido per le torte.",
        "lievito": "Non aprire mai il forno durante la lievitazione!",
        "cioccolato": "Sciogli il cioccolato a bagnomaria per evitare di bruciarlo.",
        "panna": "La panna si monta meglio se fredda. Metti anche la ciotola in frigo!",
        "farina": "Setaccia sempre la farina per evitare grumi.",
        "zucchero": "Lo zucchero a velo si scioglie più facilmente nelle creme.",
        "decorazione": "Decora quando la torta è completamente fredda!",
        "aiuto": "Sono qui per aiutarti! Chiedimi di ingredienti, tempi, temperature...",
        "ciao": "Ciao Chef! Come posso aiutarti con questa ricetta?",
        "grazie": "Prego! In bocca al lupo per la tua creazione! 🧁"
    }
    
    response = "Ottima domanda! Ricorda: la pasticceria richiede precisione e amore. Se hai dubbi specifici, chiedi pure!"
    
    for keyword, reply in responses.items():
        if keyword in message:
            response = reply
            break
    
    return jsonify({"response": response})

@app.route('/api/user-stats')
def user_stats():
    user = get_user_profile()
    user_level = calculate_level(user['total_xp'])
    badge = get_badge_for_level(user_level)
    
    return jsonify({
        "total_xp": user['total_xp'],
        "level": user_level,
        "badge": badge,
        "completed_count": len(user.get('completed_recipes', []))
    })

@app.route('/leaderboard')
def leaderboard_view():
    """Pagina completa per la classifica"""
    user_id = session.get('user_id')
    user = None
    if user_id:
        user = get_persistent_user(user_id)
        
    if not user:
         return redirect(url_for('welcome'))
         
    # Ottieni Top 100
    leaderboard = get_leaderboard(100)
    user_rank = get_user_rank(user['id'])
    
    return render_template('leaderboard.html', 
                         leaderboard=leaderboard, 
                         user=user, 
                         user_rank=user_rank)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
