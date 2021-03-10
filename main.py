import discord
from discord import Embed, File, DMChannel
import time
import os
import time
from discord.ext import tasks
import random
intents = discord.Intents.all()
client = discord.Client(intents=intents)
interval = 30


#complimenten
def randomZin():
  data1 = ["penis", "trui", "identiteit","schoen","kledingstijl","geslachtsdeel","gezicht"]
  voorwerp = random.choice(data1)
  data4 = ["lekker", "mooi", "geil", "geweldig","schattig","uitnodigend","kalmerend","heel leuk"]
  bevinding = random.choice(data4)

  data2 = ["Duits","Engels","Nederlands","CKV","godsdienst","mentorles","meneer Kinds","wiskunde","online lessen","LO"]
  vak = random.choice(data2)

  data3 = ["fietsen","rukken","neuken","poepen","janken","zeuren","school","meneer Kinds pijpen","wiskunde","economie","het leven","wiskunde","Duits","Nederlands","voetballen","tennis spelen"]
  actie = random.choice(data3)

  data5 = ["prestaties","geaardheid","positiviteit","kennis","slimheid","geweldige moeder","lengte","betrouwbaarheid"]
  reden = random.choice(data5)

  data6 = ["avontuurlijk","braaf","optimistisch","georganiseerd","betrouwbaar","gul","geduldig","aardig","creatief","enthousiast","eerlijk","proactief","helpvol","flexibel","mededogend","vriendelijk","loyaal","wijs","blij"]
  eigenschap = random.choice(data6)

  data7 = ["geil","blij","vrolijk","opgewonden","verrast","optimistisch","opgewekt","gelukkig"]
  gemaakt = random.choice(data7)

  totaal = [
" jouw " + voorwerp + " is " + bevinding +"!",
" je doet altijd zo goed je best bij "+ vak + "!",
" je bent echt goed in " + actie +"!",
" je inspireert ons door je " + reden + "!",
" je bent echt " + eigenschap + "!" ,
" je maakt ons altijd " + gemaakt + "!"

]
  zin = random.choice(totaal)
  return zin

##{randomMember.mention}

@tasks.loop(minutes=30)
async def complimenten():
    uitkomst = randomZin()
    channel = client.get_channel(818864817447239711)
    randomMember = random.choice(channel.guild.members)
    await channel.send(f"{randomMember.mention}," + uitkomst)

@client.event
async def on_ready():
    complimenten.start()
    print('We have logged in as {0.user}'.format(client))  
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Pornhub.com"))
    kanaal = client.get_channel(804013256905195582)
    await kanaal.send("**MeesBot** is **online**!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if isinstance(message.channel, DMChannel):
      if len(message.content) < 50:
        await message.channel.send("Bericht moet langer dan 50 karakters zijn!")
      else:
        anaal = client.get_channel(800692834449227776)
        berichtje = Embed(title="Nieuw bericht voor de moderators!",colour=0xDD2222)
        berichtje.set_thumbnail(url=message.author.avatar_url)
        fields = [("Gebruiker", message.author.display_name, False),
        ("Bericht", message.content, False)]
        
        for name, value, inline in fields:
          berichtje.add_field(name=name, value=value, inline=inline)
        await anaal.send(embed=berichtje)
        await message.channel.send("Je bericht is naar de moderators gestuurd!")



    elif message.content.startswith('?hello'):
      await message.channel.send('Hello!')
    elif message.content.startswith('?complimenten'):
      if message.content.startswith('?complimenten start'):
        complimenten.start()
        await message.channel.send("Complimenten staan aan en worden om de **" + str(interval) + "** minuten gestuurd!")
      elif message.content.startswith('?complimenten stop'):
        await message.channel.send("Complimenten staan uit!")
        complimenten.cancel()
      else:
        return
    elif message.content.startswith('?commands'):
      embedVar = discord.Embed(title="MeesBot Commands", description="Dit zijn de commando's waar MeesBot op zal reageren!", color=0x00ff00)
      embedVar.add_field(name="?hello", value="Gebruik dit commando om te kijken of MeesBot werkt/online is", inline=False)
      embedVar.add_field(name="?complimenten start", value="Start de verspreiding van complimenten", inline=False)
      embedVar.add_field(name="?complimenten stop", value="Stop de verspreiding van complimenten", inline=False)
      embedVar.add_field(name="?interval", value="Bekijk de tijd tussen complimenten (de waarde veranderen werkt op dit moment (nog) niet)", inline=False)
      await message.channel.send(embed=embedVar)
    elif message.content.startswith('?interval'):
      await message.channel.send("Interval is " + str(interval) + " minuten.")
    else:
      return
      

      
client.run('NDgxNzk1MTE0ODM5MTc5Mjk0.W31Qqg.M8kaWQiCOGj1TIoQoK1H2UZvq7g')