from fastapi import Fastapi

app = Fastapi()

@app.get("/")
async def hellod():
    return {"a" : "bc"}