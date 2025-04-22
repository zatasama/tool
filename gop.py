import os
os.system("python.exe -m pip install --upgrade pip")

try:
    from seleniumbase import Driver
except:
    os.system("pip install seleniumbase")
    from seleniumbase import Driver
from time import sleep
try:
    from rich.console import Console
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
except:
    os.system("pip install rich")
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
import sys
import re
import json
import tempfile
import shutil
try:
    import requests
except:
    os.system("pip install requests")
    import requests
import zipfile



def check_update():
    url = "https://raw.githubusercontent.com/zatasama/version/refs/heads/main/version"
    response = requests.get(url)
    last_version = response.text.strip()
    return last_version
def update():
    update = check_update()
    if os.path.exists("version.txt"):
        version = open("version.txt", "r").read().strip()
        if version != update:
            giaodienchinh()
            console.print("[red1]Đang cập nhật phiên bản mới nhất ...")
            response = requests.get("https://raw.githubusercontent.com/zatasama/tool/refs/heads/main/gop.py?token=GHSAT0AAAAAADCE37G7ZPZRPOMCXC6DLO4M2AHT7LQ")
            current_file = os.path.abspath(__file__)
            with open(current_file, "wb",encoding="utf-8") as f:
                f.write(response.text)
                console.print("[green1]Đã cập nhật tool mới nhất vào lại để thưởng thức!")
                input("enter to exit....")
                sys.exit()
        return version
    else:
        giaodienchinh()
        console.print("[red1]Đang cập nhật phiên bản mới nhất ...")
        with open("version.txt", "w") as f:
            f.write(check_update())
        current_file = os.path.abspath(__file__)
        response2 = requests.get("https://raw.githubusercontent.com/zatasama/tool/refs/heads/main/gop.py?token=GHSAT0AAAAAADCE37G7ZPZRPOMCXC6DLO4M2AHT7LQ")
        with open(current_file, "wb",encoding="utf-8") as f:
            f.write(response2.text)
            console.print("[green1]Đã cập nhật tool mới nhất vào lại để thưởng thức!")
            input("enter to exit....")
            sys.exit()
        


def cap_nhat_trang_thai(trangthai):
        console.print(" "*60 , end = "\r")
        console.print(f"[bold cyan]{trangthai}...[/]",end = "\r")
        sleep(0.5)

class giaodienchinh():
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.console = Console()
        banner_text = Text()
        banner_text.append("\n" + "═" * 45 + "\n", style="bright_magenta")
        banner_text.append("🔥  TOOL GOLIKE  🔥\n", style="bold cyan")
        banner_text.append("💻  CODE BY DUY MANH (KAI)  💻\n", style="bold yellow")
        banner_text.append("═" * 40 + "\n", style="bright_magenta")
        self.console.print(Panel(banner_text, title="[bold green] WELCOME TO AUTO TOOL [/]", expand=False, border_style="bright_blue"))

        
    def selectjob(self):
        self.console.print(f"[cyan1]\n1.Shopee\n2.Facebook")
        self.console.print("\n[magenta1]Vui lòng nhập tool muốn chạy(Vd: 1 2 3 ...) :",end = " ")
        tool = input()
        return tool
    def tkgolike(self):
        try:
            if os.path.exists("tkgolike.txt"):
                while True:
                    self.console.print("[dark_slate_gray1]Sử dụng lại tài khoản golike không? (Y/N) :",end = " ")
                    nguoidung = input()
                    if "Y" in nguoidung or "y" in nguoidung or nguoidung == "":
                        return 
                    elif "N" in nguoidung or "n" in nguoidung:
                        break
                    else:
                        self.console.print("[bold red]Lựa chọn không hợp lệ, vui lòng nhập lại![/]",end = "\n")

            self.console.print("[dark_slate_gray1]Nhập username tài khoản golike: ",end = " ")
            username = input()
            self.console.print("[dark_slate_gray1]Nhập password tài khoản golike:",end = " ")
            password = input()
            with open("tkgolike.txt", "w",encoding= "utf-8") as file:
                file.write(f"{username}\n{password}")
            return 
        except:
            pass
    def cookiefacebook(self):
        all_cookies = {}
        while True:
            if os.path.exists("cookies.json"):
                try:
                    with open("cookies.json", "r" , encoding = "utf-8") as f:
                        all_cookies = json.load(f)
                except:
                    pass
                if not all_cookies:
                    self.console.print("[red]⚠ Không có cookie nào được lưu.[/red]")
                    os.remove("cookies.json")
                    input("enter to exit....")
                    return None
                for i, ten in enumerate(all_cookies.keys(), start=1):
                    print(f"{i}. {ten}")
                while True:
                    print(" ")
                    chon = input("Nhập tên cookie muốn sử dụng: ").strip()
                    if chon in all_cookies:
                        print(" ")
                        self.console.print(f"[green]✅ Đã chọn cookie '{chon}'[/green]")
                        return chon
                    else:
                        self.console.print("[red]Tên không tồn tại vui lòng nhập lại")
            else:
                while True:
                    with open("cookies.json", "w", encoding="utf-8") as f:
                        pass
                    self.console.print("\n[bold cyan]Nhập cookie mới[/bold cyan]: ",end = " ")
                    cookie_str = input().strip()
                    cookies_list = []
                    ten = input("Tên tài khoản muốn lưu với cookie (vd: acc1, tiktok_a, ...): ").strip()

                    for item in cookie_str.split(";"):
                        if "=" in item:
                            key ,val = item.strip().split("=" , 1)
                            cookies_list.append({"name": key.strip(), "value": val.strip()}) 
                    
                    tiep = input("Nhập thêm cookie khác? (Y/N): ").strip().lower()
                    all_cookies[ten] = cookies_list 
                    if tiep != "y":
                        break         
                with open("cookies.json", "w", encoding="utf-8") as f:
                    json.dump(all_cookies, f, indent=2, ensure_ascii=False)
                self.console.print("[green]✅ Cookie đã được lưu[/green]")
class login(giaodienchinh):
    def __init__(self,driver):
        self.driver = driver
        super().__init__()
       
    def loggolike(self):
    
        thanhcong = False
        with open("tkgolike.txt", "r" , encoding="utf-8") as f:
            tk = f.readlines()
        username = tk[0]
        password = tk[1]
        
        self.console.print("[green1]Đang đăng nhập golike...")
        try:
            self.driver.get("https://app.golike.net/login")
            self.driver.wait_for_element_visible("xpath",'//*[@id="app"]/div/div[1]/div/form/div[1]/input', timeout=999).send_keys(username)
            self.driver.wait_for_element_visible("#app > div > div.card.login-card > div > form > div:nth-child(2) > div > input", timeout=10).send_keys(password)
            sleep(0.2)
            self.driver.wait_for_element_visible("/html/body/div[1]/div/div[1]/div/form/div[3]/button", timeout=10).click()
            sleep(1)
            for _ in range(121):
                try:
                    self.driver.find_element("css selector", 'img[alt="avatar"][src*="golike-logo.svg"]')
                    cap_nhat_trang_thai("Đăng nhập thành công")
                    thanhcong = True
                    sleep(2)

                
                    return thanhcong
                    

                except Exception as e:
                    cap_nhat_trang_thai(f"Thời gian chờ đăng nhập {_} / 120 giây")
                    sleep(0.5)
                try:
                    popup_text = self.driver.execute_script("""
                    const el = document.querySelector('.swal2-popup #swal2-content');
                    return el ? el.innerText.trim() : null;
                """)
                    if popup_text and "Tên đăng nhập hoặc mật khẩu không tồn tại" in popup_text:
                        self.console.print("[red1]🚨 Lỗi đăng nhập phát hiện! Tên đăng nhập hoặc mật khẩu không tồn tại")
                        self.driver.execute_script("""
                        const btn = document.querySelector('.swal2-popup .swal2-confirm');if (btn) btn.click();""")
                except:
                    pass
           
        except Exception as e:
            print(f"lỗi:{e}")
        return thanhcong
    def logfacebook(self,chon):
        
        cap_nhat_trang_thai("Đang đăng nhập Facebook...")
        sleep(0.1)
        self.driver.get("https://www.facebook.com")
        sleep(3)
        self.driver.delete_all_cookies()
        try:
        # Đọc file JSON
            with open("cookies.json", 'r') as file:
                cookie_data = json.load(file)
        
        # Lấy danh sách cookie từ key "kai"
            cookies = cookie_data.get(chon, [])
            if not cookies:
                self.console.print("[red1]Không tìm thấy cookie trong file![/]")
                return False

        # Truy cập trang Facebook
            self.driver.get("https://www.facebook.com")
            sleep(2)

        # Gán cookie vào trình duyệt
            for cookie in cookies:
                cookie_dict = {
                    "name": cookie["name"],
                    "value": cookie["value"],
                    "domain": ".facebook.com",  # Cần thiết để cookie hoạt động trên Facebook
                }
                try:
                    self.driver.add_cookie(cookie_dict)
                except Exception as e:
                    self.console.print(f"[red1]Lỗi khi gán cookie {cookie['name']}: {e}[/]")

            # Làm mới trang để áp dụng cookie
            cap_nhat_trang_thai("[cyan1]Đang áp dụng cookie và làm mới trang...[/]")
            self.driver.refresh()
            sleep(5) 
        except Exception as e :
            print(f"lỗi{e}")


class NhiemVuShopee(giaodienchinh):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()
    def chay(self,tong):
        
        self.console.print("[green1]Làm Shopee...")
        print(" ")
        self.console.print(f"[bold green]Số tiền đã kiếm được: {tong} đ[/]",end = " ")
        self.console.print(" "*5,end = "\n")
        hetjob = False
        tien = "0"

        try:
            self.driver.get("https://app.golike.net/jobs/shopee")
            cap_nhat_trang_thai("Đã vào danh sách công việc.")
            try:
                nhanjob = self.driver.wait_for_element_visible(
                "css selector","#app > div > div:nth-child(1) > div.page-container > div:nth-child(3) > div.card.card-job-detail.mt-3.bg-gradient-shopee > div > div > div > div.col.text-right > div",timeout=4)
                self.driver.execute_script("arguments[0].click();", nhanjob)
                cap_nhat_trang_thai("nhận job")
                sleep(2)
                try:
                    js_text = self.driver.execute_script("""
                const el = document.querySelector('.swal2-popup #swal2-content');
                return el ? el.innerText.trim() : null;
                """)
                    print(" ")
                    cap_nhat_trang_thai(f"📜 Thông báo từ golike:{js_text}")
                    if "Hiện tại chưa có jobs mới" in js_text:
                        tien = "0"
                        hetjob = True
                        return hetjob,tien
                except Exception as e:
                    hetjob = False
                    try:
                        shopee = self.driver.wait_for_element_visible(
                        "xpath","//a[contains(., 'Shopee')]",timeout=10)
                        nhiemvu = self.driver.get_text("#app > div > div:nth-child(1) > div.page-container > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div.col-auto.px-0 > span")
                        tien = self.driver.get_text("#app > div > div:nth-child(1) > div.page-container > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(2) > div.col-auto.px-0 > div > span > span > span")
                        self.driver.execute_script("arguments[0].click();", shopee)
                        cap_nhat_trang_thai(f"Đã mở link công việc {nhiemvu} với mức lương {tien}")
                        main_tab = self.driver.current_window_handle
                        sleep(0.2)
                        for tab in self.driver.window_handles:
                            if tab != main_tab:
                                self.driver.switch_to.window(tab)
                                self.driver.close()
                                break

                        self.driver.switch_to.window(main_tab)
                        sleep(3)
                        try:
                            hoan_thanh_btn = self.driver.wait_for_element_visible("//button[contains(., 'Hoàn thành')]", timeout=20)
                            sleep(1)
                            self.driver.execute_script("arguments[0].click();", hoan_thanh_btn)
                            cap_nhat_trang_thai("Đã ấn nút hoàn thành")
                            time = 0
                            while True:
                                try:
                                    js_text = self.driver.execute_script("""
                                    const el = document.querySelector('.swal2-popup #swal2-content');
                                    return el ? el.innerText.trim() : null;
                                    """)
                                    cap_nhat_trang_thai(f"📜 Thông báo từ golike: {js_text}")
                                    
                                    if js_text == None:
                                        pass
                                    else:
                                        button = self.driver.wait_for_element_visible("css selector", ".swal2-confirm", timeout=1)
                                        button.click()
                                        if "đã được thanh toán" in js_text:
                                            cap_nhat_trang_thai("Đang báo lỗi")
                                            error = self.driver.wait_for_element_visible(
                                                "css selector","#app > div > div:nth-child(1) > div.page-container > div.card.card-job-detail.mt-2 > div > div > div > div.col-12.mt-1 > div.row.mt-3 > div.col-6.pl-0.pr-2 > button",timeout = 1
                                                )
                                            self.driver.execute_script("arguments[0].click();",error)
                                            sleep(2)
                                            gui_bao_cao = self.driver.wait_for_element_visible(
                                                "css selector","#app > div > div:nth-child(1) > div.page-container > div:nth-child(3) > div > div > button",timeout = 5
                                            )
                                            self.driver.execute_script("arguments[0].click();",gui_bao_cao)
                                            sleep(2)
                                            bao_cao = True
                                            while bao_cao:
                                                timeout = 0
                                                try:
                                                    gui =self.driver.wait_for_element_visible(
                                                        "css selector","body > div.swal2-container.swal2-center.swal2-shown > div > div.swal2-actions > button.swal2-confirm.swal2-styled",timeout = 5
                                                    )
                                                    self.driver.execute_script("arguments[0].click();",gui)
                                                    tien = "0"
                                                    return tien,hetjob
                                                except Exception as j:
                                                    timeout += 1
                                                    if timeout == 30:
                                                        return tien,hetjob
                                        elif "thành công" not in js_text:
                                            self.driver.get("https://app.golike.net/jobs/shopee")
                                            cap_nhat_trang_thai("Đã vào danh sách công việc.")
                                            try:
                                                nhanjob = self.driver.wait_for_element_visible(
                                                "css selector","#app > div > div:nth-child(1) > div.page-container > div:nth-child(3) > div.card.card-job-detail.mt-3.bg-gradient-shopee > div > div > div > div.col.text-right > div",timeout=4)
                                                self.driver.execute_script("arguments[0].click();", nhanjob)
                                                cap_nhat_trang_thai("nhận job")
                                                sleep(3)
                                                try:
                                                    js_text = self.driver.execute_script("""
                                                const el = document.querySelector('.swal2-popup #swal2-content');
                                                return el ? el.innerText.trim() : null;
                                                """)
                                                    cap_nhat_trang_thai(f"📜 Thông báo từ golike:{js_text}")
                                                    if "Hiện tại chưa có jobs mới" in js_text:
                                                        tien = "0"
                                                        hetjob = True
                                                        return hetjob,tien
                                                except Exception as e:
                                                    pass
                                            except:
                                                pass
                                            cap_nhat_trang_thai("Đang báo lỗi")
                                            error = self.driver.wait_for_element_visible(
                                                "css selector","#app > div > div:nth-child(1) > div.page-container > div.card.card-job-detail.mt-2 > div > div > div > div.col-12.mt-1 > div.row.mt-3 > div.col-6.pl-0.pr-2 > button",timeout = 1
                                                )
                                            self.driver.execute_script("arguments[0].click();",error)
                                            sleep(2)
                                            gui_bao_cao = self.driver.wait_for_element_visible(
                                                "css selector","#app > div > div:nth-child(1) > div.page-container > div:nth-child(3) > div > div > button",timeout = 5
                                            )
                                            self.driver.execute_script("arguments[0].click();",gui_bao_cao)
                                            sleep(2)
                                            bao_cao = True
                                            while bao_cao:
                                                timeout = 0
                                                try:
                                                    gui =self.driver.wait_for_element_visible(
                                                        "css selector","body > div.swal2-container.swal2-center.swal2-shown > div > div.swal2-actions > button.swal2-confirm.swal2-styled",timeout = 5
                                                    )
                                                    self.driver.execute_script("arguments[0].click();",gui)
                                                    tien = "0"
                                                    return tien,hetjob
                                                except Exception as j:
                                                    timeout += 1
                                                    if timeout == 30:
                                                        return tien,hetjob
                                        else:
                                            cap_nhat_trang_thai(f"Thành công, đã nhận {tien}")
                                            return tien,hetjob
                                    time += 1
                                    cap_nhat_trang_thai(f"Thời gian chờ hoàn thành {time} / 120 giây")
                                    sleep(0.2)
                                    if time == 120:
                                        cap_nhat_trang_thai("Hết thời gian đợi hoàn thành")
                                        sleep(0.8)
                                        break
                                    
                                except Exception as e:
                                    break
                        except Exception as e:
                            cap_nhat_trang_thai(f"Lỗi khi nhấn hoàn thành: {e}")
                    except:
                        cap_nhat_trang_thai("Không tìm thấy link công việc, bỏ qua.")
                    
            except:
                cap_nhat_trang_thai("không thấy job")
            
        except:
            cap_nhat_trang_thai("Không tìm thấy danh sách công việc, bỏ qua.")
        
        return tien,hetjob
                            
class NhiemVuFacebook(giaodienchinh):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()


    def info_taikhoan(self):
        self.console.print("[green1]Làm Facebook...")
        self.console.print("[green1]Đang lấy thông tin tài khoản Facebook...")
        sleep(0.1)
        self.driver.open("https://accountscenter.facebook.com/?__wblt=1")
        sleep(8)
        text = self.driver.execute_script("""
    const element = document.querySelector(
        'div[class*="x1lliihq"] > span[class*="x193iq5w"]'
    );
    return element ? element.textContent.trim() : "Không tìm thấy tên";
""")

        self.console.print(f"[magenta1]Tên tài khoản: {text}")
        if "Không tìm thấy" in text:
            self.console.print("[red1]Đăng nhập không thành công!")
            return text
        return text
    def doi_tai_khoan(self,text):
        self.driver.get("https://app.golike.net/jobs/facebook?tab=job")
        sleep(2)
        khongcotaikhoan = False
        try:
            js_text = self.driver.execute_script("""
                    const el = document.querySelector('.swal2-popup #swal2-content');
                    return el ? el.innerText.trim() : null;
                    """)
            print("📜 Thông báo từ golike:", repr(js_text))
            if "Không tải được danh sách Job do tài khoản" in js_text:
                button = self.driver.wait_for_element_visible("css selector", ".swal2-confirm", timeout=1)
                button.click()

        except:
            pass
        sleep(0.2)
        try:
            ten_taikhoan = text
            self.driver.execute_script("""
            const targetName = arguments[0].trim();
            const cards = document.querySelectorAll("div.card.shadow-200.mt-1");
            for (let card of cards) {
                const span = card.querySelector("div.col-8 span");
                if (span && span.textContent.trim() === targetName) {
                    card.click();
                    return;
                }
            }
        """, ten_taikhoan)
            self.console.print(f"Đã Chuyển Sang tài khoản {ten_taikhoan}")
        except:
            self.console.print(f"[red1]Tài khoản không có trong golike")
            khongcotaikhoan = True
        return khongcotaikhoan
    def nhan_job(self):
        timeout = 0
        datgioihanjob = False
        
        a = "none"
        loi = False


        js = '''
        const element = document.getElementById("swal2-content");
        return element ? element.innerText : null;
        '''

        alert_text = self.driver.execute_script(js)

        if alert_text:
            self.console.print("Thông báo:", alert_text)
            if "quá 100 jobs" in alert_text:
                self.console.print("[red1]🔥 Đã đạt giới hạn job trong ngày!")
                datgioihanjob = True
                return a,loi,datgioihanjob
        else:
            cap_nhat_trang_thai("✅ Không có cảnh báo nào xuất hiện.")
            cap_nhat_trang_thai("Đang nhận Jobs")
        while True:
                
                try:
                    spans = self.driver.find_elements("xpath", '//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/span/div/div/div/div/div/div[2]/div[2]/div/span')
                    for span in spans:
                        if "LIKE cho bài viết" in span.text:
                            span.click()
                            cap_nhat_trang_thai("Đã nhận job LIKE cho bài viết")
                            a = "LIKE"
                            loi = False
                            return a,loi,datgioihanjob
                        elif "Fanpage" in span.text:
                            span.click()
                            cap_nhat_trang_thai("Đã nhận job Like Fanpage")
                            a = "Fanpage"
                            loi = False
                            return a,loi,datgioihanjob
                        elif "Theo dõi" in span.text:
                            span.click()
                            cap_nhat_trang_thai("Đã nhận job Theo dõi")
                            a = "Theo dõi"
                            loi = False
                            return a,loi,datgioihanjob
                        elif "LOVE" in span.text:
                            span.click()
                            cap_nhat_trang_thai("Đã nhận job LOVE")
                            a = "LOVE"
                            loi = True
                            return a,loi,datgioihanjob
                        elif "ANGRY" in span.text:
                            span.click()
                            cap_nhat_trang_thai("Đã nhận job ANGRY")
                            loi = True
                            a = "ANGRY"
                            return a,loi,datgioihanjob
                        elif "HAHA" in span.text:
                            span.click()
                            cap_nhat_trang_thai("Đã nhận job HAHA")
                            loi = True
                            a = "HAHA"
                            return a,loi,datgioihanjob
                        elif "SAD" in span.text:
                            span.click()
                            cap_nhat_trang_thai("Đã nhận job SAD")
                            a = "SAD"
                            loi = True
                            return a,loi,datgioihanjob
                        elif "Thương thương":
                            span.click()
                            cap_nhat_trang_thai("Đã nhận job Thương thương")
                            a = "Thương thương"
                            loi = True
                            return a,loi,datgioihanjob     
                            
                except:
                    timeout += 1
                    cap_nhat_trang_thai(f"Thời gian chờ lấy job {timeout} / 60 giây")
                    sleep(0.3)
                    if timeout == 60:
                        return
    def check_link(self):
        
        main_tab = self.driver.current_window_handle
        try:
            mo_link = self.driver.wait_for_element_visible(
                "css selector", "#app > div > div:nth-child(1) > div.page-container > div:nth-child(2) > div:nth-child(2) > div > div > a:nth-child(3) > div.col.px-0 > h6.font-14.block-text", timeout=5
            )
            if mo_link:
                self. driver.execute_script("arguments[0].click();", mo_link)
                cap_nhat_trang_thai(f"Đã mở link công việc.")
                sleep(1)
                for tab in self.driver.window_handles:
                        if tab != main_tab:
                            self.driver.switch_to.window(tab)
                            current_url = self.driver.current_url
                            break                  
                cap_nhat_trang_thai(current_url)
        except:
            pass
        return current_url, main_tab
    def mo_job(self,a,current_url,loi):
        if loi == False:
            loi2 = False   
            try:
                if current_url == "about:blank":
                    loi2 = True
                    return loi2
                if a == "LIKE" or a == "Fanpage":
                    self.driver.get(current_url)
                    sleep(9)
                    try:
                        sleep(0.3)
                        # Chờ phần tử "Like" hoặc "Thích" xuất hiện
                        like_buttons = self.driver.find_elements("xpath", "//*[contains(@aria-label, 'Like') or contains(@aria-label, 'Thích')]")
                        cap_nhat_trang_thai(f"Tìm được {len(like_buttons)} nút like.")
                        # Kéo phần tử vào vùng nhìn thấy và click vào đó
                        if len(like_buttons) < 1 :
                            cap_nhat_trang_thai("Bỏ qua job do không tìm thấy nút like.")
                            loi2 = True
                            return loi2
                        for button in like_buttons:
                            try:
                                self.driver.execute_script("arguments[0].click();", button)
                                cap_nhat_trang_thai("Đã click nút Like.")
                                loi2 = False
                                sleep(0.2)
                            except:
                                cap_nhat_trang_thai(" click like không thành công.")
                                sleep(0.2)
                                loi2 = True
                    except:
                        pass
                elif a == "Theo dõi":
                    self.driver.get(current_url)
                    sleep(9)
                    try:
                        sleep(0.2)
                        # Chờ phần tử "Follow""
                        follow_buttons = self.driver.find_elements("xpath", "//*[contains(text(), 'Follow') or contains(text(), 'Theo dõi')]")                 
                        for button in follow_buttons:
                            try:
                                self.driver.execute_script("arguments[0].click();", button)
                                cap_nhat_trang_thai("click theo dõi thành công")
                                sleep(0.2)
                                loi = False
                                break
                            except Exception as e:
                                self.cap_nhat_trang_thai("click không thành công:", e)
                                loi2 = True
                                sleep(0.2)
                    except:
                        cap_nhat_trang_thai("Không tìm thấy nút theo dõi.")
                        sleep(0.2)
                else:
                    cap_nhat_trang_thai("Không tìm thấy link công việc.")
            except Exception as e:
                cap_nhat_trang_thai(f"Đã xảy ra lỗi: {str(e)}")
            return loi2 
    def chong_block(self):
        
        self.driver.get("https://www.facebook.com/")
        sleep(7)
        timeout = 0
        while True:
            try:
                self.driver.execute_script("window.scrollBy(0, 500);")
                sleep(0.5)
                timeout += 1
                cap_nhat_trang_thai(f"Thời gian chờ chống block facebook {timeout} / 210 giây")
                if timeout == 210:
                    self.driver.get("https://app.golike.net/jobs/facebook?tab=job")
                    sleep(1)
                    return
            except:
                pass
    def baoloi(self,loi,loi2,main_tab):
        
        if loi2 or loi:
            for tab in self.driver.window_handles:
                        if tab != main_tab:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                            break
            self.driver.switch_to.window(main_tab)
            sleep(0.3)
            cap_nhat_trang_thai("Đang báo lỗi")
            error = self.driver.wait_for_element_visible(
                "css selector","#app > div > div:nth-child(1) > div.page-container > div:nth-child(3) > div.card.card-job-detail.hand > div > div > div.col.px-0 > h6.font-bold.font-18",timeout = 1
                )
            self.driver.execute_script("arguments[0].click();",error)
            sleep(2)
            gui_bao_cao = self.driver.wait_for_element_visible(
                "css selector","#app > div > div:nth-child(1) > div.page-container > div:nth-child(3) > div.card.card-job-detail.mt-2 > div > button",timeout = 5
            )
            self.driver.execute_script("arguments[0].click();",gui_bao_cao)
            sleep(0.1)
            bao_cao = True
            while bao_cao:
                timeout = 0
                try:
                    gui =self.driver.wait_for_element_visible(
                        "css selector","body > div.swal2-container.swal2-center.swal2-shown > div > div.swal2-actions > button.swal2-confirm.swal2-styled",timeout = 5
                    )
                    self.driver.execute_script("arguments[0].click();",gui)
                    break
                except Exception as j:
                    timeout += 1
                    if timeout == 30:
                        return
            loi = True
            return loi
        else:
            loi = False
            return loi
    def hoan_thanh(self,main_tab):
        
        for tab in self.driver.window_handles:
                        if tab != main_tab:
                            self.driver.switch_to.window(tab)
                            self.driver.close()
                            break
        self.driver.switch_to.window(main_tab)
        sleep(0.3)
        try:
            hoan_thanh = self.driver.wait_for_element_visible(
                "css selector","#app > div > div:nth-child(1) > div.page-container > div:nth-child(2) > div.card.card-job-detail.hand > div > div > div.col.px-0 > h6.font-bold.font-18",timeout = 5
                )
            self.driver.execute_script("arguments[0].click();", hoan_thanh)
            cap_nhat_trang_thai("Đã ấn nút hoàn thành")
            ok = True
            delay = 0
            while ok:
                try:
                    done = self.driver.wait_for_element_visible(
                        "css selector","body > div.swal2-container.swal2-center.swal2-shown > div > div.swal2-actions > button.swal2-confirm.swal2-styled",timeout = 1
                        )
                    sleep(0.3)
                    self.driver.execute_script("arguments[0].click();", done)
                    sleep(0.4)
                    break
                except Exception as d:
                    pass
                delay += 1
                cap_nhat_trang_thai(f"Thời gian chờ hoàn thành {delay} / 140 giây")
                sleep(0.9)
                if delay == 140:
                    self.driver.get("https://app.golike.net/jobs/facebook?tab=job")
                    sleep(1)
                    return
        except Exception as c:
            print(c)
            cap_nhat_trang_thai("Không tìm thấy nút hoàn thành, bỏ qua.")
        sleep(2)
        try:
            self.driver.find_elements("css selector","#app > div > div:nth-child(1) > div.page-container > div:nth-child(3) > div.card.card-job-detail.hand > div > div > div.col.px-0 > h6.font-bold.font-18")
            chuaxong = True
            return chuaxong
        except:
            chuaxong = False
            return chuaxong








if __name__ == "__main__":
    console = Console()
    url = "https://drive.usercontent.google.com/download?id=1PEg2tK9v0rVxAFcg0kXrbHH0Fw6p2cu-&export=download&authuser=0&confirm=t&uuid=07cb9142-58c5-42a0-a974-de76675e9cf7&at=APcmpoyoxP5Ojht8-QJxasUUXeEg%3A1745255059559"
    filename = "captcha.zip"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    if not os.path.exists(file_path) and not os.path.exists("captcha"):
        print("Đang cài captcha")
        r = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(r.content)
        with zipfile.ZipFile("captcha.zip", 'r') as zip_ref:
            zip_ref.extractall(".")
        print("da cai captcha")
        if os.path.exists("captcha"):
            os.remove(file_path)
    else:
        print("captcha da cai")
    version = update()
    temp_profile_dir = tempfile.mkdtemp(prefix="browser_profile_")
    
    # Khởi tạo 1 driver duy nhất
    giaodien = giaodienchinh()
    console.print(f"\n [bright_magenta]Đang dùng phiên bản {version}")
    tool = giaodien.selectjob()
    giaodien.tkgolike()
    if  "2" in tool.strip():
        chon = giaodien.cookiefacebook()
        if chon == None:
            console.print("[red1]Tool thoát do thiếu thông tin:")
            sys.exit()
            

    options = {
    "block_images": False,
    "uc": True,
    "headed": True,
    "incognito": False,
    "extension_dir": r"captcha",
    "mobile": False,  # Giả lập thiết bị di động
    "agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",  # User-Agent 
   "chromium_arg": [
        "--disable-infobars",
    ],
    "user_data_dir": temp_profile_dir,

}
    driver_chung = Driver(**options)
    sleep(2)
    driver_chung.set_window_size(450, 800)
    login = login(driver_chung)
    thanhcong = login.loggolike()
    if "1" in tool.strip() and thanhcong == True:
        tong = [0]
        while True:
            console.print(f"\n [bright_magenta]Đang dùng phiên bản {version}")
            shopee = NhiemVuShopee(driver_chung)
            tien,hetjob = shopee.chay(tong)
            if hetjob == True:
                break
            try:
                congtien = re.findall(r'\d+',tien)
                for i in congtien:
                    for j in tong:
                        tongtien = int(i) + int(j)
                        tong.clear()
                        tong.append(tongtien)

            except Exception as e:
                print(e)   
        
    if "2" in tool.strip() and thanhcong == True:
        login.logfacebook(chon)
        solanloi = 0
        sojobdalam = 0
        chongblock = 0
        facebook = NhiemVuFacebook(driver_chung)
        text = facebook.info_taikhoan()
        if text == "Không tìm thấy tên":
            pass
        else:
            khongcotaikhoan = facebook.doi_tai_khoan(text)
            if khongcotaikhoan == True:
                pass
            else:
                while True:
                    console.clear
                    giaodienchinh()
                    console.print(f"\n [bright_magenta]Đang dùng phiên bản {version}")
                    console.print("[green1]Đang làm Facebook")
                    console.print(f"[dark_slate_gray1]Đang chạy tài khoản [magenta1]{text}")
                    console.print(f"[dark_slate_gray1]Số jobs đã làm: {sojobdalam}")
                    a,loi,datgioihanjob = facebook.nhan_job()
                    if datgioihanjob == True:
                        break
                    else:
                        current_url,main_tab = facebook.check_link()
                        loi2 = facebook.mo_job(a,current_url,loi)
                        loi = facebook.baoloi(loi,loi2,main_tab)
                        if loi == False:
                            chuaxong = facebook.hoan_thanh(main_tab)   

                            if chuaxong == True:
                                loi = True
                                try:
                                    facebook.baoloi(loi,loi2,main_tab)
                                    solanloi += 1
                                    console.print(f"[red1]Số lỗi liên tiếp {solanloi} / 5 lần[/]")
                                except:
                                    console.print("[green1]Hoàn thành")
                                    sojobdalam += 1
                                    chongblock += 1
                                    solanloi = 0
                            
                        if solanloi == 5:
                            console.print(f"[red1]LỖI LIÊN TIẾP {solanloi} lần, ngưng làm job ")
                            break
                        if chongblock == 16:
                                facebook.chong_block()
                                chongblock = 0


    # Kết thúc
    if 'driver_chung' in locals():
        driver_chung.quit()  # Đóng driver trước
    if os.path.exists(temp_profile_dir):
        shutil.rmtree(temp_profile_dir, ignore_errors=True)  # Xóa thư mục profile
        print(f"Đã xóa profile tạm thời tại: {temp_profile_dir}")      
    console.print("[red1]Đã kết thúc, enter to exit...")   
    input()
    sys.exit()

                
            
        
    
   
  
    

