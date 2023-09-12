# covid-analyzer-py
<h2>Personal project to analyze disaggregated data on covid statistics</h2>
<p>The data analyzed in this project was collected from the website of https://globalhealth5050.org/</p>
<p>Python version used in this project 3.10.7</p>
<br/>
<br/>

<h3>NOTES</h3>
<ul>
  <li><p>Not all the countries names in the deaths excel file are listed in the vaccinations excel file</p></li>
  <li><p>I would like to recommend the jupyter notebook file ca2.ipynb as an alternative to the ca.py python file</p></li>
</ul>
<br/>
<br/>
<h3>Usage</h3>

<h5>1</h5>
<br/>
Is recommended to create a python virtual environment, for that run the following command in the terminal:

python -m venv canalyzer

<img width="416" alt="pic1" src="https://github.com/StanlyRod/covid-analyzer-py/assets/76764572/98e4edea-dea8-473a-83f9-4b90cb04b0f2">
<br/>
<br/>
<br/>

<h5>2</h5>
<br/>
Navigate through the virtual environment folder and open the Scripts directory and run the following command to activate the virtual environment:

Activate

<img width="442" alt="pic2" src="https://github.com/StanlyRod/covid-analyzer-py/assets/76764572/ccda9702-4f51-4485-a55b-d1976d499134">
<br/>
<br/>
<br/>

<h5>3</h5>
<br/>
<p>Create a new directory in the virtual environment folder and move all the files to the new directory and make sure that the excel files are in the same directory as the ca.py file</p>

<img width="404" alt="pic3" src="https://github.com/StanlyRod/covid-analyzer-py/assets/76764572/4e4527a6-855a-4bbd-a01e-a7b07011044f">
<br/>
<img width="258" alt="pic4" src="https://github.com/StanlyRod/covid-analyzer-py/assets/76764572/d98d95d4-159e-4c88-ab3a-e056310375f7">
<br/>
<br/>
<br/>

<h5>4</h5>
<br/>
<p>
  Inside the new directory with all necessary files in this case the src directory,
  run the following command to install all the dependencies that the project needs:
</p>

pip install -r requirements.txt

<img width="572" alt="pic5" src="https://github.com/StanlyRod/covid-analyzer-py/assets/76764572/8b2bca51-e8ab-40b6-9364-766fe2278131">
<br/>
<br/>
<br/>

<h5>5</h5>
<br/>
<p>
  Run the ca.py file and introduce a command from the command menu.
</p>
<p>The ld command will visualize the deaths data by country and gender.</p>
<br/>
<img width="451" alt="pic6" src="https://github.com/StanlyRod/covid-analyzer-py/assets/76764572/7e733ca5-abf1-46c9-9b74-165f080d73b6">
<img width="454" alt="pic7" src="https://github.com/StanlyRod/covid-analyzer-py/assets/76764572/d5c383a9-89d4-4f97-90c9-8665f85fedca">
<br/>
<br/>

<p>The fv command will visualize the vaccinations data by country and gender.</p>
<br/>
<img width="462" alt="pic8" src="https://github.com/StanlyRod/covid-analyzer-py/assets/76764572/bf6dfd92-2ea7-4ebe-b399-ea4b60cdf849">
<img width="473" alt="pic9" src="https://github.com/StanlyRod/covid-analyzer-py/assets/76764572/7b17110e-a90e-40d8-b60b-d98bec79c99c">




