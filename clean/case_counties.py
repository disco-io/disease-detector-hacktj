def clean():
    # import libraries
    import pandas as pd
    import matplotlib.pyplot as plt

    # Read in the data
    df = pd.read_csv("covid_confirmed_usafacts.csv")

    # Get all unique county names in VA
    va_counties = df[df['State'] == 'VA']['County Name'].unique()

    # Iterate through all counties in VA and create a plot for each
    for county in va_counties:
        # Find the row that matches the county name
        county_row = df[df['County Name'].str.contains(county)]

        if county_row.empty:
            print(f"County '{county}' not found in the data.")
            continue

        # Extract the Date and Count columns
        county_data = pd.DataFrame({'Date': county_row.columns[4:], 'Count': county_row.values[0][4:]})

        # Convert the Date column to a datetime object
        county_data['Date'] = pd.to_datetime(county_data['Date'])

        # Plot the data
        plt.plot(county_data['Date'], county_data['Count'])
        plt.title(county)

        # Save the plot as a png image
        plt.savefig(county + '.png')
        
        # Clear the plot to avoid overlapping plots
        plt.clf()

clean()
