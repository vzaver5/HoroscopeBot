import requests
import os
import discord
from dotenv import load_dotenv

#Make instance of Discord Client
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#Method
def getDesc(sign):
    if(sign == 'aries'):
        signNum = 1
    elif(sign == 'taurus'):
        signNum = 2
    elif(sign == 'gemini'):
        signNum = 3
    elif(sign == 'cancer'):
        signNum = 4
    elif(sign == 'leo'):
        signNum = 5
    elif(sign == 'virgo'):
        signNum = 6
    elif(sign == 'libra'):
        signNum = 7
    elif(sign == 'scorpio'):
        signNum = 8
    elif(sign == 'sagittarius'):
        signNum = 9
    elif(sign == 'capricorn'):
        signNum = 10
    elif(sign == 'aquarius'):
        signNum = 11
    elif(sign == 'pisces'):
        signNum = 12
    #Get page from internet
    page = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign='+str(signNum))
    #page to string
    pageAsString = page.text
    locDesc = pageAsString.find('</strong>')
    locDesc = locDesc +12
    locDescEnd = pageAsString.find('</p>', locDesc)
    descString = pageAsString[locDesc:locDescEnd]
    descString = "\n" + descString
    return descString

#Method
def getHoroscope(sign):
    #Get page from internet
    page = requests.get('https://www.horoscope.com/star-ratings/today/' + sign)
    #Page to string
    pageAsString = page.text
    
    #Get locations of each String
    locOfSex = pageAsString.find('<h3>Sex')
    locEndSex = pageAsString.find('</h3>', locOfSex)
    
    locOfHustle = pageAsString.find('<h3>Hustle')
    locEndHustle = pageAsString.find('</h3>', locOfHustle)
    
    locOfVibe = pageAsString.find('<h3>Vibe')
    locEndVibe = pageAsString.find('</h3>', locOfVibe)
    
    locOfSuccess = pageAsString.find('<h3>Success')
    locEndSuccess = pageAsString.find('</h3>', locOfSuccess)
    
    #Get the string
    sexString = pageAsString[locOfSex:locEndSex]
    hustleString = pageAsString[locOfHustle:locEndHustle]
    vibeString = pageAsString[locOfVibe:locEndVibe]
    successString = pageAsString[locOfSuccess:locEndSuccess]
    
    #Iterate thru the strings and find how many stars you have filled
    sexStars = sexString.count("icon-star-filled highlight")
    hustleStars = hustleString.count("icon-star-filled highlight")
    vibeStars = vibeString.count("icon-star-filled highlight")
    successStars = successString.count("icon-star-filled highlight")

    yourHoroscope = "\nSex: " +  str(sexStars) + "/5\n" + "Hustle: " + str(hustleStars) + "/5\n" + "Vibe: " + str(vibeStars) + "/5\n"+ "Success: " + str(successStars) + "/5"
    print(yourHoroscope)
    return yourHoroscope


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content=='!aries':
        response = getDesc('aries') + getHoroscope('aries')
        await message.channel.send(response)
    if message.content=='!taurus':
        response =getDesc('taurus') +  getHoroscope('taurus')
        await message.channel.send(response)
    if message.content=='!gemini':
        response =getDesc('gemini') +  getHoroscope('gemini')
        await message.channel.send(response)
    if message.content=='!cancer':
        response =getDesc('cancer') +  getHoroscope('cancer')
        await message.channel.send(response)
    if message.content=='!leo':
        response =getDesc('leo') +  getHoroscope('leo')
        await message.channel.send(response)
    if message.content=='!virgo':
        response =getDesc('virgo') +  getHoroscope('virgo')
        await message.channel.send(response)
    if message.content=='!libra':
        response =getDesc('libra') +  getHoroscope('libra')
        await message.channel.send(response)
    if message.content=='!scorpio':
        response =getDesc('scorpio') +  getHoroscope('scorpio')
        await message.channel.send(response)
    if message.content=='!sagittarius':
        response =getDesc('sagittarius') +  getHoroscope('sagittarius')
        await message.channel.send(response)
    if message.content=='!capricorn':
        response =getDesc('capricorn') +  getHoroscope('capricorn')
        await message.channel.send(response)
    if message.content=='!aquarius':
        response =getDesc('aquarius') +  getHoroscope('aquarius')
        await message.channel.send(response)
    if message.content=='!pisces':
        response =getDesc('pisces') +  getHoroscope('pisces')
        await message.channel.send(response)
client.run(TOKEN)

