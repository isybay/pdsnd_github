import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
print("Are you ready?")


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
        cities= ['chicago','new york city','washington']
        city= input("\n Which city would you like to explore? (Chicago, New York City, Washington) \n").lower()
        if city in cities:
            break
        else:
            print("\n Please, enter a valid city name.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['January','February','March','April','June','May','None']
        month = input("\n Which month would you like to consider? (January, February, March, April, May, June)? If you're not considering any month, insert 'None'.\n").title()
        if month in months:
            break
        else:
            print("\n Please, enter a valid month.\n") 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','None']
        day = input("\n Which day of the week would you like to know more about? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? Type 'None' if no preference.\n").title()         
        if day in days:
            break
        else:
            print("\n Please, enter a valid day\n") 


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
    df = pd.read_csv(CITY_DATA.get(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    
    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1    
        df = df[df['month'] == month]
        
    if day.lower() != 'all':
         days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
         day = days.index(day.lower()) + 1    
         df = df[df['day'] == int(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    com_month = df['month'].mode()[0]
    print('The most common month: ', com_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday
    com_day = df['day'].mode()[0]
    print('The most common day: ', com_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    com_hour = df['hour'].mode()[0]
    print('The most common hour: ', com_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is ", df['Start Station'].mode()[0], "\n")

    # TO DO: display most commonly used end station
    print("The most commonly used end station is ", df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is", df['Trip Duration'].sum(), "\n")

    # TO DO: display mean travel time
    print("The total mean time is", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

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
