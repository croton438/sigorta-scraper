from utils.browser import get_page

async def open_trafik():
    page = await get_page()
    try:
        await page.wait_for_selector("text=Trafik", timeout=5000)
        await page.click("text=Trafik")
        await page.wait_for_load_state("networkidle")
        return "✅ Sompo Trafik sayfası açıldı."
    except Exception as e:
        return f"⚠️ Hata: {e}"

async def open_kasko():
    page = await get_page()
    try:
        await page.wait_for_selector("text=Kasko", timeout=5000)
        await page.click("text=Kasko")
        await page.wait_for_load_state("networkidle")
        return "✅ Sompo Kasko sayfası açıldı."
    except Exception as e:
        return f"⚠️ Hata: {e}"
