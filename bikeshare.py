import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Getting user input for city (chicago, new york city, washington) and Making user input case insensitive
    city=(input('\nThere three cities to explore. There is Chicago, New York City and Washington. \nPlease type in the name of the city you are interested in:\n')).lower()

    cities=['chicago','new york city','washington']   #Cities list to compare with user input

    #Using a while loop to handle invalid inputs
    while city not in cities:
        city=(input('\nPlease choose one of the following cities.\nThere three cities to explore. There is Chicago, New York City and Washington. \nPlease type in the name of the city you are interested in:\n')).lower()

    # Getting user input for month (all, january, february, ... , june)
    months=(input('\nWhich month are you interested in? Please type the FIRST 3 letters of name of the first 6 month e.g Jan, Feb, Mar, Apr, May, Jun or type \"All\" to view every month\'s data\n')).title()
    #Months dictionary to compare with user input
    months_dic={'Jan':'January','Feb':'February','Mar':'March','Apr':'April','May':'May','Jun':'June','All':'All'}

    if months in months_dic:
        month=months_dic[months]

    #Using a while loop to handle invalid inputs
    while months not in months_dic:
        months=(input('\nPlease enter a valid input.\nWhich month are you interested in? Please type the FIRST 3 letters of name of the month e.g Jan, Feb, Mar, Apr, May, Jun or type \"All\" to view every month\'s data\n')).title()

    month=months_dic[months]


    # Getting user input for day of week (all, monday, tuesday, ... sunday)
    ui5=input('\nWhich day are you interested in? Please type the number associated with the day?\ne.g Monday = 1, Tuesday = 2 etc and to view all days in a week enter 8\n')

    #Days dictionary to compare with user input
    days_dic={'1':'Monday','2':'Tuesday','3':'Wednesday','4':'Thursday','5':'Friday','6':'Saturday','7':'Sunday','8':'All','1.0':'Monday','2.0':'Tuesday','3.0':'Wednesday','4.0':'Thursday','5.0':'Friday','6.0':'Saturday','7.0':'Sunday','8.0':'All'}

    #Checking user input and assigning day name to string variable 'day'
    number=(ui5)
    if number in days_dic:
        day=days_dic[number]

    #Using a while loop to handle invalid inputs
    while number not in days_dic:
        ui6=input('\nPlease type the number associated with the day?\ne.g Monday = 1, Tuesday = 2 etc and to view all days in a week enter 8\n')
        number=(ui6)
    day=days_dic[number]


    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    #remove spaces at both ends of the column entries
    df.columns=df.columns.str.strip()

    # convert the Start Time and End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday


    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months=['January','February','March','April','May','June']
        monthss = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == monthss]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe

        days_= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        df = df[df['day_of_week'] == (days_.index(day))]

    return df

def raw_data_displayer(df):
    """Displays different rows of data as long as the user requests based on the user's filter requirement.

    The user gets to choose how many rows to show at a time based on how many rows are available as per the filter parameters.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day."""

    # Getting user input raw data display preference
    ui7=input('\nWould like to see the Raw Data for your selected City? Type \'Yes\' to view Raw Data or \'No\' to display the Statistics\n')
    user_input = ui7.title()
    user_option=['Yes','No']

    #Using a while loop to handle invalid inputs
    while user_input not in user_option:
        ui8=input('\nPlease enter a valid selection.\n\nWould like to see the Raw Data for your selected City? Type \'Yes\' to view Raw Data or \'No\' to display the Statistics\n')
        user_input=ui8.title()

    num_string_list=[] #List to contain all row numbers converted to strings

    #Initialising variables to hold the user row increment number
    incre_num=0
    string_num='0'

    #Getting user input for row display increment if the user chooses to display raw data
    if user_input =='Yes':
        print('\nThere are {} rows for your filter option.\n'.format(df.shape[0]))
        for i in range(df.shape[0]-1):
            num_string_list.append(str(i+1))
        ui9=input('\nIn what row increments would you like to see the raw data? Please enter an integer (Whole Number)  between 0 and {}\n'.format(df.shape[0]))
        string_num=ui9

        #Using a while loop to handle invalid inputs
        while string_num not in num_string_list:
            ui10=input('\nPlease enter a valid number.\nIn what row increments would you like to see the raw data? Please enter an integer (Whole Number)  between 0 and {}\n'.format(df.shape[0]))
            string_num=ui10


    incre_num=int(string_num)
    #Initialising variables i and j for slicing the panda Dataframe df
    i=0
    j=incre_num

    #While loop to display raw data as long as the user requires the program to show more data.
    while user_input == 'Yes':
        print('\nThe raw data for your filter selection:\n ')
        print(df[i:j])

        #If statement to break the loop when all of the data has been displayed
        if j==df.shape[0]:
            print('\nAll the raw data has been displayed. Now displaying the statistics.\n')
            break;

        ui11=input('\nWould like to see more Raw Data for your selected City? Type \'Yes\' to view Raw Data or \'No\' to display the Statistics\n')
        user_input=ui11.title()

        #Using a while loop to handle invalid inputs
        while user_input not in user_option:
            ui12=input('\nPlease enter a valid selection.\n\nWould like to see more Raw Data for your selected City? Type \'Yes\' to view Raw Data or \'No\' to display the Statistics\n')
            user_input=ui12.title()

        k=j
        i+=incre_num
        j+=incre_num

        #If statement to ensure that i and j used to slice df do not go beyond the length of the Dataframe
        if j>df.shape[0]:
            i=k
            j=df.shape[0]

    print('-'*80)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month

    # Find the most popular month
    months_dic2={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June'}
    popular_month = df['month'].mode()[0]
    count=df['month'].value_counts()
    print('The most Popular month: {}       Counts: {}'.format(months_dic2[popular_month],count[popular_month]))

    # Display the most common day of week

    # Extract day from the Start Time column to create an hour column
    df['day_of_week'] = df['Start Time'].dt.weekday

    # Find the most popular day of week
    days_dic1={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    popular_day = df['day_of_week'].mode()[0]
    count1=df['day_of_week'].value_counts()
    print('\nThe most popular day: {}          Counts: {}'.format(days_dic1[popular_day],count1[popular_day]))



    # Display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    count2=df['hour'].value_counts()
    print('\nThe most popular hour: {}th hour       Counts: {}'.format(popular_hour,count2[popular_hour]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # Display most commonly used start station
    common_Start_station = df['Start Station'].mode()[0]
    print('The most common start station:',common_Start_station)

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe most common end station:',common_end_station)

    # Display most frequent combination of start station and end station trip
    df['Travel Combination'] =df['Start Station'].str.strip()+' TO '+df['End Station'].str.strip()
    print('\nThe most frequent combination of start and end station:',df['Travel Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Travel Time'] =df['End Time']-df['Start Time']
    print('Total travel time:',df['Travel Time'].sum())

    # TO DO: display mean travel time
    print('\nMean travel time:',df['Travel Time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # print value counts for each user type
    print('User Type Counts\n')
    user_types = df['User Type'].value_counts()
    for key, value in enumerate(user_types):
        print('{}:     {}'.format(user_types.index[key],value))


    # Display counts of gender
    if 'Gender' in df:

        print('\nGender Counts\n')
        gender_types = df['Gender'].value_counts()
        for key, value in enumerate(gender_types):
            print('{}:     {}'.format(gender_types.index[key],value))


    #Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        # Earliest year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('\nEarliest birth year:', int(earliest_birth_year))

        # Most recent year of birth
        recent_birth_year = df['Birth Year'].max()
        print('\nMost recent birth year:', int(recent_birth_year))

        # Most common years
        common_birth_year = df['Birth Year'].mode()[0]
        print('\nMost common birth year:', int(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data_displayer(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
