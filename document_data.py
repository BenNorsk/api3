# Here we get the data about the documents

def get_documents(base_link):
    documents =  {
        "constitution": {
            "title": "Constitution of the Crypto Society St. Gallen",
            "publication_date": "12.12.2021",
            "link": f'{base_link}documents/constitution.pdf'
        },
        "general_assembly_2022": {
            "title": "General Assembly 2022",
            "publication_date": "08.02.2022",
            "link": f'{base_link}documents/ga_2022.pdf'
        },
        "bitcoin_whitepaper": {
            "title": "Bitcoin Whitepaper",
            "publication_date": "31.10.2008",
            "link": f'{base_link}documents/bitcoin_whitepaper.pdf'
        },
        "student_engagement_award_bid": {
            "title": "Bid for the Student Engagement Award",
            "publication_date": "01.02.2022",
            "link": f'{base_link}documents/student_engagement_award_bid.pdf'
        },
    }
    return documents