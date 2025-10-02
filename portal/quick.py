from utils.browser import get_page

def open_tamamlayici_saglik():
    page = get_page()
    try:
        page.wait_for_selector("text=Tamamlayıcı Sağlık", timeout=8000)
        page.click("text=Tamamlayıcı Sağlık")
        page.wait_for_load_state("networkidle")
        return "✅ Tamamlayıcı Sağlık sayfası açıldı."
    except Exception as e:
        return f"❌ Hata: {e}"

def open_kasko():
    page = get_page()
    try:
        page.wait_for_selector("text=Kasko", timeout=8000)
        page.click("text=Kasko")
        page.wait_for_load_state("networkidle")
        return "✅ Kasko sayfası açıldı."
    except Exception as e:
        return f"❌ Hata: {e}"

def open_trafik():
    page = get_page()
    try:
        page.wait_for_selector("text=Trafik", timeout=8000)
        page.click("text=Trafik")
        page.wait_for_load_state("networkidle")
        return "✅ Trafik sayfası açıldı."
    except Exception as e:
        return f"❌ Hata: {e}"

def open_seyahat_saglik():
    page = get_page()
    try:
        page.wait_for_selector("text=Seyahat Sağlık", timeout=8000)
        page.click("text=Seyahat Sağlık")
        page.wait_for_load_state("networkidle")
        return "✅ Seyahat Sağlık sayfası açıldı."
    except Exception as e:
        return f"❌ Hata: {e}"

def open_dask():
    page = get_page()
    try:
        page.wait_for_selector("text=DASK", timeout=8000)
        page.click("text=DASK")
        page.wait_for_load_state("networkidle")
        return "✅ DASK sayfası açıldı."
    except Exception as e:
        return f"❌ Hata: {e}"

def open_konut():
    page = get_page()
    try:
        page.wait_for_selector("text=Konut", timeout=8000)
        page.click("text=Konut")
        page.wait_for_load_state("networkidle")
        return "✅ Konut sayfası açıldı."
    except Exception as e:
        return f"❌ Hata: {e}"

def open_ferdi_kaza():
    page = get_page()
    try:
        page.wait_for_selector("text=Ferdi Kaza", timeout=8000)
        page.click("text=Ferdi Kaza")
        page.wait_for_load_state("networkidle")
        return "✅ Ferdi Kaza sayfası açıldı."
    except Exception as e:
        return f"❌ Hata: {e}"
