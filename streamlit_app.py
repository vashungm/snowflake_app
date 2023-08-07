import streamlit
import pandas

streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Display the table on the page


# Let's put a pick list here so they can pick the fruit they want to include 
selected_fruits = streamlit.multiselect("Pick some fruits:", options=list(my_fruit_list.Fruit), default = ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[selected_fruits]

streamlit.dataframe(fruits_to_show)
