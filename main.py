import nextcord
import json
from discord.ext import commands

with open("config.json", "r") as f:
    config = json.load(f)

def load_roles():
    return config.get("roles", [])


crydayx = commands.Bot(command_prefix="/" , intents=nextcord.Intents.all())

@crydayx.event
async def on_ready():
    print("Bot is ready : by Cryday#1337")
    await crydayx.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="Bot by:Cryday#1337"))

@crydayx.slash_command(description="กดที่นี่เพื่อรับยศ")
async def vfy(ctx):
    
    roles = load_roles()
    user = ctx.user

    valid_roles = []
    for role_id in roles:
        if role_id and role_id.strip():
            try:
                role = ctx.guild.get_role(int(role_id))
                if role:
                    if role.position >= user.top_role.position:
                        await ctx.send(f"บทบาท `{role.name}` มีลำดับชั้นสูงเกินกว่าที่คุณจะเพิ่มได้", ephemeral=True)
                    else:
                        valid_roles.append(role)
                else:
                    await ctx.send(f"บทบาทไอดี `{role_id}` ไม่มีอยู่ในเซิร์ฟเวอร์", ephemeral=True)
            except ValueError:
                await ctx.send(f"บทบาทไม่ถูกต้อง: `{role_id}`", ephemeral=True)

    if not valid_roles:
        if not roles:
            await ctx.send("ไม่ได้ถูกกําหนดบทบาท กรุณาติดต่อแอดมิน", ephemeral=True)
        await ctx.send("ไม่มีบทบาทที่ถูกต้องที่จะเพิ่ม", ephemeral=True)
        return

    for role in valid_roles:
        if role.position >= ctx.guild.me.top_role.position:
            await ctx.send(f"บทบาท `{role.name}` มีลำดับชั้นสูงเกินกว่าที่บอทจะจัดการได้", ephemeral=True)
            return

    for role in valid_roles:
        await user.add_roles(role)

    await ctx.send(f"เพิ่มบทบาทให้กับ {user.mention} สําเร็จ!", ephemeral=True)


crydayx.run(config["TOKEN"])