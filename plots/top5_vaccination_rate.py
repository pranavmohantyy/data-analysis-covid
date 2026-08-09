from analysis import load_data, calculate_vaccination_rate, plot_vaccination_rate

df = load_data()
df = calculate_vaccination_rate(df)
plot_vaccination_rate(df)