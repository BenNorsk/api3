# This function returns all board members

def get_board_members(base_url):
    board_members = [
        {
        "title": "President",
        "name": "Gian O. Mühlemann",
        "image": f'{base_url}images/position_images/vice-president.png',
        "board_member_image": f'{base_url}images/board_member_images/gian.jpg',
        "short_description": "As President, I manage the operative and strategic tasks. I lead and assist the Board in growing the Crypto Society every day.",
        "email": "president@cryptosocietystgallen.club",
        "division": "Presidential",
        "colour": "#0098B7",
        "order": "1",
        "organ": "board"
    },
    {
        "title": "Vice-President",
        "name": "Sanna Mühlemann",
        "image": f'{base_url}images/position_images/staff.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/sanna.jpeg',
        "short_description": "As Vice-President, I assist the president in managing the operative and strategic tasks. I lead and assist the Board in growing the Crypto Society every day.",
        "email": "vice-president@cryptosocietystgallen.club",
        "division": "Presidential",
        "colour": "#529839",
        "order": "2",
        "organ": "board"
    },
    {
        "title": "Head of Legal & External Affairs",
        "name": "Alice Messner",
        "image": f'{base_url}images/position_images/legal-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/alice.jpeg',
        "short_description": "As Head of Legal & External Affairs, I manage the cooperation and communication with external partners of the Society, and take care of the legal aspects of the Society.",
        "email": "legal-affairs@cryptosocietystgallen.club",
        "division": "Legal",
        "colour": "#CC8214",
        "order": "3",
        "organ": "board",
    },
    {
        "title": "Chief of Staff",
        "name": "Mariska–Morgaine Rüger",
        "image": f'{base_url}images/position_images/staff.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/mariska.jpg',
        "short_description": "As Chief of Staff, I am your first point of contact for any questions regarding the Society. I am responsible for the internal communication and the coordination of the Board.",
        "email": "chief-of-staff@cryptosocietystgallen.club",
        "division": "Staff",
        "colour": "#529839",
        "order": "6",
        "organ": "board"
    },
    {
        "title": "Head of Events",
        "name": "Julian Schönbeck",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/julian.jpg',
        "short_description": "As Head of Events, my objective is to offer our community a variety of social platforms to connect, create and celebrate.",
        "email": "events@cryptosocietystgallen.club",
        "division": "Events",
        "colour": "#FF78CB",
        "order": "15",
        "organ": "board"
    },
    {
        "title": "Events Co-Manager",
        "name": "Alexander Moldovan",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/alexander.jpeg',
        "short_description": "As a member of the Event-Team, I help to create fun filled and engaging opportunities for like-minded individuals to connect and share unforgettable moments.",
        "email": "alexander.moldovan@student.unisg.ch",
        "division": "Events",
        "colour": "#FF78CB",
        "order": "15",
        "organ": "board"
    },
    {
        "title": "Events Co-Manager",
        "name": "Nicolas Winnewisser",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/nicolas.jpeg',
        "short_description": "My goal as a member of the Event-Team is to build our community trough organic growth to enable likeminded people to meet on one of our networking platforms and further promote our events.",
        "email": "nicolas.winnewisser@student.unisg.ch",
        "division": "Events",
        "colour": "#FF78CB",
        "order": "15",
        "organ": "board"
    },
    {
        "title": "Events Co-Manager",
        "name": "Pascal Blaser",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/pascal.jpeg',
        "short_description": "Coming up with new and innovative ideas for events to push the recognition of the Crypto Society St. Gallen.",
        "email": "events@cryptosocietystgallen.club",
        "division": "Events",
        "colour": "#FF78CB",
        "order": "15",
        "organ": "board"
    },
    {
        "title": "Events Co-Manager",
        "name": "Nikolai Michel",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/nikolai.jpeg',
        "short_description": "As a member of the event-team, I am willing to do everything in my power to provide you with to host an unforgettable evening for our guest.",
        "email": "nikolai.michel@student.unisg.ch",
        "division": "Events",
        "colour": "#FF78CB",
        "order": "15",
        "organ": "board"
    },
    {
        "title": "Events Co-Manager",
        "name": "Laurin Mengis",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/laurin.jpeg',
        "short_description": "As part of the Event-Team, my goal is to organize social gatherings for our community to make new acquaintances, find inspiration and let loose!",
        "email": "laurin.mengis@student.unisg.ch",
        "division": "Events",
        "colour": "#FF78CB",
        "order": "15",
        "organ": "board"
    },
    {
        "title": "Events Co-Manager",
        "name": "Phillip Schmid",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/phillip.jpeg',
        "short_description": "As part of the Event-Team, my goal is as well to organize social gatherings for our community to make new acquaintances, find inspiration and let loose!",
        "email": "phillip.schmid@student.unisg.ch",
        "division": "Events",
        "colour": "#FF78CB",
        "order": "15",
        "organ": "board"
    },
    {
        "title": "Head of Academic Affairs",
        "name": "Davide Brunetti",
        "image": f'{base_url}images/position_images/socials.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/davide.jpg',
        "short_description": "As Head of Academic Affairs, I defined how knowledge is shared within the Society.",
        "email": "academic-affairs@cryptosocietystgallen.club",
        "division": "Academics",
        "colour": "#FF78CB",
        "order": "13",
        "organ": "board"
    },
    {
        "title": "Academic Analyst",
        "name": "Malte Knauer",
        "image": f'{base_url}images/position_images/academic-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/malte.jpg',
        "short_description": "As Academic Analyst, I work together with the Academic Affairs team in creating relevant and interesting content for our members.",
        "email": "malte.knauer@student.unisg.ch",
        "division": "Academics",
        "colour": "#89609E",
        "order": "8",
        "organ": "board"
    },
    {
        "title": "Academic Analyst",
        "name": "Raffaello Erculiani",
        "image": f'{base_url}images/position_images/academic-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/raffaelo.jpg',
        "short_description": "As Academic Analyst, I work together with the Academic Affairs team in creating relevant and interesting content for our members.",
        "email": "raffaello.erculiani@student.unisg.ch",
        "division": "Academics",
        "colour": "#89609E",
        "order": "11",
        "organ": "board"
    },
    {
        "title": "Head of Marketing",
        "name": "Sandro Gössi",
        "image": f'{base_url}images/position_images/marketing.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/sandro.jpg',
        "short_description": "As Head of Marketing, I lead all marketing activities from social media, branding and digital campaigns to advertising and creative projects. Your vibe attracts your tribe!",
        "email": "marketing@cryptosocietystgallen.club",
        "division": "Marketing",
        "colour": "#AF4632",
        "order": "12",
        "organ": "board"
    },
    {
        "title": "Head of Crypto Projects",
        "name": "Justin Lieberherr",
        "image": f'{base_url}images/position_images/marketing.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/justin.jpeg',
        "short_description": "As Head of Crypto Projects, I bring innovation into the Crypto Society!",
        "email": "crypto-projects@cryptosocietystgallen.club",
        "division": "Projects",
        "colour": "#AF4632",
        "order": "12",
        "organ": "board"
    },
    {
        "title": "Head of the Judicial Committee",
        "name": "Benjamin L. Brückner",
        "image": f'{base_url}images/position_images/president.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/ben.jpg',
        "short_description": "As Head of the Judicial Committee, I am responsible for the enforcement of the constitution and the bylaws of the society.",
        "email": "benjamin.brueckner@bluewin.ch",
        "division": "Legal",
        "colour": "#0098B7",
        "order": "1",
        "organ": "judicial"
    },
    {
        "title": "Member of the Judicial Committee",
        "name": "Annina Schmid",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/annina.jpg',
        "short_description": "As member of the Judicial Committee, I serve the justice within the Society. You can disagree without being disagreeable!",
        "email": "annina.schmid@student.unisg.ch",
        "division": "Legal",
        "colour": "#CC8214",
        "order": "2.1",
        "organ": "judicial"
        },
    {
        "title": "Member of the Judicial Committee",
        "name": "Jan Scherrer",
        "image": f'{base_url}images/position_images/legal-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/jan.jpg',
        "short_description": "As member of the Judicial Committee and author of the constiution, I assist the Head of the Judicial Committee in the enforcement of the constitution and the bylaws of the Society.",
        "email": "legal-affairs@cryptosocietystgallen.club",
        "division": "Legal",
        "colour": "#CC8214",
        "order": "3",
        "organ": "judicial"
    },
    {
        "title": "Co-Head Auditor",
        "name": "Markus Wolf",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/markus.jpg',
        "short_description": "As Co-Head Auditors, we keep our tabs on the board and ensure the financial integrity of the Society!",
        "email": "markus.wolf2@student.unisg.ch",
        "division": "Audit",
        "colour": "#555555",
        "order": "15",
        "organ": "audit"
    },
    {
        "title": "Co-Head Auditor",
        "name": "Christian van Haastert",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/chris.jpg',
        "short_description": "As Co-Head Auditors, we keep our tabs on the board and ensure the financial integrity of the Society!",
        "email": "christian@vanhaastert.ch",
        "division": "Audit",
        "colour": "#555555",
        "order": "15",
        "organ": "audit"
    }
    ]
    return board_members