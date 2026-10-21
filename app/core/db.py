
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import config

ca_path = Path(config.DB_SSL_CA).expanduser().resolve()

if not ca_path.is_file():
    raise FileNotFoundError(
        f"MySQL CA certificate not found: {ca_path}"
    )

engine = create_engine(
    config.DATABASE_URL,
    connect_args={
        "ssl_ca": str(ca_path),
        "ssl_verify_cert": True,
        "ssl_verify_identity": True,
        "connection_timeout": 10,
        "use_pure": True,
    },
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    pool_recycle=3600,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
