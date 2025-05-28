#!/usr/bin/env python3import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie


from models import Company, Dev

if __name__ == '__main__':
    engine = create_engine(f'sqlite:///{db_path}')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()

