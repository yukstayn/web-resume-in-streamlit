import streamlit as st
from PIL import Image


st.header('My Resume')

cont_0 = st.container()
cont = st.container()
cont2 = st.container()
cont2_1 = st.container()
cont3 = st.container()
cont4 = st.container()
cont5 = st.container()

with cont_0:
	cont_1, cont_1_1 = st.columns([2,3])
	with cont_1:
		image = Image.open('Images/mypic.jpg')
		st.image(image, width = 250)
	
	with cont_1_1:
		
		
		st.write(':bust_in_silhouette: `Name` : Karl Jan O. Valenzuela')
		st.write(':iphone: `Phone No.:` +639972369226')
		st.write(':envelope: `Email:` mmxv2k18@gmail.com')
		st.write('🌐 `Facebook`: http://surl.li/braso')
		st.write('🌐 `LinkedIn:` http://surl.li/braqq')
		st.write(':cat: `GitHub:` http://surl.li/bratg')




with cont:
	
	st.subheader('About Me', anchor=True)
	st.write('My name is Karl Jan O. Valenzuela, 27 years old. I love exploring things that are beyond of my expertise. I also love learning anything about computers such as programming, Machine Learning(ML), Artificial Intelligence(AI), Data Science, Cybersecurity and many others.')
	st.write('My goal in education sector is not only to teach students with my best but also to automate most of the tasks done by teachers in the classroom or in administrative tasks.')
	
	
with cont2:
	st.subheader('Education')
	a, b = st.columns(2)
	with a:
		with st.expander('Bachelors Degree'):
			st.image('Images/seal-02.png', width = 100)
			st.write('`MSU-Iligan Institute of Technology`\n```2014-2018```:mortar_board:')
	with b:
		with st.expander('Masters Degree'):
			st.image('Images/seal-02.png', width = 100)
			st.write('`MSU-Iligan Institute of Technology`  \n    ```2019-present```:mortar_board:')

with cont2_1:
	with st.expander('Transcipt of Records'):
		st.image('Certificates/TOR 1-1.png')
		st.image('Certificates/TOR 2-1.png')
		st.image('Certificates/TOR 3-1.png')

with cont3:
	st.subheader('Certificates')
	col1, col2, col3 = st.columns(3)
	with col1:	
		with st.expander('Basic Statistic with Python'):	
			st.image('Certificates/BasicStat_Python.PNG')
		
		with st.expander('Programming for Everybody'):	
			st.image('Certificates/Python4EveryBody-1.png')
		with st.expander('Python Data Structures'):	
			st.image('Certificates/PythonDataStructures-1.png')
		with st.expander('Introduction to Data Analytics'):	
			st.image('Certificates/IntrotoDataAnalytics-1.png')

	
	with col2:	
		with st.expander('Analyze Data with Python'):	
			st.image('Certificates/AnalyzeData_Python.PNG')

		with st.expander('Introduction to IoT'):	
			st.image('Certificates/IntrotoIot-1.png')
		with st.expander('Understanding Research'):	
			st.image('Certificates/UnderstandingResearch-1.png')
		with st.expander('Model-Eliciting Activities'):	
			st.image('Certificates/Valenzuela-1.png')	

	with col3:	
		with st.expander('Visualize Data with Python'):	
			st.image('Certificates/VisualizeData_Python.PNG')

		with st.expander('Design Thinking'):	
			st.image('Certificates/Valenzuela Certificate of Completion-1.png')
		with st.expander('Hybrid Education'):	
			st.image('Certificates/Vibal-1.png')	



with cont4:
	st.subheader('Work Experience')
	with st.expander('Iligan Medical Center College'):
		st.write(':school:  I worked in IMCC-BED for 1 academic year starting 2019 to 2020.')



with cont5:
	
	st.subheader('Skills')
	cont5_1, cont5_2 = st.columns(2)

	with cont5_1:
		with st.expander('Basic'):
			st.write(':white_check_mark: Python')
			st.write(':white_check_mark: Linux')
			st.write(':white_check_mark: Data Analysis')
			st.write(':white_check_mark: Data Visualization')
			st.write(':white_check_mark: Programming')
			st.write(':white_check_mark: Video Editing')
			st.write(':white_check_mark: Photo Editing')

	with cont5_2:
		with st.expander('Intermediate'):
			st.write(':white_check_mark: Canva')
			st.write(':white_check_mark: Microsoft Office')
			st.write(':white_check_mark: Search Engine')
			st.write(':white_check_mark: Mathematics Teaching')