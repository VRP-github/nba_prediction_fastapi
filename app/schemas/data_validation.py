from pydantic import BaseModel

class getPredValidation(BaseModel):
    AST: float
    STL: float
    BLK: float
    TRB: float
    FGA: float
    FG_PERCENTAGE: float
    THREE_P:float
    THREE_PA:float
    PF: float
    eFG_PERCENTAGE : float
    FT_PERCENTAGE:float
    DRB:float
    THREE_P_PERCENTAGE:float
    TWO_P:float
    TWO_P_PERCENTAGE:float

