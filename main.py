import os
from analysis import load_data, filter_by_country, filter_by_date_range, compute_totals, calculate_death_rate, calculate_vaccination_rate, plot_death_rate, plot_vaccination_rate, plot_daily_new_cases

def main():
    df = load_data()
    country = 'United States'
    start_date = '2020-01-01'
    end_date = '2023-10-01'
    filtered_df = filter_by_country(df, country)
    date_filtered_df = filter_by_date_range(filtered_df, start_date, end_date)
    totals = compute_totals(date_filtered_df)
    print(totals)
    death_rate_df = calculate_death_rate(date_filtered_df)
    plot_death_rate(death_rate_df)
    vaccination_rate_df = calculate_vaccination_rate(date_filtered_df)
    plot_vaccination_rate(vaccination_rate_df)
    plot_daily_new_cases(date_filtered_df)

if __name__ == '__main__':
    main()
