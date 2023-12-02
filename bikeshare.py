import time

import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York City, or Washington? \n').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Please select between Chicago, New York City or Washington: \n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month - All, January, February, March, April, May, or June? \n').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('Please select between All, January, February, March, April, May, or June: \n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day - All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input(
            'Please select between All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday: \n').lower()

    print('-' * 40)
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

    # convert the Start Time and End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

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
    try:
        print('\nMost Popular Month: ', df['month'].mode()[0])
    except KeyError:
        print('\nThere is no Month data')

    # TO DO: display the most common day of week
    try:
        print('\nMost Popular Day of Week: ', df['day_of_week'].mode()[0])
    except KeyError:
        print('\nThere is no day of Week data')

    # TO DO: display the most common start hour
    try:
        print('\nMost Popular Start Hour: ', df['hour'].mode()[0])
    except KeyError:
        print('\nThere is no Hour data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        print('\nMost Popular Start Station: ', df['Start Station'].mode()[0])
    except KeyError:
        print('\nThere is no Start Station data')

    # TO DO: display most commonly used end station
    try:
        print('\nMost Popular End Station: ', df['End Station'].mode()[0])
    except KeyError:
        print('\nThere is no End Station data')

    # TO DO: display most frequent combination of start station and end station trip
    try:
        most_combination_start_and_end_station = df.groupby('Start Station')['End Station'].value_counts().idxmax()
        print('\nMost frequent combination of start station and end station trip: ',
              most_combination_start_and_end_station)
    except KeyError:
        print('\nThere is no Start Station and End Station data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
        total_duration = df['Trip Duration'].sum()
        print("\nTotal travel time in hours is: ", total_duration)
    except KeyError:
        print('\nThere is no Trip Duration data')

    # TO DO: display mean travel time
    try:
        mean_duration = df['Trip Duration'].mean()
        print("\nMean travel time in hours is: ", mean_duration)
    except KeyError:
        print('\nThere is no Trip Duration data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print('\nUser type: \n', user_types)
    except KeyError:
        print('\nThere is no User Type data')

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender type: \n', gender_types)
    except KeyError:
        print('\nThere is no Gender data')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\nThe earliest year of birth is: ', df['Birth Year'].min())
        print('\nThe most recent year of birth is: ', df['Birth Year'].max())
        print('\nThe most common year of birth is', df['Birth Year'].mode()[0])
    except KeyError:
        print('\nThere is no Birth Year data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df):
    """Raw data is displayed upon request by the user in the following manner:
    If the user want to see 5 lines of raw data,
    Display that data if the answer is 'yes',
    Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration,
    Stop the program when the user says 'no' or there is no more raw data to display."""

    print("\nWould you like to view individual trip data ? Type 'yes' or 'no' ")
    while input() != 'no':
        print(df.head())


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
