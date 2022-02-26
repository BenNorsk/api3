# This returns all data about all posts
from email.mime import base


def get_posts_data(base_url):
    posts = [
            {
                "title": "Join the Events Team!",
                "icon": f'{base_url}images/board_member_images/socials.jpg',
                "image": f'{base_url}images/position_images/socials.jpeg',
                "author": "Davide Brunetti & Andre Lubawin",
                "publication_date": "27.02.2022",
                "content": "Are you interested in managing and organising events in the most pulsating student society in St. Gallen? Apply to become an Events Co–Manager, and set the stage of where crypto is happening in St. Gallen.",
                "link": "mailto:events@cryptosocietystgallen.club",
                "link_text": "Apply!"
            },
            {
                "title": "Visit our Store!",
                "icon": f'{base_url}images/post_images/store-post/store_logo.png',
                "image": f'{base_url}images/post_images/store-post/store.png',
                "author": "Sandro Gössi",
                "publication_date": "26.02.2022",
                "content": "The Crypto Society has launched its official store. Acquire the exclusive Crypto Society hoodies today, or check out our other creations!",
                "link": "https://www.etsy.com/ch/shop/CryptoSociety?ref=simple-shop-header-name&listing_id=1178701383",
                "link_text": "To the Store!"
            },
            {
                "title": "Join the Academics Team!",
                "icon": f'{base_url}images/board_member_images/academic-affairs2.png',
                "image": f'{base_url}images/position_images/finance.jpg',
                "author": "Malte Knauer & Victor Hoppe",
                "publication_date": "20.02.2022",
                "content": "The Crypto Society has launched its official store. Acquire the exclusive Crypto Society hoodies today, or check out our other creations!",
                "link": "https://www.etsy.com/ch/shop/CryptoSociety?ref=simple-shop-header-name&listing_id=1178701383",
                "link_text": "Apply!"
            },
            {
                "title": "Review our Student Engagement Award Bid!",
                "icon": f'{base_url}images/post_images/student-post/student_engagement_logo.png',
                "image": f'{base_url}images/post_images/student-post/student_engagement_award.png',
                "author": "Davide Brunetti",
                "publication_date": "01.02.2022",
                "content": "The Crypto Society has launched its bid to win the Student Engagement Award. As the most innovative Society in St. Gallen, the Crypto Society outgrew many decade-long established associations within a matter of months. Therefore, we applied for the Student Engagement Award 2022!",
                "link": "https://www.instagram.com/p/CZcUk_GlIvz/",
                "link_text": "To the Video!"
            },
            {
                "title": "Review our X-Mas Event!",
                "icon": f'{base_url}images/post_images/x-mas-post/christmas.jpg',
                "image": f'{base_url}images/post_images/x-mas-post/xmas1.jpg',
                "author": "Benjamin L. Brückner",
                "publication_date": "23.12.2021",
                "content": "On the 22.12.2021, our first official event took place. We gathered with nearly 30 people in the Einstein Hotel, and held an introduction into the topic of Crypto, and into the Crypto Society of St. Gallen. We discussed, debated, lectured, socialised and laughed together at our very first X-Mas event! Feel free to check out some more pictures to it on our Instagram post.",
                "link": "https://www.instagram.com/p/CX68HwTNLfj/",
                "link_text": "See more!"
            }
    ]
    return posts