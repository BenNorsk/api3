# This returns all data about all posts
from email.mime import base


def get_posts_data(base_url):
    posts = [
        {
                "title": "Speaker Event",
                "icon": f'{base_url}images/post_images/speaker-post/speaker.png',
                "image": f'{base_url}images/post_images/speaker-post/speaker.png',
                "author": "Davide Brunetti & Andre Lubawin",
                "publication_date": "11.04.2022",
                "content": "Join our speaker event at the 26.04.2022, 18:30, with Head of Marketing of Bitcoin Suisse, Marc Baumann, and CEO & founder of 4bridges, Simon Fundel. Free drinks and snacks inclusive at the after social!",
                "link": "https://eventfrog.ch/de/p/kurse-seminare/computer-edv/speaker-kick-off-6916729565620959977.html",
                "link_text": "Tickets"
            },
            {
                "title": "Listen to our Podcast!",
                "icon": f'{base_url}images/post_images/podcast-post/inno-maker.png',
                "image": f'{base_url}images/post_images/podcast-post/roger.jpeg',
                "author": "Benjamin L. Brückner",
                "publication_date": "04.04.2022",
                "content": "Listen to our joint podcast with inno-maker, having Prof. Wattenhofer as guest. As a co-developer of the Lightning protocol, the renowned expert shares his views on the future of crypto in Switzerland.",
                "link": "https://open.spotify.com/episode/0VTOA9lz2xiJwZAJMQi4fp?si=a72a557802d649d7",
                "link_text": "Go To Spotify"
            },
            {
                "title": "Join our Photoshoot!",
                "icon": f'{base_url}images/post_images/photoshoot-post/photoshoot-logo.png',
                "image": f'{base_url}images/post_images/photoshoot-post/photoshoot.jpg',
                "author": "Benjamin L. Brückner & Gian O. Mühlemann",
                "publication_date": "23.03.2022",
                "content": "On the 30.03.2022, at 14:00, the Crypto Society will hold a photoshoot in front of the SQUARE. Every member and supporter is invited to come! If you want to get further updates, you are invited to also join our WhatsApp group.",
                "link": "https://chat.whatsapp.com/CUYwYyav4Hy0MLmemrhr3M",
                "link_text": "Join Us!"
            },
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
                "content": "As an Academic Analyst, you are at the core of knowledge of the entire Society. You learn from your team, and you teach your insights to all members of the society. Therefore, apply as an Academic Analyst to join the  Crytpo Society's Academics Team!",
                "link": "mailto:academic-affairs@cryptosocietystgallen.club",
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
