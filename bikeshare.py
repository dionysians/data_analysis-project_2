import time
import pandas as pd
import numpy as np
import calendar

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWhich city Would you like to analyze? enter: Chicago, New York city,  Washington?\n')
        if city.lower() in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Please enter a valid city.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month would you like to analyze? enter: All, January, February, March, April, May, June\n')
        if month.lower() in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Please enter a valid month.\n')  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day of week would you like to analyze? enter: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n')
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']:
            break
        else:
            print('Please enter a valid day of week.\n')

    print('-'*40)
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if len(df['month'].unique()) > 1:
        most_common_month = df['month'].mode()[0]
        print('the most common month is :', calendar.month_name[most_common_month])
    
    # TO DO: display the most common day of week
    if len(df['day_of_week'].unique()) > 1:
        most_common_day = df['day_of_week'].mode()[0]
        print('the most common day of week is :', most_common_day)  

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    the_most_common_start_hour = df['hour'].mode()[0]
    print('the most common start hour is :', the_most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('the most common start station is :', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('the most common end station is :', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'].str.cat(df['End Station'], sep=' -- TO --')
    most_common_trip = df['trip'].mode()[0]
    print('the most frequent combination of start station and end station trip is :', most_common_trip)    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is :', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is :', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('There are the counts of user types :\n', user_type)
    
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('\nThere are the counts of gender :\n', gender)
    except:
        print('\nThere is no gender data.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        birth_min = df['Birth Year'].min()
        print('The earliest year of birth is :', birth_min)


        birth_max = df['Birth Year'].max()
        print('The most recent year of birth is :', birth_max)

        common_year = df['Birth Year'].mode()[0]
        print('The most common year of birth is :', common_year)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    
    except:
        print('\nThere is no birth year data.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
