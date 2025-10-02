from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool
from portal import quick

app = FastAPI()

@app.get("/")
async def home():
    return {"status": "Sigorta Scraper çalışıyor"}

@app.get("/quick/tamamlayici")
async def quick_tamamlayici():
    return {"result": await run_in_threadpool(quick.open_tamamlayici_saglik)}

@app.get("/quick/kasko")
async def quick_kasko():
    return {"result": await run_in_threadpool(quick.open_kasko)}

@app.get("/quick/trafik")
async def quick_trafik():
    return {"result": await run_in_threadpool(quick.open_trafik)}

@app.get("/quick/seyahat")
async def quick_seyahat():
    return {"result": await run_in_threadpool(quick.open_seyahat_saglik)}

@app.get("/quick/dask")
async def quick_dask():
    return {"result": await run_in_threadpool(quick.open_dask)}

@app.get("/quick/konut")
async def quick_konut():
    return {"result": await run_in_threadpool(quick.open_konut)}

@app.get("/quick/ferdi-kaza")
async def quick_ferdi_kaza():
    return {"result": await run_in_threadpool(quick.open_ferdi_kaza)}
