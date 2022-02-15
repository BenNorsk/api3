# Here we get the data about the documents

def get_documents(base_link):
    documents =  {
        "constitution": {
            "title": "Constitution of the Crypto Society St. Gallen",
            "publication_date": "12.12.2021",
            "link": f'{base_link}documents/constitution.txt'
        },
        "general_assembly_2022": {
            "title": "General Assembly 2022",
            "publication_date": "08.02.2022",
            "link": f'{base_link}documents/ga.txt'
        },
        "bitcoin_whitepaper": {
            "title": "Bitcoin Whitepaper",
            "publication_date": "31.10.2008",
            "link": f'{base_link}documents/bitcoin_whitepaper.pdf'
        }
    }
    return documents