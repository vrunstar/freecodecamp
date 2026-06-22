import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset?
    race_count = df["race"].value_counts()

    # Average age of men
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(), 1
    )

    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # Advanced education: Bachelors, Masters, Doctorate
    higher_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    # Percentage with salary >50K among advanced education
    higher_education_rich = round(
        (df[higher_education]["salary"] == ">50K").mean() * 100,
        1
    )

    # Percentage with salary >50K without advanced education
    lower_education_rich = round(
        (df[~higher_education]["salary"] == ">50K").mean() * 100,
        1
    )

    # Minimum work hours per week
    min_work_hours = df["hours-per-week"].min()

    # Percentage of rich among those who work fewest hours
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    rich_percentage = round(
        (num_min_workers["salary"] == ">50K").mean() * 100,
        1
    )

    # Country with highest percentage of >50K earners
    country_percentages = (
        df.groupby("native-country")["salary"]
        .apply(lambda x: (x == ">50K").mean() * 100)
    )

    highest_earning_country = country_percentages.idxmax()
    highest_earning_country_percentage = round(
        country_percentages.max(), 1
    )

    # Most popular occupation for those earning >50K in India
    top_IN_occupation = (
        df[
            (df["native-country"] == "India")
            & (df["salary"] == ">50K")
        ]["occupation"]
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print(
            "Percentage with higher education that earn >50K:",
            higher_education_rich
        )
        print(
            "Percentage without higher education that earn >50K:",
            lower_education_rich
        )
        print("Min work time:", min_work_hours)
        print(
            "Percentage of rich among those who work fewest hours:",
            rich_percentage
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )
        print(
            "Highest percentage of rich people in country:",
            highest_earning_country_percentage
        )
        print(
            "Top occupations in India:",
            top_IN_occupation
        )

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
