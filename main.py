from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from db_config import engine

Session = sessionmaker(bind=engine)
session = Session()

queries = {
    'no_changes': text("""
        SELECT COUNT(*) FROM (
            SELECT * FROM source INTERSECT SELECT * FROM target
        ) AS common_rows;
    """),
    'inserts': text("""
        SELECT COUNT(*) FROM target t
        WHERE NOT EXISTS (SELECT 1 FROM source s WHERE s.id = t.id);
    """),
    'deletes': text("""
        SELECT COUNT(*) FROM source s
        WHERE NOT EXISTS (SELECT 1 FROM target t WHERE t.id = s.id);
    """),
    'updates': text("""
        SELECT COUNT(*) FROM source s
        JOIN target t ON s.id = t.id
        WHERE (s.name != t.name OR s.flag != t.flag);
    """),
}

def fetch_count(query):
    result = session.execute(query)
    return result.scalar()

# Fetch counts for each comparison type
counts = {key: fetch_count(query) for key, query in queries.items()}

# Print the counts for each category
for key, count in counts.items():
    print(f"{key.capitalize()}: {count}")

session.close()
