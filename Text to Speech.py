import asyncio
import edge_tts
from edge_tts import list_voices


async def main():
    tts=edge_tts.Communicate("What does the fox say?","ur-PK-AsadNeural")
    await tts.save("Fox.mp3")

asyncio.run(main())