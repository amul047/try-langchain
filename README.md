## Installation steps
- Install `Python 3.10.11` from https://www.python.org/downloads/release/python-31011/
  - The latest version at the time of writing `3.12.1` showed issues installing the LangChain libraries as per my comment here - https://github.com/dagster-io/dagster/discussions/18696#discussioncomment-8018289
- Install `LangChain` library as per https://python.langchain.com/docs/get_started/installation
- Install `OpenAI` library as per https://pypi.org/project/openai/
- Add a `.env` file with the following settings
```
OPENAI_API_KEY=sk-X...s
```
  - Note that the API key must be generated after turning to a paid account. Otherwise you will end up with 429 limit exceeded errors.