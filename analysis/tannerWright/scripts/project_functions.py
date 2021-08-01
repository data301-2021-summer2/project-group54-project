
def load_and_process(file1, file2):
    import pandas as pd
    import numpy as np
    dfPlayerPoints =(
            
            pd.read_csv(file1, encoding = "\ISO-8859-1\ " )
            .dropna()
        )

    dfPlayerAS =(
            
            pd.read_csv(file2, encoding = "\ISO-8859-1\ " )
            .dropna()
        )
   
    dfMerged =(
            pd.merge(dfPlayerPoints, dfPlayerAS)
            .drop(columns = ['ATOI','BLK','HIT','FOW','FOL','FO_percent','HART','Votes','Tm', 'plusminus','PP', 'SH', 'EV.1', 'PP.1', 'S', 'S_percent', 'TOI', 'SH.1', 'PIM','PS', 'EV', 'Age', 'Pos', 'GW'])
            .dropna(subset=['Rk', 'Player', 'GP', 'G', 'A', 'PTS', 'Season'])

        .assign(
            PPG= lambda row: (row.PTS/row.GP)
        )
        .assign(
            GPG= lambda row: (row.G/row.GP) 
        )
        .assign(
                APG = lambda row: (row.A/row.GP)
        )
    )
  
    return dfMerged
