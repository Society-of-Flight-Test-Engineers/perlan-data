import numpy as np
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


def df_to_everything(df, dirname = 'C:/Users/natha/OneDrive - Georgia Institute of Technology/Perlan/perlan-data/products'):
# Convert the DataFrame to every file format in 
# https://pandas.pydata.org/pandas-docs/stable/io.html
# except "Local clipboard"

    # Create pathname for files that will capture the filenames
    filepath = dirname + '/filenames'
    print(filepath)
    df.to_csv(filepath + '.csv')
    print('csv made')
    df.to_json(filepath + '.json')
    print('json made')
    df.to_html(filepath + '.html')
    print('html made')
    df.to_excel(filepath + '.xlsx', engine='xlsxwriter') # requires xlsxwriter
    print('excel made')
    df.to_hdf(filepath + '.h5', key='df', mode='w') # requires pytables
    print('hdf5 made')
    # Feather is deprecated
    # df.to_feather(filepath + '.feather') # requires installation of feather-format https://anaconda.org/conda-forge/feather-format
    # print('feather made')
    df.to_parquet(filepath + '.parquet', engine='pyarrow') # requires pyarrow
    print('parquet made')
    df.to_msgpack(filepath + '.msg')
    print('msgpack made')
    df.to_stata(filepath + '.dta')
    print('stata made')
    df.to_pickle(filepath + '.pkl')
    print('pkl made')
    # df.to_sql(filepath + '.')
    # df.to_gbq(filepath + '.')