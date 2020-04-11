import telethon
import time
import datetime

with telethon.TelegramClient('me', 1279413, 'b581b25aee9ec51f025ab51c4c016d15') as client:
    async def do():
        while True:
            n = datetime.datetime.now()
            if n.second == 0:
                print(n)
                nowstr = "Время смерти- " + datetime.datetime.now().strftime('%H:%M')
                try:
                    await client(telethon.functions.account.UpdateProfileRequest(about=nowstr))
                except telethon.errors.rpcerrorlist.FloodWaitError as e:
                    print('Flood waited for', e.seconds)
                    time.sleep(e.seconds + 1)
            time.sleep(1)
    client.loop.run_until_complete(do())