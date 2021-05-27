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
               (uid TEXT UNIQUE, password TEXT NOT NULL, PRIMARY KEY (uid))''')

cur.execute('''DROP TABLE IF EXISTS User_info''')
cur.execute('''CREATE TABLE User_info
               (uid TEXT UNIQUE, uname TEXT NOT NULL, budget INTEGER, PRIMARY KEY (uid), FOREIGN KEY (uid) REFERENCES User_login)''')

cur.execute('''DROP TABLE IF EXISTS User_interests''')
cur.execute('''CREATE TABLE User_interests
               (uid TEXT UNIQUE, code TEXT, PRIMARY KEY (uid), FOREIGN KEY (uid) REFERENCES User_login)''')



cur.execute('''DROP TABLE IF EXISTS User_holding''')
cur.execute('''CREATE TABLE User_holding
               (uid TEXT UNIQUE, code TEXT, num INTEGER, avg_price REAL, PRIMARY KEY (uid,code), FOREIGN KEY (code) REFERENCES Coins)''')



cur.execute('''DROP TABLE IF EXISTS Organization''')
cur.execute('''CREATE TABLE Organization
               (oid TEXT UNIQUE, oname TEXT, PRIMARY KEY (oid))''')

cur.execute('''DROP TABLE IF EXISTS Organization_info''')
cur.execute('''CREATE TABLE Organization_info
               (oname TEXT UNIQUE, owner TEXT, located_in TEXT, PRIMARY KEY (oname), FOREIGN KEY (oname) REFERENCES Organization)''')



cur.execute('''DROP TABLE IF EXISTS Administrated_by''')
cur.execute('''CREATE TABLE Administrated_by
               (oid TEXT UNIQUE, code TEXT, PRIMARY KEY (oid,code),FOREIGN KEY (oid) REFERENCES Organization,FOREIGN KEY (code) REFERENCES Coins)''')



cur.execute('''DROP TABLE IF EXISTS Company''')
cur.execute('''CREATE TABLE Company
               (cid TEXT UNIQUE, cname TEXT, PRIMARY KEY (cid))''')

cur.execute('''DROP TABLE IF EXISTS Company_info''')
cur.execute('''CREATE TABLE Company_info
               (cname TEXT UNIQUE, owner TEXT, located_in TEXT, PRIMARY KEY (cname), FOREIGN KEY (cname) REFERENCES Organization)''')



cur.execute('''DROP TABLE IF EXISTS Collaborates_with''')
cur.execute('''CREATE TABLE Collaborates_with
               (cid Text UNIQUE, code Text, PRIMARY KEY (cid,code),FOREIGN KEY (cid) REFERENCES Company,FOREIGN KEY (code) REFERENCES Coins)''')

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