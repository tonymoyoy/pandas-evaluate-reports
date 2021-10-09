import pandas as pd
import warnings

# This option is because I was getting a warning about the engine
warnings.simplefilter("ignore")

# Read the excel files to generate the dataframes
df1 = pd.read_excel('report1.xlsx', engine="openpyxl")
df2 = pd.read_excel('report2.xlsx', engine="openpyxl")

# Option to show all the columns of the Dataframe
pd.set_option('display.max_rows', None)

# This is a list of people I'm interested in, in a way I can opt-in the names instead of cleaning the unwanted entries later.
team_members = ["Rosenda Slaugh", "Jimmy Warlick", "Kelley Riss",
                "Marjorie Marsland", "Marcela Vantassell", "Sherron Philyaw"]

# Create two empty lists to calculate the hours
report_hours_1 = [0]*len(team_members)
report_hours_2 = [0]*len(team_members)

# This list will be use to calculate time for one of the reports
time_column = []
# This list is for the final dataframe
sum_hours = []
# This list will be use to calculate a report based on the type of tasks
type_column = []

# Adding a value in minutes to type of tasks
time_incident = 5
time_request = 20
time_change = 60


# Evaluate the report based on diferent columns, classify assign the time to each entry
# This can be more complex because we can get more types of work based on short description or other columns
for index, row in df1.iterrows():
    if 'Incident' in df1['Task type'][index]:
        type_column.append("Incident")
        time_column.append(time_incident)
    elif 'Create Account' in df1['Short Description'][index]:
        type_column.append("Request")
        time_column.append(time_request)
    elif 'Change Task' in df1['Short Description'][index]:
        type_column.append("Change")
        time_column.append(time_column)

# Add columns to the dataframe 1
df1.insert(len(df1.columns), "Type", type_column)
df1.insert(len(df1.columns), "Minutes", time_column)

# Populate the new lists with the sum of hours per team member
for index, team_member in zip(range(len(team_members)), team_members):
    x = df1.loc[df1['Assigned to'] == team_member]
    y = df2.loc[df2['Owner'] == team_member]
    sum_hours1 = x['Minutes'].sum()/60
    sum_hours2 = y['Hours'].sum()
    report_hours_1[index] = sum_hours1
    report_hours_2[index] = sum_hours2
    sum_hours.append(report_hours_1 + report_hours_2)


# Generate new dataframe from lists
results = pd.DataFrame(list(zip(team_members, report_hours_1, report_hours_2, sum_hours)), columns=[
                       'Name', 'Report 1', 'Report 2', 'Total'])

# Show results in screen
print(results)
