from easygui import *
import sys
import os
import wget
import json
import webbrowser

def gui_vid():
    print(pictitle)
    print(information)
    webbrowser.open(video_url)
    image = "nasa.jpg"
    msg = (
        ("Today there's no picture !\n\n")
        + str(pictitle)
        + str("\n\n")
        + str(information)
        + str("\n\nWatch the video there : ")
        + str(video_url)
    )
    choices = choices = ["Ok", "Reload"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Ok":
        sys.exit(0)
    elif reply == "Reload":
        start()
    else:
        sys.exit(0)


def gui_pic():

    print(("\n\n") + str(information))
    print(("\n\n") + str("Watch HD image there : ") + str(hdurl) + str("\n\n"))
    image = "pic-of-day.jpg"
    msg = (
        ("Nasa Astronomy Picture of the Day : ")
        + str(pictitle)
        + str("\n")
        + str(information)
    )
    choices = choices = ["Ok", "Reload"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Ok":
        sys.exit(0)
    elif reply == "Reload":
        start()
    else:
        sys.exit(0)


def start():
    global information, SkyPic, pictitle, hdurl, video_url

    filePath = "pic-of-day.jpg"

    if os.path.exists(filePath):
        os.remove(filePath)
    else:
        print("")

    filepath1 = "picture.json"

    if os.path.exists(filepath1):
        os.remove(filepath1)
    else:
        print("")

    # Get your own api key here in the " " # https://api.nasa.gov/index.html#apply-for-an-api-key
    apikey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    url = "https://api.nasa.gov/planetary/apod?api_key=" + str(apikey)

    filename = wget.download(url, out="picture.json")

    with open("picture.json", "r") as f:  # open the json file
        pod = json.load(f)  # parse the json file

        information = pod["explanation"]
        SkyPic = pod["url"]
        pictitle = pod["title"]
        try:
            hdurl = pod["hdurl"]
        except:
            pass
        try:
            video_url = pod["url"]
        except:
            pass

        if pod["media_type"] == "image":  # check if this is an image today
            url1 = SkyPic
            filename1 = wget.download(
                url1, out="pic-of-day.jpg"
            )  # The picture is downloaded and named pic-of-day.jpg
            gui_pic()
        else:
            print(
                ("\nIt's a video today ! Watch the video there :\n\n")
                + str(video_url)
                + str("\n\n")
            )
            gui_vid()


start()
