import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO
import imageio
import numpy as np
from PIL import Image, ImageSequence
import requests

class Avatar(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kana_id = 857835279259664403
    @commands.command(aliases=['avatar', 'pfp'])
    async def av(self, ctx, m1: discord.Member = None, m2: discord.Member = None):
        kana = self.client.get_user(self.kana_id)
        #for single pfp
        if m1 == None and m2 == None:
            m1 = ctx.author
            if m1.is_avatar_animated():
                asset1 = m1.avatar_url_as(size=512)
                await asset1.save("avatar.gif")
                file = discord.File("avatar.gif")
                embed = discord.Embed(color=0x2e69f2)
                embed.set_image(url="attachment://avatar.gif")
                embed.set_footer(
                text=f"Kanna Chan",
                icon_url=kana.avatar_url,
            )
            else:
                asset1 = m1.avatar_url_as(size=512)
                await asset1.save("avatar.png")
                file = discord.File("avatar.png")
                embed = discord.Embed(color=0x2e69f2)
                embed.set_image(url="attachment://avatar.png")
                embed.set_footer(
                text=f"Kanna Chan",
                icon_url=kana.avatar_url,
                )
            await ctx.send(embed=embed, file = file)
        elif m1 != None and m2 == None:
            if m1.is_avatar_animated():
                asset1 = m1.avatar_url_as(size=512)
                await asset1.save("avatar.gif")
                file = discord.File("avatar.gif")
                embed = discord.Embed(color=0x2e69f2)
                embed.set_image(url="attachment://avatar.gif")
                embed.set_footer(
                text=f"Kanna Chan",
                icon_url=kana.avatar_url,
            )
            else:
                asset1 = m1.avatar_url_as(size=512)
                await asset1.save("avatar.png")
                file = discord.File("avatar.png")
                embed = discord.Embed(color=0x2e69f2)
                embed.set_image(url="attachment://avatar.png")
                embed.set_footer(
                text=f"Kanna Chan",
                icon_url=kana.avatar_url,
                )
            await ctx.send(embed=embed, file=file)
        elif m2 == m1:
            if m1.is_avatar_animated():
                asset1 = m1.avatar_url_as(size=512)
                await asset1.save("avatar.gif")
                file = discord.File("avatar.gif")
                embed = discord.Embed(color=0x2e69f2)
                embed.set_image(url="attachment://avatar.gif")
                embed.set_footer(
                text=f"Kanna Chan",
                icon_url=kana.avatar_url,
            )
            else:
                asset1 = m1.avatar_url_as(size=512)
                await asset1.save("avatar.png")
                file = discord.File("avatar.png")
                embed = discord.Embed(color=0x2e69f2)
                embed.set_image(url="attachment://avatar.png")
                embed.set_footer(
                text=f"Kanna Chan",
                icon_url=kana.avatar_url,
                )
            await ctx.send(embed=embed, file=file)

        #for shared pfp
        elif m2 != m1:                                
            bg = Image.open("./images/img.png")
            asset1 = m1.avatar_url_as(size=512)
            asset2 = m2.avatar_url_as(size=512)
            data1 = BytesIO(await asset1.read())
            data2 = BytesIO(await asset2.read())
            pfp1 = Image.open(data1)
            pfp2 = Image.open(data2)
            pfp1 = pfp1.resize((500, 500))
            pfp2 = pfp2.resize((500, 500))

            bg.paste(pfp1, (0, 0))
            bg.paste(pfp2, (500, 0))

            if m1.is_avatar_animated() and m2.is_avatar_animated():
                im1 = "pfp1.gif"
                im2 = "pfp2.gif"
                await m1.avatar_url.save(im1)
                await m2.avatar_url.save(im2)
                def resize(image):
                    size = 200, 200
                    im = Image.open(image)
                    frames = ImageSequence.Iterator(im)
                    def thumbnails(frames):
                        for frame in frames:
                            thumbnail = frame.copy()
                            thumbnail.thumbnail(size, Image.ANTIALIAS)
                            yield thumbnail
                    frames = thumbnails(frames)
                    om = next(frames)
                    om.info = im.info
                    return om, frames
                image1, frame1 = resize(im1)
                image1.save("pp1.gif", save_all=True, append_images=list(frame1), loop=0)
                image2, frame2 = resize(im2)
                image2.save("pp2.gif", save_all=True, append_images=list(frame2), loop=0)
                av1 = imageio.get_reader("pp1.gif")
                av2 = imageio.get_reader("pp2.gif")
                all_frames = min(av1.get_length(), av2.get_length()) 
                new_gif = imageio.get_writer('final.gif')
                c = 0
                for frame_number in range(all_frames):
                    try:
                        img1 = av1.get_next_data()
                        img2 = av2.get_next_data()
                        new_image = np.hstack((img1, img2))
                        new_gif.append_data(new_image)
                    except ValueError:
                        await ctx.send("Their is large difference in size of the avatars, so Kanna is not able to align them :(")
                        c = c + 1
                        break
                if c == 0:
                    gif = Image.open("./final.gif")
                    framess = [frame.copy() for frame in ImageSequence.Iterator(gif)]
                    framess[0].save('shared.gif',
			        save_all = True, append_images = framess[1:],
			        optimize = False, duration = 100, loop=0)
                    file = discord.File('shared.gif')
                    embed=discord.Embed(color=0x2e69f2)
                    embed.set_image(url="attachment://shared.gif")
                    embed.set_footer(
                    text=f"Kanna Chan",
                    icon_url=kana.avatar_url,
                    )
                    await ctx.send(embed=embed, file=file)
            else:
                bg.save("avatar.png")
                file = discord.File("avatar.png")
                embed=discord.Embed(color=0x2e69f2)
                embed.set_image(url="attachment://avatar.png")
                embed.set_footer(
                text=f"Kanna Chan",
                icon_url=kana.avatar_url,
                )
                await ctx.send(embed=embed, file=file)
    
    @commands.command(aliases=['bn', 'bnr'])
    async def banner(self, ctx, mem: discord.User = None):
        kana = self.client.get_user(self.kana_id)
        if mem == None:
            mem = ctx.author
        req = await self.client.http.request(discord.http.Route("GET", "/users/{uid}", uid=mem.id))
        banner_id = req["banner"]
        if banner_id:
            banner_url = f"https://cdn.discordapp.com/banners/{mem.id}/{banner_id}?size=1024"
        response = requests.get(banner_url)
        img = Image.open(BytesIO(response.content))
        if img.is_animated == True:
            emb = discord.Embed(color=0x2e69f2)
            framess = [frame.copy() for frame in ImageSequence.Iterator(img)]
            framess[0].save('banner.gif',
			        save_all = True, append_images = framess[1:],
			        optimize = False, duration = 100, loop=0)
            file=discord.File("banner.gif")
            emb.set_image(url="attachment://banner.gif")
            emb.set_footer(
                text=f"Kanna Chan",
                icon_url=kana.avatar_url,
            )
            await ctx.send(embed=emb, file=file) 
        else:
            emb = discord.Embed(color=0x2e69f2)
            img.save("banner.png")
            file=discord.File("banner.png")
            emb.set_image(url="attachment://banner.png")
            emb.set_footer(
                text=f"Kanna Chan",
                icon_url=kana.avatar_url,
            )
            await ctx.send(embed=emb, file=file)
        

def setup(client):
    client.add_cog(Avatar(client))
    print(">> Avatar loaded")
