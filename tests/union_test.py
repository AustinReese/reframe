import sys
sys.path.insert(1, '../')

import pandas as pd
from reframe import Relation

def test_union():
    df = pd.DataFrame({"cats":["tony", "felix", "sue", "ezekiel"],
                       "dogs":["buddy", "sadie", "chicken little", "doug"]
                       })
    df2 = pd.DataFrame({"cats":["fella", "chief", "ruth bader ginsburg", "pat"],
                        "dogs":["coke", "wendy", "dog", "john cleese"]
                       })
    r = Relation(df)
    r2 = Relation(df2)
    r_union = r.union(r2)
    
    assert len(r_union) == 8
    assert "tony" in list(r_union.cats)
    assert "ruth bader ginsburg" in list(r_union.cats)
    assert "doug" in list(r_union.dogs)
    assert "coke" in list(r_union.dogs)
    
test_union()