import sys
sys.path.insert(1, '../')

import pytest
import sys
import pandas as pd
from reframe import Relation

def test_union_on_continent():
    '''
    assert the length a union on two dataframes queried by continent is the same as the sum of the previous two lengths
    '''
    df = Relation("../country.csv")
    africa_df = df.query("continent == 'Africa'")
    europe_df = df.query("continent == 'Europe'")
    union_df = africa_df.union(europe_df)
    assert (len(africa_df) + len(europe_df)) == len(union_df)

def test_union_remove_duplicates():
    '''
    assert union removes duplicate rows by comparing lengths of a dataframe against the length of one unioned with itself
    '''
    df = Relation("../country.csv")
    republic_df = df.query("governmentform == 'Republic'")
    union_on_itself_df = republic_df.union(republic_df)
    assert len(republic_df) == len(union_on_itself_df)
    
def test_union_compatibility():
    '''
    assert that union only accepts compatable dataframes by attempting an illegal union
    '''
    df = Relation("../country.csv")
    monarchy_df = df.query("governmentform == 'Monarchy'")
    groupby_gov_df = df.groupby(['governmentform']).count('name')
    try:
        monarchy_df.union(groupby_gov_df)
    except ValueError as e:
        assert str(e) == "Relations must be Union compatible"
    except:
        '''
        all other errors result in test failure
        '''
        pytest.fail(f"Illegal union returned an unknown exception: {sys.exc_info()[0]} : {sys.exc_info()[1]}")
