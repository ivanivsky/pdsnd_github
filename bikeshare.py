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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nPlease enter the city: ').lower()
    while city not in ('chicago', 'new york city', 'washington'):
        print('You must enter a valid city')
        city = input('\nPlease enter the city: ').lower()

    # get user input for month (all, january, february, ... , june)
    month = input('\nWould you like to filter by month? Please enter a month (January thru June) or enter "NA": ').lower()
    while month not in ('january', 'february', 'march', 'april', 'may', 'june', 'na'):
        print('You must enter a valid month')
        month = input('Please select the month: ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWould you like to filter the data by day? Please select the day (Sunday thru Saturday) of enter "NA": ').lower()
    while day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'na'):
        print('You must enter a valid day')
        day = input('Please select the day: ').lower()

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

    # Load the data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create new colums for month and day
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month
    if month != 'na':
        # use index of the months to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'na':
        # Filter by day to create new dataframe
        df = df[df['day_of_week'] == day.title()]
        print("df after day of week", df)

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most popular month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    popular_month = df['month'].mode()[0]

    print('\nThe most popular month is:', popular_month)

    # display the most common day of week
    df['Week'] = df['Start Time'].dt.week

    popular_week = df['day_of_week'].mode()

    print('\nThe most popular day of the week is:', popular_week[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]

    print('\nThe most popular hour is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_mode = df['Start Station'].mode()[0]

    print('\nThe most commonly used starting station is:', start_station_mode)

    # display most commonly used end station
    end_station_mode = df['End Station'].mode()[0]

    print('\nThe most commonly used end station is:', end_station_mode)

    # display most frequent combination of start station and end station trip
    start_stop_most_frequent = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print('\nThe most frequent combination of start and end stations are:', start_stop_most_frequent)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time_total = df['Trip Duration'].sum()

    print('\nThe total travel time for this time period is:', travel_time_total)

    # display mean travel time
    travel_time_average = df['Trip Duration'].mean()

    print('\nThe average travel time is:', travel_time_average)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_washington(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print('\nThe user types are:\n', user_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print('\nThe user types are:\n', user_types)

    # Display counts of gender
    gender_count = df['Gender'].value_counts()

    print('\nThe gender count is:\n', gender_count)

    # Display youngest birth year
    birth_year_youngest = df['Birth Year'].max()

    print('\nThe younger birth year is:', birth_year_youngest)

    # Display oldest year of birth
    birth_year_oldest = df['Birth Year'].min()
    print('\nThe oldest birth year is:', birth_year_oldest)

    birth_year_mode = df['Birth Year'].mode()[0]
    print('\nThe most common birth year is:', birth_year_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        # Get the filters
        city, month, day = get_filters()

        # Create the dataframe based on the filters
        df = load_data(city, month, day)

        # Get the time stats
        time_stats(df)

        # Get the station stats
        station_stats(df)

        # Get the trip duration stats
        trip_duration_stats(df)

        # Get the user stats
        # I'm not sure if this is a good or a bad practice, but it seemed easiest to
        # provide washington with it's own function given the difference in data that's available.
        if city.lower() != 'washington':
            user_stats(df)
        else:
            user_stats_washington(df)

        # Does the user want the first five lines of data?
        # I did my best getting this to work, but I'm sure there's a better way
        # Created a couple of indexes for use in iloc
        i = 0
        j= 5
        while True:
            # Does the user want to receive five lines of data?
            five_lines = input('\nWould you like to see five lines of raw data? Please enter "Yes" if so, or anything else for "No": ')

            # If the user does, print out five lines based on the indexes i and j
            if five_lines.lower() == 'yes':
                print(df.iloc[i:j])
                i += 5
                j += 5
                continue
            # If they don't want five lines, break from the function
            elif five_lines.lower() == 'no':
                break
            # Require that they specify Yes or No
            else:
                print('Enter either Yes or No')

        # Does the user want to restart
        restart = input('\nWould you like to restart? Enter yes or no. ')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
