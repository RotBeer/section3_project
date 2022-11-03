import csv
import psycopg2

# ref https://www.kaggle.com/datasets/whenamancodes/customer-personality-analysis

host = 'localhost'
port = '5432'
user = 'postgres'
password = '1234'
database = 'postgres'

conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS test')
cur.execute("""CREATE TABLE test (
                Id INTEGER PRIMARY KEY NOT NULL,
                Year_Birth INTEGER,
                Education VARCHAR,
                Marital_Status VARCHAR,
                Income INTEGER,
                Kidhome INTEGER,
                Teenhome INTEGER,
                Dt_Customer VARCHAR,
                Recency INTEGER,
                Complain INTEGER,

                MntWines INTEGER,
                MntFruits INTEGER,
                MntMeatProducts INTEGER,
                MntFishProducts INTEGER,
                MntSweetProducts INTEGER,
                MntGoldProds INTEGER,

                NumDealsPurchases INTEGER,
                AcceptedCmp1 INTEGER,
                AcceptedCmp2 INTEGER,
                AcceptedCmp3 INTEGER,
                AcceptedCmp4 INTEGER,
                AcceptedCmp5 INTEGER,
                Response INTEGER,

                NumWebPurchases INTEGER,
                NumCatalogPurchases INTEGER,
                NumStorePurchases INTEGER,
                NumWebVisitsMonth INTEGER
                );
            """)
cols = ['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Income',
        'Kidhome', 'Teenhome', 'Dt_Customer', 'Recency', 'Complain',
        'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
        'NumDealsPurchases', 'AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3',
        'AcceptedCmp4', 'AcceptedCmp5', 'Response',
        'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth']
cols_str = ', '.join(cols)
cols_s_len = ['%s'] * len(cols)
cols_s = ', '.join(cols_s_len)
with open('marketing_campaign.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:        
        vals = [row[col] for col in cols]
        vals = list(map(lambda x: x if x != '' else None, vals))
        cur.execute(f'INSERT INTO test ({cols_str}) VALUES ({cols_s})', vals)

conn.commit()
conn.close()