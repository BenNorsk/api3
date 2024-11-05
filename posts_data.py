# This returns all data about all posts
from email.mime import base


def get_posts_data(base_url):
    posts = [
        {
                "title": "Relaunch with our new Board!",
                "icon": f'{base_url}images/post_images/speaker-post/speaker.png',
                "image": f'{base_url}images/post_images/speaker-post/speaker.png',
                "author": "Julian Schönbeck",
                "publication_date": "05.11.2024",
                "content": "We are happy to announce a relaunch of the Crypto Society with our new board led by Laurin and Patrick. We are looking forward to a great semester with exciting events and workshops. Join us!",
                "link": "https://chat.whatsapp.com/CUYwYyav4Hy0MLmemrhr3M",
                "link_text": "Join us!"
            },
        {
                "title": "Join our Workshop!",
                "icon": f'{base_url}images/post_images/web3workshop.jpeg',
                "image": f'{base_url}images/post_images/web3workshop.jpeg',
                "author": "Gian & Sanna Mühlemann",
                "publication_date": "21.03.2023",
                "content": "Join us for an exciting company visit and Web3 workshop hosted by 4bridges on the 30.03.23. We'll be exploring topics like Smart Wallets and NFTs, with a presentation by Bruno Kellenberger, CEO of KYC Spider.",
                "link": "https://form.jotform.com/230593317294055?fbclid=PAAabI2PBlTq867_9rPU52KVFJsOSuLHqUE1WQ6cV3J7CD2JXbu9f7epMjDyk",
                "link_text": "Register Here!"
            },
        
        {
                "title": "Review our NEON party!",
                "icon": f'{base_url}images/post_images/neon.jpeg',
                "image": f'{base_url}images/post_images/neon.jpeg',
                "author": "Jules Schönbeck",
                "publication_date": "14.10.2022",
                "content": "Check out our NEON party, and stay tuned for more Crypto Society parties to come at the Garage in St. Gallen!",
                "link": "https://www.instagram.com/p/CjzrB0ptDzF/",
                "link_text": "See Video!"
            },
        {
                "title": "Join our Bitcoin Suisse Visit!",
                "icon": f'{base_url}images/post_images/btc-suisse-post/btc_suisse.png',
                "image": f'{base_url}images/post_images/btc-suisse-post/btc_suisse.png',
                "author": "Sandro Gössi",
                "publication_date": "26.09.2022",
                "content": "On the 05.10.2022, we will have a visit with Bitcoin Suisse. Join us by signing up, there are only a few spots left!",
                "link": "https://forms.gle/wfgSEfxMAeMvzDxu8",
                "link_text": "Register!"
            },
            {
                "title": "Review the Anonymous Cryptoholics Meeting!",
                "icon": f'{base_url}images/post_images/acm-post/acm.jpg',
                "image": f'{base_url}images/post_images/acm-post/acm.jpg',
                "author": "Sandro Gössi",
                "publication_date": "26.09.2022",
                "content": "Our ACM party was a total success! With over 400 people, and Maximilian I. as a special gig, it was the perfect start into the new semester! Check out the review video!",
                "link": "https://www.instagram.com/p/Ci9oInxvBaq/",
                "link_text": "See the Review Video!"
            },
            {
                "title": "General Assembly & Elections",
                "icon": f'{base_url}images/post_images/speaker-post/speaker.png',
                "image": f'{base_url}images/post_images/speaker-post/speaker.png',
                "author": "Benjamin L. Brückner",
                "publication_date": "20.09.2022",
                "content": "Join our general assembly at the 04.10.2022! Until the 30.09.2022, you may still hand in your candidacy for either President, Vice-President or Head of Legal Affairs. In order to apply, contact us!",
                "link": "mailto:president@cryptosocietystgallen.club",
                "link_text": "Hand in your candidacy!"
            },
            {
                "title": "Anonymous Cryptoholics Meeting",
                "icon": f'{base_url}images/post_images/acm-post/acm.jpg',
                "image": f'{base_url}images/post_images/acm-post/acm.jpg',
                "author": "Jules Schönbeck",
                "publication_date": "12.09.2022",
                "content": "Join our fresher's week party! At the 14.09.2022, we will host the Anonymous Cryptoholics Meeting in the Garage Club in S. Gallen, with Maximilian I. as special gig! Get your tickets now!",
                "link": "https://eventfrog.ch/de/p/party/house-techno/anonymous-cryptoholics-meeting-acm-6965636510541305607.html",
                "link_text": "Tickets!"
            },
            {
                "title": "Review the Speaker Event",
                "icon": f'{base_url}images/post_images/speaker-event-review-post/speaker_event_review.png',
                "image": f'{base_url}images/post_images/speaker-event-review-post/speaker_event_review.png',
                "author": "Davide Brunetti & Andre Lubawin",
                "publication_date": "20.05.2022",
                "content": "Review our speaker event! Check out our latest speaker event, and make sure to step by the next time!",
                "link": "https://www.instagram.com/p/CdYAASoFe2I/",
                "link_text": "Video"
            },
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
