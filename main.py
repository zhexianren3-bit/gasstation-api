from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "加油站API"}
@app.get("/nearby")
def nearby(lat: float = 39.9, lng: float = 116.4):
    return {"success": True, "stations": [{"name": "加油站1", "price": 7.5}]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
