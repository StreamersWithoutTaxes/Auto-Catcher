#3/2/2022
#discord script
import discord
# to randomize time
import random
# to randomize delay
import time
# download image script
import requests
import shutil
# md5 hash it
import hashlib
import io
from PIL import Image
# misspell words
from string import ascii_lowercase as al
from random import choice, randrange

#connect to discord
client = discord.Client()
@client.event
async def on_ready():
    print("Main user activated: {0.user}".format(client))

#channel ids
ID = ['920729529566236722']
#ID2 = etcetc

@client.event
async def on_message(message):
    #will multiply catching time by this value
    timeMultiplier = 2.5
    # get emebed
    channel = client.get_channel(ID)
    embed = message.embeds
    embeds = message.embeds
    # get embed url
    for embed in embeds:
        #get embed info
        wildPoke = embed.to_dict()
        #put all your ID's in this list
        if message.channel.id in ID:
            #check if embed has the cathc poke text
            if "Guess the pokémon" in str(wildPoke):
                print("---------------------")
                print("poke detected")
                #make sure embed isnt empty
                if len(message.embeds) > 0:
                    _embed = message.embeds[0]
                    #get image url
                    if not _embed.image.url == discord.Embed.Empty:
                        print("embed not empty")
                        image = _embed.image.url
                        print("image url: " + image)
                        channel = message.channel
                        # download embed url image
                        image_url = image
                        #name of file whjen downloaded
                        filename = "pokemoncollier.png"
                        r = requests.get(image_url, stream=True)
                        #download if its able to/output error if not
                        if r.status_code == 200:
                            r.raw.decode_content = True
                            with open(filename, "wb") as f:
                                shutil.copyfileobj(r.raw, f)
                            print("Image sucessfully Downloaded: ", filename)
                        else:
                            print("Image Couldn't be retreived")
                        # hash img
                        img = Image.open("pokemoncollier.png")
                        m = hashlib.md5()
                        with io.BytesIO() as memf:
                            img.save(memf, "PNG")
                            data = memf.getvalue()
                            m.update(data)
                            imgHash = m.hexdigest()
                            print("image hash is: " + imgHash)
                            # all poke hashes
                            pokeName = pokemon[imgHash]
                            print("the pokename is: " + pokeName)
                            # count letters in pokename
                            pokeCount = len(str(pokeName))
                            print("amount of letters in poke name: " + str(pokeCount))
                            # figure out the time to catch it
                            # time 2 is the letters multipled by .3, time3 is time2 increased by 70%- this gives us a range.
                            time2 = pokeCount * 0.3
                            time3 = time2 * 1.4
                            print("time one: " + str(time2) + " and time2: " + str(time3))
                            # picking a time between the two vars above
                            randTime = random.uniform(time2, time3)
                            # time it takes to catch after a messup
                            backupRandTime = randTime * 0.6
                            # if the time is longer then 1.83951 seconds it will default to a time in the below range
                            if randTime > 2.13951:
                                timeHolder = 1.42907
                                timeHolder2 = 1.9312
                                randTime = random.uniform(timeHolder, timeHolder2)
                                print("the original time was too long, new final time is: "+ str(randTime))                                   
                            #used to ping OTHER users for their shinies in other servers
                            #copy here
                            peoplesShinies = ['563850c3daebec8706f17ebf31f816f0',]
                            elif (message.channel.id == ID2) and (imgHash in peoplesShinies):
                                  if imgHash == '563850c3daebec8706f17ebf31f816f0':
                                      time.sleep(randTime)
                                      userID = '<@CLIENT ID>'                                      
                                      await channel.send(userID)
                            #end here
                            #if catching on other servers impliment chance for messups
                            elif message.channel.id in ID:
                                print("caught on: " + message.guild.name + " : in channel : " + message.channel.mention)
                                # chance to misspell words
                                spellChance = random.uniform(0, 100)
                                time multiplier to easily change output time
                                #.5% chance to misspell 3 letters
                                if spellChance > 0 and spellChance < .5:
                                    nameHolder = pokeName
                                    for i in range(3):
                                        pokeName = pokeName.replace(choice(list(pokeName)), choice(al))
                                    pokeName = list(pokeName)
                                    int1 = randrange(0, len(pokeName))
                                    int2 = randrange(0, len(pokeName))
                                    pokeName[int1], pokeName[int2] = (pokeName[int2],pokeName[int1])
                                    print("pokemon not caught - 3 letters misspelled")
                                    randTime = randTime * timeMultiplier
                                    print("Sleeping for: " + str(randTime))
                                    time.sleep(randTime)
                                    await channel.send("p!c " + "".join(pokeName))
                                    backupRandTime = randTime * 0.7
                                    print("messed up, waiting: " + str(backupRandTime))
                                    time.sleep(backupRandTime)
                                    await channel.send("p!c " + nameHolder)
                                #1% chance to misspell 2 letters
                                elif spellChance > .501 and spellChance < 1.5:
                                    nameHolder = pokeName
                                    for i in range(2):
                                        pokeName = pokeName.replace(choice(list(pokeName)), choice(al))
                                    pokeName = list(pokeName)
                                    int1 = randrange(0, len(pokeName))
                                    int2 = randrange(0, len(pokeName))
                                    pokeName[int1], pokeName[int2] = (pokeName[int2],pokeName[int1])
                                    randTime = randTime * timeMultiplier
                                    print("Sleeping for: " + str(randTime))
                                    time.sleep(randTime)
                                    await channel.send("p!c " + "".join(pokeName))
                                    print("pokemon not caught - 2 letters misspelled")
                                    backupRandTime = randTime * 0.7
                                    print("messed up, waiting: " + str(backupRandTime))
                                    time.sleep(backupRandTime)
                                    await channel.send("p!c " + nameHolder)
                                #1.5% chance to misspell 1 letters
                                elif spellChance > 1.501 and spellChance < 3:
                                    nameHolder = pokeName
                                    for i in range(1):
                                        pokeName = pokeName.replace(choice(list(pokeName)), choice(al))
                                    pokeName = list(pokeName)
                                    int1 = randrange(0, len(pokeName))
                                    int2 = randrange(0, len(pokeName))
                                    pokeName[int1], pokeName[int2] = (pokeName[int2],pokeName[int1])
                                    randTime = randTime * timeMultiplier
                                    print("Sleeping for: " + str(randTime))
                                    time.sleep(randTime)
                                    await channel.send("p!c " + "".join(pokeName))
                                    print("pokemon not caught - 1 letters misspelled")
                                    backupRandTime = randTime * 0.7
                                    print("messed up, waiting: " + str(backupRandTime))
                                    time.sleep(backupRandTime)
                                    await channel.send("p!c " + nameHolder)
                                #5% chance to remove a letter
                                if spellChance > 3.01 and spellChance < 7:
                                    nameHolder = pokeName
                                    pokeName = pokeName[:-1]
                                    print("Sleeping for: " + str(randTime))
                                    randTime = randTime * timeMultiplier
                                    time.sleep(randTime)
                                    await channel.send("p!c " + str(pokeName))
                                    print("pokemon not caught - 1 letter removed")
                                    backupRandTime = randTime * 0.7
                                    print("messed up, waiting: " + str(backupRandTime))
                                    time.sleep(backupRandTime)
                                    await channel.send("p!c " + nameHolder)
                                #1% chance to type random letters before catching it
                                elif spellChance > 7.01 and spellChance < 8:
                                    randomLetters = random.choice(string.ascii_letters[int(pokeCount)])
                                    await channel.send("p!c " + randomLetters)
                                    backupRandTime = randTime * 0.7
                                    print("messed up, waiting: " + str(backupRandTime))
                                    time.sleep(backupRandTime)
                                    await channel.send("p!c " + pokeName)                                   
                                # the rest is normal catches                                    
                                else:
                                    randTime = randTime * timeMultiplier
                                    print("Sleeping for: " + str(randTime))
                                    time.sleep(randTime)
                                    await channel.send("p!c " + pokeName)
                                    print("pokemon caught")
                                
                                #actions to possible take AFTER catching
                                actionChance = random.uniform(0, 100)
                                #1% chance to check market for last caught poke
                                if actionChance > 1 and actionChance < 2:
                                    randTime = randTime * 2
                                    print("sleeping for " + str(randTime))
                                    time.sleep(randTime)
                                    print("CHECKING MARKET")
                                    await channel.send("p!m s --n " + pokeName)
                                #4% chance to type p!i l after catching a poke
                                if actionChance > 2.01 and actionChance < 6:
                                    randTime = randTime * 2
                                    print("sleeping for " + str(randTime))
                                    time.sleep(randTime)
                                    print("CHECKING POKE STATS")
                                    await channel.send("p!i l")
                                #2% chance to type p!pk after catching a poke
                                elif actionChance > 12.01 and actionChance < 14:
                                    randTime = randTime * 2
                                    print("sleeping for " + str(randTime))
                                    time.sleep(randTime)
                                    print("CHECKING ALL POKES")
                                    await channel.send("p!pk")
                                #4% chance to claim all dex 
                                elif actionChance > 17.01 and actionChance < 21:
                                    randTime = randTime * 2
                                    print("sleeping for " + str(randTime))
                                    time.sleep(randTime)
                                    print("CLAIMING DEX")
                                    await channel.send("p!dex claim all")                               
                                print("~~~~waiting for next pokemon~~~~")
#bot token
client.run("")
