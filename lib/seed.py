#!/usr/bin/env python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

# Absolute path for SQLite DB
db_path = os.path.join(os.path.dirname(__file__), 'freebies.db')
engine = create_engine(f'sqlite:///{db_path}')
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

# Create companies
companies = [
    Company(name="DevWorks", founding_year=2010),
    Company(name="CodeBase", founding_year=2018)
]
session.add_all(companies)

# Create developers
devs = [
    Dev(name="Charlie"),
    Dev(name="Diana"),
    Dev(name="Eve")
]
session.add_all(devs)

# Commit companies and devs to get IDs
session.commit()

# Create freebies
freebies = [
    Freebie(item_name="Backpack", value=30, dev=devs[2], company=companies[0]),
    Freebie(item_name="Notebook", value=5, dev=devs[1], company=companies[1]),
    Freebie(item_name="Water Bottle", value=12, dev=devs[0], company=companies[1]),
    Freebie(item_name="Socks", value=8, dev=devs[0], company=companies[0]),
    Freebie(item_name="Cap", value=14, dev=devs[2], company=companies[0]),
    Freebie(item_name="Keychain", value=3, dev=devs[1], company=companies[0]),
    Freebie(item_name="USB Drive", value=20, dev=devs[2], company=companies[1])
]
session.add_all(freebies)

# Final commit
session.commit()

print("Database seeded successfully with data!")
