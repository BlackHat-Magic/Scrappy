from pygelbooru import Gelbooru
import asyncio, requests

gelbooru = Gelbooru("ec9dd148c802c79d26b8726e5eb7d1895817dd1bbb00e3283a3b2569e613d00a", "730371")

async def tags(tags, exclude_tags):
    results = await gelbooru.search_posts(
        tags=tags, 
        exclude_tags=exclude_tags
    )
    print(f"Found {len(results)} results...")
    for result in results:
        print(f"Downloading image {result.id} from {result.file_url}...")
        img = requests.get(result.file_url).content
        with open(f"{result.id}.jpg", "wb") as handler:
            handler.write(img)
        print(f"Done downloading {result.id}.")

async def scrape(start, end, url):
    for i in range(start, end):
        try:
            result = await gelbooru.get_post(i)
            if(not "jpg" in result.file_url and not "png" in result.file_url and not "jpeg" in result.file_url and not "webm" in file.url):
                print(f"Image {result.id} is not a jpeg, png, or webm; skipping...")
            else:
                print(f"Downloading image {result.id} from {result.file_url}...")

                img = requests.get(result.file_url).content
                # with open(f"images/{'{:07d}'.format(result.id)}.jpg", "wb") as handler:
                #     handler.write(img)

                # new_image = Image(
                #     siteid = str(result.id),
                #     url = result.file_url,
                #     tags = result.tags,
                #     height = result.height,
                #     width = result.width
                # )
                # session.add(new_image)
                # session.commit()

                requests.post(url, json = {
                    "siteid": str(result.id),
                    "url": result.file_url,
                    "tags": result.tags,
                    "height": result.height,
                    "width": result.width,
                    "content": img
                })
        except:
            print(f"Post {i} not found.")

start = int(input("Enter the start post ID: "))
end = int(input("Enter the end post ID: "))
url = input("Enter the url of the hub server: ")

asyncio.run(scrape(start, end, url))