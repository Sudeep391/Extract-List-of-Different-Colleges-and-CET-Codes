from groq import Groq
from serpapi import GoogleSearch

GROQ_API_KEY = "YOUR_GROQ_API_KEY"
SERPAPI_KEY = "YOUR_SERPAPI_KEY"

client = Groq(api_key=GROQ_API_KEY)

def web_search(query):
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 5
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    snippets = []
    if "organic_results" in results:
        for r in results["organic_results"]:
            snippets.append(r.get("snippet", ""))

    return "\n".join(snippets)

def generate_ai_advice(rank, df):

    local_data = df.head(5).to_string()

    web_data = web_search(
        "best engineering branches placements future demand India"
    )

    prompt = f"""
    You are a professional CET counselor.

    Student rank: {rank}

    LOCAL DATA:
    {local_data}

    WEB DATA:
    {web_data}

    TASK:
    - Suggest best branches
    - Suggest best colleges
    - Explain based on placements and future scope
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
