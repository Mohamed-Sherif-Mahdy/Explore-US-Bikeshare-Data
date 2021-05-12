import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '/home/mohamedsherif/Downloads/Compressed/bikeshare/chicago.csv',
              'new york city': '/home/mohamedsherif/Downloads/Compressed/bikeshare/new_york_city.csv',
              'washington': '/home/mohamedsherif/Downloads/Compressed/bikeshare/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    while True:
        try:
            city=input("enter the name of the city you want"+'\n')
            
            # get user input for month (all, january, february, ... , june)
            month=input("enter the name of the month you want or all for all months"+'\n')

            # get user input for day of week (all, monday, tuesday, ... sunday)
            day=input("enter the name of the day you want or all for all days"+'\n')
            if city in CITY_DATA and month in ['january', 'february', 'march', 'april', 'may', 'june','all'] and day in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
                break
            else:
                print("Sorry, I didn't understand that.")
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue


    #print('Hello! Let\'s explore some US bikeshare data!'+'\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #city=input("enter the name of the city you want"+'\n')

    # get user input for month (all, january, february, ... , june)
    #month=input("enter the name of the month you want or all for all months"+'\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    #day=input("enter the name of the day you want or all for all days"+'\n')

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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour


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

    # display the most common month
    print("most common month")
    print(df['Start Time'].dt.month.mode()[0])
    
    # display the most common day of week
    print("most common day of week")
    print(df['Start Time'].dt.day.mode()[0])

    # display the most common start hour
    print("most common start hour")
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("most commonly used start station")
    print(df["Start Station"].mode()[0])

    # display most commonly used end station
    print("most commonly used end station")
    print(df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    print("most frequent combination of start station and end station trip")
    print(df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("total travel time")
    print(df['Trip Duration'].sum())

    # display mean travel time
    print("mean travel time")
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("counts of user types")
    print(pd.value_counts(df['User Type']))

    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        # Display counts of gender
        print("counts of gender")
        print(pd.value_counts(df['Gender']))
        print("earliest year of birth")
        print(df['Birth Year'].min())
        print("most recent year of birth")
        print(df['Birth Year'].max())
        print("most common year of birth")
        print(df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
