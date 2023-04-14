import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
	
#	Request user inputs
	
    while True:
        city = input("Would you like to see bikeshare data on Chicago, New York City, or Washington? ")
        city = city.lower()
        if city in CITY_DATA:
            df = pd.read_csv(CITY_DATA.get(city))
            break
        else:       
            print("City entry is invalid, please retry")

    while True:
        month_str = input("What month would you like to filter on? (Type 'all' if no filter desired)")
        if month_str.lower() == "all":
            month = None
            break
    
        month_dic = {'january': 1,
                     'february': 2,
                     'march': 3,
                     'april': 4,
                     'may': 5,
                     'june': 6,
                     'july': 7,
                     'august': 8,
                     'september': 9,
                     'october': 10,
                     'november': 11,
                     'december': 12}
        month = month_dic.get(month_str.lower())
        if month is not None:
            break
        else:
            print("Month invalid, please retry")
            
    while True:
        day_str = input("What day of the week would you like to filter on? (type 'all' if no filter desired)")
        if day_str.lower() == "all":
            day = None
            break        
        day = day_str.title()
        day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        if day in day_list:
            break
        else:
            print("Day invalid, please retry")
    
    print("City: {}   Month:{}   Day:{}".format(city, month_str, day_str))
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])    
    
    if month and day:
        filtered_df = df[(df['Start Time'].dt.month == month) & (df['Start Time'].dt.weekday_name == day)]
    elif month:
        filtered_df = df[df['Start Time'].dt.month == month]
    elif day:
        filtered_df = df[df['Start Time'].dt.weekday_name == day]
    else:
        filtered_df = df  
    
    column_to_return = 'Start Time'
    
    if filtered_df.empty:
        print("No data available in this month.")
    else:
        filtered_column = filtered_df[column_to_return]
                      
                      
    print('-'*40)
  
#	Calculates most frequent time traveled

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    if not filtered_df.empty:
        stats_month = filtered_df['Start Time'].dt.month.mode()[0]
        stats_day = filtered_df['Start Time'].dt.day.mode()[0]
        stats_hr = filtered_df['Start Time'].dt.hour.mode()[0]
    print("Most common month: {}".format(stats_month))
    print("Most common day: {}".format(stats_day))
    print("Most common hr: {}".format(stats_hr))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
	print('-'*40)

    pop_start_station = filtered_df['Start Station'].mode()[0]
    print("Most popular start station: {}".format(pop_start_station))
	print('-'*40)

    pop_end_station = filtered_df['End Station'].mode()[0]
    print("Most popular end station: {}".format(pop_end_station))
	print('-'*40)

    all_stations = pd.concat([filtered_df['Start Station'], filtered_df['End Station']])
    pop_all_stations = all_stations.mode()[0]
    print("Most commonly used station:{}".format(pop_all_stations))
	print('-'*40)
    
    df['trip'] = filtered_df['Start Station'] + ' to ' + filtered_df['End Station']
    pop_trip = df['trip'].mode()[0]
    print("Most common trip: {}".format(pop_trip))
	print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_trip_duration = filtered_df['Trip Duration'].sum()
    print("Total trip duration: {}".format(total_trip_duration))
    
    mean_trip_duration = filtered_df['Trip Duration'].mean()
    print("Mean trip duration: {}".format(mean_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type_counts = filtered_df.groupby("User Type").size()
    print("User Types: {}".format(user_type_counts))

    
    if "Gender" in filtered_df.columns:
        gender_counts = filtered_df.groupby("Gender").size()
        print("\nUser Genders: {}".format(gender_counts)) 
    else:
        print("No Gender Data Available")
 
    
    
    if "Birth Year" in filtered_df.columns:
        earliest = int(filtered_df["Birth Year"].min()) 
        most_common = int(filtered_df["Birth Year"].mode())
        print("\nOldest User: {}".format(earliest))
        print("Most Common Year of Birth: {}".format(most_common)) 
    else:
        print("No Birth Data Available")
         
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    raw_data = input('\nWould you like to review raw data?  Type yes or no \n')
    if raw_data.lower() == 'yes':
        print(filtered_df.head(5))
    
    row = 0
    
    while True:
        raw_data = input('\nWould you like to review 5 more rows?  Type yes or no \n')
        if raw_data.lower() == 'yes':
            print(filtered_df[row+5:row+10])
            row += 5
        
        else:
            break


def main():
    while True:

        get_filters()


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
