from __future__ import print_function
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from .forms import URLform
from .models import URL, API
from django.http import HttpResponse
import urllib2
import Tkinter as tk
import tkMessageBox
import json
import csv
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

    templist = []
    templist1 = []
    root = tk.Tk()
    root.withdraw()
    var = revenue*24
    if var > price:
      print("GoodBuy")
      tkMessageBox.showwarning('Box', 'GoodBuy')
    if var < price:
      print("BadBuy")
      tkMessageBox.showwarning('Box', 'BadBuy')
    urlData = "http://apiv2.ahrefs.com/?token=e00142a235d1f0fa3c81dca033026165772acc07&target="+myurl+"&limit=10&output=json&from=backlinks_one_per_domain&mode=subdomains&order_by=ahrefs_rank:desc&select=url_from,links_external,nofollow"
    #urlData2 = "http://api.semrush.com/?type=domain_organic&key=acdf8d05751c2b18b79f7dfcb62ba3b8&display_filter=%2B%7CPh%7CCo%7Cseo&output=json&display_limit=10&export_columns=Ph,Po,Nq,Tr&domain=blog.ahrefs.com&display_sort=tr_desc&database=us"
    #urlData3 = "http://api.semrush.com/analytics/v1/?key=acdf8d05751c2b18b79f7dfcb62ba3b8&target=blog.ahrefs.com&type=backlinks&target_type=root_domain"
    #urlData4 = "http://api.semrush.com/analytics/v1/?key=acdf8d05751c2b18b79f7dfcb62ba3b8&target="+myurl+"backlinks_anchors&target_type=root_domain"
    weburl = urllib2.urlopen(urlData)
    # hdr = {'User-Agent': 'Mozilla/5.0'}
    # req = urllib2.Request(urlData2,headers=hdr)
    #weburl2 = urllib2.urlopen(urlData2)
    #weburl3 = urllib2.urlopen(urlData3)
    #weburl4 = urllib2.urlopen(urlData4)
    data = weburl.read()
    #data2 = weburl2.read()
    jsonStr = data.decode("utf-8")
    #datareader = csv.reader(io.TextIOWrapper(weburl2))
    #datareader1 = csv.reader(weburl2.read().decode('utf-8').splitlines())
    #datareader2 = csv.reader(weburl3.read().decode('utf-8').splitlines())
    #datareader3 = csv.reader(weburl4.read().decode('utf-8').splitlines())

    #data2 = list(datareader1)
    #print (data2)
    #data11 = list(datareader2)
    #print (data11)
    #data11 = list(datareader3)
    #print (data11)
    
    
    #print ("shef")
    # for r in datareader:
    # 	print (r)

    #for row in data2:
    #	print("\n".join(row))
    #encoding = weburl.info().get_content_charset('utf-8')
    #parsed = json.loads(data.decode(encoding))
    parsed = json.loads(jsonStr)
  
    for item in parsed['refpages']:
      templist.append(item['url_from'])
      print(item['url_from'],item['nofollow'],item['links_external'])
      # API(apiurl=item['url_from'], nofollow=item['nofollow'], mainurl=myurl).save()
      api_access = urllib2.HTTPPasswordMgrWithDefaultRealm()
      api_url = "http://lsapi.seomoz.com/linkscape/url-metrics/%s" % (item['url_from'])
      print (api_url)
      newarray = []
      api_access.add_password(None, api_url, ACCESS_ID, SECRET_KEY)
      handler = urllib2.HTTPBasicAuthHandler(api_access)
      opener = urllib2.build_opener(handler)
      fetch = opener.open(api_url)
      result = fetch.read()
      print ("result:")
      abc = result.decode("utf-8")
      output = json.loads(abc)
      print (json.dumps(output))
      print (output['uu'])
      print (output['pda'])
      print (output['upa'])
      API(apiurl=item['url_from'], nofollow=item['nofollow'], mainurl=myurl, da=output['pda'],pa=output['upa']).save()
      # API(da=output['pda'],pa=output['upa']).save()
 
      
        #API(apiurl=item['url_from'], nofollow=item['nofollow']).save()
      #templist1.append(item['nofollow'])
      
      #print(item['url_from'],item['nofollow'])
    # s = parsed['refpages']
    
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
    shef=API.objects.order_by('-id')[:5]

    context={
    "detail": shef
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