import pandas as pd

df=pd.read_csv("C:/Users/Rajesh.Sudam/Downloads/Netflix/data/netflix_titles.csv")

def test_dataset_not_empty():
    assert len(df)>0

def test_show_id_exists():
    assert df['show_id'].isnull().sum()==0

def test_release_year_valid():
    assert df['release_year'].min()>1990

def test_content_type():
    valid=['Movie','TV Show']

    for t in df['type'].unique():
        assert t in valid

