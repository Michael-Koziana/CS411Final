import twint

def scrape(query):
# Configure
    c = twint.Config()
    c.Search = query
    c.Limit = 25
    c.Output = "./test.json"
    c.Store_json = True
    c.Lang = 'en'
    # Run
    twint.run.Search(c)