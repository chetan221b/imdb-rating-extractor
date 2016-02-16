from bs4 import BeautifulSoup
import re
import requests
pname = raw_input('Please enter the name of the movie:\n')
name = pname.split()
try:
	url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=%s+%s+%s+%s+%s&s=all" % (name[0], name[1], name[2], name[3], name[4])
except:
	try:
		url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=%s+%s+%s+%s&s=all" % (name[0], name[1], name[2], name[3])
	except:
		try:
			url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=%s+%s+%s&s=all" % (name[0], name[1], name[2])
		except:
			try:
				url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=%s+%s&s=all" % (name[0], name[1])
			except:
				try:
					url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=%s&s=all" % (name[0])
				except:
					pass
fh = requests.get(url)
soup = BeautifulSoup(fh.content,'html.parser')
data = soup.find_all('td',{'class':'result_text'})
for item in data:
	data1=str(item)
	y = re.findall('tt[0-9]+',data1)
	try:
		new1= str(y[0])
	except:
		pass
	url = "http://www.imdb.com/title/%s" % (new1)
	ff= requests.get(url)
	soup1=BeautifulSoup(ff.content,'html.parser')
	data1 = soup1.find_all('div',{'class':'ratingValue'})
	data2 = soup1.find_all('h1',{'class':''},{'itemprop':'name'})
	for item1 in data1:
		for item2 in data2:
			print item2.text,item1.text
	
	
    





	

	
	
	





