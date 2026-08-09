from analysis import load_data, calculate_death_rate, plot_death_rate

df = load_data()
df = calculate_death_rate(df)
plot_death_rate(df)