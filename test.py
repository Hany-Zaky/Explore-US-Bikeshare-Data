import time
import pandas as pd
import numpy as np

CITY_DATA = { 'c': 'chicago.csv',
              'n': 'new_york_city.csv',
              'w': 'washington.csv' }

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
    city = input(
        "Would you like to see data? \n You can type \n n  for new york city,\n w  for washington, or\n c  for chicago \n: ").lower()
    while city not in CITY_DATA.keys():
        print(' Please enter one of the above three cities')
        city = input(
            "Would you like to see data? \n You can type \n n  for new york city,\n w  for washington, or\n c  for chicago \n: ").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april", "may", "june", "all"]
    month = input(
        "'Please choose a month from this list: \n all,\n january,\n february,\n march,\n april,\n may, \njune,\n: ").lower()
    while month not in months:
        print("Invalid month choose")
        month = input(
            "'Please choose a month from this list: \n all,\n january,\n february,\n march,\n april,\n may, \njune,\n:").lower()
        if month.title() in months:
            break
    print(month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week = ["monday", "tuesday", "wednesday" "thursday", "friday", "saturday", "sunday", "all"]
    day = input(
        "'Please choose a day of week from this list:\n all, \n monday,\n tuesday,\n wednesday, \n thursday, \n friday,\n saturday,\n sunday,\n: ").lower()
    while day not in day_of_week:
        print("Invalid day choose")
        day = input(
            "'Please choose a day of week from this list: \n all, \n monday,\n tuesday,\n wednesday, \n thursday, \n friday,\n saturday,\n sunday,\n:  ").lower()
        if day.title() in day_of_week:
            break

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour

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
     print(df["month"].mode()[0])
     # TO DO: display the most common day of week
     print(df["day_of_week"].mode()[0])

     # TO DO: display the most common start hour
     print(df["hour"].mode()[0])

     print("\nThis took %s seconds." % (time.time() - start_time))
     print('*'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("the most commonly used start station is:", common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("the most commonly used end station is:", common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = df["Start Station"] + "-" + df["End Station"]
    combination =(df["combination"].mode()[0])
    print("\n the most frequent combination of start station and end station trip :\n",combination )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('+'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print(" total travel time is:", total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print(" mean travel time is :", mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth
    print(df["User Type"].value_counts())
    # TO DO: Display counts of gender
    if city != "w":
        counts_of_gender = df["Gender"].value_counts()
        print("\n counts of user types :", counts_of_gender)
        # TO DO: Display earliest, most recent, and most common year of birth
        common_year_birth = int(df['Birth Year'].mode()[0])
        print("\n the most common year of birth:", common_year_birth)
        earliest_year_birth = int(df['Birth Year'].min())
        print("\n the earliest year of birth:", earliest_year_birth)
        recent_year_birth = int(df['Birth Year'].max())
        print("\n the most recent year of birth:", recent_year_birth)
    else:
        print("Gender status canot be calculated because Gender does not appear in dataframe")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Goodbye.... Have a nice Day")
            break


if __name__ == "__main__":
	main()
