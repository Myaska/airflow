from dataclasses import dataclass

# import pydantic as pyd


class ExtractClient:
    async def get(url: int) -> dict[str, str]: ...


@dataclass
class ExtractProperties:
    MolecularFormula = "MolecularFormula"
    MolecularWeight = "MolecularWeight"
    CanonicalSMILES = "CanonicalSMILES"
    IsomericSMILES = "IsomericSMILES"
    InChI = "InChI"
    InChIKey = "InChIKey"
    IUPACName = "IUPACName"
    Title = "Title"
    XLogP = "XLogP"
    ExactMass = "ExactMass"
    MonoisotopicMass = "MonoisotopicMass"
    TPSA = "TPSA"
    Complexity = "Complexity"


# class ExtractTask(pyd.BaseModel):
#     cid: int
#     properties: str
#     extract_client: ExtractClient
