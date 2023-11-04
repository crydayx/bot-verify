# BOT VERIFY SLASHCOMMAND
> บอทรับยศ ด้วย slash command

## **Feature**
- ใข้งานง่าย ด้วย python และ json
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