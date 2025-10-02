from playwright.sync_api import sync_playwright
import os
import threading
import asyncio
from concurrent.futures import ThreadPoolExecutor
import queue

STORAGE_FILE = "quick_storage.json"

_playwright = None
_browser = None
_page = None
_browser_thread = None
_command_queue = queue.Queue()
_result_queue = queue.Queue()
_lock = threading.Lock()

def _browser_thread_main():
    """Ayrı bir thread'de Playwright çalıştır"""
    global _playwright, _browser, _page
    
    try:
        # Bu thread'de yeni bir event loop oluştur
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # Windows subprocess sorununu çöz
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
        print("🔄 Playwright başlatılıyor...")
        _playwright = sync_playwright().start()
        print("🔄 Browser açılıyor...")
        _browser = _playwright.chromium.launch(headless=False, slow_mo=200)
        
        if os.path.exists(STORAGE_FILE):
            print("🔄 Context oluşturuluyor...")
            _context = _browser.new_context(storage_state=STORAGE_FILE)
            _page = _context.new_page()
            print("🔄 Sayfaya gidiliyor...")
            _page.goto("https://portal.quicksigorta.com/")
            print("✅ Quick portal açıldı (çerez ile).")
        else:
            error_msg = f"⚠️ Çerez bulunamadı: {STORAGE_FILE}"
            print(error_msg)
            _result_queue.put(("error", error_msg))
            return
        
        # Browser hazır sinyali gönder
        _result_queue.put(("ready", None))
        
        # Komutları işle
        while True:
            cmd, args = _command_queue.get()
            if cmd == "stop":
                break
            try:
                result = cmd(*args)
                _result_queue.put(("success", result))
            except Exception as e:
                import traceback
                _result_queue.put(("error", f"{str(e)}\n{traceback.format_exc()}"))
                
    except Exception as e:
        import traceback
        error_detail = f"{str(e)}\n{traceback.format_exc()}"
        print(f"❌ Browser thread hatası: {error_detail}")
        _result_queue.put(("error", error_detail))
    finally:
        if _browser:
            try:
                _browser.close()
            except:
                pass
        if _playwright:
            try:
                _playwright.stop()
            except:
                pass

def _ensure_browser_started():
    """Browser thread'ini başlat"""
    global _browser_thread
    
    if _browser_thread is not None:
        return
    
    with _lock:
        if _browser_thread is not None:
            return
            
        _browser_thread = threading.Thread(target=_browser_thread_main, daemon=True)
        _browser_thread.start()
        
        # Browser'ın hazır olmasını bekle
        status, error = _result_queue.get(timeout=30)
        if status == "error":
            raise Exception(f"Browser başlatılamadı: {error}")

def get_page():
    _ensure_browser_started()
    return _page
