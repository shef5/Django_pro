from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from .forms import URLform
from .models import URL, API
from django.http import HttpResponse
from hashlib import sha1
import urllib.request
import urllib
import json

#import tkMessageBox
import requests 
import time
import csv
import hmac
import io
# Create your views here.
ACCESS_ID = "mozscape-7a6e66f8d3"
SECRET_KEY = "b327d72ac7071269f10af062d507ff45"
def home(request):
  form = URLform(request.POST or None)
  context = {
       "form": form,
  }
 


  if form.is_valid():
    instance = form.save(commit=False)
    myurl = form.cleaned_data.get("myurl")

    if not myurl:
      myurl = "New myurl" 
    instance.myurl = myurl
    price = form.cleaned_data.get("price")
    if not  price:
      price = "New price" 
    instance.price = price
    revenue = form.cleaned_data.get("revenue")
    if not revenue:
      myurl = "New revenue" 
    instance.revenue = revenue
    instance.save()
    pa = 0
    da = 0
    templist = []
    templist1 = []
    api_access = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    api_url = "http://lsapi.seomoz.com/linkscape/url-metrics/%s" % (myurl)
    print (api_url)
    newarray = []
    api_access.add_password(None, api_url, ACCESS_ID, SECRET_KEY)
    handler = urllib.request.HTTPBasicAuthHandler(api_access)
    opener = urllib.request.build_opener(handler)
    fetch = opener.open(api_url)
    result = fetch.read()
    print ("result:")
    abc = result.decode("utf-8")
    output = json.loads(abc)
    pa = output['upa']
    da = output['pda']
    print (json.dumps(output))
    URL(myurl=myurl,d_a=output['pda'],p_a=output['upa']).save()
    urlData2 = "http://api.semrush.com/analytics/v1/?key=0656b4e1326c95a92c56cc7f188b5a71&target="+myurl+"&type=backlinks&target_type=url&display_limit=4&export_columns=nofollow,source_url,external_num&display_sort=page_score_desc"
    #urlData2 = "http://api.semrush.com/?type=domain_organic&key=acdf8d05751c2b18b79f7dfcb62ba3b8&display_filter=%2B%7CPh%7CCo%7Cseo&output=json&display_limit=10&export_columns=Ph,Po,Nq,Tr&domain=blog.ahrefs.com&display_sort=tr_desc&database=us"
    urlData3 = "http://api.semrush.com/?type=domain_organic&key=0656b4e1326c95a92c56cc7f188b5a71&display_limit=10&export_columns=Nq&domain="+myurl+"&display_sort=tr_desc&database=us"
    #urlData3 = "http://api.semrush.com/analytics/v1/?key=acdf8d05751c2b18b79f7dfcb62ba3b8&target=blog.ahrefs.com&type=backlinks&target_type=root_domain"
    #urlData4 = "http://api.semrush.com/analytics/v1/?key=acdf8d05751c2b18b79f7dfcb62ba3b8&target="+myurl+"backlinks_anchors&target_type=root_domain"
    #weburl = urllib2.urlopen(urlData)
    # hdr = {'User-Agent': 'Mozilla/5.0'}
    # req = urllib2.Request(urlData2,headers=hdr)
    weburl2 = urllib.request.urlopen(urlData2)
    #print(weburl2)
    weburl3 = urllib.request.urlopen(urlData3)
    #weburl4 = urllib2.urlopen(urlData4)
    #data2 = weburl2.read()
    #data2 = weburl2.read()
    #jsonStr = data.decode("utf-8")
    #datareader1 = csv.reader(io.TextIOWrapper(weburl2))
    datareader1 = csv.reader(weburl2.read().decode('utf-8').splitlines())
    datareader2 = csv.reader(weburl3.read().decode('utf-8').splitlines())
    #datareader3 = csv.reader(weburl4.read().decode('utf-8').splitlines())
    mylist = []
    mylist1 = []
    total_val = 0
    data2 = list(datareader1)
    print (data2[1][0])
    text = data2[1][0]
    x=len(data2)
    print(x)
    words = text.split(";")
    print(words)
    data11 = list(datareader2)
    data11.pop(0)
    y=len(data11)
    for j in range(y):
      total_val = total_val + int(data11[j][0]) 
   
    #print (data11)
    #data11 = list(datareader3)
    #print (data11)
    counter = 0
    # print (data2[0][0])
    # print (data2[0][0])
    
    #print ("shef")
    # for r in datareader:
    # 	print (r)

    #for row in data2:
    #print("\n".join(row))
    #encoding = weburl.info().get_content_charset('utf-8')
    #parsed = json.loads(data.decode(encoding))
    #parsed = json.loads(jsonStr)
    our_pa =  0
    our_da = 0
    for i in range(x):
      text=data2[i][0]
      words = text.split(";")
      c = 1
      
      if words[2] < '40' and words[0] == 'True':
        c += 1
        templist.append(words[1])
      else:
        print('Hello')
      # expires = time.time() + 300
      # username = 'mayank'
      # stringtosign = ACCESS_ID+"\n"+str(expires)
      # binarySig = hmac.new(SECRET_KEY, stringtosign, sha1)
      # urlsafeSig = urllib2.urlopen("binarySig")
      # page = response.read(urlsafeSig)
      # cols = "34359738368"
      # requestUrl = "http://lsapi.seomoz.com/linkscape/url-metrics/?Cols="+cols+"&AccessID="+ACCESS_ID+"&Expires="+expires+"&Signature="+urlsafeSig
      # batchedDomains = item['url_from']
      # encodedDomains = json.dumps(batchedDomains)
      # resp = requests.post(encodedDomains, json=dict(username=username), verify=True)
      # data = resp.json()
      # print(data)   
    #   print(item['url_from'],item['nofollow'],item['links_external'])
    #   # API(apiurl=item['url_from'], nofollow=item['nofollow'], mainurl=myurl).save()
      api_access = urllib.request.HTTPPasswordMgrWithDefaultRealm()
      api_url = "http://lsapi.seomoz.com/linkscape/url-metrics/%s" % (words[1])
      #api_url = "http://lsapi.seomoz.com/linkscape/url-metrics/?Cols=103079215104&%s" % (words[1])
      print (api_url)
      newarray = []
      api_access.add_password(None, api_url, ACCESS_ID, SECRET_KEY)
      handler = urllib.request.HTTPBasicAuthHandler(api_access)
      opener = urllib.request.build_opener(handler)
      fetch = opener.open(api_url)
      result = fetch.read()
      print ("result:")
      abc = result.decode("utf-8")
      output = json.loads(abc)
      print (json.dumps(output))
      our_pa = our_pa + output['upa']
      print (our_pa)
      our_da = our_da + output['pda']
      API(apiurl=words[1], nofollow=words[0], mainurl=myurl, da=output['pda'],pa=output['upa']).save()
    print (our_pa)
    print (our_da)
    if our_pa/c > 20.0:
       counter += 1
       print ("counter 1")
    #total_val = 35760
    visitor_val = 0.2
    earnings = (total_val*0.3)*visitor_val
    if da*0.3 + pa*0.2 > 11:
      counter += 1
      print ("counter 2")
    if earnings > revenue:
      counter += 1
      print ("counter 3")
      print (revenue)
    if revenue*24 > price:
      counter += 1
      print ("counter 4")
    print (output['uu'])
    print (output['pda'])
    print (output['upa'])
    print (counter)
    #API(apiurl=words[1], nofollow=words[0], mainurl=myurl, da=output['pda'],pa=output['upa']).save()
      # API(da=output['pda'],pa=output['upa']).save()
 
      
        #API(apiurl=item['url_from'], nofollow=item['nofollow']).save()
      #templist1.append(item['nofollow'])
      
      #print(item['url_from'],item['nofollow'])
    # s = parsed['refpages']
    # root = tk.Tk()
    # root.withdraw()
    if counter == 4:
      i = 1
      print ('Perfect Buy')
      #tkMessageBox.showwarning('Box', 'PerfectBuy')

    if counter == 3:
      i = 2
      print ('Good Buy')
      #tkMessageBox.showwarning('Box', 'Good BUy')

    elif counter < 3:
      i = 3
      print ('Bad Buy')
      #tkMessageBox.showwarning('Box', 'BadBuy')
    #b = s['url_form']
    #print (parsed['refpages']['url_from'])
    #print(templist)
    #print(templist1)
    #print (json.dumps(parsed['refpages'][0]['url_from']))

    #print (json.dumps(parsed))
    context = {
        "title": "Thank You",
        "form": form,
    }





  # if request.user.is_authenticated() and request.user.is_staff:
  #   # for instance in SignUp.objects.all():
  #   #   print (instance.full_name)

  #   queryset = SignUp.objects.all().order_by('-timestamp')
    # context = {
    # "queryset" : templist,
    # "he" : templist1
    # }
    shef=API.objects.order_by('-id')[:4]
    shef5=URL.objects.order_by('-id')[:1]
    
    context={
    "main": shef5,
    "detail": shef,
    "image": i,
    }
  
  return render(request, "home.html", context)


def contact(request):
  title = 'Contact Us'
  form = ContactForm(request.POST or None)
  if form.is_valid():
    #print settings.SITE_ID
    # for key in form.cleaned_data:
    #   print (key)
    #   print (form.cleaned_data.get(key))
    email = form.cleaned_data.get("email")
    message = form.cleaned_data.get("message")
    full_name = form.cleaned_data.get("full_name")
    subject = "Site contact form"
    from_email = settings.EMAIL_HOST_USER
    to_email = [from_email, 'jaiswal.mayank42@gmail.com']
    contact_message = "%s: %s via %s"%(full_name, message, email)
    send_mail(subject, 
      contact_message,
       from_email, 
       [to_email], 
       fail_silently=False)


  context ={
        "form": form,
        "title": title,
  }
  return render(request, "forms.html", context)


def history(request):
  
  his=URL.objects.all().order_by('-id')
  his_url ={
  "url1": his
  }
  return render(request,"history.html", his_url)
    # his_url={
    # "url1": his
    #  }
    # print (his_url)
#return render(request,"history.html", {})