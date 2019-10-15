import sys
sys.path.insert(1, '../')

import pandas as pd
from reframe import Relation

def test_rename():
    df = pd.DataFrame({"cats":["tony", "felix", "sue", "ezekiel"],
                       "dogs":["buddy", "sadie", "chicken little", "doug"],
                       "birds":["polly", "burt reynolds", "tim", "baker"],
                       "ferrets":["spook", "boo", "chowder", "chef"]
                       })
    r = Relation(df)
    new_r = r.rename("cats", "foes")
    assert "cats" in r.columns
    assert "foes" not in r.columns
    assert "foes" in new_r.columns
    assert "cats" not in new_r.columns
