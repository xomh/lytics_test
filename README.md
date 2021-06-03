# lytics_test
This Python Script has as objective:


* Obtain from variable ``url`` automatically COVID-19 cases in USA.
    * In function ``create()``:
        ```bash
        url = PATH #url is a parameter (csv file url to its raw url format) passed to the read_csv() function to obtain the data record
        ```

* Set the info in a Pandas Dataframe.
    * In function ``create()``:
        ```bash
        df = pd.read_csv(PATH) #df is our Dataframe
        ```

* Show a table with total cases per day.
    * In function ``showtable()``:
        ```bash
        df = casesperday() #create our Dataframe with a new column with the cases per day using the 'cases' column (daily cumulative number of cases)

        df_res = df[['columnns']].copy() #create a copy of Dataframe only with the necessary columns

        #finally print the table with total cases per day
        ```
* Display the chart with the top ten days with the most cases.
    * In function ``displaychart(bool)``:
        ```bash
        df.sort_values() #sort Dataframe to obtain the top ten
        
        column = df_aux.head(10)['column'].tolist() #convert a column with the first ten values to a list
        
        column.reverse() #for a better visualization of the chart, the values are ordered in reverse order
        
        axis = np.array(column) #set the values in x and y axis

        #set the properties to the chart view
        
        if bool: #if the bool value is true, the window where the chart is going to be seen is resize to the max size
        ```
* Save the chart in local storage.
     * In function ``displaychart(bool)``:
        ```bash
        #if the bool value is false, create the "Get the current figure" with the function gcf() and after save it:
        
        else:
            fig = plt.gcf()
            fig.savefig("name.png")
        ```