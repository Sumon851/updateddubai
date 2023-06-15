import pandas as pd
def final_tab(a,b):

	criteria=a
	answer=b
	df_final_tab=pd.DataFrame(data={'criteria':a,'Project Area Infromation':b})
	df_final_tab.to_csv('final_tab.csv',index=False)