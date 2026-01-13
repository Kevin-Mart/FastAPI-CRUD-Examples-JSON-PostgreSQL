import httpx 

class AgifyService ():
    async def get_ages(self, name :str):
        url = f"https://api.agify.io/?name={name}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        return response.json()
