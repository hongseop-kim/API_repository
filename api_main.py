from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# MySQL 데이터베이스 설정
DATABASE_URL = "mysql+pymysql://hong:1234@database-1.cn482mka8n93.ap-northeast-2.rds.amazonaws.com:3306/test"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 모델 정의
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

# DB 초기화
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Dependency: 세션 생성 및 해제
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD endpoints
@app.post("/items/")
def create_item(name: str, description: str, db: SessionLocal = Depends(get_db)):
    item = Item(name=name, description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
