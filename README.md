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
    James: .
    Kelsey: MongoDB.
    Amarilli: Website, visualization, README. 
    Hisako: Tableau's visualizations.


### The importance of Accountability Rating

Texas public schools, charters, and districts receive academic accountability ratings on an annual basis. The ratings consider student performance on state standardized tests, graduation rates, and readiness for college, careers, and the military. They also evaluate school progress, student achievement, and whether the schools are closing achievement gaps among different student groups.

We aim to construct a precise, user-friendly machine-learning model to forecast accountability ratings. We intend to develop a model that can accurately determine the degree of responsibility in a manner that is easily comprehensible to our target audience. Our focus is on building a model that utilizes the latest advancements in machine learning and adhering to established standards of accuracy and reliability. We are confident that our proposed model will prove to be an important contribution to the field of accountability rating prediction.

To achieve our goal, we chose the most recent dataset available about Texas District and Charter Detail Data on [Texas Education Agency Statistics ](https://rptsvr1.tea.texas.gov/perfreport/snapshot/download.html), based on data from 2021-2022, and decided to use deep learning and neural network machine learning.

### The Model

Our model


### A Visual Analysis of the Weight of Accountability Rating

Several visualizations were created using Seaborn and Matplotlib to demonstrate the correlation between the Accountability Rating and various factors.

In 2021-2022 the majority of the schools in Texas are rated A, followed by B, and lastly C

where:

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

The following heatmap uses the data frame we created for our model and demonstrates the correlation between Accountability Rating and

![heatmap](https://github.com/Amarilli/project-4/blob/main/website/static/images/heatmap_labeled.png)

Lastly, we created a scatter plot with a linear regression fit line to quickly evaluate how two variables (attendance rate and graduation rate) correlate and whether the trend is consistent across different accountability ratings.

![correlation](https://github.com/Amarilli/project-4/blob/main/Images/correlation.png)


