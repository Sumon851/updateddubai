import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='NAWE DUBAI INTELLIGENCE PLATFORM',initial_sidebar_state='collapsed')
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
st.header('NAWE DUBAI INTELLIGENCE PLATFORM')
st.markdown("---")
#st.subheader('please select following criteria to estimate budget
def main_col(a):
	df=pd.read_excel('duration.xlsx',sheet_name=a)
	
	df=df.fillna('')
	
	
	prj_area=st.selectbox('How large is your project area?',options=df.area.unique())
	df1=df.loc[df['area']==prj_area]
	df1.reset_index(drop=True)
	df1.to_csv('new.csv',index=False)
main_service=st.selectbox('Please select your main service?', options=['', 'Stormwater','Water','Sewer'])

if main_service=='Stormwater':
	service=st.selectbox('Please select the sub-service', options=['','Stormwater Investigation for detailed plan area','Stormwater Investigation for building permit (bygglov) and and flooding investigation in SCALGO','Stormwater Investigation for existing properties and flooding investigation in SCALGO','Flood Investigation in Mike+ (1D stormwater pipe modelling)',
	'Flood Investigation in Mike+(1D-2D overland runoff  and pipe modelling)', 'Rain bed design with calculations ','Stormwater pipe network design in 2D','Technically feasible strormwater pipe network design in 3D','In detail stormwater pipe network design in 3D'] )
	
	if service=='Stormwater Investigation for detailed plan area' or service=='Stormwater Investigation for building permit (bygglov) and and flooding investigation in SCALGO'or service=='Stormwater Investigation for existing properties and flooding investigation in SCALGO' or service == 'Rain bed design with calculations ' or service== 'Stormwater pipe network design in 2D'  or service == 'Technically feasible strormwater pipe network design in 3D' or service == 'In detail stormwater pipe network design in 3D':
		main_col('duration-1')
		
		if st.button('next :arrow_forward:'):
			switch_page('web_app')
	elif service=='Flood Investigation in Mike+ (1D stormwater pipe modelling)':
		main_col('duration-2')
		if st.button('next :arrow_forward:'):
			switch_page('web_app-st6')
		
	elif service=='Flood Investigation in Mike+(1D-2D overland runoff  and pipe modelling)':
		main_col('duration-3')

		if st.button('next :arrow_forward:'):
			switch_page('web_app-st8')

if main_service=='Water':
	service=st.selectbox('Please select the sub-service', options=['','Water distribution network modelling in Mike+','Water hammer analysis in Mike+(DHI)',
	'Existing water distribution network investigation','Water pipe network design in 2D','Technically feasible water pipe network design in 3D','In detail water pipe network design in 3D' , 'Design review'] )
	if service=='Water hammer analysis in Mike+(DHI)' or service=='Existing water distribution network investigation' or service=='Water pipe network design in 2D' or service=='Technically feasible water pipe network design in 3D' or service=='In detail water pipe network design in 3D' or service=='Design review' :
		main_col('duration-1')
		
		if st.button('next :arrow_forward:'):
			switch_page('web_app')
	elif service=='Water distribution network modelling in Mike+':
		main_col('duration-2')
		if st.button('next :arrow_forward:'):
			switch_page('web_app-st6')

if main_service=='Sewer':
	service=st.selectbox('Please select the sub-service', options=['','Sewer collection network investigation(Gravity)','Sewer collection network investigation(Pressure)',
	'Sewer collection network investigation(Combined)','Sewer collection network modelling in Mike+','Sewer distribution network investigation','Inleak analysis according to flow measurement and rainfall data','Sewer pump analysis and calculation ','Sewer pipe network design in 2D','Technically feasible sewer pipe network design in 3D','In detail sewer pipe network design in 3D','Design review'] )


	if service=='Sewer collection network investigation(Gravity)' or service=='Sewer collection network investigation(Pressure)' or service=='Sewer collection network investigation(Combined)' or service=='Sewer distribution network investigation' or service=='Inleak analysis according to flow measurement and rainfall data' or service== 'Sewer pump analysis and calculation ' or service=='Sewer pipe network design in 2D' or service=='Technically feasible sewer pipe network design in 3D' or service == 'In detail sewer pipe network design in 3D' or service == 'Design review':
		main_col('duration-1')
		
		if st.button('next :arrow_forward:'):
			switch_page('web_app')
	elif service=='Sewer collection network modelling in Mike+':
		main_col('duration-2')
		if st.button('next :arrow_forward:'):
			switch_page('web_app-st6')

		
	
