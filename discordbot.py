import discord
import os
from dotenv import load_dotenv
load_dotenv()

import random
from dotenv import load_dotenv
from discord.ui import Button, View
from discord import ButtonStyle
from discord.ext import commands
from discord.utils import get


TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents) # client 생성. 디스코드와 연결

# 콜백 스타일: 콜백은 기본적으로는 무엇인가 일어났을때 호출되는 기능
@client.event # 데코레이터 - 이벤트 등록
async def on_ready(): # 봇이 로깅을 끝내고 여러가지를 준비한 뒤 호출
    print(f'We have logged in as {client.user}1111')

@client.event
async def on_message(message): # 봇이 메시지를 받았을 때 호출됩니다
    
    if message.author == client.user: # 봇이 보낸 메세지면 무시
        return

    if message.content.startswith('#hello'): # 메세지가 #hello로 시작하는 경우 
        await message.channel.send(f'{message.author.mention}, hello!') # 답장 x
    elif message.content.startswith('#안녕하세요'): # 메세지가 #안녕하세요 로 시작하는 경우
        await message.channel.send(f'{message.author.display_name}, 안녕하세요!', reference=message) # 답장
    elif message.content.startswith('❈다이스'): # 메세지가 dice로 시작하는 경우
        dice_result = str(random.randint(1,100)) # 1~100 랜덤 선택 (1d100)
        await message.channel.send(f'다이스를 굴리자... <{dice_result}>이 나왔다.', reference=message) # 답장 o
    elif message.content.startswith('❈가챠'): # 메세지가 ❈가챠 로 시작하는 경우
        dice_result = str(random.choice(['모르는 이름이 써진 네임택', '티 타임용 쿠키세트', '작은 씨앗', '챙 넓은 모자', '고래 인형', '워터볼', '검은 강아지 인형', '동화책 [어느 숲속 이야기]', '텔 원석', '건네 준 사람과의 추억이 재생되는 거울 모양 마도구', '민들레 홀씨', '새장', '모조 다이아', '새하얀 천', '금박장식 비녀', '고사성어 사전', '별자리 무드등', '「쉽게 배우는 마공학 이론」', '새하얀 양 인형', '실타래', 'SEI☆의 사인지', '무선마이크', '목이 기다란 도마뱀 인형', '공룡이 그려진 동화책', '낡은 누더기 옷', '행운 기원 팔찌', '기념품가게 팔찌', '향수', '화상 연고', '의료용 안대', '목화 다발', '자개 장식', '공단 리본', '레이스가 달린 원피스', '물감', '긴 천', '편지지 세트', '알록달록한 펜', '애벌레 인형', '발냄새 나는 양말'])) # 1~100 랜덤 선택 (1d100)
        await message.channel.send(f'달각 달각, 가챠 기계에서 나온 것은…… <{dice_result}>…!', reference=message) # 답장 o
    elif message.content.startswith('#버튼'):
         button1 = Button(label="하이", emoji="❤", style = ButtonStyle.primary)
         button2 = Button(label="로우", emoji="💛", style = ButtonStyle.danger)
    
         async def button1_callback(intents=intents):
            dice_result = str(random.choice(['하이','로우']))
            await message.channel.send(f'{dice_result}')

         async def button2_callback(intents=intents):
            dice_result = str(random.choice(['하이','로우']))
            await message.channel.send(f'{dice_result}')    

         button1.callback = button1_callback
         button2.callback = button2_callback

         view = View()
         view.add_item(button1)
         view.add_item(button2)
         dice_result = str(random.randint(1,100))
         await message.channel.send(embed = discord.Embed(title='메뉴 선택하기',description="원하시는 버튼을 클릭해주세요", colour=discord.Colour.blue()), view=view, reference=message)
    elif message.content.startswith('#캐서린'):
          embed = discord.Embed(title="캐서린 림나티스", description="도레아 구조대원", color=0x000000)

          embed.set_author(name="프로필", url="https://entelechysbox.wixsite.com/telos/catherine", icon_url="https://cdn.discordapp.com/attachments/1072809890017456160/1073816879786897479/vL9kdccM_400x400.jpg")
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1072809890017456160/1073814147822800896/KakaoTalk_20230122_234854943_01.png")
          embed.set_image(url="https://cdn.discordapp.com/attachments/1072809890017456160/1073814147822800896/KakaoTalk_20230122_234854943_01.png")

          embed.add_field(name="이능력 성장 유형", value="패널티 감소", inline=True)
          embed.add_field(name="보유 EP", value="2", inline=True)

          embed.set_footer(text="뭐 쓰지 고민", icon_url="https://cdn.discordapp.com/attachments/1072809890017456160/1073814147822800896/KakaoTalk_20230122_234854943_01.png")

          await message.channel.send(embed=embed)
    elif message.content.startswith('❈이용가이드'):
          embed = discord.Embed(title="가챠봇 이용가이드",description="가챠봇을 이용하기 위한 명령어 키워드들입니다", color=0x00aaaa)
          embed.add_field(name="❈가챠", value="1텔을 소모하여 선지자 후보들의 호불호 아이템을 랜덤으로 뽑습니다.", inline=False)
          embed.add_field(name="❈다이스", value="1d100 다이스를 굴립니다.", inline=False)
          embed.add_field(name="❈복권", value="오늘의 일일 복권을 뽑습니다.", inline=False)
          embed.add_field(name="❈슬롯머신", value="슬롯머신을 돌립니다.잭팟을 노려봅시다!", inline=False)
          await message.channel.send(embed=embed)
    elif message.content.startswith('❈슬롯머신'):
          randomNum = random.randrange(1, 8) # 1~6까지 랜덤수
          print(randomNum)
          if randomNum == 1:
              await message.channel.send(embed=discord.Embed(description=':🎰: '+ ':one:'+ ':one:'+ ':one:'))
          if randomNum == 2:
              await message.channel.send(embed=discord.Embed(description=':🎰: ' + ':two:'))
          if randomNum ==3:
              await message.channel.send(embed=discord.Embed(description=':🎰: ' + ':three:'))
          if randomNum ==4:
              await message.channel.send(embed=discord.Embed(description=':🎰: ' + ':four:'))
          if randomNum ==5:
              await message.channel.send(embed=discord.Embed(description=':🎰: ' + ':five:'))
          if randomNum ==6:
              await message.channel.send(embed=discord.Embed(description=':🎰: ' + ':six: '))
          if randomNum ==7:
              await message.channel.send(embed=discord.Embed(description=':🎰: ' + ':seven: '+ ':seven: '+ ':seven: '))
    elif message.content.startswith('❈랜덤테스트'):
          SlotMachine = [ '🐋', '🍺', '🍇', '🃏','7️⃣', ':tomato:', ':strawberry:', ':eggplant:', ':apple:', ':pineapple:', ':lemon:', ':melon:', ':kiwi:', ':snake:', ':hatched_chick:', ':gift:', ':star2:', ':tangerine:']
          sFirst = random.choice(SlotMachine)
          sSecond = random.choice(SlotMachine)
          sThird = random.choice(SlotMachine)
          print(sFirst + sSecond + sThird)
          await message.channel.send(f'{sFirst + sSecond + sThird}', reference=message)

    elif message.content.startswith('❈랜덤테스트2'):
          SlotMachine = [ '🐋', '🍺', '🍇', '🃏','7️⃣', ':tomato:', ':strawberry:', ':eggplant:', ':apple:', ':pineapple:', ':lemon:', ':melon:', ':kiwi:', ':snake:', ':hatched_chick:', ':gift:', ':star2:', ':tangerine:']
          sFirst = random.choice(SlotMachine)
          sSecond = random.choice(SlotMachine)
          sThird = random.choice(SlotMachine)
          sResult = sFirst + sSecond + sThird

          embed = discord.Embed(description = sResult ,
          colour = discord.Color.purple()
          )
          await message.channel.send(sResult)
          # await message.channel.send(embed=embed)
    elif message.content.startswith('#저녁메뉴'):
          menu = [ '김치찌개', '된장찌개', '치킨', '피자', '햄버거', '카레', '김밥', '족발', '보쌈', '라면', '초밥', '돈까스', '파스타', '닭발', '우동', '오돌뼈', '떡볶이']
          dinner = str(random.choice(menu)) # 랜덤으로 하나 선택
          print(dinner)
          await message.channel.send(f'오늘의 저녁메뉴는... <{dinner}>로 하자.', reference=message)
    elif message.content.startswith("❈복권"):
          channel = client.get_channel(1077114207813767210)
          Text = ""
          number = [1, 2, 3, 4, 5, 6, 7] # 배열크기 선언해줌
          count = 0
          for i in range(0, 7):
              num = random.randrange(1, 46)
              number[i] = num
              if count >= 1:
                  for i2 in range(0, i):
                      if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                          numberText = number[i]
                          print("작동 이전값 : " + str(numberText))
                          number[i] = random.randrange(1, 46)
                          numberText = number[i]
                          print("작동 현재값 : " + str(numberText))
                          if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                              numberText = number[i]
                              print("작동 이전값 : " + str(numberText))
                              number[i] = random.randrange(1, 46)
                              numberText = number[i]
                              print("작동 현재값 : " + str(numberText))
                              if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                  numberText = number[i]
                                  print("작동 이전값 : " + str(numberText))
                                  number[i] = random.randrange(1, 46)
                                  numberText = number[i]
                                  print("작동 현재값 : " + str(numberText))

              count = count + 1
              Text = Text + "  " + str(number[i])

          print(Text.strip())
          embed = discord.Embed(
              title="카두케우스 복권",
              description=Text.strip(),
              colour=discord.Color.purple()
          )
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1077116103978930186/1077144635870302309/c6563cd45e25d15a.png")
          await channel.send(embed=embed)      
    else:
        start = message.content.find('[')
        end = message.content.find(']')
        if (start != -1 and end != -1) and start<end: # [] 조건 찾기. [, ]가 존재해야 하고, 닫는 괄호가 여는 괄호보다 앞에 있으면 안된다.
            mention_keyword = message.content[start+1:end].strip().split('/') # /를 기준으로 나눠 리스트로 저장. 현재 받은 메세지에는 /가 없으므로 그냥 ['다이스'] 로 저장된다. 
            first_keyword = mention_keyword[0].strip()
            if first_keyword == '다이스':
                dice_result = str(random.randint(1,100))
                await message.channel.send(f'다이스를 굴리자... <{dice_result}>이 나왔다.', reference=message) # 답장 o     


client.run(TOKEN)
