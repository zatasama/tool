
import os
try:
      import json
      from rich.console import Console ,Group
      from rich.table import Table
      from rich.padding import Padding
      from rich.text import Text
      import time
      import random
      import sys
      from ctypes import  windll, Structure, c_short
      from ppadb.client import Client as AdbClient
      import uiautomator2 as u2
      from threading import Thread
      from curl_cffi import requests
      from rich import box
      from rich.panel import Panel
      import signal
except:
      pass
console = Console()
namedevice = None
danhsach = []
from threading import Lock
lock_thao_tac_dien_thoai = Lock()
chucnang = []
adb = AdbClient(host='127.0.0.1', port=5037)
d = None
running = True
def device():
      while True:
            try:
                  print('\n')
                  devices = adb.devices()
                  if not devices:
                        console.print('[red]Không tìm thấy thiết bị nào![/red]')
                        quit()

                  # In danh sách thiết bị
                  console.print("Danh sách thiết bị:",style = 'bright_cyan')
                  for i, dev in enumerate(devices, 1):
                        console.print(f"[red]{i}[/red] : [bright_green]{dev.serial}")

                  # Nhập số để chọn thiết bị
                  while True:
                        try:
                              console.print('chọn thiết bị chạy:', style = 'bright_magenta'  , end = ' ')
                              select = int(input())
                              if 1 <= select <= len(devices):
                                    break
                              else:
                                    console.print('vui lòng chọn thiết bị phù hợp', style = 'red')
                        except ValueError:
                              console.print("Vui lòng nhập một số hợp lệ", style = 'red1')
                  selected_device = devices[select - 1]
                  global d
                  d = u2.connect(selected_device.serial)
                  console.print(f"Đã kết nối với devices {selected_device.serial}",style = 'cyan1')
                  d.shell('svc power stayon true')
                  global namedevice
                  namedevice =  selected_device.serial
                  return selected_device.serial
                        
            except Exception as e:
                  console.print(f"Lỗi khi kết nối với thiết bị: {e}",style = 'red')
                  os.system("adb start-server")
            
def lay_thong_tin():
      table = Table()
      table.add_column('[green][^-^] ==> [red1] Tool chạy cùng lúc (Đa luồng) [/red1]')
      table.add_row('[bright_cyan][:D] ==> 1. Tool instagram (ADB) \n')
      table.add_row('[bright_cyan][:D] ==> 2. Tool snapchat (ADB) \n')
      table.add_row('[bright_cyan][:D] ==> 3. Tool linkedin (ADB)\n')
      table.add_row('[bright_cyan][:D] ==> 4. Tool pinterest (COOKIE)\n')
      console.print(table)                  
      console.print('\n [green1]Chọn chức năng muốn dùng vd 1,2,3: [/green1]',end = '')
      chucnang1 = str(input()).split(',')
      global chucnang
      for i in range(len(chucnang1)):
            chucnang.append(i)
      return chucnang1
def logo():
      logo = ''' [dark_slate_gray2]                                                                                                   
      ██╗  ██╗ █████╗ ██╗
      ██║ ██╔╝██╔══██╗██║
      █████╔╝ ███████║██║
      ██╔═██╗ ██╔══██║██║
      ██║  ██╗██║  ██║██║
      ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
      [/dark_slate_gray2]'''
      separator = Text("===============================================================================", style="bright_yellow")
      panel = Panel(f"{logo}",expand=False,border_style="dark_slate_gray2",box=box.DOUBLE,height=10,width=80)
      return Group(
            Padding(panel, (0, 8, 0, 3)),  # Logo trước
            Padding(separator, (0, 0, 0, 3)),  # Hàng rào ngay dưới logo
      )
      

def signal_handler(sig, frame):
    global running
    running = False
    try:
        print('\n'*10)
        print('\nCtrl+C detected. Stopping...')
        d.press("home")
    except:
        pass
    finally:
      set_cursor_position(0,23)
      end = Panel(f"[green]\nCảm ơn bro đã sử dụng tool![/green]",expand=False,border_style="red1",box=box.DOUBLE)
      console.print(Padding(end,(0,0,0,20)))
      sys.exit(0)
def giao_dien_chinh():

      table = Table(title = '\r WE ARE THE SHADOW GARDEN' , title_style= 'bright_red',box=box.DOUBLE , title_justify='center' ,border_style="white",collapse_padding = True,width=121)
      table.add_column('STT' , header_style='blue_violet', style = 'green',justify='center',ratio=0.8)
      table.add_column('THREAD' , style = 'yellow2' , header_style= 'bright_blue',justify='center',ratio=1.4)
      table.add_column('DEVICE' , style = 'bright_yellow' , header_style='bright_yellow',ratio=2,justify='center')
      table.add_column('ACC GET JOB',style = 'cyan1' , header_style='cyan1',justify='center',ratio=2)
      table.add_column('ACC IN PHONE' , style = 'dark_slate_gray2' , header_style='dark_slate_gray2',justify='center',ratio=2.5)
      table.add_column('ERROR',style = "red",header_style = 'red3',justify='center',ratio=1)
      table.add_column('SUCCESS' , style= 'green1',header_style = 'green1',justify='center',ratio=1.5)
      table.add_column('TOTAL_COIN',style= 'bright_cyan',justify='center',ratio=1.8)
      table.add_column('STATUS',style= 'bright_cyan' , header_style='bright_cyan',no_wrap=True,ratio=5,justify='center')
      for hang in danhsach:
            table.add_row(hang[0],hang[1],namedevice,hang[3],hang[4],hang[5],hang[6],hang[7],hang[8])
            table.add_section()     
      return table  
class ACCGOLIKE:
      def __init__(self):
            self.thongtin = []
            self.headers = {
                  'accept': 'application/json, text/plain, */*',
                  'accept-language': 'vi',
                  'authorization': '',
                  'content-type': 'application/json;charset=utf-8',
                  'origin': 'https://app.golike.net',
                  'priority': 'u=1, i',
                  'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
                  'sec-ch-ua-mobile': '?1',
                  'sec-ch-ua-platform': '"Android"',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-site',
                  't': 'VFZSak1VMTZXWGhOYW1jeVQwRTlQUT09',
                  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
                  }
      def thong_tin_acc(self):
            try:
                  response = requests.get('https://gateway.golike.net/api/statistics/report', headers=self.headers,impersonate='chrome').json()
                  response1 = requests.get('https://gateway.golike.net/api/users/me', headers=self.headers,impersonate = 'chrome').json()
            except:
                  pass
            self.current_coin = response['current_coin']
            self.user_name = response1['data']['username']
            self.pending_coin = sum(
                  value['pending_coin']
                  for value in response.values()
                  if isinstance(value, dict) and 'pending_coin' in value
            )
            
      def ghi_acc(self):
            tiep = False
            base_dir = os.path.dirname(os.path.abspath(__file__))
            base_dir = os.path.join(base_dir, 'data.json')
            while True:
                  os.system('cls' if os.name == 'nt' else 'clear')
                  console.print(logo())
                  check_data = os.path.exists(base_dir)
                  try:
                        with open(base_dir,'r',encoding='utf-8') as f:
                              data = json.load(f)
                        data[0]['authorization']
                  except:
                        check_data = False
                  if check_data is False:  #khi chưa có file json
                        console.print("[green]\nChưa thêm tài khoản golike vui lòng nhập authorization: ",end = '')
                        authorization = input()
                        self.headers['authorization'] = authorization
                        self.so_acc = '0'
                        try:
                              self.thong_tin_acc()
                        except:
                              console.print('[red]Authe sai![/red]')
                              continue
                        data = [{
                              'username': f"{self.user_name}",
                              'authorization': f'{authorization}'
                        }]
                        with open(base_dir,'w',encoding='utf-8') as f:
                              json.dump(data,f,indent=2,ensure_ascii=False)
                  elif check_data is True: #khi đã có file json và muốn thêm acc
                        with open(base_dir,'r',encoding='utf-8') as f:
                              try:
                                    data = json.load(f)
                                    self.tableacc = Table(title = '\nDanh sách tài khoản golike ', title_style= 'bright_green' , title_justify='center',box = box.DOUBLE,border_style="white",expand=False)
                                    self.tableacc.add_column('STT' , header_style='blue_violet', style = 'green')
                                    self.tableacc.add_column('USERNAME' , style = 'yellow2' , header_style= 'bright_blue')
                                    self.tableacc.add_column('Pending Coin' , style = 'bright_yellow' , header_style='bright_yellow')
                                    self.tableacc.add_column('Current Coin' , style = 'cyan1' , header_style='cyan1')
                                    for i in range(len(data)):
                                          self.so_acc = str(i)
                                          self.headers['authorization'] = data[i]['authorization']
                                          self.thong_tin_acc()
                                          self.tableacc.add_row(f'{self.so_acc}',f'{self.user_name}',f'{self.pending_coin} VND',f'{self.current_coin} VND')
                                          self.tableacc.add_section()
                                    self.list_acc = Padding(self.tableacc,(0,0,0,3))
                                    console.print(self.list_acc)
                                    tiep = True
                              except Exception as e:
                                    console.print("[red] Không tìm thấy tài khoản được thêm vào[/red]")

                        console.print('\n  [green]Muốn thêm tài khoản golike không(y/n/cls để xoá tất cả tài khoản)[/green]: ',end = '')
                        ykien = str(input())
                        if 'y' in  ykien.lower():
                              with open(base_dir,'r',encoding='utf-8') as f:
                                    data = json.load(f)
                              console.print('  [green]Nhập authorization: ',end = '')
                              authorization = input()
                              self.headers['authorization'] = authorization
                              data.append({
                              'username': f"{self.user_name}",
                              'authorization': f'{authorization}'
                              })
                              with open(base_dir,'w',encoding='utf-8') as f:
                                    json.dump(data,f,indent=2)
                        elif 'n' in ykien.lower():
                              break
                        elif 'cls' in ykien.lower():
                              os.remove(base_dir)
                              console.print('[red1]Đã xoá tất cả tài khoản![/red1]')
                        else:
                              console.print('[red]NHẬP CÁI CHÓ GÌ VẬY ?')
                              time.sleep(1)
                        
            while tiep:
                  with open(base_dir,'r',encoding='utf-8') as f:
                        data = json.load(f)
                  console.print('\n[green]   Nhập số tương ứng với tài khoản muốn chạy: [/green]',end = '')
                  chontaikhoan = input()
                  for i in range(len(data)):
                        if str(i) == chontaikhoan:
                              self.headers['authorization'] = data[i]['authorization']
                              return data[i]['authorization']
                  console.print('[red] Không tìm thấy tài khoản tương ứng![/red]')

class GolikeIG:
      def __init__(self,authe):
            global chucnang
            self.stt = int(chucnang[0])
            chucnang.remove(chucnang[0])
            a = [str(self.stt + 1) , 'INSTAGRAM' , 'namedevice','accgetjob','None' , "0" , "0","0" , "wait..."]
            danhsach.append(a)
            self.delay = [4, 5,5.5, 6,6.5, 7,7.5, 8.5, 9, 10]
            self.authe = authe
            self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi',
            'authorization': self.authe,
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://app.golike.net',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            't': 'VFZSak1VMXFUVFJPUkVrd1RWRTlQUT09',
            'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 CrKey/1.54.248666',
            }
            self.loi = 0
            self.hoanthanh = 0
            self.account_id = None
            self.account_username = None
            self.devices = None
            self.accrun = None
            self.idacc = None
            self.nojob = []
            self.username_acc_run = None
            self.chuyenacc = True
            self.total_coin = 0
            self.coin = '0'
            self.total_error = 0

      def get_acc(self):
            if self.hoanthanh >= 15:
                  danhsach[self.stt][8] = 'Delay chống block...'
                  time.sleep(300)
            if self.account_username == None:
                  table = Table(title = '\nDanh sách acc instagram có trong tài khoản golike', title_style= 'bright_red' , title_justify='center')
                  headers = {
                        
                  'sec-ch-ua-platform': '"Android"',
                  'Authorization': f'{self.authe}',
                  'Referer': '',
                  'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
                  'sec-ch-ua-mobile': '?0',
                  'User-Agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 CrKey/1.54.248666',
                  'Accept': 'application/json, text/plain, */*',
                  't': 'VFZSak1VMXFVVEZQVkdjMFRrRTlQUT09',
                  'Content-Type': 'application/json;charset=utf-8',
                  }
                  table.add_column('STT' , header_style='blue_violet', style = 'green')
                  table.add_column('USERNAME' , style = 'yellow2' , header_style= 'bright_blue')
                  table.add_column('ID' , style = 'bright_yellow' , header_style='bright_yellow')
                  try:
                        response = requests.get('https://gateway.golike.net/api/instagram-account', headers=headers,impersonate='chrome').json()
                  except:
                        pass
                  data = response['data']
                  for i in range(len(data)):
                        table.add_row(str(i),str(data[i]['instagram_username']),str(data[i]["id"]))
                        table.add_section()
                  console.print(table)
                  console.print(f'\n Nhập những acc có trong thiết bị [{namedevice}] (VD : 0,1,2): ',end = '')
                  listacc = input()
                  listacc = listacc.split(',')
                  dsacc = []
                  dsid = []
                  for acc in listacc:
                        dsacc.append(data[int(acc)]['instagram_username'])
                        dsid.append(data[int(acc)]['id'])
                  self.accrun = dsacc
                  self.idacc = dsid
                       
      def doiacc(self):
            if self.chuyenacc == True:
                  danhsach[self.stt][8] = 'Chờ tí...'
                  so =  len(self.idacc) - len(self.accrun)
                  if so == len(self.idacc):
                        self.accrun = self.nojob.copy()
                        self.nojob.clear()
                        self.account_id = self.idacc[0]
                        self.account_username = self.accrun[0]
                  else:
                        self.account_id = self.idacc[so]
                        self.account_username = self.accrun[0]
                        
                  

      def check_job(self,tp):
            if tp == 'follow':
                  try:
                        time.sleep(2)
                        c = d(text='Thêm vào danh sách Bạn thân').wait(timeout=2)
                        if c == False:
                              d.xpath('//*[@resource-id="com.instagram.android:id/profile_header_user_action_follow_button"]').click_exists(timeout=10)
                              c = d(text='Thêm vào danh sách Bạn thân').wait(timeout=5)
                        time.sleep(2)
                        if c:
                              danhsach[self.stt][8] = "Đã fl thanh cong"
                              return True
                        else:
                              danhsach[self.stt][8] = "chua fl thanh cong"
                              return False
                  except Exception as e:
                        pass
            elif tp == 'like':
                  try:
                        time.sleep(1)
                        c = d.xpath('//*[@content-desc="Đã thích"]').wait(timeout=5)
                        if c:
                              danhsach[self.stt][8] = "Đã like thanh cong"
                              return True
                              
                        else:
                              danhsach[self.stt][8] = "chua like thanh cong"
                              return False
                  except Exception as e:\
                  pass  
      def acchientai(self):
            if self.username_acc_run == None:
                  while True:
                        if lock_thao_tac_dien_thoai.acquire(blocking=False):
                                    try:
                                          danhsach[self.stt][8] = "Đang lấy acc trong máy..."
                                          d.app_start('com.instagram.android', wait=True , stop= True)
                                          time.sleep(4)
                                          d.xpath('//*[@resource-id="com.instagram.android:id/profile_tab"]').click_exists(timeout = 10)
                                          time.sleep(3)
                                          try:
                                                self.username_acc_run = d.xpath('//*[@resource-id="com.instagram.android:id/action_bar_large_title_auto_size"]').get_text()
                                          except:
                                                self.username_acc_run = d.xpath('//*[@resource-id="com.instagram.android:id/action_bar_title"]').get_text()
                                          danhsach[self.stt][4] = str(self.username_acc_run)
                                    except Exception as e:
                                          danhsach[self.stt][8] = str(e)
                                    finally:
                                          lock_thao_tac_dien_thoai.release()
                                    break
                        else:           
                              danhsach[self.stt][8] = 'Đang chờ lượt hành động...'
                              time.sleep(2)
                  
            danhsach[self.stt][6] = str(self.hoanthanh)
            danhsach[self.stt][5] = str(self.total_error)
            danhsach[self.stt][7] = str(self.total_coin) + 'Đ'
            danhsach[self.stt][3] = str(self.account_username)
      def get_job(self):
            bayacc = d.xpath('//*[@text="Bạn phải hoàn tất hành động này thì mới có thể sử dụng tài khoản của mình."]').wait(timeout=4)
            if bayacc == True:
                  menu = d.xpath('//*[@content-desc="Menu"]').click_exists(timeout= 5)
                  if menu == True:
                        d.xpath('//*[@content-desc="Tiếp tục"]').click_exists(timeout=5)
                        return False
            if self.loi >= 12:
                  danhsach[self.stt][8] = f'lỗi liên tiếp {self.loi}, đã ngừng chạy'
                  return False
            params = {
                  'instagram_account_id': self.account_id,
                  'data': 'null',
      }     
            danhsach[self.stt][8] = 'Đang lấy job...'  
            try:
                  response = requests.get('https://gateway.golike.net/api/advertising/publishers/instagram/jobs', params=params, headers=self.headers, impersonate="chrome").json()
            except:
                  pass
            # print(response)
            try:
                  self.link = response['data']["link"]
                  self.coin = str(response['data']["price_after_cost"])
                  self.adid = response['lock']["instagram_users_advertising_id"]
                  self.type = response['lock']["type"]
                  danhsach[self.stt][8] = f"type:{self.type} - {self.coin}đ"
                  self.object_id = response['lock']["object_id"]
                  danhsach[self.stt][8] = str(self.link)
                  self.chuyenacc = False
                  while self.username_acc_run != self.account_username:
                        if lock_thao_tac_dien_thoai.acquire(blocking=False):
                              try:
                                    danhsach[self.stt][8] = 'Đang chuyển acc...'
                                    d.app_start('com.instagram.android', wait=True , stop= True)
                                    a = d.xpath('//*[@resource-id="com.instagram.android:id/profile_tab"]')
                                    a.click(timeout = 2)
                                    try:
                                          self.username_acc_run = d.xpath('//*[@resource-id="com.instagram.android:id/action_bar_large_title_auto_size"]').get_text()
                                    except:
                                          try:
                                                self.username_acc_run = d.xpath('//*[@resource-id="com.instagram.android:id/action_bar_title"]').get_text()
                                          except:
                                                pass
                                    if self.username_acc_run == self.account_username:
                                          break
                                    chuyenacc = d.xpath('//*[@resource-id="com.instagram.android:id/action_bar_title_chevron"]')
                                    chuyenacc1 = chuyenacc.wait(7)
                                    if chuyenacc1:
                                          chuyenacc.click(timeout = 4)
                                          time.sleep(3)
                                          clickus = d.xpath(f'//*[@text="{self.account_username}"]')
                                          clickus.click(timeout = 3)
                                    else:
                                          time.sleep(4)
                                          b = a.center()
                                          time.sleep(2)
                                          d.double_click(b[0],b[1])
                                          time.sleep(2)
                                    
                                    self.username_acc_run = d.xpath('//*[@resource-id="com.instagram.android:id/action_bar_large_title_auto_size"]').get_text()
                                    danhsach[self.stt][4] = str(self.username_acc_run)
                              except:
                                    pass
                              finally:
                                    danhsach[self.stt][4] = str(self.username_acc_run)
                                    lock_thao_tac_dien_thoai.release()
                              time.sleep(2)
                        else:
                              danhsach[self.stt][8] = 'Đang chờ lượt hành động...'
                              time.sleep(2)
                  return True

            except:
                  danhsach[self.stt][8] = 'Đã hết job đợi get job mới...'
                  self.chuyenacc = True
                  try:
                        self.nojob.append(self.accrun[0])
                        self.accrun.remove(self.accrun[0])
                  except:
                        pass
                  time.sleep(10)
                  return None
            
      def success(self):
            json_data = {
                  'instagram_users_advertising_id': self.adid,
                  'instagram_account_id': self.account_id,
            }
            try:
                  response = requests.post(
                        'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs',
                        headers=self.headers,
                        json=json_data,impersonate="chrome"
                  ).json()
            except:
                  pass
            done = (response['message'])
            danhsach[self.stt][8] = str(done)
            if  'Báo cáo thành công' in done:
                  self.hoanthanh += 1
                  self.total_coin += int(self.coin)
                  self.loi = 0
                  d.press('back')
                  time.sleep(1)
                  d.press('back')
            else:
                  danhsach[self.stt][8] = "Đang bỏ qua job"
                  if self.type == "follow":
                        d.xpath('//*[@text="Bỏ theo dõi"]').click(timeout=10)
                  self.report()

      def report(self):
            try:
                  json_data = {
                  'ads_id': self.adid,
                  'object_id': self.object_id,
                  'account_id': self.account_id,
                  'type': self.type,
      }       
                  response = requests.post(
                  'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs',
                  headers=self.headers,
                  json=json_data,impersonate="chrome"
      ).json()
                  danhsach[self.stt][8] = str(response['message',self.type])
                  self.loi += 1
            except:
                  pass
            
            self.total_error += 1
            d.press('back')
            time.sleep(1)
            d.press('back')
      def thao_tac(self):
            if self.chuyenacc == False:
                  while True:
                        if lock_thao_tac_dien_thoai.acquire(blocking=False):
                              time.sleep(2)
                              try:
                                    danhsach[self.stt][8] = "Đang chuyển hướng"
                                    d.shell('am start -a android.intent.action.VIEW -d "'+self.link+'" com.instagram.android')
                                    time.sleep(6)
                                    
                                    if self.type == "follow":
                                          try:
                                                danhsach[self.stt][8] = "Đang làm nhiệm vụ..."
                                                d.xpath('//*[@resource-id="com.instagram.android:id/profile_header_user_action_follow_button"]').click_exists(timeout=5)
                                                delay = random.choice(self.delay)
                                                tp = "follow"
                                                check = self.check_job(tp)
                                                if check:
                                                      danhsach[self.stt][8] = "delay hoan  thanh job " + str(delay) + " giay"
                                                      time.sleep(delay)
                                                      self.success()
                                                else:
                                                      danhsach[self.stt][8] = "Đang bỏ job"
                                                      self.report()
                                          except Exception as e:
                                                self.report()
                                                delay = random.choice(self.delay)
                                                danhsach[self.stt][8] = 'delay that bai job ' + str(delay) + ' giay'
                                                time.sleep(delay)
                                    elif self.type == "like":
                                          try:
                                                danhsach[self.stt][8] = "Đang làm nhiệm vụ..."
                                                d.swipe(0,600,0,0)
                                                l = d.xpath('//*[@content-desc="Thích"]').click_exists(timeout=5)
                                                if l == False:
                                                      d.xpath('//*[@resource-id="com.instagram.android:id/row_feed_button_like"]').click_exists(timeout=5)
                                                time.sleep(2)
                                                delay = random.choice(self.delay)
                                                tp = "like"
                                                check = self.check_job(tp)
                                                if check:
                                                      danhsach[self.stt][8] = "delay hoan  thanh job " + str(delay) + " giay"

                                                      self.success()
                                                      time.sleep(delay)
                                                else:
                                                      self.report()
                                                      delay = random.choice(self.delay)
                                                      danhsach[self.stt][8] = 'delay that bai job ' + str(delay) + ' giay'
                                                      time.sleep(delay)
                                          except Exception as e:
                                                self.report()    
                                                delay = random.choice(self.delay)
                                                danhsach[self.stt][8] = 'delay that bai job ' + str(delay) + ' giay'
                                                time.sleep(delay)
                                    elif self.type == 'comment':
                                          try:
                                                danhsach[self.stt][8] = "Đang bỏ job cmt"
                                                self.report()
                                          except:
                                                pass
                              except Exception as e:
                                    danhsach[self.stt][8] = f'lỗi khi thực hiện thao tác: {e}'
                                    self.report()
                              finally:
                                    lock_thao_tac_dien_thoai.release()
                                    break
                        else:
                              danhsach[self.stt][8] = 'Đang chờ lượt hành động...'
                              time.sleep(2)
      def main(self):
            while True:
                  self.doiacc()
                  self.acchientai()
                  st = self.get_job()
                  if st == False:
                        break
                  time.sleep(2)
                  self.thao_tac()
class GolikeSNAP:
      def __init__(self,authe):
            global chucnang
            self.stt = int(chucnang[0])
            chucnang.remove(chucnang[0])
            a = [str(self.stt + 1) , 'SNAPCHAT' , f'{namedevice}','accgetjob','None' , "0" , "0","0" , "wait..."]
            danhsach.append(a)
            self.authe = authe
            headers = {
                  'accept': 'application/json, text/plain, */*',
                  'accept-language': 'vi',
                  'authorization': f'{self.authe}',
                  'content-type': 'application/json;charset=utf-8',
                  'origin': 'https://app.golike.net',
                  'priority': 'u=1, i',
                  'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
                  'sec-ch-ua-mobile': '?1',
                  'sec-ch-ua-platform': '"Android"',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-site',
                  't': 'VFZSak1FOUVVVFZOVkZVelRXYzlQUT09',
                  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
            }
            self.headers = headers
      def get_acc(self):
            danhsach[self.stt][8] = 'Đang lấy acc...'
            try:
                  response = requests.get("https://gateway.golike.net/api/snapchat-account",headers=self.headers,impersonate="chrome").json()
            except:
                  pass
            for i in range(len(response["data"])):
                  data = response["data"][i]
                  self.id = data["id"]
                  self.name = data["name"]
                  self.uid = data["uid"]
                  danhsach[self.stt][3] = str(self.name)
                  danhsach[self.stt][4] = str(self.name)
      def get_job(self):
            danhsach[self.stt][8] = 'Đang lấy job...'
            try:
                  response = requests.get(f"https://gateway.golike.net/api/advertising/publishers/snapchat/jobs?account_id={self.id}",impersonate="chrome",headers=self.headers).json()
            except:
                  pass
            try:
                  self.account_id = response["lock"]["account_id"]
                  self.ads_id = response["lock"]["ads_id"]
                  type = response["lock"]["type"]
            except:
                  danhsach[self.stt][8] = response["message"]
                  if 'tiktok trong' in response['message']:
                        danhsach[self.stt][8] = 'Cần làm 2 nhiệm vụ tiktok mới được getjob'
                  time.sleep(10)
                  return False
            self.link = response["data"]["link"]
            status = response["status"]
            self.coin = response["data"]["price_after_cost"] 
            self.objectid = response["data"]["object_id"]
            danhsach[self.stt][8] = f"{status} - type:{type} - {self.coin}đ"
            time.sleep(1)
            danhsach[self.stt][8] = str(self.link)
            return True

      def complete(self):
            json_data = {
                  'account_id' : self.account_id,
                  'ads_id' : self.ads_id
            }
            try:
                  response = requests.post("https://gateway.golike.net/api/advertising/publishers/snapchat/complete-jobs",impersonate="chrome",headers = self.headers,json=json_data).json()
            except:
                  pass
            status = response["status"]
            success = response["success"]
            message = response["message"]
            if 'thành công' in message:
                  coin = ''.join(c for c in danhsach[self.stt][7] if c.isdigit())
                  danhsach[self.stt][7] = str(int(coin) + int(self.coin)) + 'Đ'
                  danhsach[self.stt][6] = str(int(danhsach[self.stt][6]) + 1)
            else:
                  danhsach[self.stt][5] = str(int(danhsach[self.stt][5]) + 1)
            danhsach[self.stt][8] = f"{status} | {success} | {message}"
      def skip_job(self):
            json_data = {
                  'account_id': self.account_id,
                  'ads_id': self.ads_id,
                  'object_id': self.objectid,
            }
            try:
                  response = requests.post(
            'https://gateway.golike.net/api/advertising/publishers/snapchat/skip-jobs',
            headers=self.headers,
            json=json_data,impersonate="chrome"
            ).json()
            except:
                  pass
            danhsach[self.stt][8] = str(response["message"])
            danhsach[self.stt][5] = str(int(danhsach[self.stt][5]) + 1) 
      def follow(self):
            while True:
                  if lock_thao_tac_dien_thoai.acquire(blocking=False):
                        try:
                              time.sleep(2)
                              danhsach[self.stt][8] = "Đang chuyển hướng..."
                              a = self.link.split("/")
                              formatlink = a[len(a)-1]
                              d.open_url(f"snapchat://add/{formatlink}")
                              time.sleep(5)
                              try:
                                    danhsach[self.stt][8] = 'Đang follow...'
                                    d.xpath('//*[@resource-id="subscribe-button"]').click(timeout = 3)
                                    danhsach[self.stt][8] = 'Đã ấn theo dõi'
                                    time.sleep(3)
                              except Exception as e:
                                    try:
                                          d.xpath('//*[@content-desc="Thêm"]').click(timeout = 3)
                                          time.sleep(3) 
                                          danhsach[self.stt][8] = 'Đã ấn theo dõi'
                                    except:
                                          pass
                              done = d.xpath('//*[@resource-id="snap-button"]').wait(3.0) or d.xpath('//*[@resource-id="unsubscribe-button"]').wait(3.0)
                              self.hoanthanh = None
                              if done == True:
                                    danhsach[self.stt][8] = 'theo dõi thành công'
                                    self.complete()
                              else:
                                    danhsach[self.stt][8] = 'theo dõi không thành công'
                                    self.skip_job()
                        except Exception as e:
                              danhsach[self.stt][8] = str(e)
                              time.sleep(7)
                        finally:
                              lock_thao_tac_dien_thoai.release()
                              break
                  else:
                        danhsach[self.stt][8] = 'Đang chờ lượt hành động...'
                        time.sleep(2)
      def main(self):
            self.get_acc()
            while True:
                  tiep = self.get_job()
                  if tiep != False:
                        self.follow()
class GolikeLINKEDIN:
      def __init__(self,authe):
            global chucnang
            self.stt = int(chucnang[0])
            chucnang.remove(chucnang[0])
            a = [str(self.stt + 1) , 'LINKEDIN' , f'{namedevice}','accgetjob','None' , "0" , "0","0" , "wait..."]
            danhsach.append(a)
            self.delay = [4, 5,5.5, 6,6.5, 7,7.5, 8.5, 9, 10]
            self.authe = authe
            self.headers = {
                  'accept': 'application/json, text/plain, */*',
                  'accept-language': 'vi',
                  'authorization': self.authe , 
                  'content-type': 'application/json;charset=UTF-8',
                  'origin': 'https://app.golike.net',
                  'priority': 'u=1, i',
                  'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-platform': '"Android"',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-site',
                  't': 'VFZSak1VMXFUVFJPUkVrd1RWRTlQUT09',
                  'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 CrKey/1.54.248666',
            }
            danhsach[self.stt][8] = 'Đang lấy acc...'
            try:
                  response = requests.get('https://gateway.golike.net/api/linkedin-account', headers=self.headers , impersonate = 'chrome').json()
            except:
                  pass
            self.idacc = response['data'][0]['id']
            self.accname = response['data'][0]['name']
            danhsach[self.stt][3] = self.accname
            danhsach[self.stt][4] = self.accname
            self.account_id = None
            self.account_username = None
      def get_job(self):
            danhsach[self.stt][8] = 'Đang lấy job...'
            params = {
                  'account_id': self.idacc,
            }
            try:
                  response = requests.get('https://gateway.golike.net/api/advertising/publishers/linkedin/jobs', params=params, headers=self.headers , impersonate = 'chrome').json()
            except:
                  pass
            status = response['status']
            try:
                  self.id  = response['data']["id"]
            except:
                  if 'linkedin' in response['message']:
                        danhsach[self.stt][8] = 'Tài khoản linkedin đã bị khoá'
                  else:
                        danhsach[self.stt][8] = 'Hết job đợi get job mới...'
                  time.sleep(40)
                  return False
            self.link = response['data']["link"]
            self.coin  = response['data']["price_after_cost"]
            self.object_id = response['data']["object_id"]
            self.type = response['data']["type"]
            danhsach[self.stt][8] = f"{status}|type:{self.type}|{self.coin}đ|{self.link}"
            return True
      def open_app(self):
            while True:
                  if lock_thao_tac_dien_thoai.acquire(blocking=False):
                        try:
                              time.sleep(2)
                              danhsach[self.stt][8] = "Đang chuyển hướng"
                              d.shell('am start -a android.intent.action.VIEW -d "'+self.link+'"com.linkedin.android')
                              time.sleep(4)
                              if self.type == "follow":
                                    try:
                                          done = d(text='Theo dõi').click_exists(timeout = 5.0)
                                          if done:
                                                danhsach[self.stt][8] = 'đã follow delay 8s...'
                                                time.sleep(8)
                                                self.succes()
                                                time.sleep(1)
                                          else:
                                                danhsach[self.stt][8] = 'follow không thành công'
                                                self.report()
                                                time.sleep(4)
                                    except:
                                          pass
                              if self.type == "like":
                                    self.report()
                        except Exception as e:
                                    danhsach[self.stt][8] = str(e)
                                    time.sleep(7)
                                    pass
                        finally:
                              lock_thao_tac_dien_thoai.release()
                              break
                  else:
                        danhsach[self.stt][8] = 'Đang chờ lượt hành động...'
                        time.sleep(2)
      def succes(self):
            json_data = {
                  'account_id': self.idacc,
                  'ads_id': self.id,
            }
            try:
                  response = requests.post(
                        'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs',
                        headers=self.headers,
                        json=json_data,
                        impersonate= 'chrome'
                  ).json()
            except:
                  pass
            if response['success'] == True:
                  coin = ''.join(c for c in danhsach[self.stt][7] if c.isdigit())
                  danhsach[self.stt][7] = str(int(coin) + int(self.coin)) + 'Đ'
                  danhsach[self.stt][6] = str(int(danhsach[self.stt][6]) + 1)
            else:
                  danhsach[self.stt][5] = str(int(danhsach[self.stt][5]) + 1)
            d.press('back')
      def report(self):
            json_data = {
                  'account_id': self.idacc,
                  'ads_id': self.id,
                  'object_id': self.object_id,
            }
            try:
                  response = requests.post(
                        'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs',
                        headers=self.headers,
                        json=json_data,
                        impersonate = 'chrome'
                  ).json()
            except:
                  pass
            danhsach[self.stt][5] = str(int(danhsach[self.stt][5]) + 1)
            danhsach[self.stt][8] = str(response['message'])
            d.press('back')
      def main(self):
            while True:
                  tiep = self.get_job()
                  if tiep != False:
                        self.open_app()
class pinterest:
      def __init__(self,authe):
            global chucnang
            self.stt = int(chucnang[0])
            chucnang.remove(chucnang[0])
            a = [str(self.stt + 1) , 'PINTEREST' ,'cookie','accgetjob','None' , "0" , "0","0" , "wait..."]
            danhsach.append(a)
            self.authe = authe
            headers = {
                  'accept': 'application/json, text/plain, */*',
                  'accept-language': 'vi',
                  'authorization': f'{self.authe}',
                  'content-type': 'application/json;charset=utf-8',
                  'origin': 'https://app.golike.net',
                  'priority': 'u=1, i',
                  'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
                  'sec-ch-ua-mobile': '?1',
                  'sec-ch-ua-platform': '"Android"',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-site',
                  't': 'VFZSak1FOUVXVEZQUkdzeVRuYzlQUT09',
                  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
            }
            self.headers = headers
            self.acc_id = None
      def get_acc(self):
            try:
                  response = requests.get('https://gateway.golike.net/api/pinterest-account', headers=self.headers,impersonate='chrome').json()
                  danhsach[self.stt][3] = str(response['data'][0]['name'])
                  self.acc_id = response['data'][0]['id']
                  danhsach[self.stt][4] = str(response['data'][0]['id'])
            except:
                  pass
      def get_job(self):
            
            params = {
                  'account_id': f'{self.acc_id}',
            }
            try:
                  response = requests.get('https://gateway.golike.net/api/advertising/publishers/pinterest/jobs', params=params, headers=self.headers ,
            
                  impersonate="chrome").json()
            except:
                  pass
            status = response["success"]
            try:
                  self.ads_id = response["lock"]["ads_id"]
                  self.account_id = response["lock"]["account_id"]
            except Exception as e:
                  danhsach[self.stt][8] = str(response["message"])
            type = response["lock"]["type"]
            self.link = response["data"]["link"]
            self.coin = response["data"]["price_after_cost"]
            self.object_id = response["lock"]["object_id"]
            danhsach[self.stt][8] = f"{status}|{type}|{self.link}|"
      def complete(self):
            
            json_data = {
                  'account_id': self.account_id,
                  'ads_id': self.ads_id,
            }
            try:
                  response = requests.post(
                  'https://gateway.golike.net/api/advertising/publishers/pinterest/complete-jobs',
                  headers=self.headers,
                  json= json_data,impersonate="chrome").json()
            except:
                  pass
            print(response["message"])
            danhsach[self.stt][8] = str(response['message'])
            danhsach[self.stt][7] = str(int(danhsach[self.stt][7]) + int(self.coin)) + 'Đ'
            danhsach[self.stt][6] = str(int(danhsach[self.stt][6]) + 1)
      def skip(self):
            
            json_data = {
                  'account_id': self.account_id,
                  'ads_id': self.ads_id,
                  'object_id': self.object_id,
            }
            try:
                  response = requests.post(
                        'https://gateway.golike.net/api/advertising/publishers/pinterest/skip-jobs',
                        headers=self.headers,
                        json=json_data,
                  ).json()
            except:
                  pass
            danhsach[self.stt][8] = response['message']
            danhsach[self.stt][5] = str(int(danhsach[self.stt][5])+1)

      def follow(self):
            
            
            headers = {
                  'accept': 'application/json, text/javascript, */*, q=0.01',
                  'accept-language': 'vi',
                  'content-type': 'application/x-www-form-urlencoded',
                  'origin': 'https://www.pinterest.com',
                  'priority': 'u=1, i',
                  'referer': 'https://www.pinterest.com/',
                  'screen-dpr': '2',
                  'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
                  'sec-ch-ua-full-version-list': '"Chromium";v="136.0.7103.116", "Google Chrome";v="136.0.7103.116", "Not.A/Brand";v="99.0.0.0"',
                  'sec-ch-ua-mobile': '?1',
                  'sec-ch-ua-model': '"Nexus 5"',
                  'sec-ch-ua-platform': '"Android"',
                  'sec-ch-ua-platform-version': '"6.0"',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-origin',
                  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
                  'x-app-version': 'bd365d3',
                  'x-b3-flags': '0',
                  'x-b3-parentspanid': '61968c3333e2277c',
                  'x-b3-spanid': '23006c09d925b9cd',
                  'x-b3-traceid': '61968c3333e2277c',
                  'x-csrftoken': '4f6d397399d68164b136e2f2c14d794a',
                  'x-pinterest-appstate': 'active',
                  'x-pinterest-pws-handler': 'www/[username].js',
                  # 'x-pinterest-source-url': '/symnakasya12/',
                  'x-requested-with': 'XMLHttpRequest',
                  'cookie': 'ar_debug=1; csrftoken=4f6d397399d68164b136e2f2c14d794a; _auth=1; _b="AYUv7Cc+nWVM+YW6WkbknBXMDtpWGM9XNyj562zqDevNLTvLVJ+oE9DA4GSzttoOyKs="; ar_debug=1; _pinterest_sess=TWc9PSZ0OVBzU09rZXlsaWQyVmdvNkhsWlpJeFZFNnBZV2VBNVE1dnYwTUhLaEVnU1RtUDNWNnhJQTF0QjN3aWk2REs0L0dUWnNONjdqZ3ZibTI5a2g4VHhwTkRuZER0RmFpMjRkWjUyNStnYmpMcU16WUV2MDV1ckNEODNNdHQ3SlZjZmxyR25MR1RucStCY0tGbjZaV0dxeC9MTG9EaWY5Vkk2SkNZWk5SS0gzSE9iaWxoY2FyNkdEZ0FxN21NOHNiTlh1QWt6R1JrQ2YrWDQ0K1JiMitGR0RDaWZCZi9EbzhWTVpqSDJVaVM2elVSZGtwdmFqM0lBVzR6NDNtZ2xjRVBseDFZcHBpQlQzN25nekxjejZrcXZOcVhMemRRR1FXRTAzU21MbHBYei9Ub2RyMFJxSWF1bEVtbnFvcWFKendnRGhBS3pkb1g2cHRraDlxRkFkbXNnVERiTHRrSHlndk1rSlpaUzJBTmpxSXFsMW41ZHZKUWpoeXhSdEsrdFN1algzVXJRU1JXdWlVdDhzWGxtMTg5alBwQXA4dUp3citjbUxHUFZhN3JKdWozb0orbmozY05YdnE2VGZNZ1UzejFQVllFZ0VJaGF4Y1V6YmJUVkJzVEwvWDB5NUZUSHBId0NoT1Y4WnBGNWtFTWtISFZhQ1BFa0R3YUdiYTVtSC92ZksvOFRkVnNFbEYxZzdpdDIxcWRqVXFtczJRWlNsc09HS2UvdUFXd1pVZDR4bmlaNzFwVk9TUTZrMUpTcytKUFcwM21zcmZkb2E0MDUyYTJkZ09OaHhGRlJ1MFFoNm1kbTkxbWFzbXo2UDBra29rMWswM2hZTlJXWm9yaUZCemEzTFhRQ1NWUVdDamo5WWNFSEZHTFM3S21Sc0hxelRnQUdac0t0RkJHUUJjakRSaVJ5WWlLcVFTQ1hhSmpQWFVMN0JLcjNWZ29Id1BmRVVqNjJKSGV0T0Z2U3g5TXp1OWlwME1hSERKNHhjTERKZ24vTGR4cGh1RGlxRmxaZFA2a241NWNpNkREN1VVelNYVS8zak9ad1dYZXBuR3FXYk5VR3RFUU0zMU1LTm1ZRTNUVUJOTThWdDZheVRhSEZvd2JHK3J2a3FGbkh2ejZ4R1YrUURvTFFVOWZ4STA3T0RGSWY0Q0VqTWxCZm44SU5OVkhaRDlBY01udVU1Z3J5L2J6Q3plc1M4MkhKWkFtQXBUdkppMTJ4TklicHdsdG9YMjQ1TnFhOHFWYTM5Zyt0YjJrdzY5aFlPRTlpcXI2UjZ1UmZ2WUpOSFp5eEhrczF2SksrWXp5OTQwNWpOTU0veVRvUjRaU05kS2loVVBLdjc3WVNwVHJ1a2ZVSmdBazZLU3BTWkRkN1QrNG1iM3VxV1gyVkY4Y1JWRGdoRzBxeUxwT0wrcXdOVHFWNDZJbXZTVnVEN3dQWFhnaG5neWdkVy9jWnB4cUhtMW9VZURwV1JwaXdaR0hhcTRrTFRoMWdKNjB1TDJhOTFRbzgvdmNGWVQ1L2w1T1JnNTB5dVE3enpZd3YrTTNqWVlyc0txVmcwK09jOFVoWVhhcDlkNU5sWVc1UmQwcWVJMXJwNUhPM0Nlb2xHTStia2EwMTlFdHlRRmRCTU5lenpCUGlzQUd1SXVkaEgvdTl5THU0WjB0T2tsR0Z6TnR3S3Bxd0N0dXJHMHJJNmR2RDZweEU4blMvaHJ5VVVtSnZFZGNOejdIQXJrOUlNQ0g3ZWF6VzZPU1RIbStUdm9xbXBoVXVVUk9vdUs1MXNLeGcvNHFicUR1OGl6bU0mY1d6dDRmT1NJTXhHeGFidHFrU1JuVGU3WVNRPQ==; __Secure-s_a=cmtjM1JQSWJkNkF6Y3VIL0JLWVloSllZQXJibkFVdGpXWkNJQ3RxeXF5SThnWndqVG41Q1R3Y2REdjhWK0g2QnMxVkRnWDZzOTJhanR3ZmJHQmJ4SlNScVV1UEdmb01LNmFkOTRCc2N6Nko2OFBrdzQyNGVVakhtWmNRS1dBeDFyU25ORkxsT2YvbjFDdUwzd052U2RydGV1R1l4bVJNWlYxT1N6dW5FdTF3VTRZVld2Zm45VVh6NXRQVG9ONWE4VCtoWHBYQzg4bTZDVTlmSHYwcjcxdlRUSXM0SVFWOE9hcTZzRkx1ZzlrcU9zeFlleXp2eWgzeTlSZkxxemlPdWt5d2JVT0NWaHBJbzlkeXluL1ErMCt1bUxheW4weXZSOC9rOEV5SnQzTEZObWpaS3JTcTJLMi9qeGZEMmlrbld1ZFJWSFBHK3hRdFpFYmg5U09FNGVnWU5INGlLZHJpdUN6ZUlrSVhVcjFrdTdOaFZtOG5FanNLLzF3dGVZcWM1a0FJWElzY1BFNHViV0N4WVZoZ2RSajhBd1lnUCtya3dDVFBzcWtneGhucllQY3BXNW1mYzlpNDd2djJhb1NuSThXYnd0eENsbHVneTd2WVdKTXF3UlBDZy96VzRQMnBZZmpaeDNNWG1NbndMa2cvTGZBSXJDMlpySDJZYitHVFl1bVlGZ0F5eWROYjRZNkFTdzdNeThQZG9jZWpuNWJtWlJ3dFpRWXhQRU56c2ZJMUVKYWRvdnNRRFUzZlNvUnBZNWJ6MnpGK0lyYjdSRVd1Skhxb2tuMGkzTTJLZ0NoajEwVjFjSHhTbG1YS2JKVXZWOVFaV2Yvd2tRS1lIc3BFMHUxN2s3NHh6VXZKWS9VemlDc295eWNydGZrKzVYcnoyMzR3QjQ1dCtyZHpobGpsbVgrYnpNQkhidXlWVVVkYm5GVlRma2lab3RrREZISUtBeHJDeXJsSStoSE9HV09JeVpIL201WTh5aXhVL2FOSkhsU0E5cHU1WllZRUxGeEFOK29rU0VPQkpTQk1vQnJ5bEJWTEJxQjJLRDY2SW5zbDMxeEpWSEpVTEtkN09MelVadXZLMnd0aVNQQ2syREhPQ2Qyam4rMno3TEpFV1lRL0dvNUFIUUw4bDhkdjliSUNtZXVOS2Iyb1FkVGNCaHdtQitkWDZhNVdDUUpNYkVpVjVxTEVNREF6a2lzR0VnUkRIWXlNc2orcHJuYmhoSVpwengrbVNZRzZiWCtjc093bUptZzJiVmJiVGdZaGU0VGpRSDBCNDRiVG9LYmhhcWIvODZMMFM2OGx3aFpaL0ozU1NVNEtza25nakVKOD0mRUtMeVV0UStGVWhMRXJnZndHQThqNFQ5dEFnPQ==; _pinterest_cm=TWc9PSZPVzAvVXNOZEtZdkFWNFRTbENQQ3Jpekx2NEhhZmJhM2krTUpCc1N5dS9OL1kyUzBLMEFVR00vcm00NGxhTnJWWG84aE01dzdvQjFCWTJYWlpqRXJWaDB1aXNteWV6UHo1REJrRXpYN0dHUll3MEpqZkxGRmJRMTliY0dkNmZaT01ud3h2NXdkcE9aK0QwQTR4cElZczU1MUQ5SlEzRms2Nlo0UXc3emFDU25DOWlaYnBSTEk2VGRlL3FHU2JGSlomU0MxUGEwQlhrTUNKNGJyWmxhNFkzelRYYlNnPQ==; _routing_id="ece325ca-f724-49c4-a596-53aba555f81c"; sessionFunnelEventLogged=1',
            }

            link = self.link.split("/")[len(self.link.split("/"))-2]
            
            data = {
                  'source_url': f"/{link}/",
                  'data': json.dumps({
                  "options": {
                        "user_id": self.object_id
                  },
                  "context": {}
                  })
            }
                  
            try:
                  response = requests.post(
                  'https://www.pinterest.com/resource/UserFollowResource/create/',
                  headers=headers,
                  data=data,impersonate="chrome"
                  ).json()
                  danhsach[self.stt][8] = f'{response}|Đã follow'
            except Exception as e:
                  danhsach[self.stt][8] = str(e)
      def main(self):
            while True:
                  self.get_acc()
                  try:
                        self.get_job()
                        time.sleep(1)
                        self.follow()
                        time.sleep(4)
                        self.complete()
                        time.sleep(5)
                  except Exception as e:
                        danhsach[self.stt][8] = "Hết job , chờ 5p get job lại...."
                        time.sleep(300)

def set_cursor_position(x, y):
    
    class COORD(Structure):
        _fields_ = [("X", c_short), ("Y", c_short)]

    handle = windll.kernel32.GetStdHandle(-11)
    windll.kernel32.SetConsoleCursorPosition(handle, COORD(x, y))
def get_console_size():
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines
    except:
        return 0,0
old_size = get_console_size()
def main():
      global old_size
      grlogo = logo()
      os.system('cls')
      console.print(grlogo)
      chucnang1 = lay_thong_tin()
      if chucnang1 != '':
            os.system('cls')
            console.print(grlogo)
            tk = ACCGOLIKE()
            auther = tk.ghi_acc()
            if len(chucnang1) == 1 and chucnang1[0] == '4':
                  pass
            else:
                  os.system('cls')
                  console.print(grlogo)
                  device()
                  os.system('cls')
                  console.print(grlogo)
      if chucnang == "":
            sys.exit(0)
      if '1' in chucnang1:
            ig = GolikeIG(auther)
            ig.get_acc()
            Thread(target=ig.main, daemon=True).start()

      if '2' in chucnang1:
            snap = GolikeSNAP(auther)
            Thread(target=snap.main, daemon=True).start()

      if '3' in chucnang1:
            linkedin = GolikeLINKEDIN(auther)
            Thread(target=linkedin.main, daemon=True).start()
      if '4' in chucnang1:
            pin = pinterest(auther)
            Thread(target=pin.main, daemon=True).start()
      os.system('cls')
      console.print(grlogo)
      cursor_y_start = 0
      while running:
            set_cursor_position(0, 0)
            new_size = get_console_size()
            table = giao_dien_chinh()
            set_cursor_position(0, 0)
            if new_size != old_size:
                  set_cursor_position(0, 0)
                  os.system('cls')
                  print("\033[?25l", end="")
                  old_size = os.get_terminal_size()
            set_cursor_position(0, 0)
            print("\033[?25l", end="")  # Ẩn con trỏ nhấp nháy
            set_cursor_position(0, cursor_y_start)
            group = Group(
                  logo(),
                  Padding(table, (1,new_size[0]-124 ,5,3))
            )
            console.print(group,end = set_cursor_position(0, 0))
            set_cursor_position(0, 0)
            time.sleep(2)
if __name__ == "__main__":
      signal.signal(signal.SIGINT, signal_handler)
      main()

