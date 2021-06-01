# Dukyoung Eom dukyoung.eom@stonybrook.edu
import os
import sqlite3

print(os.path.abspath(os.path.dirname(__file__)))

conn = sqlite3.connect('cryptoCurrencies.db')

cur = conn.cursor()

# Create tables
cur.execute('''DROP TABLE IF EXISTS Coins''')
cur.execute('''CREATE TABLE Coins
               (name TEXT UNIQUE, code TEXT UNIQUE, PRIMARY KEY (code))''')

cur.execute('''DROP TABLE IF EXISTS Coins_category''')
cur.execute('''CREATE TABLE Coins_category
               (name TEXT UNIQUE, category TEXT, PRIMARY KEY (name), FOREIGN KEY (name) REFERENCES Coins)''')

cur.execute('''DROP TABLE IF EXISTS Coins_info''')
cur.execute('''CREATE TABLE Coins_info
               (name TEXT UNIQUE, market_cap REAL, global INTEGER, founder TEXT, PRIMARY KEY (name), FOREIGN KEY (name) REFERENCES Coins)''')

cur.execute('''DROP TABLE IF EXISTS User_login''')
cur.execute('''CREATE TABLE User_login
               (uid INTEGER UNIQUE, uname TEXT NOT NULL, password TEXT NOT NULL, PRIMARY KEY (uid))''')

cur.execute('''DROP TABLE IF EXISTS User_info''')
cur.execute('''CREATE TABLE User_info
               (uid INTEGER UNIQUE, budget INTEGER, PRIMARY KEY (uid), FOREIGN KEY (uid) REFERENCES User_login)''')

cur.execute('''DROP TABLE IF EXISTS User_interests''')
cur.execute('''CREATE TABLE User_interests
               (uid INTEGER, code TEXT, PRIMARY KEY (uid,code), FOREIGN KEY (uid) REFERENCES User_login, FOREIGN KEY (code) REFERENCES Coins)''')

cur.execute('''DROP TABLE IF EXISTS User_holding''')
cur.execute('''CREATE TABLE User_holding
               (uid INTEGER, code TEXT, num REAL, avg_price REAL, PRIMARY KEY (uid,code), FOREIGN KEY (code) REFERENCES Coins)''')

cur.execute('''DROP TABLE IF EXISTS Transaction_history''')
cur.execute('''CREATE TABLE Transaction_history
               (uid INTEGER, code TEXT, num REAL, price REAL, date TEXT, trade_type INTEGER, completed INTEGER, PRIMARY KEY (uid,code), FOREIGN KEY (uid) REFERENCES User_login, FOREIGN KEY (code) REFERENCES Coins)''')

cur.execute('''DROP TABLE IF EXISTS Organization''')
cur.execute('''CREATE TABLE Organization
               (oid TEXT UNIQUE, oname TEXT, PRIMARY KEY (oid))''')

cur.execute('''DROP TABLE IF EXISTS Organization_info''')
cur.execute('''CREATE TABLE Organization_info   
               (oname TEXT UNIQUE, owner TEXT, located_in TEXT, PRIMARY KEY (oname), FOREIGN KEY (oname) REFERENCES Organization)''')

cur.execute('''DROP TABLE IF EXISTS Administrated_by''')
cur.execute('''CREATE TABLE Administrated_by
               (oid TEXT UNIQUE, code TEXT, PRIMARY KEY (oid,code),FOREIGN KEY (oid) REFERENCES Organization, FOREIGN KEY (code) REFERENCES Coins)''')

cur.execute('''DROP TABLE IF EXISTS Company''')
cur.execute('''CREATE TABLE Company
               (cid TEXT UNIQUE, cname TEXT, PRIMARY KEY (cid))''')

cur.execute('''DROP TABLE IF EXISTS Company_info''')
cur.execute('''CREATE TABLE Company_info
               (cname TEXT UNIQUE, owner TEXT, located_in TEXT, PRIMARY KEY (cname), FOREIGN KEY (cname) REFERENCES Organization)''')

cur.execute('''DROP TABLE IF EXISTS Collaborates_with''')
cur.execute('''CREATE TABLE Collaborates_with
               (cid Text UNIQUE, code Text, PRIMARY KEY (cid,code),FOREIGN KEY (cid) REFERENCES Company,FOREIGN KEY (code) REFERENCES Coins)''')
# Triggers
cur.execute('''CREATE TRIGGER new_user AFTER INSERT ON User_login
BEGIN
 INSERT INTO User_info VALUES (new.uid, 10000000);
 END;''')

cur.execute('''CREATE TRIGGER insert_transaction1 AFTER INSERT ON Transaction_history
WHEN new.code NOT IN (SELECT code FROM User_holding WHERE uid = new.uid)
BEGIN
     INSERT INTO User_holding (uid,code,num,avg_price) VALUES (new.uid, new.code, new.num, new.price);
END;''')

# Insert rows of data

# Coins
cur.execute("INSERT INTO Coins VALUES ('Bitcoin','KRW-BTC')")
cur.execute("INSERT INTO Coins VALUES ('Ethereum','KRW-ETH')")
cur.execute("INSERT INTO Coins VALUES ('Bitcoin Cash','KRW-BCH')")
cur.execute("INSERT INTO Coins VALUES ('Litecoin','KRW-LTC')")
cur.execute("INSERT INTO Coins VALUES ('Bitcoin SV','KRW-BSV')")
cur.execute("INSERT INTO Coins VALUES ('Ethereum Classic','KRW-ETC')")
cur.execute("INSERT INTO Coins VALUES ('Bitcoin Gold','KRW-BTG')")
cur.execute("INSERT INTO Coins VALUES ('NEO','KRW-NEO')")
cur.execute("INSERT INTO Coins VALUES ('Strike','KRW-STRK')")
cur.execute("INSERT INTO Coins VALUES ('Chainlink','KRW-LINK')")
cur.execute("INSERT INTO Coins VALUES ('Polkadot','KRW-DOT')")
cur.execute("INSERT INTO Coins VALUES ('Bitcoin Cash ABC','KRW-BCHA')")
cur.execute("INSERT INTO Coins VALUES ('Augur','KRW-REP')")
cur.execute("INSERT INTO Coins VALUES ('Waves','KRW-WAVES')")
cur.execute("INSERT INTO Coins VALUES ('Flow','KRW-FLOW')")
cur.execute("INSERT INTO Coins VALUES ('Cosmos','KRW-ATOM')")
cur.execute("INSERT INTO Coins VALUES ('SteemDollars','KRW-SBD')")
cur.execute("INSERT INTO Coins VALUES ('Qtum','KRW-QTUM')")
cur.execute("INSERT INTO Coins VALUES ('GAS','KRW-GAS')")
cur.execute("INSERT INTO Coins VALUES ('TON','KRW-TON')")
cur.execute("INSERT INTO Coins VALUES ('Theta Token','KRW-THETA')")
cur.execute("INSERT INTO Coins VALUES ('EOS','KRW-EOS')")
cur.execute("INSERT INTO Coins VALUES ('Serum','KRW-SRM')")
cur.execute("INSERT INTO Coins VALUES ('OmiseGo','KRW-OMG')")
cur.execute("INSERT INTO Coins VALUES ('Cobak Token','KRW-CBK')")
cur.execute("INSERT INTO Coins VALUES ('Lisk','KRW-LSK')")
cur.execute("INSERT INTO Coins VALUES ('Axie Infinity','KRW-AXS')")
cur.execute("INSERT INTO Coins VALUES ('Alpha Quark Token','KRW-AQT')")
cur.execute("INSERT INTO Coins VALUES ('Tezos','KRW-XTZ')")
cur.execute("INSERT INTO Coins VALUES ('Kava','KRW-KAVA')")
cur.execute("INSERT INTO Coins VALUES ('Dawn Protocol','KRW-DAWN')")
cur.execute("INSERT INTO Coins VALUES ('Stratis','KRW-STRAX')")
cur.execute("INSERT INTO Coins VALUES ('Swipe','KRW-SXP')")
cur.execute("INSERT INTO Coins VALUES ('Metal','KRW-MTL')")
cur.execute("INSERT INTO Coins VALUES ('Kyber Network','KRW-KNC')")
cur.execute("INSERT INTO Coins VALUES ('Ada','KRW-ADA')")
cur.execute("INSERT INTO Coins VALUES ('Komodo','KRW-KMD')")
cur.execute("INSERT INTO Coins VALUES ('Pundi X','KRW-PUNDIX')")
cur.execute("INSERT INTO Coins VALUES ('IOTA','KRW-IOTA')")
cur.execute("INSERT INTO Coins VALUES ('Ark','KRW-ARK')")
cur.execute("INSERT INTO Coins VALUES ('Enjin','KRW-ENJ')")
cur.execute("INSERT INTO Coins VALUES ('Ontology','KRW-ONT')")
cur.execute("INSERT INTO Coins VALUES ('PayCoin','KRW-PCI')")
cur.execute("INSERT INTO Coins VALUES ('Mil.k','KRW-MLK')")
cur.execute("INSERT INTO Coins VALUES ('Ripple','KRW-XRP')")
cur.execute("INSERT INTO Coins VALUES ('Storj','KRW-STORJ')")
cur.execute("INSERT INTO Coins VALUES ('0x Protocol','KRW-ZRX')")
cur.execute("INSERT INTO Coins VALUES ('Stacks','KRW-STX')")
cur.execute("INSERT INTO Coins VALUES ('Decentraland','KRW-MANA')")
cur.execute("INSERT INTO Coins VALUES ('Groestlcoin','KRW-GRS')")
cur.execute("INSERT INTO Coins VALUES ('Basic Attention Token','KRW-BAT')")
cur.execute("INSERT INTO Coins VALUES ('AdEx','KRW-ADX')")
cur.execute("INSERT INTO Coins VALUES ('Steem','KRW-STEEM')")
cur.execute("INSERT INTO Coins VALUES ('ONG','KRW-ONG')")
cur.execute("INSERT INTO Coins VALUES ('DMarket','KRW-DMT')")
cur.execute("INSERT INTO Coins VALUES ('Lumen','KRW-XLM')")
cur.execute("INSERT INTO Coins VALUES ('Hive','KRW-HIVE')")
cur.execute("INSERT INTO Coins VALUES ('Dogecoin','KRW-DOGE')")
cur.execute("INSERT INTO Coins VALUES ('Civic','KRW-CVC')")
cur.execute("INSERT INTO Coins VALUES ('Maro','KRW-MARO')")
cur.execute("INSERT INTO Coins VALUES ('Golem','KRW-GLM')")
cur.execute("INSERT INTO Coins VALUES ('Chiliz','KRW-CHZ')")
cur.execute("INSERT INTO Coins VALUES ('Aelf','KRW-ELF')")
cur.execute("INSERT INTO Coins VALUES ('The Sandbox','KRW-SAND')")
cur.execute("INSERT INTO Coins VALUES ('PlayDapp','KRW-PLA')")
cur.execute("INSERT INTO Coins VALUES ('Power ledger','KRW-POWR')")
cur.execute("INSERT INTO Coins VALUES ('Theta Fuel','KRW-TFUEL')")
cur.execute("INSERT INTO Coins VALUES ('Einsteinium','KRW-EMC2')")
cur.execute("INSERT INTO Coins VALUES ('Aergo','KRW-AERGO')")
cur.execute("INSERT INTO Coins VALUES ('Polymath','KRW-POLY')")
cur.execute("INSERT INTO Coins VALUES ('Hedera Hashgraph','KRW-HBAR')")
cur.execute("INSERT INTO Coins VALUES ('Ardor','KRW-ARDR')")
cur.execute("INSERT INTO Coins VALUES ('NEM','KRW-XEM')")
cur.execute("INSERT INTO Coins VALUES ('HUNT','KRW-HUNT')")
cur.execute("INSERT INTO Coins VALUES ('BORA','KRW-BORA')")
cur.execute("INSERT INTO Coins VALUES ('Solve.Care','KRW-SOLVE')")
cur.execute("INSERT INTO Coins VALUES ('dKargo','KRW-DKA')")
cur.execute("INSERT INTO Coins VALUES ('WAX','KRW-WAXP')")
cur.execute("INSERT INTO Coins VALUES ('Crypto.com Chain','KRW-CRO')")
cur.execute("INSERT INTO Coins VALUES ('Zilliqa','KRW-ZIL')")
cur.execute("INSERT INTO Coins VALUES ('Ankr','KRW-ANKR')")
cur.execute("INSERT INTO Coins VALUES ('VeChain','KRW-VET')")
cur.execute("INSERT INTO Coins VALUES ('LBRY Credits','KRW-LBC')")
cur.execute("INSERT INTO Coins VALUES ('Status Network Token','KRW-SNT')")
cur.execute("INSERT INTO Coins VALUES ('FirmaChain','KRW-FCT2')")
cur.execute("INSERT INTO Coins VALUES ('Moss Coin','KRW-MOC')")
cur.execute("INSERT INTO Coins VALUES ('Metadium','KRW-META')")
cur.execute("INSERT INTO Coins VALUES ('Humanscape','KRW-HUM')")
cur.execute("INSERT INTO Coins VALUES ('Sentinel Protocol','KRW-UPP')")
cur.execute("INSERT INTO Coins VALUES ('TRON','KRW-TRX')")
cur.execute("INSERT INTO Coins VALUES ('Orbs','KRW-ORBS')")
cur.execute("INSERT INTO Coins VALUES ('Ignis','KRW-IGNIS')")
cur.execute("INSERT INTO Coins VALUES ('Loom Network','KRW-LOOM')")
cur.execute("INSERT INTO Coins VALUES ('JUST','KRW-JST')")
cur.execute("INSERT INTO Coins VALUES ('PIXEL','KRW-PXL')")
cur.execute("INSERT INTO Coins VALUES ('SOMESING','KRW-SSX')")
cur.execute("INSERT INTO Coins VALUES ('MediBloc','KRW-MED')")
cur.execute("INSERT INTO Coins VALUES ('Standard Tokenization Protocol','KRW-STPT')")
cur.execute("INSERT INTO Coins VALUES ('Endor','KRW-EDR')")
cur.execute("INSERT INTO Coins VALUES ('Lambda','KRW-LAMB')")
cur.execute("INSERT INTO Coins VALUES ('Quiztok','KRW-QTCON')")
cur.execute("INSERT INTO Coins VALUES ('IOST','KRW-IOST')")
cur.execute("INSERT INTO Coins VALUES ('StormX','KRW-STMX')")
cur.execute("INSERT INTO Coins VALUES ('Siacoin','KRW-SC')")
cur.execute("INSERT INTO Coins VALUES ('QuarkChain','KRW-QKC')")
cur.execute("INSERT INTO Coins VALUES ('MVL','KRW-MVL')")
cur.execute("INSERT INTO Coins VALUES ('Observer','KRW-OBSR')")
cur.execute("INSERT INTO Coins VALUES ('12SHIPS','KRW-TSHP')")
cur.execute("INSERT INTO Coins VALUES ('Everipedia','KRW-IQ')")
cur.execute("INSERT INTO Coins VALUES ('Refereum','KRW-RFR')")
cur.execute("INSERT INTO Coins VALUES ('Thunder Token','KRW-TT')")
cur.execute("INSERT INTO Coins VALUES ('Mainframe','KRW-MFT')")
cur.execute("INSERT INTO Coins VALUES ('Carry Protocol','KRW-CRE')")
cur.execute("INSERT INTO Coins VALUES ('AhaToken','KRW-AHT')")
cur.execute("INSERT INTO Coins VALUES ('MovieBloc','KRW-MBL')")
cur.execute("INSERT INTO Coins VALUES ('BitTorrent','KRW-BTT')")
cur.execute("INSERT INTO Coins VALUES ('Icon','KRW-ICX')")

cur.execute("INSERT INTO Coins_category VALUES ('Bitcoin', 'Major')")
cur.execute("INSERT INTO Coins_category VALUES ('Ethereum', 'Major')")
cur.execute("INSERT INTO Coins_category VALUES ('Ripple', 'Major')")
cur.execute("INSERT INTO Coins_category VALUES ('Ada', 'Major')")
cur.execute("INSERT INTO Coins_category VALUES ('Polkadot', 'Major')")
cur.execute("INSERT INTO Coins_category VALUES ('Litecoin', 'Major')")
cur.execute("INSERT INTO Coins_category VALUES ('Bitcoin Cash', 'Major')")
cur.execute("INSERT INTO Coins_category VALUES ('Lumen', 'Major')")
cur.execute("INSERT INTO Coins_category VALUES ('NEM', 'Major')")
cur.execute("INSERT INTO Coins_category VALUES ('VeChain', 'Semi-Major')")
cur.execute("INSERT INTO Coins_category VALUES ('Theta Token', 'Semi-Major')")
cur.execute("INSERT INTO Coins_category VALUES ('EOS', 'Semi-Major')")
cur.execute("INSERT INTO Coins_category VALUES ('TRON', 'Semi-Major')")
cur.execute("INSERT INTO Coins_category VALUES ('NEO', 'Semi-Major')")
cur.execute("INSERT INTO Coins_category VALUES ('Bitcoin SV', 'Semi-Major')")
cur.execute("INSERT INTO Coins_category VALUES ('Crypto.com Chain', 'Semi-Major')")
cur.execute("INSERT INTO Coins_category VALUES ('Tezos', 'Semi-Major')")
cur.execute("INSERT INTO Coins_category VALUES ('FirmaChain', 'Minor')")
cur.execute("INSERT INTO Coins_category VALUES ('SOMESING', 'Minor')")
cur.execute("INSERT INTO Coins_category VALUES ('TON', 'Minor')")
cur.execute("INSERT INTO Coins_category VALUES ('HUNT', 'Minor')")
cur.execute("INSERT INTO Coins_category VALUES ('Observer', 'Minor')")
cur.execute("INSERT INTO Coins_category VALUES ('DMarket', 'Minor')")
cur.execute("INSERT INTO Coins_category VALUES ('Aergo', 'Minor')")
cur.execute("INSERT INTO Coins_category VALUES ('MovieBloc', 'Minor')")
cur.execute("INSERT INTO Coins_category VALUES ('Endor', 'Minor')")

cur.execute("INSERT INTO Coins_info VALUES ('Bitcoin', 712455673236488, 1, 'Satoshi Nakamoto')")
cur.execute("INSERT INTO Coins_info VALUES ('Ethereum', 293267100926272, 1, 'Vitalik Buterin')")
cur.execute("INSERT INTO Coins_info VALUES ('Ada', 48696914147108, 1, 'Charles Hoskinson')")
cur.execute("INSERT INTO Coins_info VALUES ('Dogecoin', 42338028270288, 1, 'Billy Markus')")
cur.execute("INSERT INTO Coins_info VALUES ('Ripple', 42034953830860, 1, 'Jed McCaleb')")
cur.execute("INSERT INTO Coins_info VALUES ('Polkadot', 20291064852073, 1, 'Gavin Wood')")
cur.execute("INSERT INTO Coins_info VALUES ('Litecoin', 12012074735486, 1, 'Charlie Lee')")
cur.execute("INSERT INTO Coins_info VALUES ('Chainlink', 11970254157179, 1, 'Sergey Nazaro')")
cur.execute("INSERT INTO Coins_info VALUES ('Lumen', 9112518943390, 1, 'Jed McCaleb')")
cur.execute("INSERT INTO Coins_info VALUES ('Ethereum Classic', 8129642261641, 1, 'Gavin Wood')")
cur.execute("INSERT INTO Coins_info VALUES ('Theta Token', 6905244024759, 1, 'Mitch Liu')")
cur.execute("INSERT INTO Coins_info VALUES ('VeChain', 6866625937215, 1, 'Sunny Lu')")

cur.execute("INSERT INTO User_login VALUES ( 1,'deom', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 2,'triggertest', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 3,'Nielsen', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 4,'Lindsay', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 5,'Britney', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 6,'Ravinder', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 7,'Roosevelt', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 8,'Simmons', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 9,'Mercado', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 10,'Georgiana', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 11,'Tonisha ', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 12,'Mclellan', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 13,'Mcculloch', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 14,'Sweeney', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 15,'Benitez', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 16,'Mcgowan', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 17,'Calderon', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 18,'Barajas', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 19,'Kristina', 'test')")
cur.execute("INSERT INTO User_login VALUES ( 20,'Carrillo', 'test')")




cur.execute("INSERT INTO User_holding VALUES ( 1, 'KRW-MLK', 828.73502754, 2516)")
cur.execute("INSERT INTO User_holding VALUES ( 1, 'KRW-CRO', 1269.77360992, 306)")
cur.execute("INSERT INTO User_holding VALUES ( 2, 'KRW-DOGE', 38.98372839, 50)")
cur.execute("INSERT INTO User_holding VALUES ( 2, 'KRW-NEO', 63.36231144, 68780)")
cur.execute("INSERT INTO User_holding VALUES ( 2, 'KRW-WAVES', 142.72947923, 16135)")
cur.execute("INSERT INTO User_holding VALUES ( 3, 'KRW-GAS', 48.39473823, 11441)")
cur.execute("INSERT INTO User_holding VALUES ( 3, 'KRW-QTUM', 138.83649204, 14983)")
cur.execute("INSERT INTO User_holding VALUES ( 4, 'KRW-LSK', 569.37485920, 4038)")
cur.execute("INSERT INTO User_holding VALUES ( 4, 'KRW-EOS', 34.82648301, 8367)")
cur.execute("INSERT INTO User_holding VALUES ( 4, 'KRW-BTC', 0.00012412, 42748392)")
cur.execute("INSERT INTO User_holding VALUES ( 5, 'KRW-ETC', 73.93829420, 83082)")
cur.execute("INSERT INTO User_holding VALUES ( 5, 'KRW-BTC', 0.00003245, 42748392)")
cur.execute("INSERT INTO User_holding VALUES ( 6, 'KRW-STRK', 45.03948329, 52092)")
cur.execute("INSERT INTO User_holding VALUES ( 6, 'KRW-LINK', 23.93874623, 30483)")
cur.execute("INSERT INTO User_holding VALUES ( 7, 'KRW-ARK', 142.98372938, 1543)")
cur.execute("INSERT INTO User_holding VALUES ( 7, 'KRW-IOTA', 74.47382039, 1503)")
cur.execute("INSERT INTO User_holding VALUES ( 7, 'KRW-PCI', 34.92839543, 1305)")
cur.execute("INSERT INTO User_holding VALUES ( 8, 'KRW-ETC', 34.02789382, 83082)")
cur.execute("INSERT INTO User_holding VALUES ( 8, 'KRW-BTC', 0.00045136, 42748392)")
cur.execute("INSERT INTO User_holding VALUES ( 9, 'KRW-ADA',302.93872839, 1734)")
cur.execute("INSERT INTO User_holding VALUES ( 9, 'KRW-ENJ', 103.87398423, 1603)")
cur.execute("INSERT INTO User_holding VALUES ( 10, 'KRW-MLK', 452.98472938, 2516)")
cur.execute("INSERT INTO User_holding VALUES ( 10, 'KRW-DOGE', 290.33890935, 50 )")

cur.execute("INSERT INTO Transaction_history VALUES (2, 'KRW-BTC', 1, 35000000, '2021-06-01', 1, 1)")
# Save (commit) the changes
conn.commit()

cur = conn.cursor()
#for row in cur.execute('SELECT * FROM roles ORDER BY id'):
#    print(row)

#for row in cur.execute('SELECT * FROM users ORDER BY id'):
#    print(row)

# To see what these names are
print(__file__)
print(__name__)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()