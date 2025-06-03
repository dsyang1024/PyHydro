def FDC (streamflow, title='', unit=r'ft$^{3}$/sec'):

    """_summary_
        `FDC` is a function that generates a Flow Duration Curve (FDC) plot for a given streamflow data.
    
    Args:
        streamflow (_list_): a numerical list of the streamflow data.
        title (str): title of the plot. Default is None.
        unit (str): unit of the streamflow data. Default is ft^3/sec.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    plt.rcParams["font.family"] = "Times New Roman"
    
    # Sort the streamflow data in descending order
    sorted_streamflow = np.sort(streamflow)[::-1]

    # Calculate exceedance probability
    exceedance_probability = np.arange(1, len(sorted_streamflow) + 1) / (len(sorted_streamflow) + 1)

    # Create the FDC plot
    plt.figure(figsize=(6, 4))
    plt.plot(exceedance_probability * 100, sorted_streamflow, color='darkblue')
    
    plt.yscale('log')
    plt.ylabel(r'Streamflow ('+unit+')')

    plt.xlabel("Flow Exceedance(%)")
    plt.xlim(0,100)
    plt.xticks([0,10,40,60,90,100])
    plt.grid()

    plt.title(title+' FDC') if title != '' else None
    plt.tight_layout()
    plt.savefig('FDC.png',dpi=600)
    # plt.show()
    plt.clf()




def boxplot (wq_data, unit=r'mg/L',criteria='all'):
    """_summary_
        `boxplot` is a function that generates a boxplot for a given water quality data.
    Args:
        wq_data (pandas DataFrame): DataFrame containing water quality data. Index must be date(yyyy-mm-dd) and columns are parameters
        unit (str): unit of the water quality data. Default is mg/L
        criteria (str): criteria for which boxplot is to be generated (all, monthly, annual, seasonal). Default is 'all'
    """
    import matplotlib.pyplot as plt
    plt.rcParams["font.family"] = "Times New Roman"


    if criteria == 'all':
        # Create the boxplot for each parameter
        for i in wq_data.columns.to_list():
            plt.figure(figsize=(6, 4))
            wq_data[i].plot.box()
            plt.ylabel('Concentration ('+unit+')')
            plt.tight_layout()
            plt.grid()
            plt.savefig(i+'_Boxplot.png',dpi=600)
            # plt.show()
            plt.clf()
    
    elif criteria == 'monthly':
        # Create the boxplot for each parameter for each month
        for i in wq_data.columns.to_list():
            temp = wq_data[i].to_frame()
            temp.groupby(temp.index.month).boxplot(subplots=False,figsize=(6, 4))
            plt.ylabel('Concentration ('+unit+')')
            # set xtick label as month name
            plt.xticks(ticks=range(1,13),labels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
            plt.tight_layout()
            plt.savefig(i+'_Monthly_Boxplot.png',dpi=600)
            # plt.show()
            plt.clf()

    elif criteria == 'annual':
        print ('Annual option is not recommended at this point. It will be updated in the future release.')
        # Create the boxplot for each parameter for each month
        wq_data.groupby(wq_data.index.year).boxplot(subplots=False,figsize=(6, 4), rot=45)
        plt.xlabel('Year, WQ')
        plt.ylabel('Concentration ('+unit+')')
        plt.tight_layout()
        plt.savefig('Annual_Boxplot.png',dpi=600)
        # plt.show()
        plt.clf()

    elif criteria == 'seasonal':
        # Create the boxplot for each parameter for each month
        for i in wq_data.columns.to_list():
            temp = wq_data[i].to_frame()
            # if month is 3,4,5 then it is spring, 6,7,8 then summer, 9,10,11 then autumn, 12,1,2 then winter
            temp['season'] = temp.index.month.map({1: '4-Winter', 2: '4-Winter', 3: '1-Spring', 4: '1-Spring', 5: '1-Spring', 6: '2-Summer', 7: '2-Summer', 8: '2-Summer', 9: '3-Autumn', 10: '3-Autumn', 11:'3-Autumn', 12: '4-Winter'})
            temp.groupby(temp['season']).boxplot(subplots=False,figsize=(5, 3))
            # change xtick order
            plt.xticks(ticks=[1,2,3,4],labels=['Spring','Summer','Autumn','Winter'])
            plt.ylabel('Concentration ('+unit+')')
            plt.tight_layout()
            plt.savefig(i+'_Seasonal_Boxplot.png',dpi=600)
            # plt.show()
            plt.clf()




def hydrograph (sp_df, title='', unit=r'ft$^{3}$/sec'):
    """_summary_
        `hydrograph` is a function that generates a hydrograph plot for a given streamflow data.
    Args:
        sp_df (pandas DataFrame): DataFrame containing streamflow and precipitation data index must be date(yyyy-mm-dd) and columns are streamflow and precipitation
        title (str): title of the plot. Default is ''
        unit (str): unit of the streamflow data. Default is ft^3/sec
    """
    import matplotlib.pyplot as plt
    plt.rcParams["font.family"] = "Times New Roman"

    # plot streamflow
    sp_df['streamflow'].plot.line(color='darkblue', figsize=(10, 5), linewidth=1.5, label='Streamflow')

    plt.ylabel('Streamflow ('+unit+')')

    plt.xlabel('Date')
    plt.grid()
    plt.suptitle(title+' Hydrograph') if title != '' else None
    plt.tight_layout()
    plt.savefig('Hydrograph.png',dpi=600)
    # plt.show()
    plt.clf()




def test_version(a, b, c):
    """_summary_

    Args:
        a (_int_): major version number
        b (_float_): minor update number
        c (_name_): last editor
    """

    version = f"{a}.{b}_{c}"
    import PyHydro
    print('PyHydro version:', version)



def sim_vali(simlist, obslist, title='', unit=r'ft$^{3}$/sec'):
    """_summary_
        `sim_vali` is a function that generates a scatter plot for simulated and observed values.
    
    Args:
        simlist (_list_): a numerical list of the simulated values.
        obslist (_list_): a numerical list of the observed values.
        title (str): title of the plot. Default is ''
        unit (str): unit of the values. Default is ft^3/sec
    """
    import matplotlib.pyplot as plt
    plt.rcParams["font.family"] = "Times New Roman"

    if len(simlist) != len(obslist):
        raise ValueError("The length of simulated and observed lists must be the same.")

    plt.figure(figsize=(5, 5))
    plt.scatter(obslist, simlist, color='darkblue', alpha=0.5)
    plt.plot([min(obslist), max(obslist)], [min(obslist), max(obslist)], color='red', linestyle='--')

    plt.xlabel('Observed ('+unit+')')
    plt.ylabel('Simulated ('+unit+')')
    plt.title(title+' Simulated vs Observed') if title != '' else None
    # add infinite 45 degree line for reference
    plt.axline((0, 0), slope=1, color='green', linestyle='--', label='1:1 Line')

    # add linear regression line
    from sklearn.linear_model import LinearRegression
    import numpy as np
    X = np.array(obslist).reshape(-1, 1)
    y = np.array(simlist)
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    plt.plot(obslist, y_pred, color='red', label='Linear Regression', linewidth=1.5)
    
    graph_min = min(min(obslist), min(simlist))
    graph_max = max(max(obslist), max(simlist))
    plt.xlim(graph_min, graph_max)
    plt.ylim(graph_min, graph_max)
    plt.grid()
    plt.tight_layout()
    plt.legend()
    plt.savefig('Simulated_vs_Observed.png',dpi=600)
    # plt.show()
    plt.clf()
