# This function returns all board members

def get_board_members(base_url):
    board_members = {
    "president": {
        "title": "President",
        "name": "Benjamin L. Brückner",
        "image": f'{base_url}images/position_images/president.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/president.jpeg',
        "short_description": "As President, I lead and assist the Board in growing and designing the society each and every day.",
        "email": "president@cryptosocietystgallen.club",
        "order": "1"
        },
    "vice_president": {
        "title": "Vice-President",
        "name": "Gian O. Mühlemann",
        "image": f'{base_url}images/position_images/vice-president.png',
        "board_member_image": f'{base_url}images/board_member_images/vice-president.jpg',
        "short_description": "As Vice-President, I support and advise the president in his operative and strategic tasks. Together we lead and assist the Board in creating a growing cryptosociety.",
        "email": "vice-president@cryptosocietystgallen.club",
        "order": "2"
    },
    "head_of_legal_affairs": {
        "title": "Head of Legal Affairs",
        "name": "Jan Scherrer",
        "image": f'{base_url}images/position_images/legal-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/legal-affairs.jpg',
        "short_description": "As Head of Legal Affairs, my responsibilities include inter alia the creation and management of all legal documents, the society’s official incorporation, and the appointment of the Judicial Committee.",
        "email": "legal-affairs@cryptosocietystgallen.club",
        "order": "3"
    },
    "head_of_crypto_projects": {
        "title": "Head of Crypto Projects",
        "name": "Robert Jacobs",
        "image": f'{base_url}images/position_images/legal-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/crypto-projects.png',
        "short_description": "Coming soon.",
        "email": "crypto-projects@cryptosocietystgallen.club",
        "order": "4"
        },
    "chief_of_staff": {
        "title": "Chief of Staff",
        "name": "Sanna Mühlemann",
        "image": f'{base_url}images/position_images/staff.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/staff.png',
        "short_description": "As Chief of Staff, I am your first point of contact. I will make sure to help you if there are any issues or questions regarding to our society.",
        "email": "chief-of-staff@cryptosocietystgallen.club",
        "order": "5"
        },
    "vice_chief_of_staff": {
        "title": "Vice Chief of Staff",
        "name": "Mariska–Morgaine Rüger",
        "image": f'{base_url}images/position_images/staff.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/staff.png',
        "short_description": "As Vice Chief of Staff, I am your first point of contact. I will make sure to help you if there are any issues or questions regarding to our society.",
        "email": "chief-of-staff@cryptosocietystgallen.club",
        "order": "6"
        },
    "head_of_finance": {
        "title": "Head of Finance",
        "name": "Elias Henke",
        "image": f'{base_url}images/position_images/finance.jpg',
        "board_member_image": f'{base_url}images/board_member_images/finance.jpg',
        "short_description": "As Head of Finance, I am responsible for managing all financial affairs of the society as well as for the development of the finance department.",
        "email": "finance@cryptosocietystgallen.club",
        "order": "7"
    },
    "head_of_academic_affairs1": {
        "title": "Co–Head of Academic Affairs",
        "name": "Malte Knauer",
        "image": f'{base_url}images/position_images/academic-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/academic-affairs.jpg',
        "short_description": "As Co–Head of Academic Affairs, I develop and plan how knowledge about crypto is shared throughout the society.",
        "email": "academic-affairs@cryptosocietystgallen.club",
        "order": "8"
    },
    "head_of_academic_affairs2": {
        "title": "Co–Head of Academic Affairs",
        "name": "Victor Hoppe",
        "image": f'{base_url}images/position_images/academic-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/academic-affairs2.png',
        "short_description": "Coming soon.",
        "email": "academic-affairs@cryptosocietystgallen.club",
        "order": "9"
    },
    "head_of_marketing": {
        "title": "Head of Marketing",
        "name": "Sandro Gössi",
        "image": f'{base_url}images/position_images/marketing.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/marketing.jpg',
        "short_description": "As Head of Marketing, I lead all marketing activities from social media, branding and digital campaigns to advertising and creative projects. Your vibe attracts your tribe!",
        "email": "marketing@cryptosocietystgallen.club",
        "order": "10"
    },
    "head_of_events1": {
        "title": "Co–Head of Events",
        "name": "Davide Brunetti",
        "image": f'{base_url}images/position_images/socials.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/socials.jpg',
        "short_description": "As Co–Head of Events, I contribute to the social platform of the society and I am determined to establish a pleasant environment of social exchange.",
        "email": "social-events@cryptosocietystgallen.club",
        "order": "11"
        },
    "head_of_events2": {
        "title": "Co–Head of Events",
        "name": "Andre Lubawin",
        "image": f'{base_url}images/position_images/socials.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/socials.jpg',
        "short_description": "As Co–Head of Events, I contribute to the social platform of the society and I am determined to establish a pleasant environment of social exchange.",
        "email": "events@cryptosocietystgallen.club",
        "order": "12"
        }
    }
    return board_members