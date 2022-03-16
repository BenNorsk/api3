# This function returns all board members

def get_board_members(base_url):
    board_members = [
    {
        "title": "President",
        "name": "Benjamin L. Brückner",
        "image": f'{base_url}images/position_images/president.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/president.jpeg',
        "short_description": "As President, I lead and assist the Board in growing and designing the society each and every day.",
        "email": "president@cryptosocietystgallen.club",
        "order": "1"
        },
        {
        "title": "Vice-President",
        "name": "Gian O. Mühlemann",
        "image": f'{base_url}images/position_images/vice-president.png',
        "board_member_image": f'{base_url}images/board_member_images/vice-president.png',
        "short_description": "As Vice-President, I support and advise the president in his operative and strategic tasks. Together we lead and assist the Board in creating a growing cryptosociety.",
        "email": "vice-president@cryptosocietystgallen.club",
        "order": "2"
    },
    {
        "title": "Head of the Judicial Committee",
        "name": "Annina Schmid",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/annina.jpg',
        "short_description": "As Head of the Judicial Committee, I serve the justice within the Society. You can disagree without being disagreeable!",
        "email": "annina.schmid@student.unisg.ch",
        "order": "2.1"
        },
    {
        "title": "Head of Legal Affairs",
        "name": "Jan Scherrer",
        "image": f'{base_url}images/position_images/legal-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/legal-affairs.jpg',
        "short_description": "As Head of Legal Affairs, my responsibilities include inter alia the creation and management of all legal documents, the society’s official incorporation, and the appointment of the Judicial Committee.",
        "email": "legal-affairs@cryptosocietystgallen.club",
        "order": "3"
    },
    {
        "title": "Head of Crypto Projects",
        "name": "Robert Jacobs",
        "image": f'{base_url}images/position_images/legal-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/crypto-projects.png',
        "short_description": "As Head of Crypto Projects, I oversee the practical projects that the Society is developping in the real of crypto.",
        "email": "crypto-projects@cryptosocietystgallen.club",
        "order": "4"
        },
    {
        "title": "Chief of Staff",
        "name": "Sanna Mühlemann",
        "image": f'{base_url}images/position_images/staff.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/staff.png',
        "short_description": "As Chief of Staff, I am your first point of contact. I will make sure to help you if there are any issues or questions regarding to our society.",
        "email": "chief-of-staff@cryptosocietystgallen.club",
        "order": "5"
        },
    {
        "title": "Vice Chief of Staff",
        "name": "Mariska–Morgaine Rüger",
        "image": f'{base_url}images/position_images/staff.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/vice-chief-of-staff.png',
        "short_description": "As Vice Chief of Staff, I support Sanna Mühlemann in helping you out if any questions appear concerning our society. I try my best that you will have all informations you need.",
        "email": "vice-chief-of-staff@cryptosocietystgallen.club",
        "order": "6"
        },
    {
        "title": "Head of Finance",
        "name": "Elias Henke",
        "image": f'{base_url}images/position_images/finance.jpg',
        "board_member_image": f'{base_url}images/board_member_images/finance.jpg',
        "short_description": "As Head of Finance, I am responsible for managing all financial affairs of the society as well as for the development of the finance department.",
        "email": "finance@cryptosocietystgallen.club",
        "order": "7"
    },
    {
        "title": "Co–Head of Academic Affairs",
        "name": "Malte Knauer",
        "image": f'{base_url}images/position_images/academic-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/academic-affairs.jpg',
        "short_description": "Together, we define how knowledge is shared throughout the society.",
        "email": "academic-affairs@cryptosocietystgallen.club",
        "order": "8"
    },
    {
        "title": "Co–Head of Academic Affairs",
        "name": "Victor Hoppe",
        "image": f'{base_url}images/position_images/academic-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/academic-affairs2.png',
        "short_description": "Together, we define how knowledge is shared throughout the society.",
        "email": "academic-affairs@cryptosocietystgallen.club",
        "order": "9"
    },
    {
        "title": "Academic Analyst",
        "name": "Johannes Hohl",
        "image": f'{base_url}images/position_images/academic-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/academic_analyst.png',
        "short_description": "Coming Soon.",
        "email": "johannes.hohl@student.unisg.ch",
        "order": "10"
    },
    {
        "title": "Academic Analyst",
        "name": "Raffaello Erculiani",
        "image": f'{base_url}images/position_images/academic-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/academic_analyst2.jpeg',
        "short_description": "As Academic Analyst, I work together with the Academic Affairs team in creating relevant and interesting content for our members.",
        "email": "raffaello.erculiani@student.unisg.ch",
        "order": "11"
    },
    {
        "title": "Academic Analyst",
        "name": "Marlon Richter",
        "image": f'{base_url}images/position_images/academic-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/marlon.jpg',
        "short_description": "As Academic Analyst, I contribute to the mission of constant learning in the Society through research and presentations about current crypto related topics.",
        "email": "marlon.richter@student.unisg.ch",
        "order": "11"
    },
    {
        "title": "Head of Marketing",
        "name": "Sandro Gössi",
        "image": f'{base_url}images/position_images/marketing.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/marketing.jpg',
        "short_description": "As Head of Marketing, I lead all marketing activities from social media, branding and digital campaigns to advertising and creative projects. Your vibe attracts your tribe!",
        "email": "marketing@cryptosocietystgallen.club",
        "order": "12"
    },
    {
        "title": "Co–Head of Events",
        "name": "Davide Brunetti",
        "image": f'{base_url}images/position_images/socials.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/socials.jpg',
        "short_description": "As Co–Head of Events, I contribute to the social platform of the society and I am determined to establish a pleasant environment of social exchange.",
        "email": "social-events@cryptosocietystgallen.club",
        "order": "13"
        },
    {
        "title": "Co–Head of Events",
        "name": "Andre Lubawin",
        "image": f'{base_url}images/position_images/socials.jpg',
        "board_member_image": f'{base_url}images/board_member_images/events2.jpg',
        "short_description": "As Co–Head of Events, I contribute to the social platform of the society and I am determined to establish a pleasant environment of social exchange.",
        "email": "events@cryptosocietystgallen.club",
        "order": "14"
        },
    {
        "title": "Events Co–Manager",
        "name": "Laura Carrieri",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/events_co_manager.png',
        "short_description": "As Events Co–Manager, I contribute to the social platform of the society and I am determined to establish a pleasant environment of social exchange.",
        "email": "laura.carrieri@student.unisg.ch",
        "order": "15"
        },
    {
        "title": "Co-Head Auditor",
        "name": "Markus Wolf",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/markus.jpg',
        "short_description": "As Co-Head Auditors, we keep our tabs on the board and ensure the financial integrity of the Society!",
        "email": "markus.wolf2@student.unisg.ch",
        "order": "15"
        },
    {
        "title": "Co-Head Auditor",
        "name": "Christian van Haastert",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/chris.jpg',
        "short_description": "As Co-Head Auditors, we keep our tabs on the board and ensure the financial integrity of the Society!",
        "email": "christian@vanhaastert.ch",
        "order": "15"
        }
    ]
    return board_members