# Texas Education and Accountability Rating: a Machine Learning Model

### Team Members: 
- James Draper
- Kelsey Kraft
- Mariah McLelan
- Amarilli Novel
- Hisako Yamanaka

  
### Project Overview:

Question to answer: Can a school's accountability rating be predicted?

This is the third part of our team project focused on [Texas ISDs](https://github.com/mariahmclelan/TexasISDs). We aim to develop a Machine Learning Model to predict a school's accountability rating. The Texas Education Agency (TEA) assesses public schools and districts based on state accountability requirements, accrediting public schools in Texas at the district level for grades K-12. The Texas Administrative Code (TAC) outlines the rules for accrediting school districts, specifying four statuses: **Accredited**, **Accredited-Warned**, **Accredited-Probation**, and **Not Accredited-Revoked**. The TAC rules encompass accreditation standards and sanctions, including definitions, purpose, and oversight appointments[^1].

[^1]: For more info [TEA](https://tea.texas.gov/texas-schools/accountability)

Our team is undertaking a challenging task: investigating the feasibility of predicting a school's accountability rating using a custom MongoDB database and Machine Learning. This complex and intricate endeavor requires our collective expertise and dedication.

### Data Sets and Sources:

[Texas Education Agency](https://tea.texas.gov/)

[Texas Education Agency Statistics ](https://rptsvr1.tea.texas.gov/perfreport/snapshot/download.html)

[How Accountability System Works](https://tea.texas.gov/texas-schools/accountability/academic-accountability/performance-reporting/how-accountability-ratings-work)

[2022 Texas Accountability System](https://tea.texas.gov/texas-schools/accountability/academic-accountability/performance-reporting/2022-accountability-rating-system)

[2023 Texas Accountability System](https://tea.texas.gov/texas-schools/accountability/academic-accountability/performance-reporting/2023-accountability-system)

### Break Down of Task:

    Mariah: Machine Learning Model.
    James: Deployment of the Flask App.
    Kelsey: MongoDB.
    Amarilli: Website, visualization, README. 
    Hisako: Tableau's visualizations.


### The importance of Accountability Rating

Texas public schools, charters, and districts receive academic accountability ratings on an annual basis. The ratings consider student performance on state standardized tests, graduation rates, and readiness for college, careers, and the military. They also evaluate school progress, student achievement, and whether the schools are closing achievement gaps among different student groups.

We aim to construct a precise, user-friendly machine-learning model to forecast accountability ratings. We intend to develop a model that can accurately determine the degree of responsibility in a manner that is easily comprehensible to our target audience. Our focus is on building a model that utilizes the latest advancements in machine learning and adhering to established standards of accuracy and reliability. We are confident that our proposed model will prove to be an important contribution to the field of accountability rating prediction.

To achieve our goal, we chose the most recent dataset available about Texas District and Charter Detail Data on [Texas Education Agency Statistics ](https://rptsvr1.tea.texas.gov/perfreport/snapshot/download.html), based on data from 2021-2022, and decided to use deep learning and neural network machine learning.

### The Model

We built a neural network machine learning model that can predict the accountability rating of every school (district and charter) in Texas. The target for the model was the District Accountability Ratings and the features were: 
- Total Students
- Attendance Rate
- STAAR % ELA/READING at approaches grade level standard or above
- STAAR % ELA/READING at meets grade level standard or above
- STAAR % ELA/READING at masters grade level standard or above
- STAAR % Mathematics at approaches grade level standard or above
- STAAR % Mathematics at meets grade level standard or above
- STAAR % Mathematics at masters grade level standard or above
- College Admissions % Tested
- College Admissions % at/above criterion
- Graduation Rate

The model summary :
![image](https://github.com/Amarilli/project-4/assets/148505481/b0573026-3605-494a-aecd-9244fa797684)


The evaluations of the model and the classification report tell us that the model was 79% accurate in predicting the accountability ratings of schools.

![image](https://github.com/Amarilli/project-4/assets/148505481/621687e0-774f-425e-9733-effa9450a94f)



### The predictor

![predictor](https://github.com/Amarilli/project-4/blob/main/Images/predictor.png)

We built a predictor using `pymongo` and `Flask`.

Upon selecting the relevant categories for our Machine Learning Model, the insertion of thsoe same features enables the predictor to forecast the accountability rating with an accuracy of 79% just like the model.

Example of prediction A:

![pred a](https://github.com/Amarilli/project-4/blob/main/Images/rating_a.png)

Example of prediction B:
![pred B](https://github.com/Amarilli/project-4/blob/main/Images/rating_b.png)

The predictor runs locally using `gunicorn` and its complete set up is visible here: [tar-predictor](https://github.com/Amarilli/tar-predictor)


### A Visual Analysis of the Weight of Accountability Rating

Several visualizations were created using Seaborn and Matplotlib to demonstrate the correlation between the Accountability Rating and various factors.

In 2021-2022, most of the schools in Texas are rated A, followed by B, and lastly, C.

Where:

- A – Exemplary performance
- B – Recognized performance
- C – Acceptable performance
- D – In need of improvement
- F – Unacceptable performance

This simple bar char displays the frequency of A(0), B(1), C(2)

![accountability](https://github.com/Amarilli/project-4/blob/main/Images/accountability_freq.png)

The following Violin Plot demonstrates how Accountability Rating and Attendance Rate are connected:

![attendance](https://github.com/Amarilli/project-4/blob/main/Images/acc_attendance.png)

The boxplot showcases the correlation between test scores (STAAR) and accountability rating:

![boxplot](https://github.com/Amarilli/project-4/blob/main/Images/boxplot.png)

The following heatmap uses the data frame we created for our model and demonstrates the correlation between Accountability Rating and all the categories used for our machine model comparing data from two different school years
: 2020-2021 and 2021-2022.

![heatmap](https://github.com/Amarilli/project-4/blob/main/website/static/images/heatmap_labeled.png)

Lastly, we created a scatter plot with a linear regression fit line to quickly evaluate how two variables (attendance and graduation rates) correlate and whether the trend is consistent across different accountability ratings.

![correlation](https://github.com/Amarilli/project-4/blob/main/Images/correlation.png)

## Tableau Visualizations

We also created a dashboard on Tableau.

The following maps show that the student-per-teacher ratio is evenly distributed, and there is a correlation between the number of Non-White Students and Non-White Teachers. However, this doesn’t mean that school 
districts offer educational diversity for students. Teachers specializing in bilingual & ESL education are not distributed according to the number of bilingual & ESL students. For example, 32.5% of Austin ISD’s students are bilingual & ESL, and 24.4% of its teachers offer bilingual & ESL education. On the contrary, 50.7% of Irving ISD’s students are bilingual & ESL, but only 11.90% of its teachers offer bilingual & ESL education. Speaking two or more languages has great benefits, especially in Texas. The ACS shows that of the 27.3 million people aged five or older living in Texas, 17.7 million speak English at home, 64.9% of all Texans. About 28.5% speak Spanish at home — almost 7.8 million people — and about 6.6% speak another language at home[^2]. 

[^2]: For more info [Kxan](https://www.kxan.com/news/texas/census-bureau-estimates-1-in-3-texans-speak-a-language-other-than-english-at-home/#:~:text=The%20new%20five%2Dyear%20ACS,speak%20another%20language%20at%20home)

We tried to identify whether the quality of teachers affects student’s performance. When we look at the chart that visualizes average teachers' salary vs. average SAT scores when teachers’ salaries were 40K - 80K, SAT scores are always between 500 - 1500. When a teacher's salary goes above 100K, some school districts like Highland Park ISD (teachers' average salary is 113.5K and average SAT score is 2,338) seem to offer better education, however school 
district like Valley View ISD pays teachers 112.7K annually on average and average SAT score is 1,041, which is almost the same as Austin ISD’s average SAT score (Average teacher’s salary: 56.4K, Average SAT score 1,048). From this comparison, I can conclude that a teacher's salary could affect students' performance however there’s no strong correlation.

![tableau](https://github.com/Amarilli/project-4/blob/main/Images/Tableau.png)


