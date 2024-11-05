# This function returns all board members

def get_board_members(base_url):
    board_members = [
        {
        "title": "President",
        "name": "Laurin Kuster",
        "image": f'{base_url}images/position_images/vice-president.png',
        "board_member_image": f'{base_url}images/board_member_images/laurin2.jpeg',
        "short_description": "As President, I manage the operative and strategic tasks. I lead and assist the Board in growing the Crypto Society every day.",
        "email": "president@cryptosocietystgallen.club",
        "division": "Presidential",
        "colour": "#0098B7",
        "order": "1",
        "organ": "board"
    },
    {
        "title": "Vice-President",
        "name": "Patrick Hurschler",
        "image": f'{base_url}images/position_images/staff.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/patrik.jpg',
        "short_description": "As Vice-President, I assist the president in managing the operative and strategic tasks. I lead and assist the Board in growing the Crypto Society every day.",
        "email": "vice-president@cryptosocietystgallen.club",
        "division": "Presidential",
        "colour": "#529839",
        "order": "2",
        "organ": "board"
    },
    {
        "title": "Head of Legal & External Affairs",
        "name": "David Percy",
        "image": f'{base_url}images/position_images/legal-affairs.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/david2.jpeg',
        "short_description": "As Head of Legal & External Affairs, I manage the cooperation and communication with external partners of the Society, and take care of the legal aspects of the Society.",
        "email": "board@cryptosocietystgallen.club",
        "division": "Legal",
        "colour": "#CC8214",
        "order": "3",
        "organ": "board",
    },
    {
        "title": "Board Member",
        "name": "Noé Helbling",
        "image": f'{base_url}images/position_images/staff.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/noe.jpeg',
        "short_description": "Board member of the Crypto Society St. Gallen.",
        "email": "board@cryptosocietystgallen.club",
        "division": "Staff",
        "colour": "#529839",
        "order": "6",
        "organ": "board"
    },

    {
        "title": "Head of the Judicial Committee",
        "name": "Julian Schönbeck",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/julian.jpg',
        "short_description": "As Head of the Judicial Committee and former President, I advise the board and enforce the bylaws of the society.",
        "email": "julian.schoenbeck@hotmail.com",
        "division": "Legal",
        "colour": "#FF78CB",
        "order": "15",
        "organ": "judicial"
    },
    {
        "title": "Member of the Judicial Committee",
        "name": "Benjamin L. Brückner",
        "image": f'{base_url}images/position_images/president.jpeg',
        "board_member_image": f'{base_url}images/board_member_images/ben.jpg',
        "short_description": "As former President, I am delighted to assist Jules in heading the Judicial Committee.",
        "email": "benjamin.brueckner@bruecknerdata.com",
        "division": "Legal",
        "colour": "#0098B7",
        "order": "1",
        "organ": "judicial"
    },
    {
        "title": "Member of the Judicial Committee",
        "name": "Alice Messner",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/alice.jpeg',
        "short_description": "As former Head of Legal Affairs, I contribute my vast knowledge of the society's legal framework.",
        "email": "alice.messner@student.unisg.ch",
        "division": "Legal",
        "colour": "#CC8214",
        "order": "2.1",
        "organ": "judicial"
        },
    {
        "title": "Head Auditor",
        "name": "Markus Wolf",
        "image": f'{base_url}images/position_images/events2.jpg',
        "board_member_image": f'{base_url}images/board_member_images/markus.jpg',
        "short_description": "As Co-Head Auditors, we keep our tabs on the board and ensure the financial integrity of the Society!",
        "email": "markus.wolf2@student.unisg.ch",
        "division": "Audit",
        "colour": "#555555",
        "order": "15",
        "organ": "audit"
    }
    ]
    return board_members