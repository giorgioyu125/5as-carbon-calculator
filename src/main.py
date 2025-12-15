import sys

# DATI

"""
Dati-fattori
Informazioni condivise per il calcolo del carico delle emissioni per attivita' svolta
"""

transport = { # values in kg_co2eq / P.km
    "bus": {
        "media": 0.11945,
        "autobus_urbano": {
            "media": 0.11945,
            "gas": {
                "media": 0.1069,
                "piccolo": 0.1464,
                "medio": 0.1034,
                "grande": 0.0709,
            },
            "diesel": {
                "media": 0.1320,
                "piccolo": 0.1716,
                "medio": 0.1338,
                "grande": 0.0905,
            }
        },
        "autobus_extraurbano": 0.0465,
        "filobus": 0.0296,
    },

    "automobili": {
        "media": 0.1564,     # Very approximative, the provided mean is not an arithmetic mean
        "gas": {
            "media": 0.12646,
            "piccolo": 0.1033,
            "medio": 0.1233,
            "grande": 0.1528,
        },
        "diesel": {
            "media": 0.189,
            "piccolo": 0.1109,
            "medio": 0.1322,
            "grande": 0.1757,
        },
        "gasolio": {
            "media": 0.186,
            "piccolo": 0.1297,
            "medio": 0.1506,
            "grande": 0.2004,
        }
    },

    "aereo": {
        "media": 0.263,
        "lunga_percorrenza": {
            "media": 0.2372,
            "economy": 0.1895,
            "business": 0.3914,
            "first": 0.6031,
        },
        "breve_percorrenza": {
            "media": 0.3192,
            "economy": 0.2918,
            "business": 0.4488,
        }
    },

    "treno": {
        "media": 0.11286,
        "a_piedi": 0.11286,
        "in_macchina":  0.12952,
    },

    "motociclo": {
        "media": 0.1636,
        "piccolo": 0.121,
        "medio": 0.1548,
        "grande": 0.2036,
    },

    "biciclette": {
        "media": 0.00845,
        "E-bike": 0.0113,
        "normale": 0.0056,
    }
}

electricity = { # kg_co2eq / kWh
    "ES": 0.17709,
    "CN": 0.5572,
    "PM": 0.79231,
    "IN": 0.7132,
    "TO": 0.69327,
    "MS": 0.79231,
    "TT": 0.42871,
    "HT": 0.68827,
    "BA": 0.9708,
    "BO": 0.26967,
    "MQ": 0.79231,
    "RU": 0.34362,
    "VC": 0.59423,
    "CR": 0.01573,
    "SE": 0.00731,
    "CK": 0.47539,
    "NR": 0.79231,
    "UA": 0.20375,
    "ML": 0.50868,
    "GY": 0.70497,
    "TZ": 0.36013,
    "BJ": 0.7593,
    "PY": 0.00143,
    "CH": 0.00278,
    "GL": 0.13205,
    "GH": 0.33563,
    "NE": 0.70428,
    "KP": 0.14784,
    "AS": 0.79231,
    "PK": 0.32737,
    "BR": 0.1295,
    "EH": 0.79231,
    "NZ": 0.13111,
    "RE": 0.55147,
    "AZ": 0.5212,
    "JP": 0.4615,
    "NC": 0.68384,
    "GN": 0.2166,
    "NI": 0.36238,
    "MM": 0.32444,
    "LR": 0.33587,
    "YE": 0.58073,
    "MN": 0.80174,
    "RW": 0.31692,
    "GP": 0.61058,
    "NL": 0.34089,
    "SR": 0.39223,
    "ME": 0.64377,
    "AL": 0.0,
    "ZW": 0.39607,
    "DJ": 0.79231,
    "KR": 0.4113,
    "CD": 0.00215,
    "GW": 0.79231,
    "DZ": 0.44513,
    "SD": 0.26763,
    "LB": 0.62887,
    "UG": 0.02414,
    "PR": 0.77062,
    "SI": 0.27329,
    "CF": 0.0,
    "SZ": 0.05916,
    "VU": 0.56977,
    "KZ": 0.64995,
    "ZA": 0.8665,
    "BE": 0.13882,
    "LS": 0.0,
    "NO": 0.00832,
    "MA": 0.64226,
    "TM": 0.42542,
    "MG": 0.53016,
    "MV": 0.73229,
    "BN": 0.66003,
    "VI": 0.76967,
    "BH": 0.42529,
    "RO": 0.31148,
    "KM": 0.79231,
    "IE": 0.35216,
    "CM": 0.29822,
    "PL": 0.87761,
    "HR": 0.25469,
    "FK": 0.39616,
    "MZ": 0.10527,
    "FO": 0.49048,
    "KW": 0.42512,
    "MK": 0.53802,
    "TW": 0.55746,
    "BB": 0.73307,
    "VE": 0.19141,
    "KI": 0.79231,
    "IT": 0.36425,
    "BG": 0.55371,
    "TD": 0.76675,
    "CZ": 0.76413,
    "AF": 0.1241,
    "AT": 0.14723,
    "AO": 0.18537,
    "NG": 0.31727,
    "HN": 0.38705,
    "AE": 0.41789,
    "JO": 0.35336,
    "MT": 0.42689,
    "MR": 0.58159,
    "KN": 0.7563,
    "SL": 0.07546,
    "CG": 0.35343,
    "GA": 0.43964,
    "LV": 0.14807,
    "BS": 0.79231,
    "IQ": 0.46178,
    "SC": 0.6948,
    "PF": 0.53198,
    "SN": 0.5428,
    "NA": 0.03809,
    "KG": 0.08876,
    "TR": 0.4261,
    "FI": 0.0953,
    "CI": 0.40343,
    "BT": 0.0,
    "NP": 0.0,
    "SS": 0.77841,
    "BF": 0.68818,
    "AM": 0.18481,
    "GE": 0.10128,
    "US": 0.40706,
    "UY": 0.07148,
    "SO": 0.71501,
    "KY": 0.7706,
    "DM": 0.60588,
    "SK": 0.17622,
    "SV": 0.16363,
    "UZ": 0.46613,
    "LT": 0.2711,
    "SY": 0.53139,
    "BY": 0.35708,
    "LU": 0.08493,
    "GR": 0.3784,
    "AG": 0.74704,
    "SB": 0.79231,
    "TH": 0.446,
    "SG": 0.408,
    "PS": 0.4758,
    "EE": 0.75353,
    "TN": 0.40675,
    "VG": 0.79231,
    "CU": 0.63716,
    "ZM": 0.06617,
    "GB": 0.22499,
    "MD": 0.69981,
    "SA": 0.6142,
    "GD": 0.79231,
    "MX": 0.3,
    "ID": 0.7848,
    "LK": 0.48882,
    "WS": 0.51267,
    "HK": 0.68,
    "LA": 0.23817,
    "MU": 0.65073,
    "MO": 0.42542,
    "CL": 0.32345,
    "AU": 0.77,
    "ER": 0.7747,
    "DE": 0.44912,
    "PT": 0.15641,
    "CA": 0.11,
    "LC": 0.79231,
    "PG": 0.5825,
    "MW": 0.12332,
    "PE": 0.22693,
    "DO": 0.57048,
    "DK": 0.18731,
    "KH": 0.41038,
    "FR": 0.06207,
    "GM": 0.79231,
    "LY": 0.53136,
    "QA": 0.42515,
    "EG": 0.46029,
    "AR": 0.2881,
    "GF": 0.26934,
    "IS": 0.00017,
    "BD": 0.56719,
    "HU": 0.27037,
    "PA": 0.18387,
    "ET": 0.00059,
    "TC": 0.79231,
    "TJ": 0.06352,
    "CO": 0.1464,
    "CV": 0.66906,
    "MY": 0.53834,
    "OM": 0.42358,
    "GU": 0.75748,
    "ST": 0.71308,
    "IR": 0.45473,
    "BZ": 0.50149,
    "BW": 0.85966,
    "PH": 0.60756,
    "BI": 0.24284,
    "VN": 0.37789,
    "RS": 0.96323,
    "IL": 0.51764,
    "KE": 0.08078,
    "GT": 0.29645,
    "CY": 0.65493,
    "GQ": 0.54681,
    "FJ": 0.28849,
    "TG": 0.49698,
    "JM": 0.53139,
    "AW": 0.66452,
    "EC": 0.19018
}

heating_fuel = { # kg_co2eq / kg_fuel
    "carbone": 0.35,
    "gas": 0.18,
    "LPG": 0.21,
    "benzina": 0.27,
    "pellet_legno": 0.01074,
    "trucioli_legno": 0.01074,
}

foods = { # kg_co2eq / kg_cibo
    "manzo_bestiame": 100,
    "manzo_media": 71,
    "cioccolato": 34,
    "caffe'": 29,
    "gamberetti": 27,
    "manzo_dalatte": 33,
    "formaggio": 24,
    "carne_suino": 12,
    "pollo": 10,
    "pesce_allevato": 14,
    "uova": 5,
    "tofu": 3,
    "avocado": 2.5,
    "pomodori": 2,
    "riso": 4.5,
    "fagiolo": 2,
    "mais": 2,
    "piselli": 1,
    "banane": 1,
    "patate": 0.5,
    "mele": 0.4,
    "noccioline": 0.4,
    "vegetali_radici": 0.4,
}

from enum import Enum

class Categoria(Enum):
    TRASPORTI = "trasporti"
    ELETTRICITA = "elettricita'"
    RISCALDAMENTO = "riscaldamento"
    CIBO = "cibo"

global_data = {
    Categoria.TRASPORTI: transport,
    Categoria.ELETTRICITA: electricity,
    Categoria.RISCALDAMENTO: heating_fuel,
    Categoria.CIBO: foods,
}

# CODICE

KEYS_MEDIA = ['media', 'manzo_media']

default_after_question = "(premere invio per la media)" # Questo viene messo alla fine di ogni query
                                                        # I valori medi sono presenti per tutto
p_cibo = "Quanti kg di"

completed = "(Sezione completata.)",
not_complete = "(Sezione saltata o incompleta.)"

queries = {
    "trasporti": {
        "_titolo": "\n=== SEZIONE TRASPORTI ===",
        "_input_unit": "km",
        "bus": {
            1: "Qual'e' il tipo di bus che vuoi considerare? (autobus_urbano, autobus_extraurbano, filobus)",
            2: "Quale tipo di combustibile usava il bus? (gas, diesel)",
            3: "Qual'e' la taglia del bus che vuoi considerare? (piccolo, medio, grande)",
        },
        "automobili": {
            1: "Qual'e' il tipo di carburante che vuoi considerare? (gas, diesel, gasolio)",
            2: "Qual'e' la dimensione della macchina da considerare? (piccolo, medio, grande)"
        },
        "aereo": {
            1: "Di che lunghezza si vuole considerare i viaggi in aereo? (lunga_percorrenza, breve_percorrenza)", # Nel caso l'utente abbia scelto la seconda non puo' selezionare first-class
            2: "In che classe si sono svolti questi viaggi? (economy, business, first)",
        },
        "treno": {
            1: "Dei viaggi in treno si vuole considerare in macchina o a piedi? (a_piedi, in_macchina)"
        },
        "motociclo": {
            1: "Qual'e' la taglia della moticicletta di cui si vuole considerare? (piccolo, medio, grande)"
        },
        "biciclette": {
            1: "Quale tipo di bicicletta si vuole considerare? (E-bike, normale)"
        }
    },

    "cibo": {
        "_titolo": "\n=== SEZIONE ALIMENTAZIONE ===",
        "_input_unit": "kg_cibo",

        "manzo_bestiame": f"{p_cibo} manzo (da allevamento)?", "manzo_media": f"{p_cibo} manzo (media generica, da inserire solo se non si hanno abbastanza informazioni)?",
        "cioccolato": f"{p_cibo} cioccolato?",
        "caffe'": f"{p_cibo} caffè?",
        "gamberetti": f"{p_cibo} gamberetti?",
        "manzo_dalatte": f"{p_cibo} carne da vacche da latte?",
        "formaggio": f"{p_cibo} formaggio?",
        "carne_suino": f"{p_cibo} carne di maiale?",
        "pollo": f"{p_cibo} pollo?",
        "pesce_allevato": f"{p_cibo} pesce d'allevamento?",
        "uova": f"{p_cibo} uova?",
        "tofu": f"{p_cibo} tofu?",
        "avocado": f"{p_cibo} avocado?",
        "pomodori": f"{p_cibo} pomodori?",
        "riso": f"{p_cibo} riso?",
        "fagiolo": f"{p_cibo} fagioli?",
        "mais": f"{p_cibo} mais?",
        "piselli": f"{p_cibo} piselli?",
        "banane": f"{p_cibo} banane?",
        "patate": f"{p_cibo} patate?",
        "mele": f"{p_cibo} mele?",
        "noccioline": f"{p_cibo} noccioline?",
        "vegetali_radici": f"{p_cibo} vegetali a radice (carote, rape)?",
    },

    "riscaldamento": {
        "_titolo": "\n=== SEZIONE RISCALDAMENTO ===",
        "_domanda": "Che combustibile usi per il riscaldamento? (Inserisci i kg consumati)",
        "_input_unit": "kg_combustibile",
        "carbone": "Carbone",
        "gas": "Gas naturale",
        "LPG": "GPL",
        "benzina": "Benzina (generatori)",
        "pellet_legno": "Pellet",
        "trucioli_legno": "Legna/Trucioli"
    },

    "elettricita'": {
        "_titolo": "\n=== SEZIONE ENERGIA ===",
        "_domanda": "Seleziona il tuo paese per il calcolo dei kWh (IT, DE etc.):",
        "_input_unit": "kWh",
    },

}

def safe_input(prompt: str) -> str:
    while True:
        try:
            val = input(prompt).strip()
            if val.lower() == 'exit':
                sys.exit(0)
            return val
        except (KeyboardInterrupt, EOFError):
            print("\nNon puoi uscire così. Digita 'exit'.")

def choice_is_no(text):
    return text.strip().lower() in ['n', 'no', 'non so', 'bho', '0']

def input_num(prompt: str) -> float:
    s = safe_input(prompt).strip().replace(',', '.') or '0'
    try:
        return float(s)
    except ValueError:
        return 0.0

def ask_queries() -> float:
    print(f"Benvenuto! Calcoliamo la tua impronta ecologica in C02eq.")
    result: float = 0.0

    # Trasporti
    print(queries["trasporti"]["_titolo"])
    for types, questions in queries["trasporti"].items():
        if types.startswith("_"):
            continue

        if choice_is_no(safe_input(f"vuoi inserire dati per '{types}'? (s/n) > ")):
            continue

        root_data = transport[types]

        while True:
            n = 1
            saved_values = []
            while True:
                if n not in questions:
                    break
                testo_domanda = questions[n]
                risposta = safe_input(f"{testo_domanda} > ")
                saved_values.append(risposta)
                n += 1

            km = input_num("quanti km? > ")

            current_node = root_data
            for val in saved_values:
                if not isinstance(current_node, dict):
                    break
                try:
                    current_node = current_node[val]
                except KeyError:
                    print(f"   (Info: '{val}' non trovato, uso la media corrispondente)")
                    current_node = current_node.get("media", list(current_node.values())[0])

            while isinstance(current_node, dict):
                current_node = current_node.get("media", list(current_node.values())[0])

            parziale = current_node * km
            result += parziale
            print(f"  -> Aggiunti {parziale:.2f} kgCO2")

            if choice_is_no(safe_input(f"Vuoi aggiungere un altro viaggio in '{types}'? (s/n) > ")):
                break

    # Cibo
    print(queries["cibo"]["_titolo"])
    for food_type, question in queries["cibo"].items():
        if choice_is_no(safe_input(f"\nvuoi inserire dati per la categoria cibo? (s/n) > ")):
            break

        if food_type.startswith("_"):
            continue

        kg = input_num(f"{question} (kg) > ")
        if kg <= 0:
            continue

        coefficiente = foods[food_type]
        parziale = kg * coefficiente
        result += parziale

        print(f"  -> Aggiunti {parziale:.2f} kgCO2")

    # Riscaldamento
    print(queries["riscaldamento"]["_titolo"])
    for fuel_type, label in queries["riscaldamento"].items():
        if fuel_type.startswith("_"):
            continue

        kg = input_num(f"{label} (kg) > ")

        if kg <= 0:
            continue

        coefficiente = heating_fuel[fuel_type]
        parziale = kg * coefficiente
        result += parziale

        print(f"  -> Aggiunti {parziale:.2f} kgCO2")

    # Elettricità
    print(queries["elettricita'"]["_titolo"])
    paese = safe_input("Codice paese (IT, DE, FR...; Invio per IT) > ").upper()
    coefficiente = electricity.get(paese, electricity["IT"])

    kwh = input_num("quanti kWh consumi? > ")

    if kwh > 0:
        parziale = kwh * coefficiente
        result += parziale
        print(f"  -> Aggiunti {parziale:.2f} kgCO2")


    return result

def main() -> None:
    totale = ask_queries()

    print("\n" + "=" * 40)
    print(f"TOTALE EMISSIONI: {totale:.2f} kgCO2eq")
    print("=" * 40)

if __name__ == "__main__":
    main()
