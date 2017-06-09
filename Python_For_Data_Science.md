• Form Meaning player groups

• Discover other players that are similar to your favorite athlete

• Form string teams by using analytics


### Asking the Right Question
     • Define the problem
     • Assess the Situation
        • Risks
        • Benefits
        • Contigencies
        • Regulations
        • Resources
        • Requirements
    • Define Goals
        • Objective
        • Criteria

### Order is:
    Define the problem    =
    Assess the Situation  =     Formulate the Question
    Define Goals          =

As yourself:
"What insights do I expect to get!"

## INSIGHTS
	• Better undersanding and insights on
	  • player strengths
	  • enhancing performance
	  • critical attributes for a player's performance

## ACTIONS
	• Coach can design programs that improve these areas in teams

There are five key steps in the overall process of data science, namely, data acquisition, data preparation, data analysis, presentation and reporting of insights and turning these insights into data-driven actions.

## ACQUIRE
	• Import raw dataset into your analytics platform
	• Identify data sets
	• Retrieve data
	• Query data

Where's data come?'
Traditional databases - SQL and query browsers
Remote data - Web Services
Text files - Scripting languages
NoSQL storage = Web Services & Programming Interfaces

## PREPARE
	• Explore & Visualize
		1º Step:
		    • Explore data
		      • Premiliminary analysis
		      • Understand nature of data
      		First step in data preparation involves literally looking at the data to understand its nature, what it means, it's quality, and format.

			First thing to do is find correlations, general trends, outliers.

			Correlation graphs can be used to explore the dependenciesbetween different variables in the data.
			General trends show you a simple graph of how the data is progressing over time.
			Outliers show you the data points that are distant from other data points.

			Mean and median are measures of the location of specific values.
			Mode is the value that occurs most frequently in your data set.
			And range and standard deviation are measures of spread in your data.

			A heat map, for instance, such as the one shown here, can quickly give you an idea where the hot spots are.
			Many different types of graphs can be used.
			Histograms show the distribution of the data and can show skewness or unusual dispersion.
			Boxplots are another type of plot for showing data distribution.
			Line graphs are useful for seeing how values in your data change over time.
			Spikes in the data are also easy to spot.
			Scatter plots can show correlation between two variables.
			Overall, there are many types of graphs
			that visualize data.

			Data Exploration -> Data Understanding -> Informed Analysis.

	• Perform Data Cleaning
		2º Step:
		    • Pre-process Data
		      • Clean
		      • Integrate
		      • Package

		Clean + Transform

		Real-world data is messy!
		    • Inconsistent values
		    • Duplicate records
		    • Missing values
		    • Invalid data
		    • Outliers
		Addressing Data Quality Issue
		    • Remove data with missing values
		    • Merge duplicate records
		    • Generate best estimate for invalid values
		    • Remove outliers

		Data Munging:
		    • Dimensionality Reduction
		    • Data Manipulation
		    • Transformation
		    • Feature Selection
		    • Scaling

## ANALYZE
	• Feature Selection
	• Model Selection
	• Analyze the results
    • Select analytical techniques, Build models.
	
### Build Model:

**Input Data -> Analysis Technique -> Model -> Model Output**

**Classification:** Predict category of the input data e.g.: Weather, Tumor (benign, malignant)

**Regression:** Predict numeric value e.g.: Weekly sales of a new product, predicting the score on a test.

**Clustering:** Organize similar items into groups e.g.: Seniors, Adults, Teenagers.

**Association Analysis:** Find rules to capture associations between items e.g.: diapers and beers, market

**Graph Analytics:** Use graph structure to find connetions between entities e.g.: epidemic by analyzing hospitals and doctors' records.
	
### Evaluate the model:
	Classification and Regression
		• Predict value vs Correct Value - We have the correct output for each sample in our input data. Comparing the correct output and the output predicted by the model provides a way to evaluate the model.

	Clustering
		• Should be examined to see if they make sense for your application. For example, do the customer segments reflect your customer base? Are they helpful for use

	Association Analysis and Graph Analytics
		• Some investigation will be needed to see if the results are correct. For example, network traffic delays need to be investigated to see if what your model predicts is actually happening, and whether the sources of the delays are where they are predicted to be in the real system.


Determine Next Steps
	• Repeat analysis?
		• Should the analysis be performed with more data in order to get better model performance?
	• Take deeper dive?
	• Act on results?

Modeling Starts:
	Select technique -> Build model -> Validate model

	Evaluating the model


## REPORT
	• Present your findings
    	• Communicate results
	
### Reporting Insights
	Communicate Results (Insights)
		• Look at your results and decide what to present
			• Part of that means determining what part of your analysis is mos important to offer the BIGGEST value:
				• What's my punchline? What are the main results?
				• How can the model add to this application? How do the results compare to the success criteria determined at the beginning of the project for that application's specific purpose?
				
## ACT
	• Use them
    	• Apply Results, Results => Purpose
	• Apply Results -> Purpose
	• big data and data science are only useful if the insights can be turned into actions, and action should be carefully defined and evaluated.

Data Cleaning:

	Why do we need to clean data?
		• Missing entries
		• Garbage values
		• NULLs
	How do we clean data?
		• Remove the entries
		• Impute these entries with a counterpart
		  • Ex. Average vales of the column
		  • Ex. Assign 0, -1, etc

# Programming:

Exploring the dataset on Python
df.describe().transpose() - Generate vital statistical summary of your datasets loke mean and standard deviation.

```python
# is any row NULL ?

# 0 = ROW
# 1 = COLUMN

rows = df.shape[0]
df.isnull().any().any(), df.shape

# Fix it

df = df.dropna()
```

library "scikit-learn" is a library for Machine Learning on Python

K-MEANS clustering in python:
```python
from sklearn.cluster import Kmeans

Y = KMeans(c_clusters=3, random_state=random_state).fit_predict(x)
```
Analysis and Modeling:
	• Supervised Learning
		• 
	• Unsupervised Learning
		• 
	• Semi supervised Learning
		• 

Data Analysis Study Case:

What are instrinsic attributes on which 'you' would group players?

You can also build complex features 
f ( shot power, reaction time)

Interpreting Clustering Results
	• How many players per cluster?
	  • Too many in few clusters?
	  • Too few?
	  
## Numpy
	• Support for multi-dimensional arrays.
	• Built-in array operations.
	• Simplified, but powerful array nteractions -> broadcasting.
	• Integration of other languages (Fortran, C, C++).

### Why numpy for data science?
	• Speed.
	• Functionaliy.
	
