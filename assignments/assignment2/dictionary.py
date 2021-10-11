import datetime
urlDetails = {}



def shortenUrl(short_url, content):
    urlDetails[short_url] = {
        "long_url" : content["long_url"],
        "clicks"   : 0,
    }
    print(urlDetails)



def createUrl(short_url, content):
    content["clicks"] = 0
    urlDetails[short_url] = content
    print(urlDetails)


def updateUrl(bitlink, request_content):
    print(bitlink)
    content = urlDetails[bitlink]
    print("CONTENT")
    print(content)
    clicks = content["clicks"]
    print("CLICKS")
    print(clicks)
    urlDetails[bitlink] = request_content
    urlDetails[bitlink]["clicks"] = clicks
    urlDetails[bitlink]["created_at"] = datetime.datetime.now()
    print("URLDETAILS")
    print(urlDetails)
    return urlDetails[bitlink]


def getUrl(bitlink):
    clicks = urlDetails[bitlink]["clicks"]
    clicks = clicks + 1
    urlDetails[bitlink]["clicks"] = clicks
    print(urlDetails[bitlink]["clicks"])
    return urlDetails[bitlink]


def getClicks(bitlink, queryparam):
    click = urlDetails[bitlink]["clicks"]
    response = {"clicks" : click}
    print("INSIDE ********************************************************* GET CLICKS ********************************************")
    print(queryparam)
    print(urlDetails[bitlink])
    if int(queryparam) == 1:
        print("INSIDE ************************* QUERY PARAM ******************************** GET CLICKS ********************************************")
        date_created = urlDetails[bitlink]["created_at"]
        response["date_created"] = date_created
    print(response)
    return response


