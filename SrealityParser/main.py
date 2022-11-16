from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from crawler import crawl
from html_translate import port_run


def main():
    apartments = crawl()
    print(f"{5432:#^60}")  # port sql

    engine = create_engine("postgresql://luxonis:2022@database:5432/apartments_db")
    db = scoped_session(sessionmaker(bind=engine))
    if engine.dialect.has_table(engine.connect(), table_name="apartments500"):
        db.execute("DROP TABLE apartments500")
    db.execute("CREATE TABLE apartments500 (id INTEGER NOT NULL, name VARCHAR NOT NULL, locality VARCHAR NOT NULL, "
                "price_czk INTEGER NOT NULL, photo VARCHAR NOT NULL, PRIMARY KEY (id));")

    for idx in range(len(apartments)):
        row = "INSERT INTO apartments500 (id, name, locality, price_czk, photo) " \
              "VALUES ('{id}', '{name}', '{locality}', '{price}', '{img_url}');".format(id=idx+1, **apartments[idx])
        db.execute(row)
    db.commit()
    db.close()

    # port: 8080
    port_run(apartments=apartments)

if __name__ == "__main__":
    main()

