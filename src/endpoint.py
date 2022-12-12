from fastapi import FastAPI

app = FastAPI()

# テスト
@app.get("/test/")
async def test():
    return 'テスト'
