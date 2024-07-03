from jobs.extract_client import ExtractClient

# import requests


class PubChemExtract(ExtractClient):

    def url_builder(cid: int, properties: str) -> str:
        url = f"/{cid}/property/{properties}/JSON"

    async def get(url: str) -> dict[str, str]:
        basic_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/"
