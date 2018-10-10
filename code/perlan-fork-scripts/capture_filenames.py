import pandas as pd 


def filenames2df(fname_list):
# Given a list of urls and the filenames available at that url
# Convert the list to a Pandas dataframe


    # Create a dataframe with the
    # subdirectory, full filename, file extension

    # pd.DataFrame(urls) is NOT the way to go, because it takes the list of dictionaries
    # and makes each dictionary a separate column, with the key as the column name
    # and the value's entire list as a single entry 

    # We want the key to be in the "subdirectory" column as many times as there
    # are files in the subdirectory

    # We want full filename to be in the "filename" column, with NULL if the directory
    # had no files

    # We want the file extension to be in the "extension" column

    pd_list = []

    # Iterate through fname_list
    for url in fname_list:
        (k, v), = url.items()
        if v:
            for fname in v:
                pd_list.append(
                        pd.DataFrame(
                            {'directory' : [k.replace('http://www.perlanproject.cloud','')], 
                            'filename' : [fname], 
                            'extension' : [fname.split(".")[1]]}
                        )
                )

    return pd.concat(pd_list, ignore_index=True)


def df_to_everything(df, dirname = 'C:/Users/natha/OneDrive - Georgia Institute of Technology/Perlan/perlan-data/code/perlan-fork-scripts'):
# Convert the DataFrame to every file format in 
# https://pandas.pydata.org/pandas-docs/stable/io.html
# except "Local clipboard"

    # Create pathname for csv file that will capture the filenames
    filepath = dirname + '/filenames'

