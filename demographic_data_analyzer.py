import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    n = len(df)
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    white_race = (df['race']=='White')
    black_race = (df['race']=='Black')
    
    race_count = (sum(white_race), sum(black_race))

    # What is the average age of men?
    male_sex = (df.groupby('sex', as_index='Male').age.mean())
    average_age_men = male_sex['Male']

    # What is the percentage of people who have a Bachelor's degree?
    people_with_bachelors = sum(df['education']=='Bachelors')
    percentage_bachelors = (people_with_bachelors/n) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = (higher_education[higher_education['salary'] == '>50K']['salary'].count() / higher_education.shape[0])*100
    lower_education_rich = (lower_education[lower_education['salary'] == '>50K']['salary'].count() / lower_education.shape[0])*100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == 1]['hours-per-week'].count().max()

    rich_percentage = (df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].shape[0] / num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?
    country = df[df['salary'] == '>50K'][['native-country', 'salary']]
    top = country.describe()
    highest_earning_country = top.loc['top', 'native-country']
    
    USA = country.count().max()
    highest_earning_country_percentage = (USA/n)*100

    # Identify the most popular occupation for those who earn >50K in India.
    popular = df[df['salary'] == '>50K'][['occupation', 'salary']]
    top = popular.describe()
    top_IN_occupation = top.loc['top', 'occupation']


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
