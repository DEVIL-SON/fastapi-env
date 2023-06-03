from fastapi import FastAPI
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World from Saurabh Vaishya"}

@app.get("/test")
async def root():
    return {"message":"this is test"}
    
