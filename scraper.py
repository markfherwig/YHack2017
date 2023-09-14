import urllib

urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'

file = urllib.URLopener()

for year in range(2009, 2018):
    for month in range(1, 13):
        name = "RS_" + str(year) + "-" + str(month).zfill(2) + ".bz2"
        url = "https://files.pushshift.io/reddit/submissions/" + name
        
        try:
            file.retrieve(url, name)
            print(name)
        except IOError:
            print(url + " failed.")


# from urllib import request
# user_agents = [ 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11', 'Opera/9.25 (Windows NT 5.1; U; en)', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)', 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12', 'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9']
# for year in range(2009, 2018):
#     for month in range(1, 12):
#         name = "RS_" + str(year) + "-" + str(month).zfill(2) + ".bz2"
#         url = "https://files.pushshift.io/reddit/submissions/" + name
#         print(url)
#         # try:
#         request.urlretrieve(url, name, user_agents)
#         print(name)
#         # except IOError:
#             # print(url + " failed.")


#https://files.pushshift.io/reddit/submissions/RS_2006-01.bz2

