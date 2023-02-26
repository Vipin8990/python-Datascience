import pandas as pd 
import streamlit as st
import plotly.express as px

# page config
st.set_page_config(
    page_title='Pokemon App', 
    page_icon='🃏',
    layout='wide'
)

st.sidebar.title('🐼 Pokeman App🐼')
st.image('papp/pokemon.jpg', use_column_width=True)

# load data 
@st.cache_data
def load_pokemon():
    data = pd.read_csv('papp/pokemon.csv', index_col=0)
    return data 

with st.spinner('Loading Pokemon Data ...'):
    pokemon = load_pokemon()
    st.sidebar.success('Loaded Pokemon Data')

# sidebar

show_data = st.sidebar.checkbox('show the dataset')
if show_data:
    st.subheader('Pokemon Data')
    st.dataframe(pokemon, use_container_width=True)

type1 = st.sidebar.selectbox('Select Pokemon Type', pokemon['Type 1'].unique())

subset = pokemon[pokemon['Type 1'] == type1] #filter

tabs = st.tabs(['Data', 'Univarate Analysis', 'Bivariate Analysis', 'Trivariate Analysis '])

#Data Tab

tabs[0].subheader(f'{type1} pokemons')
tabs[0].dataframe(subset,use_container_width=True)

# univarate Analysis tab
#Attack
ss = subset.sort_values(by='Attack')
fig1 = px.histogram(ss, x = "Attack", nbins = 20 )
fig2 = px.bar(subset, x = "Name", y="Attack")
tabs[1].subheader(f'{type1} stats')
tabs[1].subheader('Attack')
tabs[1].plotly_chart(fig1, use_container_width=True)
tabs[1].plotly_chart(fig2, use_container_width=True)

#Defence 

ss = subset.sort_values(by='Defense')
fig1 = px.histogram(ss, x = "Defense", nbins = 20 )
fig2 = px.bar(subset, x = "Name", y="Defense")
tabs[1].subheader(f'{type1} stats')
tabs[1].subheader('Defense')
tabs[1].plotly_chart(fig1, use_container_width=True)
tabs[1].plotly_chart(fig2, use_container_width=True)

#Hp attack
ss = subset.sort_values(by='HP')
fig1 = px.histogram(ss, x = "HP", nbins = 20 )
fig2 = px.area(subset, x = "Name", y="HP")
tabs[1].subheader(f'{type1} stats')
tabs[1].subheader('HP')
tabs[1].plotly_chart(fig1, use_container_width=True)
tabs[1].plotly_chart(fig2, use_container_width=True)

#Sp.Atk
ss = subset.sort_values(by='Sp. Atk')
fig1 = px.histogram(ss, x = "Sp. Atk", nbins = 20 )
fig2 = px.box(subset, x = "Name", y="Sp. Atk")
tabs[1].subheader(f'{type1} stats')
tabs[1].subheader('Sp. Atk')
tabs[1].plotly_chart(fig1, use_container_width=True)
tabs[1].plotly_chart(fig2, use_container_width=True)

#Bivarate Analysis tab
x = tabs[2].selectbox('Select X', pokemon.select_dtypes('number').columns)
y = tabs[2].selectbox('Select Y', pokemon.select_dtypes('number').columns)
c = tabs[2].selectbox('Select color',pokemon.select_dtypes(exclude='number').columns)
fig = px.scatter(subset, x=x, y=y, color=c, hover_data=['Name'] , size=x, size_max=60)
tabs[2].subheader(f'{type1}: {x} vs {y} by {c}')
tabs[2].plotly_chart(fig, use_container_width=True)

# trivarite Analysis 

x = tabs[3].selectbox('Select X data', pokemon.select_dtypes('number').columns)
y = tabs[3].selectbox('Select Y data ', pokemon.select_dtypes('number').columns)
z = tabs[3].selectbox('Select Z data', pokemon.select_dtypes('number').columns)
c = tabs[3].selectbox('Select color type',pokemon.select_dtypes(exclude='number').columns)
fig = px.scatter_3d(subset, x=x, y=y, z=z , color=c, hover_data=['Name'] , size=x, size_max=60)
tabs[3].subheader(f'{type1}: {x} vs {y} vs {z} by {c}')
tabs[3].plotly_chart(fig, use_container_width=True)