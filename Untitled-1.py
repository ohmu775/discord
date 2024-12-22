@client.event

async def on_message(message):

    if message.content.startswith ("!인증 "):
        if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by. 바코드 #1741")
            await message.author.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '역할 이름')
            await user.add_roles(role)

        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))

bot.run(MTMyMDIwOTgzOTI0NjU0NDk4Nw.GoxN1r.i1lwNqDTi3zXHDmp8ObPpn6BlRR24DmwAO3rGo)
