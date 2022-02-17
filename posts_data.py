# This returns all data about all posts
def get_posts_data(base_url):
    posts = {
        "x-mas":
            {
                "title": "Review our X-Mas Event!",
                "icon": f'{base_url}images/post_images/x-mas-post/christmas.jpg',
                "author": "Benjamin L. Brückner",
                "content": "On the 22.12.2021, our first official event took place. We gathered with nearly 30 people in the Einstein Hotel, and held an introduction into the topic of Crypto, and into the Crypto Society of St. Gallen. We discussed, debated, lectured, socialised and laughed together at our very first X-Mas event! Feel free to check out some more pictures to it on our Instagram post.",
                "link": "https://www.instagram.com/p/CX68HwTNLfj/"
            }
    }
    return posts