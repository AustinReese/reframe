import sys
sys.path.insert(1, '../')

from reframe import Relation

def test_rename_removes_col():
    '''
    assert that renaming a column removes the first column header and adds the second
    '''
    df = Relation("../country.csv")
    renamed_df = df.rename("indepyear", "yearofindep")
    assert "indepyear" in df.columns
    assert "yearofindep" not in df.columns
    assert "indepyear" not in renamed_df.columns
    assert "yearofindep" in renamed_df.columns
    
def test_rename_preserves_data():
    '''
    assert that renaming a column preserves the data
    '''
    df = Relation("../country.csv")
    renamed_df = df.rename("governmentform", "formofgov")
    assert df["governmentform"].equals(renamed_df["formofgov"])
    

def test_rename_nonexistent_cols():
    '''
    assert that renaming a fake column returns the same dataframe as before and that a new empty column is not added
    '''
    df = Relation("../country.csv")
    renamed_df = df.rename("a_fake_column", "something_nice")
    assert "something_nice" not in renamed_df.columns
    assert df.equals(renamed_df)
    