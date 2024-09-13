import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from db_config import db_config

# Asynchronous database connection URL
DATABASE_URL = f"postgresql+asyncpg://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"   

# Create the asynchronous engine
async_engine = create_async_engine(DATABASE_URL, echo=False)

# Create an asynchronous session factory
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

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

async def fetch_count(query):
    async with AsyncSessionLocal() as session:
        result = await session.execute(query)
        return result.scalar()

async def fetch_parallel_queries(queries):
    tasks = [fetch_count(query) for query in queries.values()]
    results = await asyncio.gather(*tasks)  # Run all tasks concurrently
    for key, count in zip(queries.keys(), results):
        print(f"{key.capitalize()}: {count}")

# Entry point for running asynchronous tasks
if __name__ == "__main__":
    asyncio.run(fetch_parallel_queries(queries))
