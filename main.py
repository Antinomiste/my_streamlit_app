import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Many Cars')

countries = [" All",
             " Europe",
             " US",
             " Japan",
            ]

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link, dtype={"mpg":float,
                                   "cylinders":int,
                                   "cubicinches":int,
                                   "weightlbs":int,
                                   "time-to-60":int,
                                   "year":str,
                                   "continent":str,
                                  })
df_cars["continent"] = df_cars["continent"].apply(lambda x: x[:-1])
#st.write(df_cars)

country = st.sidebar.radio(
    "Specify a country",
    (item for item in countries))

df_selected = df_cars.copy()
if country != " All":
    df_selected = df_cars[df_cars["continent"] == country].reset_index()

#st.write(country)
#st.write(df_selected)

#st.line_chart(df_cars['MAX_TEMPERATURE_C'])
viz_correlation, ax = plt.subplots()
ax = sns.heatmap(df_selected.corr(),
				 center=0,
				 cmap = sns.color_palette("vlag", as_cmap=True),
                 annot=True,
				 )

st.pyplot(viz_correlation.figure)

viz_distribution, axs = plt.subplots(2,2, figsize=(10,10))

sns.violinplot(df_selected["mpg"],ax=axs[0,0])
axs[0,0].set_title("miles per galon")

sns.violinplot(df_selected["weightlbs"],ax=axs[0,1])
axs[0,1].set_title("weight in lbs")

sns.violinplot(df_selected["time-to-60"],ax=axs[1,0])
axs[1,0].set_title("seconds to 60 miles per hour")

sns.violinplot(df_selected["cylinders"],ax=axs[1,1])
axs[1,1].set_title("cylinders")

st.pyplot(viz_distribution.figure)
