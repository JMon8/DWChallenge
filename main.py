import pandas as pd
import requests

# Make api call
def get_book_data():
    url = 'http://openlibrary.org/subjects/exercise.json'
    page_size = 100
    offset = 0

    books_list = []
    while(True):
        response = requests.get(url, params={'limit': page_size, 'offset': offset})
        print(f'Offset: {offset}, Status: {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            if 'works' in data:
                books_list.extend(data['works'])
            else:
                break
        else:
            print('Error:', response.status_code)
            break
        
        offset += page_size
        if offset > data['work_count']:
            break
    
    works_df = pd.DataFrame(books_list)
    return works_df

works_df = get_book_data()

# Limit to relevant fields and expand author list
works2_df = works_df[['key', 'title', 'authors',  'first_publish_year']]
works2_df = works2_df.explode('authors')
works2_df[['author_key','author_name']]= works2_df['authors'].apply(pd.Series)[['key','name']]
works2_df = works2_df.drop(columns=['authors'])

# Create author and book dataframes
authors_df = works2_df[['author_key', 'author_name']].drop_duplicates()
books_df = works2_df[['key', 'title',  'first_publish_year']].drop_duplicates()
book_authors_df = works2_df[['key', 'author_key']].drop_duplicates()

output_path = 'outputs/'
authors_df.to_csv(f'{output_path}authors.csv', index=False)
books_df.to_csv(f'{output_path}books.csv', index=False)
book_authors_df.to_csv(f'{output_path}book_authors.csv', index=False)

# # Write to Database
# from sqlalchemy import create_engine
# engine = create_engine('postgresql:///user:pass@host/db_name')
# authors_df.to_sql('authors', con=engine, if_exists='replace', index=False)
# books_df.to_sql('books', con=engine, if_exists='replace', index=False)
# book_authors_df.to_sql('book_authors', con=engine, if_exists='replace', index=False)