	
import streamlit as st 
import pandas as pd
import webbrowser
st.set_page_config(page_title='NAWE DUBAI INTELLIGENCE PLATFORM',initial_sidebar_state='collapsed',layout='wide')
from streamlit_extras.switch_page_button import switch_page
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


df=pd.read_csv('new.csv')
df['budget']=df['col1']
budget=df.loc[0,'budget']

st.subheader('Additional Requirements ')
extra_prompt1=st.selectbox("Do you want PM report to be in Swedish?",options=[' ','No','Yes'] )
extra_prompt2=st.selectbox("Do you want external meetings?",options=[' ','No','Yes'] )


TOTAL=[budget]
if extra_prompt1=='Yes':
	#st.write(df['col2'])
	budget1=df.loc[0,'col2']
	print(budget1)
	TOTAL.append(budget1)
else:
	budget1=0
if extra_prompt2=='Yes':
	hours=st.slider('How many?',1,20,1)
	budget2=df.loc[0,'col3']*int(hours)
	TOTAL.append(budget2)
else:
	budget2=0
#st.write(budget,budget1)

print(TOTAL)

#placeholder.empty()

	
df=pd.read_csv('new.csv')

df1=pd.read_csv('final_tab.csv')
tab1, tab2, tab3, tab4,tab5 = st.tabs(['Main task','Data Requirement','Duration', 'Deliverables', 'Project Area Information'])
with tab1:
   st.subheader(':blue[Main Task]')
   st.write(df.loc[0,'Main tasks'])

with tab2:
	st.subheader(':blue[Data Requirement]')
	st.write('*:red[Client is required to provide all the necessary data beforehand in order to iniate project activities]*')
	st.write(df.loc[0,'Data requirement'])

with tab3:
	st.subheader(':blue[Duration]')
	st.write(df.loc[0,'duration'])

with tab4:
	st.subheader(':blue[Deliverables]')
	st.write(df.loc[0,'Deliverable'])

with tab5:
	st.subheader(':blue[Project Area Information]')
	

	st.table(df1.set_index(df1.columns[0]))

st.divider()

if len(TOTAL)>1:
	
	st.write('*:red[Final estimated budget', f'SEK {round(budget+budget1+budget2)} ]*')
else:
	st.write('*:red[Preliminary estimated budget ', f'SEK {round(budget)} ]*')
st.divider()

if st.button('Home:house: '):
	switch_page('main')
url = 'https://www.nawebangladesh.com/about-us/'

if st.button('NAWE Home'):
    webbrowser.open_new_tab(url)