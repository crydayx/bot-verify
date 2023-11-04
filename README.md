# BOT VERIFY SLASHCOMMAND
> บอทรับยศ ด้วย slash command

![Image](https://cdn.discordapp.com/attachments/1148622219396796559/1170377224092922038/image.png?ex=6558d1ba&is=65465cba&hm=3244ec0bf2eb0b77e18a988df8693b9ea9355a8378077f6fa41b58b09dfefd69&)

![Image](https://cdn.discordapp.com/attachments/1148622219396796559/1170377604428222576/image.png?ex=6558d215&is=65465d15&hm=506b5aedfefba6837ee7bd35e8bb88730f823dce93bb83757a975d201a400522&)

## **Feature**
- ใช้งานง่าย ด้วย python และ json
- มีระบบจัดการกับข้อผิดพลาด
- ปรับแต่งได้ตามต้องการ รูปแบบ : source code

## **Requirement**

1. Discord Bot Token **[Guide](https://discordjs.guide/preparations/setting-up-a-bot-application.html#creating-your-bot)**  
   1.1. เปิดใช้งาน 'Message Content Intent' ใน Discord Developer Portal

   ![Image](https://cdn.discordapp.com/attachments/1095025373986685022/1102635940528271390/image.png)
    
2. install python **[Download here!](https://www.python.org)** <br>


## Configuration

แก้ไขข้อมูลในไฟล์ `config.json`

```
{
    "TOKEN":"ใส่ TOKEN บอทของคุณ",
    
    "roles": [
        "ID ยศที่ต้องการให้"
    ]
}
```
หากต้องการกําหนดมากกว่าหนึ่งบทบาท สามารถเพิ่มไอดีใน array ได้ตามต้องการ

## Run

ติดตั้งไลบรารีที่จำเป็น
```
pip install nextcord
```

รันบอทด้วย `py main.py`

# Code by CrydayX
โค้ดมีปัญหา discord: crydayx