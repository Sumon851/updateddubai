import streamlit as st
import pandas as pd

st.write('**Please provide following landuse information**')
def landuse():
	landuse_button=['','agriculture','office','industry','school', 'residential', 'commercial','block']
	option_landuse=[' ','0-10','11-30','31-50','51-100','101-200','201-350','351-500','501-700','701-1000','>1000']
	option_block=[' ','0-2','3-5','6-10','11-20','21-35','36-50','51-65','66-80','81-100','>100']
	
	factor_landuse=['0','0.2','0.5','1','1.5','2.1','2.8','3.6','4.5','6','10']
	
	
		
	landuse_button=st.selectbox('What is the landuse in the area? Please choose from the follwing options. If landuse is mixed, select- *:blue[block]* ', options=landuse_button)
	if not landuse_button=='':
		if landuse_button=='block':
			block=st.selectbox('Number of block/ property', options=option_block)
			index=option_block.index(block)
			f=float(factor_landuse[index])
			
		else:
			use=st.selectbox(f'Area of {landuse_button} (st)', options=option_landuse)
			index=option_landuse.index(use)
			f=float(factor_landuse[index])
		return f
