from preswald import connect, get_df, slider, text, plotly, table
import plotly.express as px

# Connect & load
connect()
df = get_df("netflix_titles")
df = df.dropna(subset=["release_year", "listed_in", "title", "type"])

# Slider for release year
year = slider("Select a year", min_val=2000, max_val=2021, default=2020)

# Filter data
filtered = df[df["release_year"] == year]

# Header & description
text(f"# Netflix Wrapped!: {year}")
text("Slide the bar to see what was everyone's top picks of the year. Dive into genres, titles, and trends.")

# Genre chart
genre_counts = (
    filtered["listed_in"].str.split(", ").explode().value_counts().reset_index()
)
genre_counts.columns = ["Genre", "Count"]
fig = px.bar(genre_counts, x="Genre", y="Count", title="Top Genres That Year")

# Display
plotly(fig)
table(filtered[["title", "type", "listed_in"]].head(10), title="📺 Top Titles During this Time")
