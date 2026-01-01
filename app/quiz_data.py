# quiz_data.py
"""
Quiz Data for PasterChef - 50 Recipes
Ogni ricetta ha 5 domande a scelta multipla
"""

QUIZ_DATA = {
    # ==================== LIVELLO 1-10: BASE ====================
    1: [  # Biscotti Base
        {"question": "Quale farina si usa per i Biscotti Base?", "options": ["Farina 00", "Farina Manitoba", "Farina di Mandorle", "Farina Integrale"], "correct": 0, "explanation": "La Farina 00 rende i biscotti friabili! 🍪"},
        {"question": "Quanto burro serve per i Biscotti Base?", "options": ["100g", "150g", "200g", "50g"], "correct": 0, "explanation": "100g di burro è la dose perfetta!"},
        {"question": "A che temperatura si cuociono i Biscotti Base?", "options": ["180°C", "160°C", "200°C", "140°C"], "correct": 0, "explanation": "180°C per 12-15 minuti è l'ideale!"},
        {"question": "Quale aroma si usa nei Biscotti Base?", "options": ["Vanillina", "Cannella", "Limone", "Arancia"], "correct": 0, "explanation": "La vanillina dona un profumo delicato!"},
        {"question": "Quante uova servono per i Biscotti Base?", "options": ["1", "2", "3", "0"], "correct": 0, "explanation": "Un solo uovo basta per legare l'impasto!"},
    ],
    2: [  # Muffin Magici
        {"question": "Quale ingrediente rende magici i Muffin?", "options": ["Gocce di cioccolato", "Uvetta", "Noci", "Canditi"], "correct": 0, "explanation": "Le gocce di cioccolato sono irresistibili! 🧁"},
        {"question": "Quanto latte serve per i Muffin Magici?", "options": ["100ml", "200ml", "50ml", "150ml"], "correct": 0, "explanation": "100ml di latte per un impasto morbido!"},
        {"question": "Quante uova servono per i Muffin?", "options": ["2", "1", "3", "4"], "correct": 0, "explanation": "Due uova per muffin soffici!"},
        {"question": "A che temperatura si cuociono i Muffin?", "options": ["180°C", "160°C", "200°C", "150°C"], "correct": 0, "explanation": "180°C per una cottura uniforme!"},
        {"question": "Quanto tempo cuociono i Muffin?", "options": ["20-25 minuti", "10-15 minuti", "30-35 minuti", "40 minuti"], "correct": 0, "explanation": "20-25 minuti per la doratura perfetta!"},
    ],
    3: [  # Crostata Croccante
        {"question": "Quale grasso si usa nella frolla della Crostata?", "options": ["Burro", "Olio", "Strutto", "Margarina"], "correct": 0, "explanation": "Il burro rende la frolla friabile! 🥧"},
        {"question": "Quanti tuorli servono per la Crostata?", "options": ["2", "1", "3", "4"], "correct": 0, "explanation": "Due tuorli per una frolla dorata!"},
        {"question": "Cosa si mette come farcitura?", "options": ["Marmellata", "Crema", "Cioccolato", "Ricotta"], "correct": 0, "explanation": "La marmellata è il classico!"},
        {"question": "Quanto riposa la frolla in frigo?", "options": ["30 minuti", "10 minuti", "1 ora", "2 ore"], "correct": 0, "explanation": "30 minuti per un impasto lavorabile!"},
        {"question": "A che temperatura si cuoce la Crostata?", "options": ["180°C", "160°C", "200°C", "150°C"], "correct": 0, "explanation": "180°C per 35 minuti circa!"},
    ],
    4: [  # Tiramisù Tradizionale
        {"question": "Quale formaggio si usa nel Tiramisù?", "options": ["Mascarpone", "Ricotta", "Philadelphia", "Robiola"], "correct": 0, "explanation": "Il mascarpone è fondamentale! 🍰"},
        {"question": "Quante uova servono per il Tiramisù?", "options": ["4", "2", "6", "3"], "correct": 0, "explanation": "4 uova per una crema ricca!"},
        {"question": "Cosa si usa per bagnare i savoiardi?", "options": ["Caffè", "Latte", "Liquore", "Acqua"], "correct": 0, "explanation": "Il caffè è essenziale!"},
        {"question": "Quanto riposa il Tiramisù in frigo?", "options": ["4 ore", "1 ora", "30 minuti", "8 ore"], "correct": 0, "explanation": "Almeno 4 ore per compattare!"},
        {"question": "Cosa si spolvera sopra il Tiramisù?", "options": ["Cacao", "Cannella", "Zucchero a velo", "Caffè"], "correct": 0, "explanation": "Il cacao amaro è tradizionale!"},
    ],
    5: [  # Profiteroles Pazzi
        {"question": "Quale impasto si usa per i bignè?", "options": ["Pasta choux", "Pasta sfoglia", "Pasta frolla", "Pan brioche"], "correct": 0, "explanation": "La pasta choux è perfetta! 🍩"},
        {"question": "Quante uova servono per la choux?", "options": ["4", "2", "3", "5"], "correct": 0, "explanation": "4 uova per una pasta elastica!"},
        {"question": "A che temperatura si cuociono i bignè?", "options": ["200°C", "180°C", "160°C", "220°C"], "correct": 0, "explanation": "200°C per farli gonfiare bene!"},
        {"question": "Con cosa si ricoprono i Profiteroles?", "options": ["Cioccolato", "Glassa", "Caramello", "Panna"], "correct": 0, "explanation": "Il cioccolato fuso è delizioso!"},
        {"question": "Con cosa si farciscono i bignè?", "options": ["Panna", "Crema", "Nutella", "Marmellata"], "correct": 0, "explanation": "La panna montata è classica!"},
    ],
    6: [  # Cannoli Creativi
        {"question": "Quale grasso si usa nell'impasto dei Cannoli?", "options": ["Strutto", "Burro", "Olio", "Margarina"], "correct": 0, "explanation": "Lo strutto rende croccanti! 🥮"},
        {"question": "Quale vino si usa nell'impasto?", "options": ["Marsala", "Vino rosso", "Prosecco", "Moscato"], "correct": 0, "explanation": "Il Marsala dà aroma unico!"},
        {"question": "Con cosa si farciscono i Cannoli?", "options": ["Ricotta", "Mascarpone", "Panna", "Crema"], "correct": 0, "explanation": "La ricotta è tradizione siciliana!"},
        {"question": "Cosa si aggiunge alla farcia?", "options": ["Pistacchi", "Noci", "Mandorle", "Arachidi"], "correct": 0, "explanation": "I pistacchi sono tipici!"},
        {"question": "Come si cuociono i Cannoli?", "options": ["Fritti", "Al forno", "Bolliti", "Al vapore"], "correct": 0, "explanation": "La frittura li rende croccanti!"},
    ],
    7: [  # Babà al Rum
        {"question": "Quale lievito si usa per il Babà?", "options": ["Lievito di birra", "Lievito chimico", "Bicarbonato", "Cremor tartaro"], "correct": 0, "explanation": "Il lievito di birra è essenziale! 🍮"},
        {"question": "Quanto deve lievitare l'impasto?", "options": ["2 ore", "30 minuti", "1 ora", "4 ore"], "correct": 0, "explanation": "2 ore per un babà soffice!"},
        {"question": "Quale liquore si usa per la bagna?", "options": ["Rum", "Limoncello", "Amaretto", "Cognac"], "correct": 0, "explanation": "Il rum è tradizionale!"},
        {"question": "A che temperatura si cuoce il Babà?", "options": ["180°C", "160°C", "200°C", "150°C"], "correct": 0, "explanation": "180°C per una cottura uniforme!"},
        {"question": "Con cosa si serve il Babà?", "options": ["Panna", "Gelato", "Crema", "Frutta"], "correct": 0, "explanation": "La panna è perfetta!"},
    ],
    8: [  # Torta Sacher
        {"question": "Quanto cioccolato serve per la Sacher?", "options": ["200g", "100g", "300g", "150g"], "correct": 0, "explanation": "200g per un sapore intenso! 🍫"},
        {"question": "Quante uova servono per la Sacher?", "options": ["6", "4", "3", "8"], "correct": 0, "explanation": "6 uova per una torta ricca!"},
        {"question": "Quale marmellata si usa?", "options": ["Albicocche", "Fragole", "Lamponi", "Arance"], "correct": 0, "explanation": "Le albicocche sono tradizionali!"},
        {"question": "A che temperatura si cuoce?", "options": ["170°C", "180°C", "160°C", "190°C"], "correct": 0, "explanation": "170°C per 50 minuti!"},
        {"question": "Come si rifinisce la Sacher?", "options": ["Glassata", "Spolverata", "Decorata con panna", "Nuda"], "correct": 0, "explanation": "La glassa di cioccolato è iconica!"},
    ],
    9: [  # Macaron Mignon
        {"question": "Quale farina si usa per i Macaron?", "options": ["Farina di mandorle", "Farina 00", "Fecola", "Farina di cocco"], "correct": 0, "explanation": "Le mandorle sono essenziali! 🍪"},
        {"question": "Quanti albumi servono?", "options": ["3", "2", "4", "5"], "correct": 0, "explanation": "3 albumi per la giusta consistenza!"},
        {"question": "Cosa si usa per colorare?", "options": ["Colorante alimentare", "Succo di frutta", "Cacao", "Caffè"], "correct": 0, "explanation": "I coloranti gel sono perfetti!"},
        {"question": "A che temperatura si cuociono?", "options": ["150°C", "180°C", "160°C", "140°C"], "correct": 0, "explanation": "150°C per 14 minuti!"},
        {"question": "Con cosa si farciscono?", "options": ["Ganache", "Marmellata", "Panna", "Nutella"], "correct": 0, "explanation": "La ganache è classica!"},
    ],
    10: [  # Torta della Nonna
        {"question": "Cosa si mette sopra la Torta della Nonna?", "options": ["Pinoli", "Mandorle", "Noci", "Nocciole"], "correct": 0, "explanation": "I pinoli sono tradizionali! 🎂"},
        {"question": "Quale crema si usa?", "options": ["Crema pasticcera", "Crema chantilly", "Crema al burro", "Ganache"], "correct": 0, "explanation": "La pasticcera è perfetta!"},
        {"question": "Quanto latte serve per la crema?", "options": ["500ml", "250ml", "750ml", "1 litro"], "correct": 0, "explanation": "500ml per una crema densa!"},
        {"question": "Quanti tuorli per la crema?", "options": ["4", "2", "6", "3"], "correct": 0, "explanation": "4 tuorli per cremosità!"},
        {"question": "A che temperatura si cuoce?", "options": ["180°C", "160°C", "200°C", "170°C"], "correct": 0, "explanation": "180°C per 40 minuti!"},
    ],
    # ==================== LIVELLO 11-20: INTERMEDIO ====================
    11: [  # Millefoglie Classica
        {"question": "Quale pasta si usa per la Millefoglie?", "options": ["Pasta sfoglia", "Pasta frolla", "Pasta choux", "Pasta brisée"], "correct": 0, "explanation": "La sfoglia è fondamentale!"},
        {"question": "A che temperatura si cuoce la sfoglia?", "options": ["200°C", "180°C", "160°C", "220°C"], "correct": 0, "explanation": "200°C per sfogliare bene!"},
        {"question": "Quale frutta si usa per decorare?", "options": ["Fragole", "Mele", "Pere", "Arance"], "correct": 0, "explanation": "Le fragole sono classiche!"},
        {"question": "Quale crema si usa?", "options": ["Crema pasticcera", "Crema al cioccolato", "Panna cotta", "Budino"], "correct": 0, "explanation": "La pasticcera è tradizionale!"},
        {"question": "Cosa si spolvera sopra?", "options": ["Zucchero a velo", "Cacao", "Cannella", "Cocco"], "correct": 0, "explanation": "Lo zucchero a velo è elegante!"},
    ],
    12: [  # Cheesecake New York
        {"question": "Quale formaggio si usa?", "options": ["Philadelphia", "Mascarpone", "Ricotta", "Robiola"], "correct": 0, "explanation": "Il Philadelphia è originale!"},
        {"question": "Quali biscotti per la base?", "options": ["Digestive", "Oreo", "Savoiardi", "Frollini"], "correct": 0, "explanation": "I digestive sono perfetti!"},
        {"question": "Quante uova servono?", "options": ["3", "2", "4", "5"], "correct": 0, "explanation": "3 uova per cremosità!"},
        {"question": "Come si cuoce la Cheesecake?", "options": ["A bagnomaria", "Forno statico", "Forno ventilato", "Microonde"], "correct": 0, "explanation": "Il bagnomaria evita crepe!"},
        {"question": "Quale aroma si aggiunge?", "options": ["Vaniglia", "Cannella", "Limone", "Arancia"], "correct": 0, "explanation": "La vaniglia è classica!"},
    ],
    13: [  # Éclair al Cioccolato
        {"question": "Quale pasta si usa per gli Éclair?", "options": ["Pasta choux", "Pasta sfoglia", "Pasta frolla", "Pan brioche"], "correct": 0, "explanation": "La choux è essenziale!"},
        {"question": "Con cosa si farciscono?", "options": ["Crema pasticcera", "Panna", "Ganache", "Nutella"], "correct": 0, "explanation": "La pasticcera è tradizionale!"},
        {"question": "Come si glassano?", "options": ["Con cioccolato fondente", "Con glassa reale", "Con caramello", "Con zucchero"], "correct": 0, "explanation": "Il cioccolato fondente è delizioso!"},
        {"question": "A che temperatura si cuociono?", "options": ["200°C", "180°C", "160°C", "220°C"], "correct": 0, "explanation": "200°C per farli gonfiare!"},
        {"question": "Quale forma hanno gli Éclair?", "options": ["Allungata", "Rotonda", "Quadrata", "A mezzaluna"], "correct": 0, "explanation": "La forma allungata è caratteristica!"},
    ],
    14: [  # Panna Cotta Frutti Bosco
        {"question": "Quale addensante si usa?", "options": ["Gelatina", "Amido", "Agar agar", "Fecola"], "correct": 0, "explanation": "La gelatina dà la consistenza giusta!"},
        {"question": "Quanta panna serve?", "options": ["500ml", "250ml", "750ml", "1 litro"], "correct": 0, "explanation": "500ml per 4-6 porzioni!"},
        {"question": "Quanto riposa in frigo?", "options": ["4 ore", "1 ora", "2 ore", "8 ore"], "correct": 0, "explanation": "Almeno 4 ore per solidificare!"},
        {"question": "Cosa si prepara con i frutti?", "options": ["Coulis", "Marmellata", "Confettura", "Sciroppo"], "correct": 0, "explanation": "Il coulis è fresco e colorato!"},
        {"question": "Quale aroma si usa?", "options": ["Vaniglia", "Cannella", "Limone", "Menta"], "correct": 0, "explanation": "La vaniglia è perfetta!"},
    ],
    15: [  # Paris-Brest
        {"question": "Quale forma ha il Paris-Brest?", "options": ["Anello (ciambella)", "Rettangolare", "Quadrata", "Triangolare"], "correct": 0, "explanation": "L'anello ricorda una ruota di bici!"},
        {"question": "Quale crema si usa?", "options": ["Crema mousseline", "Crema pasticcera", "Panna", "Ganache"], "correct": 0, "explanation": "La mousseline al pralinato è tradizionale!"},
        {"question": "Cosa si aggiunge alla crema?", "options": ["Pralinato di nocciole", "Cioccolato", "Caffè", "Pistacchio"], "correct": 0, "explanation": "Il pralinato è iconico!"},
        {"question": "Cosa si sparge sopra prima di cuocere?", "options": ["Mandorle a scaglie", "Pinoli", "Zucchero", "Cacao"], "correct": 0, "explanation": "Le mandorle decorano e croccantizzano!"},
        {"question": "A che temperatura si cuoce?", "options": ["190°C", "180°C", "200°C", "170°C"], "correct": 0, "explanation": "190°C per una cottura perfetta!"},
    ],
    16: [  # Torta Caprese
        {"question": "Quale frutta secca si usa?", "options": ["Mandorle", "Nocciole", "Noci", "Pistacchi"], "correct": 0, "explanation": "Le mandorle sono essenziali! 🍫"},
        {"question": "Quanto cioccolato serve?", "options": ["250g", "150g", "300g", "200g"], "correct": 0, "explanation": "250g per sapore intenso!"},
        {"question": "Quante uova servono?", "options": ["5", "3", "4", "6"], "correct": 0, "explanation": "5 uova per una torta ricca!"},
        {"question": "La Caprese contiene farina?", "options": ["No, è senza glutine", "Sì, 100g", "Sì, 200g", "Solo fecola"], "correct": 0, "explanation": "È naturalmente senza farina!"},
        {"question": "A che temperatura si cuoce?", "options": ["160°C", "180°C", "170°C", "150°C"], "correct": 0, "explanation": "160°C per 45 minuti!"},
    ],
    17: [  # Sfogliatella Riccia
        {"question": "Quale grasso si spalma sulla pasta?", "options": ["Strutto", "Burro", "Olio", "Margarina"], "correct": 0, "explanation": "Lo strutto crea le sfoglie!"},
        {"question": "Quale cereale si usa nel ripieno?", "options": ["Semola", "Farina", "Riso", "Orzo"], "correct": 0, "explanation": "La semola è tradizionale!"},
        {"question": "Con cosa si aromatizza il ripieno?", "options": ["Cannella", "Vaniglia", "Limone", "Arancia"], "correct": 0, "explanation": "La cannella è tipica!"},
        {"question": "Quale formaggio nel ripieno?", "options": ["Ricotta", "Mascarpone", "Robiola", "Crescenza"], "correct": 0, "explanation": "La ricotta è essenziale!"},
        {"question": "Cosa si aggiunge al ripieno?", "options": ["Canditi", "Uvetta", "Noci", "Cioccolato"], "correct": 0, "explanation": "I canditi sono tradizionali!"},
    ],
    18: [  # Crème Brûlée
        {"question": "Quanti tuorli servono?", "options": ["5", "3", "4", "6"], "correct": 0, "explanation": "5 tuorli per cremosità!"},
        {"question": "Quanta panna serve?", "options": ["500ml", "250ml", "750ml", "1 litro"], "correct": 0, "explanation": "500ml per la giusta densità!"},
        {"question": "Come si caramella lo zucchero?", "options": ["Con cannello", "Al forno", "Con zucchero a velo", "Con miele"], "correct": 0, "explanation": "Il cannello crea la crosticina!"},
        {"question": "Quale zucchero per caramellare?", "options": ["Zucchero di canna", "Zucchero a velo", "Zucchero semolato", "Miele"], "correct": 0, "explanation": "Lo zucchero di canna caramella meglio!"},
        {"question": "A che temperatura si cuoce?", "options": ["160°C", "180°C", "150°C", "170°C"], "correct": 0, "explanation": "160°C a bagnomaria!"},
    ],
    19: [  # Torta Mimosa
        {"question": "Quale base si usa?", "options": ["Pan di spagna", "Pasta frolla", "Pasta sfoglia", "Biscotto"], "correct": 0, "explanation": "Il pan di spagna è tradizionale!"},
        {"question": "Quale frutta si usa?", "options": ["Ananas", "Fragole", "Pesche", "Arance"], "correct": 0, "explanation": "L'ananas è classico!"},
        {"question": "Come si decora l'esterno?", "options": ["Con cubetti di pan di spagna", "Con panna", "Con zucchero", "Con cacao"], "correct": 0, "explanation": "I cubetti ricordano la mimosa!"},
        {"question": "Quale crema si usa?", "options": ["Crema pasticcera", "Crema al burro", "Panna", "Ganache"], "correct": 0, "explanation": "La pasticcera è perfetta!"},
        {"question": "Per quale occasione è tradizionale?", "options": ["8 marzo (festa donna)", "Pasqua", "Natale", "Ferragosto"], "correct": 0, "explanation": "È il dolce della festa della donna!"},
    ],
    20: [  # Cassata Siciliana
        {"question": "Quale formaggio si usa?", "options": ["Ricotta", "Mascarpone", "Philadelphia", "Robiola"], "correct": 0, "explanation": "La ricotta siciliana è essenziale!"},
        {"question": "Con cosa si ricopre?", "options": ["Pasta reale (marzapane)", "Fondant", "Glassa", "Cioccolato"], "correct": 0, "explanation": "La pasta reale è tradizionale!"},
        {"question": "Cosa si aggiunge alla ricotta?", "options": ["Canditi", "Uvetta", "Noci", "Nocciole"], "correct": 0, "explanation": "I canditi sono tipici!"},
        {"question": "Quale liquore si usa?", "options": ["Maraschino o rum", "Limoncello", "Amaretto", "Grappa"], "correct": 0, "explanation": "Il maraschino aromatizza!"},
        {"question": "Con cosa si decora sopra?", "options": ["Ciliegine candite", "Fragole", "Lamponi", "Mirtilli"], "correct": 0, "explanation": "Le ciliegine sono decorative!"},
    ],
    # ==================== LIVELLO 21-30: AVANZATO ====================
    21: [  # Saint-Honoré
        {"question": "Quali paste si usano?", "options": ["Sfoglia e choux", "Solo sfoglia", "Solo choux", "Frolla e choux"], "correct": 0, "explanation": "La combinazione è caratteristica!"},
        {"question": "Quale crema speciale si usa?", "options": ["Crema chiboust", "Crema pasticcera", "Panna montata", "Crema al burro"], "correct": 0, "explanation": "La chiboust è leggera e ariosa!"},
        {"question": "Come si fissano i bignè?", "options": ["Con caramello", "Con cioccolato", "Con glassa", "Con marmellata"], "correct": 0, "explanation": "Il caramello li incolla!"},
        {"question": "Quale forma ha la base?", "options": ["Rotonda", "Quadrata", "Rettangolare", "Triangolare"], "correct": 0, "explanation": "La base rotonda di sfoglia!"},
        {"question": "Come si decora?", "options": ["Con fili di caramello", "Con zucchero a velo", "Con cacao", "Con granella"], "correct": 0, "explanation": "I fili di caramello sono eleganti!"},
    ],
    22: [  # Opera Cake
        {"question": "Quanti strati ha l'Opera Cake?", "options": ["7 strati", "3 strati", "5 strati", "4 strati"], "correct": 0, "explanation": "7 strati sottili e precisi!"},
        {"question": "Quale biscotto si usa?", "options": ["Biscuit joconde", "Pan di spagna", "Savoiardi", "Biscotto al cacao"], "correct": 0, "explanation": "Il joconde alle mandorle!"},
        {"question": "Quale aroma ha la crema?", "options": ["Caffè", "Vaniglia", "Cioccolato", "Nocciola"], "correct": 0, "explanation": "Il caffè è caratteristico!"},
        {"question": "Con cosa si glassa sopra?", "options": ["Cioccolato lucido", "Glassa reale", "Caramello", "Zucchero"], "correct": 0, "explanation": "La glassa al cioccolato è iconica!"},
        {"question": "Cosa si scrive sopra tradizionalmente?", "options": ["Opera (in oro)", "Buon appetito", "Niente", "Il nome"], "correct": 0, "explanation": "La scritta 'Opera' in oro!"},
    ],
    23: [  # Tarte Tatin
        {"question": "Quale frutta si usa?", "options": ["Mele", "Pere", "Pesche", "Albicocche"], "correct": 0, "explanation": "Le mele sono tradizionali!"},
        {"question": "Come si dispongono le mele?", "options": ["Sul fondo con caramello", "Sopra la sfoglia", "A strati", "Mescolate"], "correct": 0, "explanation": "Si caramellano prima, poi si aggiunge la sfoglia!"},
        {"question": "Come si serve?", "options": ["Capovolta", "Dritta", "A fette", "In coppette"], "correct": 0, "explanation": "Si capovolge per mostrare le mele!"},
        {"question": "Quale spezia si può aggiungere?", "options": ["Cannella", "Zenzero", "Noce moscata", "Chiodi garofano"], "correct": 0, "explanation": "La cannella è perfetta con le mele!"},
        {"question": "A che temperatura si cuoce?", "options": ["200°C", "180°C", "160°C", "220°C"], "correct": 0, "explanation": "200°C per caramellare bene!"},
    ],
    24: [  # Charlotte Royale
        {"question": "Come si fodera lo stampo?", "options": ["Con rotolo di biscuit", "Con savoiardi", "Con pan di spagna", "Con wafer"], "correct": 0, "explanation": "Le fette di rotolo creano il pattern!"},
        {"question": "Quale mousse si usa?", "options": ["Mousse ai frutti di bosco", "Mousse cioccolato", "Mousse vaniglia", "Mousse caffè"], "correct": 0, "explanation": "I frutti di bosco sono classici!"},
        {"question": "Cosa si spalma sul biscuit?", "options": ["Marmellata", "Crema", "Cioccolato", "Panna"], "correct": 0, "explanation": "La marmellata prima di arrotolare!"},
        {"question": "Come si serve la Charlotte?", "options": ["Fredda, sformata", "Calda", "Tiepida", "Congelata"], "correct": 0, "explanation": "Si serve fredda dopo averla sformata!"},
        {"question": "Quanto deve riposare in frigo?", "options": ["Tutta la notte", "2 ore", "30 minuti", "1 ora"], "correct": 0, "explanation": "Una notte per solidificare!"},
    ],
    25: [  # Croquembouche
        {"question": "Di cosa è fatta la piramide?", "options": ["Bignè", "Macarons", "Meringhe", "Biscotti"], "correct": 0, "explanation": "Centinaia di bignè impilati!"},
        {"question": "Con cosa si incollano i bignè?", "options": ["Caramello", "Cioccolato", "Glassa", "Crema"], "correct": 0, "explanation": "Il caramello caldo li salda!"},
        {"question": "Quale decorazione tradizionale?", "options": ["Zucchero filato", "Fiori di zucchero", "Praline", "Confetti"], "correct": 0, "explanation": "Lo zucchero filato è scenografico!"},
        {"question": "Per quale occasione è tipico?", "options": ["Matrimoni", "Compleanni", "Pasqua", "Natale"], "correct": 0, "explanation": "È il dolce nuziale francese!"},
        {"question": "Cosa significa 'croquembouche'?", "options": ["Scrocchia in bocca", "Torre di crema", "Dolce alto", "Bignè dorati"], "correct": 0, "explanation": "Dal francese 'croque en bouche'!"},
    ],
    26: [  # Torta Setteveli
        {"question": "Quanti strati ha la Setteveli?", "options": ["7 strati", "5 strati", "3 strati", "9 strati"], "correct": 0, "explanation": "7 veli come i 7 cieli!"},
        {"question": "Quale frutta secca si usa?", "options": ["Nocciole", "Mandorle", "Noci", "Pistacchi"], "correct": 0, "explanation": "Le nocciole sono protagoniste!"},
        {"question": "Quale base si usa?", "options": ["Dacquoise", "Biscotto", "Pan di spagna", "Frolla"], "correct": 0, "explanation": "La dacquoise alle nocciole!"},
        {"question": "Come si rifinisce?", "options": ["Glassa a specchio", "Zucchero a velo", "Cacao", "Panna"], "correct": 0, "explanation": "La glassa a specchio è perfetta!"},
        {"question": "Di quale città è tipica?", "options": ["Palermo", "Napoli", "Roma", "Milano"], "correct": 0, "explanation": "È una creazione palermitana!"},
    ],
    27: [  # Fraisier
        {"question": "Quale frutto è protagonista?", "options": ["Fragole", "Lamponi", "Mirtilli", "More"], "correct": 0, "explanation": "Le fragole sono essenziali!"},
        {"question": "Quale crema si usa?", "options": ["Crema mousseline", "Crema pasticcera", "Panna", "Crema al burro"], "correct": 0, "explanation": "La mousseline è perfetta!"},
        {"question": "Con cosa si ricopre sopra?", "options": ["Pasta di mandorle", "Fondant", "Panna", "Glassa"], "correct": 0, "explanation": "La pasta di mandorle verde!"},
        {"question": "Come si dispongono le fragole?", "options": ["Tagliate lungo i bordi", "Sopra", "Nel centro", "A dadini"], "correct": 0, "explanation": "Si vedono dalla cinta laterale!"},
        {"question": "Quale base si usa?", "options": ["Génoise", "Pan di spagna", "Biscuit", "Frolla"], "correct": 0, "explanation": "La génoise francese!"},
    ],
    28: [  # Torta Foresta Nera
        {"question": "Quale frutto si usa?", "options": ["Ciliegie", "Fragole", "Lamponi", "Mirtilli"], "correct": 0, "explanation": "Le ciliegie sono essenziali!"},
        {"question": "Quale liquore si usa?", "options": ["Kirsch", "Rum", "Cognac", "Amaretto"], "correct": 0, "explanation": "Il Kirsch (liquore di ciliegie)!"},
        {"question": "Di che colore è il pan di spagna?", "options": ["Scuro (al cacao)", "Chiaro", "Bicolore", "Giallo"], "correct": 0, "explanation": "Il cacao lo rende scuro!"},
        {"question": "Come si decora?", "options": ["Scaglie di cioccolato", "Granella", "Zucchero", "Cocco"], "correct": 0, "explanation": "Le scaglie sono iconiche!"},
        {"question": "Quale crema per farcire?", "options": ["Panna montata", "Crema pasticcera", "Ganache", "Crema al burro"], "correct": 0, "explanation": "La panna soffice e leggera!"},
    ],
    29: [  # Mousse al Cioccolato
        {"question": "Quanto cioccolato fondente serve?", "options": ["300g", "200g", "400g", "150g"], "correct": 0, "explanation": "300g per intensità!"},
        {"question": "Quante uova servono?", "options": ["6", "4", "3", "8"], "correct": 0, "explanation": "6 uova per volume!"},
        {"question": "Cosa si monta a neve?", "options": ["Albumi", "Panna", "Tuorli", "Latte"], "correct": 0, "explanation": "Gli albumi montati a neve!"},
        {"question": "Quanto riposa in frigo?", "options": ["4 ore", "1 ora", "30 minuti", "8 ore"], "correct": 0, "explanation": "Almeno 4 ore per compattare!"},
        {"question": "Cosa si può aggiungere per aromatizzare?", "options": ["Caffè", "Vaniglia", "Rum", "Tutti"], "correct": 3, "explanation": "Tutti sono ottimi abbinamenti!"},
    ],
    30: [  # Zuppa Inglese
        {"question": "Quante creme si usano?", "options": ["2 (gialla e cioccolato)", "1", "3", "4"], "correct": 0, "explanation": "Due creme alternate!"},
        {"question": "Quale liquore rosso si usa?", "options": ["Alchermes", "Grenadine", "Campari", "Aperol"], "correct": 0, "explanation": "L'alchermes è tradizionale!"},
        {"question": "Quale base si bagna?", "options": ["Pan di spagna", "Savoiardi", "Biscotti", "Brioche"], "correct": 0, "explanation": "Il pan di spagna assorbe bene!"},
        {"question": "Di quale regione è tipica?", "options": ["Emilia-Romagna", "Toscana", "Lazio", "Veneto"], "correct": 0, "explanation": "Dell'Emilia-Romagna!"},
        {"question": "Come si serve?", "options": ["Fredda in coppette", "Calda", "Tiepida", "Congelata"], "correct": 0, "explanation": "Fredda, come dolce al cucchiaio!"},
    ],
    # ==================== LIVELLO 31-40: ESPERTO ====================
    31: [  # Torta Dobos
        {"question": "Quanti strati di biscotto ha?", "options": ["6 strati", "4 strati", "8 strati", "5 strati"], "correct": 0, "explanation": "6 strati sottilissimi!"},
        {"question": "Come si decora lo strato superiore?", "options": ["Caramello tagliato", "Cioccolato", "Zucchero a velo", "Panna"], "correct": 0, "explanation": "Il caramello in spicchi!"},
        {"question": "Perché si taglia il caramello caldo?", "options": ["Perché indurisce subito", "Per estetica", "Per facilità", "Per gusto"], "correct": 0, "explanation": "Il caramello diventa durissimo!"},
        {"question": "Di quale paese è tipica?", "options": ["Ungheria", "Austria", "Germania", "Francia"], "correct": 0, "explanation": "È una torta ungherese!"},
        {"question": "Quale crema si usa?", "options": ["Crema al cioccolato", "Crema pasticcera", "Panna", "Ganache"], "correct": 0, "explanation": "La crema al cioccolato e burro!"},
    ],
    32: [  # Torta Margherita Farcita
        {"question": "Quale farina si usa?", "options": ["Fecola di patate", "Farina 00", "Farina Manitoba", "Amido mais"], "correct": 0, "explanation": "La fecola rende soffice!"},
        {"question": "Quante uova servono?", "options": ["6", "4", "3", "8"], "correct": 0, "explanation": "6 uova per leggerezza!"},
        {"question": "Con cosa si farcisce?", "options": ["Crema e fragole", "Solo panna", "Solo crema", "Cioccolato"], "correct": 0, "explanation": "Crema e fragole fresche!"},
        {"question": "Quale aroma si usa?", "options": ["Limone", "Vaniglia", "Arancia", "Mandorla"], "correct": 0, "explanation": "La scorza di limone è classica!"},
        {"question": "A che temperatura si cuoce?", "options": ["170°C", "180°C", "160°C", "190°C"], "correct": 0, "explanation": "170°C per una cottura delicata!"},
    ],
    33: [  # Pastiera Napoletana
        {"question": "Quale cereale si usa?", "options": ["Grano cotto", "Riso", "Orzo", "Farro"], "correct": 0, "explanation": "Il grano è tradizionale!"},
        {"question": "Per quale festa è tipica?", "options": ["Pasqua", "Natale", "Carnevale", "Ferragosto"], "correct": 0, "explanation": "È il dolce pasquale napoletano!"},
        {"question": "Quale acqua aromatizzata si usa?", "options": ["Acqua di fiori d'arancio", "Acqua di rose", "Acqua di menta", "Acqua semplice"], "correct": 0, "explanation": "I fiori d'arancio sono tipici!"},
        {"question": "Quale formaggio si usa?", "options": ["Ricotta", "Mascarpone", "Philadelphia", "Crescenza"], "correct": 0, "explanation": "La ricotta di pecora è tradizionale!"},
        {"question": "Cosa si aggiunge alla farcia?", "options": ["Canditi", "Uvetta", "Noci", "Cioccolato"], "correct": 0, "explanation": "I canditi arricchiscono!"},
    ],
    34: [  # Bûche de Noël
        {"question": "Quale forma ha?", "options": ["Tronco d'albero", "Rotonda", "Quadrata", "A cupola"], "correct": 0, "explanation": "Ricorda un ceppo natalizio!"},
        {"question": "Come si crea l'effetto corteccia?", "options": ["Con forchetta sulla ganache", "Con stampino", "Con glassa", "Con zucchero"], "correct": 0, "explanation": "I rebbi della forchetta creano le venature!"},
        {"question": "Per quale festa è tradizionale?", "options": ["Natale", "Pasqua", "Capodanno", "Epifania"], "correct": 0, "explanation": "È il dolce natalizio francese!"},
        {"question": "Quale base si usa?", "options": ["Biscuit roulé", "Pan di spagna", "Sfoglia", "Frolla"], "correct": 0, "explanation": "Il biscuit arrotolato!"},
        {"question": "Con cosa si decora?", "options": ["Meringhe e frutti rossi", "Solo zucchero", "Canditi", "Fiori"], "correct": 0, "explanation": "Funghi di meringa e agrifoglio di zucchero!"},
    ],
    35: [  # Tarte au Citron
        {"question": "Quale agrume è protagonista?", "options": ["Limone", "Arancia", "Pompelmo", "Lime"], "correct": 0, "explanation": "Il limone in quantità!"},
        {"question": "Come si cuoce la base?", "options": ["In bianco (copertura)", "Con la crema", "Senza cottura", "Al microonde"], "correct": 0, "explanation": "Prima in bianco, poi si aggiunge la crema!"},
        {"question": "Cosa si mette sopra?", "options": ["Meringa", "Panna", "Zucchero", "Frutta"], "correct": 0, "explanation": "La meringa italiana!"},
        {"question": "Come si brucia la meringa?", "options": ["Con cannello", "Al forno", "Con zucchero", "Non si brucia"], "correct": 0, "explanation": "Il cannello la dora!"},
        {"question": "Quale pasta per la base?", "options": ["Pasta frolla", "Pasta sfoglia", "Pasta brisée", "Pasta choux"], "correct": 0, "explanation": "La frolla dolce!"},
    ],
    36: [  # Entremets Exotic
        {"question": "Quale frutto tropicale si usa?", "options": ["Mango e passion fruit", "Banana", "Ananas", "Papaya"], "correct": 0, "explanation": "Mango e passion fruit sono perfetti insieme!"},
        {"question": "Come si rifinisce?", "options": ["Glassa a specchio", "Zucchero a velo", "Cacao", "Panna"], "correct": 0, "explanation": "La glassa lucida è caratteristica!"},
        {"question": "Quale base si usa?", "options": ["Biscotto al cocco", "Pan di spagna", "Frolla", "Biscuit"], "correct": 0, "explanation": "Il cocco richiama i tropici!"},
        {"question": "Dove si assembla?", "options": ["In cerchio d'acciaio", "In stampo classico", "A mano libera", "In pirofila"], "correct": 0, "explanation": "Il cerchio dà precisione!"},
        {"question": "Come si sforma?", "options": ["Con cannello sul bordo", "Capovolgendo", "Tagliando", "Con acqua calda"], "correct": 0, "explanation": "Il calore scioglie i bordi!"},
    ],
    37: [  # Croissant
        {"question": "Quante pieghe si fanno?", "options": ["3 pieghe", "2 pieghe", "4 pieghe", "5 pieghe"], "correct": 0, "explanation": "3 pieghe a libro!"},
        {"question": "Quanto burro per la sfogliatura?", "options": ["280g", "150g", "200g", "350g"], "correct": 0, "explanation": "Tanto burro per la sfogliatura!"},
        {"question": "Quale lievito si usa?", "options": ["Lievito di birra", "Lievito chimico", "Bicarbonato", "Pasta madre"], "correct": 0, "explanation": "Il lievito di birra è essenziale!"},
        {"question": "Quanto deve lievitare prima di cuocere?", "options": ["2-3 ore", "30 minuti", "1 ora", "5 ore"], "correct": 0, "explanation": "La lievitazione finale è cruciale!"},
        {"question": "A che temperatura si cuociono?", "options": ["200-220°C", "180°C", "160°C", "240°C"], "correct": 0, "explanation": "Alto calore per sfogliare!"},
    ],
    38: [  # Torta Red Velvet
        {"question": "Quale colorante si usa?", "options": ["Rosso", "Blu", "Verde", "Giallo"], "correct": 0, "explanation": "Il rosso vibrante è iconico!"},
        {"question": "Quale latticino si usa nell'impasto?", "options": ["Buttermilk", "Panna", "Yogurt", "Latte normale"], "correct": 0, "explanation": "Il buttermilk dà morbidezza!"},
        {"question": "Quale frosting è tradizionale?", "options": ["Cream cheese", "Ganache", "Panna", "Glassa"], "correct": 0, "explanation": "Il frosting al formaggio!"},
        {"question": "Di quale paese è originaria?", "options": ["Stati Uniti", "Inghilterra", "Francia", "Italia"], "correct": 0, "explanation": "È americana, del Sud!"},
        {"question": "Cosa reagisce col colorante?", "options": ["Bicarbonato e aceto", "Solo lievito", "Solo burro", "Solo uova"], "correct": 0, "explanation": "La reazione chimica intensifica il rosso!"},
    ],
    39: [  # Meringata
        {"question": "Quanti albumi servono?", "options": ["6", "4", "3", "8"], "correct": 0, "explanation": "6 albumi per una bella struttura!"},
        {"question": "Quanto zucchero per albume?", "options": ["Circa 50g", "Circa 30g", "Circa 70g", "Circa 100g"], "correct": 0, "explanation": "50-60g per albume è la proporzione!"},
        {"question": "A che temperatura si cuoce?", "options": ["100°C", "150°C", "180°C", "80°C"], "correct": 0, "explanation": "Bassa temperatura per asciugare!"},
        {"question": "Con cosa si farcisce?", "options": ["Panna e frutti di bosco", "Solo crema", "Solo cioccolato", "Marmellata"], "correct": 0, "explanation": "Panna e frutti sono classici!"},
        {"question": "Come deve essere la meringa dentro?", "options": ["Morbida", "Croccante", "Liquida", "Gommosa"], "correct": 0, "explanation": "Morbida dentro, croccante fuori!"},
    ],
    40: [  # Torta Tre Latti
        {"question": "Quali sono i tre latti?", "options": ["Condensato, evaporato, panna", "Latte, panna, yogurt", "Burro, latte, panna", "Tre tipi di latte"], "correct": 0, "explanation": "La combinazione dei tre latti!"},
        {"question": "Di quale paese è tipica?", "options": ["Messico/America Latina", "Italia", "Francia", "Spagna"], "correct": 0, "explanation": "È latinoamericana!"},
        {"question": "Come si bagna la torta?", "options": ["Bucando e versando", "A pennello", "Immergendo", "A spruzzo"], "correct": 0, "explanation": "Si buca e si versa il mix!"},
        {"question": "Quale base si usa?", "options": ["Pan di spagna", "Biscotto", "Frolla", "Sfoglia"], "correct": 0, "explanation": "Il pan di spagna assorbe bene!"},
        {"question": "Con cosa si decora?", "options": ["Panna e cannella", "Cioccolato", "Frutta", "Glassa"], "correct": 0, "explanation": "Panna e una spolverata di cannella!"},
    ],
    # ==================== LIVELLO 41-50: MAESTRO ====================
    41: [  # Wedding Cake 3 Piani
        {"question": "Quanti piani ha?", "options": ["3 piani", "2 piani", "4 piani", "5 piani"], "correct": 0, "explanation": "3 piani maestosi!"},
        {"question": "Con cosa si ricopre?", "options": ["Fondant", "Panna", "Ganache", "Glassa"], "correct": 0, "explanation": "Il fondant per una superficie liscia!"},
        {"question": "Cosa sostiene i piani?", "options": ["Supporti interni", "Solo torta", "Crema", "Colonne visibili"], "correct": 0, "explanation": "I supporti nascosti sono essenziali!"},
        {"question": "Che tipo di decorazioni?", "options": ["Fiori di zucchero", "Solo panna", "Caramello", "Cioccolato"], "correct": 0, "explanation": "I fiori di zucchero sono eleganti!"},
        {"question": "Quanto tempo prima si prepara?", "options": ["2-3 giorni", "Il giorno stesso", "1 settimana", "1 mese"], "correct": 0, "explanation": "Serve tempo per assemblare tutto!"},
    ],
    42: [  # Pièce Montée
        {"question": "Di cosa è composta?", "options": ["Centinaia di bignè", "Macarons", "Cupcakes", "Tartellette"], "correct": 0, "explanation": "Tantissimi bignè incollati!"},
        {"question": "Cosa lega i bignè?", "options": ["Caramello caldo", "Cioccolato", "Crema", "Pasta di zucchero"], "correct": 0, "explanation": "Il caramello li salda!"},
        {"question": "Quale decorazione si usa?", "options": ["Zucchero tirato/fiori", "Solo confetti", "Panna", "Canditi"], "correct": 0, "explanation": "Decorazioni artistiche in zucchero!"},
        {"question": "Per quale occasione?", "options": ["Matrimoni", "Compleanni", "Battesimi", "Lauree"], "correct": 0, "explanation": "È tradizionale per i matrimoni francesi!"},
        {"question": "Quale forma classica ha?", "options": ["Conica/piramide", "Sferica", "Cubica", "Cilindrica"], "correct": 0, "explanation": "A cono o piramide!"},
    ],
    43: [  # Torta Moderna Art
        {"question": "Quale tecnica di glassatura si usa?", "options": ["Glassa a specchio", "Fondant", "Panna", "Glassa reale"], "correct": 0, "explanation": "La glassa a specchio è moderna!"},
        {"question": "Quali stampi si usano?", "options": ["Stampi in silicone 3D", "Teglie classiche", "Stampini carta", "Forme libere"], "correct": 0, "explanation": "Il silicone crea forme innovative!"},
        {"question": "Come si decora?", "options": ["Con tecniche d'avanguardia", "Tradizionale", "Solo panna", "Solo frutta"], "correct": 0, "explanation": "Creatività e innovazione!"},
        {"question": "Quale struttura interna?", "options": ["Mousse e inserti", "Solo pan di spagna", "Solo crema", "Solo biscotto"], "correct": 0, "explanation": "Strati di mousse con inserti a sorpresa!"},
        {"question": "A che temperatura si assembla?", "options": ["Congelata", "Fredda", "Ambiente", "Calda"], "correct": 0, "explanation": "Si congela per sformare con la glassa!"},
    ],
    44: [  # Petit Fours Assortiti
        {"question": "Che dimensione hanno?", "options": ["Piccoli (1-2 bocconi)", "Medi", "Grandi", "Variabili"], "correct": 0, "explanation": "Piccoli e preziosi, un morso!"},
        {"question": "Quanti tipi si preparano?", "options": ["Almeno 4-5 varietà", "1 tipo", "2 tipi", "3 tipi"], "correct": 0, "explanation": "L'assortimento è caratteristico!"},
        {"question": "Con cosa si ricoprono?", "options": ["Glasse colorate", "Solo zucchero", "Niente", "Panna"], "correct": 0, "explanation": "Glasse colorate e lucide!"},
        {"question": "Quale base si usa?", "options": ["Génoise tagliata", "Pasta frolla", "Biscotti", "Meringhe"], "correct": 0, "explanation": "La génoise in piccoli pezzi!"},
        {"question": "Come si presentano?", "options": ["In eleganti scatole", "Su piatto", "In ciotola", "Sfusi"], "correct": 0, "explanation": "La presentazione è fondamentale!"},
    ],
    45: [  # Scultura Cioccolato
        {"question": "Quanto cioccolato serve?", "options": ["3kg o più", "500g", "1kg", "2kg"], "correct": 0, "explanation": "Tanto cioccolato per sculture grandi!"},
        {"question": "A che temperatura si lavora?", "options": ["Temperato (30-32°C)", "Caldo (50°C)", "Freddo (20°C)", "Ambiente"], "correct": 0, "explanation": "La tempera è fondamentale!"},
        {"question": "Quale strumento per scaldare?", "options": ["Pistola termica", "Microonde", "Forno", "Bagnomaria"], "correct": 0, "explanation": "La pistola per saldare i pezzi!"},
        {"question": "Come si creano i pezzi?", "options": ["Con stampi in silicone", "A mano", "Con stampante 3D", "Tagliando"], "correct": 0, "explanation": "Gli stampi danno precisione!"},
        {"question": "Come si colorano i dettagli?", "options": ["Coloranti liposolubili", "Coloranti ad acqua", "Vernici", "Non si colorano"], "correct": 0, "explanation": "I coloranti liposolubili per cioccolato!"},
    ],
    46: [  # Torta Decostruita
        {"question": "Cosa significa 'decostruita'?", "options": ["Elementi separati nel piatto", "Torta rotta", "Senza forma", "Non cotta"], "correct": 0, "explanation": "Gli elementi classici presentati in modo nuovo!"},
        {"question": "Quale tecnica moderna si usa?", "options": ["Sferificazione", "Cottura tradizionale", "Frittura", "Bollitura"], "correct": 0, "explanation": "La sferificazione crea sfere di sapore!"},
        {"question": "Cosa si usa per le texture?", "options": ["Agar agar e alginato", "Solo gelatina", "Solo amido", "Niente"], "correct": 0, "explanation": "Addensanti moderni per texture innovative!"},
        {"question": "Come si presenta?", "options": ["Nel piatto, artisticamente", "In ciotola", "Su torta tradizionale", "In bicchiere"], "correct": 0, "explanation": "La presentazione è artistica!"},
        {"question": "Quale cucina ha ispirato questa tecnica?", "options": ["Cucina molecolare", "Cucina classica", "Pasticceria francese", "Cucina italiana"], "correct": 0, "explanation": "La gastronomia molecolare!"},
    ],
    47: [  # Torta Gravity
        {"question": "Quale effetto crea?", "options": ["Caramelle che cadono", "Torta che vola", "Panna che esce", "Cioccolato che cola"], "correct": 0, "explanation": "L'effetto anti-gravità è magico!"},
        {"question": "Cosa sostiene le caramelle?", "options": ["Struttura nascosta", "Colla alimentare", "Crema densa", "Fili invisibili"], "correct": 0, "explanation": "Un supporto interno nascosto!"},
        {"question": "Cosa si usa tipicamente?", "options": ["M&M's o Smarties", "Frutta", "Fiori", "Biscotti"], "correct": 0, "explanation": "Le caramelle colorate sono scenografiche!"},
        {"question": "Da dove 'cadono' le caramelle?", "options": ["Da un contenitore sospeso", "Dal soffitto", "Da una nuvola", "Da un bicchiere"], "correct": 0, "explanation": "Un barattolo o tazza sospesa!"},
        {"question": "Per chi è ideale?", "options": ["Feste bambini", "Matrimoni", "Funerali", "Conferenze"], "correct": 0, "explanation": "Perfetta per stupire i bambini!"},
    ],
    48: [  # Number Cake
        {"question": "Quale forma ha?", "options": ["Numero o lettera", "Rotonda", "Quadrata", "A cuore"], "correct": 0, "explanation": "Il numero dell'età o le iniziali!"},
        {"question": "Quale base si usa?", "options": ["Pasta sablée", "Pan di spagna", "Sfoglia", "Biscuit"], "correct": 0, "explanation": "La sablée è croccante e perfetta!"},
        {"question": "Come si farcisce?", "options": ["Crema a ciuffetti", "Crema spalmata", "Niente crema", "Solo frutta"], "correct": 0, "explanation": "Ciuffetti con sac-à-poche!"},
        {"question": "Con cosa si decora?", "options": ["Frutta, fiori, macarons", "Solo zucchero", "Solo cioccolato", "Niente"], "correct": 0, "explanation": "Decorazioni ricche e colorate!"},
        {"question": "Quanti strati di numeri?", "options": ["2 strati", "1 strato", "3 strati", "4 strati"], "correct": 0, "explanation": "Due strati identici sovrapposti!"},
    ],
    49: [  # Semifreddo Strati
        {"question": "A che temperatura si serve?", "options": ["Semi-congelato", "Temperatura ambiente", "Caldo", "Completamente congelato"], "correct": 0, "explanation": "Semi-congelato per la giusta consistenza!"},
        {"question": "Quanti strati diversi?", "options": ["3 o più gusti", "1 gusto", "2 gusti", "Nessuno"], "correct": 0, "explanation": "Almeno 3 gusti diversi!"},
        {"question": "Quale base croccante si usa?", "options": ["Croccante alle nocciole", "Biscotto", "Wafer", "Niente"], "correct": 0, "explanation": "Il croccante dà contrasto!"},
        {"question": "Come si sforma?", "options": ["Scaldando lo stampo", "Capovolgendo", "Tagliando", "Con acqua fredda"], "correct": 0, "explanation": "Un attimo sul fuoco scioglie i bordi!"},
        {"question": "Dove si congela?", "options": ["In stampo a plumcake", "In coppette", "In piatto", "In teglia"], "correct": 0, "explanation": "Lo stampo rettangolare dà la forma!"},
    ],
    50: [  # Il Capolavoro Finale
        {"question": "Quanti ingredienti può avere?", "options": ["25 o più", "5-10", "10-15", "Infiniti"], "correct": 0, "explanation": "Un dolce che usa tutto ciò che hai imparato!"},
        {"question": "Quale ingrediente segreto serve?", "options": ["Amore e passione", "Oro alimentare", "Tartufo", "Zafferano"], "correct": 0, "explanation": "L'ingrediente più importante! ❤️"},
        {"question": "Chi può creare questo dolce?", "options": ["Solo un vero Maestro", "Chiunque", "Solo chef stellati", "Solo pasticceri"], "correct": 0, "explanation": "Chi completa tutto il percorso!"},
        {"question": "Quanto tempo richiede?", "options": ["Giorni di lavoro", "1 ora", "30 minuti", "2 ore"], "correct": 0, "explanation": "Un capolavoro richiede tempo!"},
        {"question": "Cosa rappresenta questo dolce?", "options": ["Il culmine del percorso", "Solo un dolce", "Un test", "Una sfida"], "correct": 0, "explanation": "Sei diventato un Maestro! 🏆"},
    ],
}

# ==================== HELPER FUNCTIONS ====================

def get_quiz(recipe_id):
    """Ritorna le 5 domande per la ricetta specificata"""
    return QUIZ_DATA.get(recipe_id, [])

def calculate_score(correct_answers):
    """
    Calcola XP in base a risposte corrette
    correct_answers: numero di risposte corrette (0-5)
    """
    score_map = {5: 100, 4: 80, 3: 60, 2: 40, 1: 20, 0: 0}
    return score_map.get(correct_answers, 0)

def get_all_quiz_ids():
    """Ritorna tutti gli ID delle ricette con quiz disponibili"""
    return list(QUIZ_DATA.keys())

