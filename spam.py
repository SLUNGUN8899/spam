import requests, sys, re
from concurrent.futures import ThreadPoolExecutor
 
 
def gas(no):
	s = requests.Session()
	url = "https://www.google.com/search?q=update.neptunegame.com&client=ms-android-xiaomi-rev1&sxsrf=ALiCzsbgHbZgXj26VJJk8_mT3Xrg9hX00g%3A1659658411180&ei=q2DsYs3SCofez7sPjPCNSA&oq=update.neptunegame.com&gs_lcp=ChNtb2JpbGUtZ3dzLXdpei1zZXJwEAMyBAgjECc6BwgjEOoCECc6CAgAEIAEELEDOgUIABCABDoOCC4QgAQQsQMQgwEQ1AI6BQguEIAEOggIABCxAxCDAToECC4QQzoECAAQQzoLCAAQgAQQsQMQgwE6CwguEIAEEMcBEK8BOgcIABCxAxBDOgoIABCxAxCDARBDOggIABCABBDJAzoECAAQHjoECAAQEzoGCAAQHhATOgYIABAeEAhKBQg-EgExSgQIQRgAUMEiWPRsYJJvaANwAHgAgAGFBIgBxCWSAQwwLjEwLjguMy4wLjGYAQCgAQGwAQ_AAQE&sclient=mobile-gws-wiz-serp"
	req = s.get(url).text
	token = re.findall(r"name=\"_token\" value=\"(.*?)\"", req)[0]
		
	data = {
	"_token":token,
	"msisdn":no
	}

	spam = s.post(url, data=data).text

	return spam

def main(cnt, no):
	jml = 0
	with ThreadPoolExecutor(max_workers=2) as e:
		futures = []
		for x in range(int(cnt)):
			futures.append(e.submit(gas, no))
		for i, future in enumerate(futures):
			jml += 1
			spam = future.result()
			if "Gagal!" or "dikirim" in spam:
				print(f"[{jml}] Spammed {no}")
			else:
				print("* ERROR *")
				sys.exit()
	print("")
 
if __name__ == '__main__':
	try:
		print("""\033[1m
 
 | AUTO JACKPOT
 | AUTO JACKPOT using api from IndiHome
 | Coded by Sipolan_maut - \033[31;2mIndo\033[39;2mSec\033[0;1m
 | ID: 0123456789xxxxx\033[0m
	""")

		no = input("ID    : ")
		if(no.isdigit()):
			pass
		else:
			print("Check your number id!")
			sys.exit()

		if len(no) < 9:
			print("Check your number id!")
			sys.exit()

		cnt = input("Count : ")

		if bool(cnt.isdigit()) == 0:
			print("Check your count!")
			sys.exit()
		else:
			print("")
			main(cnt, no)
	except(KeyboardInterrupt, EOFError):
		print("\n")
		sys.exit()
