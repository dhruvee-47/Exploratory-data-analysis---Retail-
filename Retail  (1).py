#!/usr/bin/env python
# coding: utf-8

# #                     EXPLORATORY DATA ANALYSIS - RETAIL 

# Project by 
#        ~Dhruvee Vadhvana 

# In[2]:


#Loading all the necessary libraries 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#Importing warnings 
import warnings
warnings.filterwarnings('ignore')


# In[53]:


#Read dataset 
data=pd.read_csv("C:/Users/Dhruvee Vadhvana/Documents/Internship/SampleSuperstore.csv")
data


# In[35]:


data.head()


# In[36]:


data.tail()


# In[37]:


data.shape


# In the given data set there is 9994 Rows & 13 Columns.  

# In[38]:


data.describe()


# In[39]:


# Checking the dupilication in data
data.duplicated().sum()


# In[40]:


#Checking number of null values in the dataset 
data.isnull().sum()


# In[41]:


#Checking the number of null values in the dataset 
data.isnull().sum()


# There is no null value in the given dataset. 

# In[42]:


#Listing down all the 13 Columns of dataset 
data.columns


# In[43]:


data.nunique()


# In this section, we're figuring out the various distinct values for target columns and rows. As a sample, the ShipMode component has been found to have 4 different values, namely First Class, Same Day, Second Class, and Standard class, respectively and so on for other columns as well. 

# # Exploratory Data Analysis : 

# In[44]:


plt.figure(figsize=(14,7))
plt.bar('Sub-Category','Category', data=data, color='black')
plt.title('Category vs Sub Category')
plt.xlabel('Sub-Catgory')
plt.ylabel('Category')
plt.xticks(rotation=45)
plt.show()


# The number of subcategories that come under Category can be seen in this graph. Phones, Accessories, Machines, and Copies therefore take up the most area in the graph.

# In[45]:


plt.figure(figsize=(8,5))
sns.kdeplot(data['Sales'],color='red',label='Sales',shade=True,bw=25)
sns.kdeplot(data['Profit'],color='Blue',label='Profit',shade=True,bw=25)
plt.legend()


# Even though profit is higher than sales, there are some areas where profit could be raised.

# In[46]:


data.hist(bins=50 ,figsize=(20,15))
plt.show();


# In[47]:


data.corr()


# In[48]:


corr=data.corr()
sns.heatmap(corr,annot=True,cmap='YlGnBu')


# # Analysis from Heatmap
# * Sales and Profit are Moderately Correlated.
# * Discount and Profit are Negatively Correlated.
# * Quantity and Profit are less Moderately Correlated. 

# In[49]:


#Analysis using Pairplot of each column 
sns.pairplot(data)


# In[50]:


#Analysis Based on the Catagory 
sns.pairplot(data,hue='Category')


# In[51]:


#Analysis Based on the Catagory 
sns.pairplot(data,hue='Segment')


# In[52]:


data.value_counts()


# In[53]:


sns.countplot(x=data['Ship Mode'])


# In[54]:


sns.countplot(x=data['Segment'])


# In[55]:


sns.countplot(x=data['Category'])


# In[56]:


sns.countplot(x=data['Sales'])


# In[57]:


sns.countplot(x=data['Quantity'])


# In[58]:


sns.countplot(x=data['Profit'])


# In[59]:


data.value_counts('Sub-Category')


# In[60]:


plt.figure(figsize=(15,15))
sns.countplot(x=data['State'])
plt.xticks(rotation=90)
plt.title("STATE")
plt.show()


# In[61]:


fig, axs = plt.subplots(ncols=2, nrows = 2, figsize = (10,10))
sns.distplot(data['Sales'], color = 'red',  ax = axs[0][0])
sns.distplot(data['Profit'], color = 'orange',  ax = axs[0][1])
sns.distplot(data['Quantity'], color = 'green',  ax = axs[1][0])
sns.distplot(data['Discount'], color = 'blue',  ax = axs[1][1])
axs[0][0].set_title('Sales Distribution', fontsize = 20)
axs[0][1].set_title('Profit Distribution', fontsize = 20)
axs[1][0].set_title('Quantity distribution', fontsize = 20)
axs[1][1].set_title('Discount Distribution', fontsize = 20)
plt.show()


# In[62]:


plt.figure(figsize=(14,11))
data['Sub-Category'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True)
plt.legend()
plt.show()


# In[63]:


from plotnine import *


# In[65]:


Profit_plot = (ggplot(data, aes(x='Sub-Category', y='Profit', fill='Sub-Category')) + geom_col() + coord_flip()
                + scale_fill_brewer(type='div', palette="Spectral") + theme_classic() + ggtitle('Pie Chart'))

display(Profit_plot)


# The pie chart above displays the profit and loss for each subcategory. The "binders" subcategory has experienced the greatest quantity of loss and profit among all other sub-Categories, as shown in the graph. (At this time, we are unable to hypothesize as to the cause, but it could be related to discounts offered on the subcategory of binders).The next subcategory, "Copiers," has the greatest profit with no losses. There are other sub-categories as well, but they have not experienced any losses and have poor profit margins.Suffering from highest loss is machines.

# # Statewise Analysis

# In[66]:


data['Country'].value_counts()


# In[68]:


data1 = data['State'].value_counts()
data1.head(10)


# In[70]:


data1.plot(kind='bar',figsize=(15,5), color='red')
plt.ylabel('Number of deals')
plt.xlabel('States')
plt.title('StateWise Analysis', fontsize = 20)
plt.show()


# * Here as we can see there is top 3 states where frequency of deals are highest : 
# 1. California 
# 2. New York
# 3. Texas 
# 
# * And the state with lowest number of deals is Wyoming. 

# In[71]:


data['State'].value_counts().mean()


# * Approximately 204 deals are averaged out across all states. 

# # City Wise Analysis of dealings : 

# In[84]:


data2 = data['City'].value_counts()
data2=data2.head(15)


# In[85]:


data2.plot(kind='bar',figsize=(15,5), color='red')
plt.ylabel(' Number of deals')
plt.xlabel('City')
plt.title('City Wise Analysis', fontsize = 20)
plt.show()


# *  Here as we can see there is top 3 Cities where frequency of deals are highest : 
# 1. New York
# 2. Los Angeles
# 3. Philadelphia

# In[86]:


data['City'].value_counts().mean()


# * Approximately 19 deals are averaged out across all Cities. 

# #  analysis of Profit, Discount and sell Statewise

# In[87]:


data['State'].value_counts().head(10)


# In[89]:


data_state= data.groupby(['State'])[['Sales', 'Discount', 'Profit']].mean()
data_state.head()


# #### Statewise Profit Analysis : 

# In[91]:


data_state1=data_state.sort_values('Profit')
data_state1[['Profit']].plot(kind = 'bar', figsize = (15,4), color='orange')
plt.title('State wise Profit Analysis', fontsize = 20)
plt.ylabel('Profit per Sate')
plt.xlabel('States')
plt.show()


# __RESULT:- The state with the greatest profit is Vermont, which is shown in the above bar graph, which also shows the state with the lowest profit. Colorado and Ohio are the states with the least profit, respectively.

# #### Statewise Discount Analysis : 

# In[93]:


data_state1['Discount'].plot(kind='bar',figsize=(18,5), color='red')
plt.title('StateWise analysis of Discount', fontsize=20)


# __RESULT:- The graph above demonstrates that Illinois and Texas have the highest discounts. North Dakota, Kansas, Louisiana, Maine, and many other states are among those with the lowest discount rates.

# #### Statewise Sale Analysis

# In[101]:


data_state['Sales'].plot(kind='pie',
                        figsize = (20,20),
                        autopct='%1.1f%%',
                        startangle=90,     # start angle 90° (Africa)
                        shadow=True)
plt.title('State wise analysis of Sale',fontsize=20)


# __RESULT:- Here the state with Highest amount of sales is Wyoming(11.8%) among all and the state with lowest amount of sales is South Dakota(0.8%). 

# # Segment wise analysis of Profit, Discount and sell. 

# In[102]:


data['Segment'].value_counts()


# In[103]:


data_segment= data.groupby(['Segment'])[['Sales', 'Discount', 'Profit']].mean()
data_segment


# In[106]:


#1. sales
#2. Discount
#3. Profit
data_segment.plot.pie(subplots=True, 
                    autopct='%1.1f%%',
                    figsize=(18, 20),
                    startangle=90,     # start angle 90° (Africa)
                    shadow=True,
                    labels = data_segment.index)
plt.title('Segment wise analysis of Sale, Discount, profit')


# __RESULT:- [1]Sales: Consumer:32%, Corporate:33.5% & Home-Office: 34.5%
#            [2]Discount: Consumer:34.1%, Corporate:34.1% & Home-Office:31.7% 
#            [3]Profit: Consumer:28.7%, Corporate:33.8% & Home-Office:37.5% 

# # Citywise Analysis of the Profit : 

# In[5]:


data_city= data.groupby(['City'])[['Sales', 'Discount', 'Profit']].mean()
data_city = data_city.sort_values('Profit')
data_city.head()


# In[6]:


#1.Low Profit
data_city['Profit'].head(30).plot(kind='bar',figsize=(15,5),color = 'Pink')
plt.title('City wise analysis of Sale, Discount, profit')


# __RESULT:- The graph above demonstrates that while a lot of cities have little profit, Bethlehem has the biggest loss.

# In[8]:


#2. High Profit
data_city['Profit'].tail(30).plot(kind='bar',figsize=(15,5),color = 'Pink')
plt.title('City wise analysis of Sale, Discount, profit')


# __RESULT:- The graph above demonstrates that Jamestown has seen the highest quantity of profit out of all the cities.

# # QUANTITY WISE SALES, PROFIT AND DISCOUNT ANALYSIS

# In[9]:


data_quantity = data.groupby(['Quantity'])[['Sales', 'Discount', 'Profit']].mean()
data_quantity.head()


# In[12]:


#1. sales 2. Discount 3. Profit
data_quantity.plot.pie(subplots=True, 
                    autopct='%1.1f%%',
                    figsize=(20, 20),
                     pctdistance=0.69,
                    startangle=90,     # start angle 90° (Africa)
                    shadow=True,
                    labels = data_quantity.index)
plt.title('Quantity wise Sale, profit & Discount analysis')


# The greatest sales and profit are for the quantity with the number 13. The greatest Discount is found in the TENTH Quantity, according to the Discount. 

# # CATAGORY WISE SALES DISCOUNT AND PROFIT

# In[13]:


data_category = data.groupby(['Category'])[['Sales', 'Discount', 'Profit']].mean()
data_category


# In[15]:


data_category.plot.pie(subplots=True, 
                     figsize=(18, 20), 
                     autopct='%1.1f%%', 
                     labels = data_category.index)


# According to the visualizations above, we may conclude that Technology possesses the highest amount of sales, while Furniture has the highest percentage of discounts and again Technology has the highest profit respectively.  

# # Sub-Category wise Sales, Profit & Discount: 

# In[16]:


data_sub_category = data.groupby(['Sub-Category'])[['Sales', 'Discount', 'Profit']].mean()
data_sub_category.head()


# #### [1] BASED ON THE DISCOUNT

# In[18]:


plt.figure(figsize = (15,15))
plt.pie(data_sub_category['Discount'], labels = data_sub_category.index, autopct = '%1.1f%%')
plt.title('Sub-Category Wise Discount Analysis', fontsize = 20)
plt.legend()
plt.show()


# According to the diagram above, among all the Sub-Categories, Binders (14.6%), Machines (12.0%), and Tables (10.2%) have the greatest percentages of discounts. 

# #### [2]BASED ON THE SALES

# In[19]:


plt.figure(figsize = (15,15))
plt.pie(data_sub_category['Sales'], labels = data_sub_category.index, autopct = '%1.1f%%')
plt.title('Sub-Category Wise Sales Analysis', fontsize = 20)
plt.legend()
plt.show()


# The diagram above makes it clearly obvious that machines (22.6% of sales), copiers (30.2%), and tables (8.9%) contribute to the majority of sales. 

# #### [3]BASED ON THE PROFIT

# In[20]:


data_sub_category.sort_values('Profit')[['Sales','Profit']].plot(kind='bar',
                                                              figsize= (10,5),
                                                              label=['Avg Sales Price($)','Profit($)'])


# Looking at the above bar diagrams, the structure it is crystal obvious that copiers have the greatest profit and maximum sales. Machines and tables also have an acceptable amount of sales. Fasteners, Art, and Labels, all of which come under the category of Office supplies, show a small amount of sales and profit. In a nutshell we can say that Office Supplies has the lowest sales and profits (Fasteners, Art and Labels). 

# # SHIP MODE WISE ANALYSIS

# In[21]:


sns.countplot(x=data['Ship Mode'])


# In[25]:


data_shipmode = data.groupby(['Ship Mode'])[['Sales', 'Discount', 'Profit']].mean()
data_shipmode.plot.pie(subplots=True,
                     figsize=(18, 20), 
                     autopct='%1.1f%%', 
                     labels = data_shipmode.index)


# Taking a look at the sales first, we can see that Same Day(25.5%) Ship Mode has the greatest sales out of all. Further analysis of the discount chart reveals that First Class (26.7%) has the greatest discount, and First Class (26%) also has the highest profit. 

# # REGION WISE ANALYSIS 

# In[26]:


sns.countplot(x=data['Region'])


# In[28]:


data_region = data.groupby(['Region'])[['Sales', 'Discount', 'Profit']].mean()
data_region


# In[30]:


data_region.plot.pie(subplots=True, 
                   figsize=(18, 20), 
                   autopct='%1.1f%%',
                   labels = data_region.index)


# First, we can clearly see from the sales pie visualization that the South region (26.2%) has the most sales. Moving on to the Discount Chart, we can see that the Central Region (37.4%) covers the largest portion of the graph, making it the region with the highest discount rate overall, and that the West Region (20.2%) has the highest profit. 

# # Using Cluster Analysis(K-Mean Clustering) 

# In[32]:


x = data.iloc[:, [9, 10, 11, 12]].values
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', 
                    max_iter = 300, n_init = 10, random_state = 0).fit(x)
    wcss.append(kmeans.inertia_)


# In[33]:


sns.set_style("whitegrid") 
sns.FacetGrid(data, hue ="Sub-Category",height = 6).map(plt.scatter,'Sales','Quantity')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], 
            s = 100, c = 'yellow', label = 'Centroids')
plt.legend()
plt.show()


# In[34]:


sns.set_style("whitegrid") 
sns.FacetGrid(data, hue ="Sub-Category",height = 6).map(plt.scatter,'Sales','Profit')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], 
            s = 100, c = 'yellow', label = 'Centroids')
plt.legend()
plt.show()


# In[35]:


fig, ax = plt.subplots(figsize = (10 , 6))
ax.scatter(data["Sales"] , data["Profit"])
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
ax.set_title('Sales vs Profit')
plt.show()


# We can improve in those States by offering discounts in the preferred range so that the business and the consumer will both be profitable from the aforementioned data visualization and clustering, which shows which states and which categories have high or low sales and earnings.Therefore, technical analysis is required in order to determine that range.One can accomplish this using factor analysis or neural networks.
# <ul>
# <li>A consideration to continually keep in mind is that even though the superstore is losing money by offering discounts on its goods, they are unable to stop. The majority of the steep discounts are offered during holidays, end-of-season, and clearance sales, which are essential for the retailer to create room in their warehouses for new inventory. Additionally, the business benefits in the future by gaining more loyal customers as a result of its minor losses. Consequently, the modest discounts losses are a crucial component of the business of the firm.</li>

# # Overall Analysis:  

# <ul>
# <li>Discounts are the primary cause of loss because some areas experience loss due to more discounts while other areas experience fewer sales due to fewer discounts. As a result, it needs to be improved.</li>
# <li>It is preferable to offer greater discounts during holiday seasons, as this will boost sales.</li>
# <li>The Home office segment needs better improvement.</li>
# <li>Lack of awareness may be the cause of some places lower sales, so advertising in those areas may increase sales.</li>
# </ul>

# # Result & Conclusion : 

# <ul>
#         <li>Even though profit is higher than sales, there are some places where profit could be raised.</li>
# <ul>
#       <li>Wyoming : Lowest Number of deal,Highest amount of sales= Wyoming(11.8%)</li>
#       <li>Lowest amount of sales= South Dakota(0.8%)</li>
#       <li>Here is top 3 city where deals are Highest.</li>
#     <ul>
#       <li>New York City</li>
#       <li>Los Angeles</li>
#       <li>Philadelphia</li>
#     </ul>
#     </ul>
# <ul>
#     <li>State: Ohio: Lowest Profit</li>
#     <li>State: Vermont: Highest Profit</li>
#     <li>Segment: Home-office: High Profit & sales</li>
#     <li>Category: Minimun profit obtain in Furniture</li>
#     <li>Category: Maximun sales and Profit obtain in Technology.</li>
#     <li>Sub-category: Binders , Machines and then tables have high Discount.</li>
#     <li>Sub-category: Copier: High Profit & sales</li>
#     <li>Sales is high for Same day ship</li>
#     <li>Profit and Discount is high in First Class</li>
# </ul>
# 

# #### Let's examine the sales of a few states chosen at random from each profit bracket—high profit, medium profit, low profit, low loss, and high loss—and attempt to spot any significant patterns that might aid in boosting sales.

# #### We have a few questions to answer here:- 

# <ol>
#     <li>Which product category needs to be strengthened in order to increase profits?</li>
#     <li>What products do the loss bearing states buy?</li>
#     <li>What products do the most profit making states buy?</li>
# </ol>

# In[40]:


import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[43]:


state_code = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA','District of Columbia': 'WA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY'}
data['state_code'] = data.State.apply(lambda x: state_code[x])
state_code


# In[44]:


state_data = data[['Sales', 'Profit', 'state_code']].groupby(['state_code']).sum()
fig = go.Figure(data=go.Choropleth(
    locations=state_data.index, 
    z = state_data.Sales, 
    locationmode = 'USA-states', 
    colorscale = 'Reds',
    colorbar_title = 'Sales in USD',
))
fig.update_layout(
    title_text = 'Total State-Wise Sales',
    geo_scope='usa',
    height=800,
)
fig.show()


# In[65]:


def state_data_viewer(states):
    product_data = data.groupby(['State'])
    for state in states:
        data1 = product_data.get_group(state).groupby(['Category'])
        fig, ax = plt.subplots(1, 3, figsize = (28,5))
        fig.suptitle(state, fontsize=14)        
        ax_index = 0
        for cat in ['Furniture', 'Office Supplies', 'Technology']:
            cat_data = data1.get_group(cat).groupby(['Sub-Category']).sum()
            sns.barplot(x = cat_data.Profit, y = cat_data.index, ax = ax[ax_index])
            ax[ax_index].set_ylabel(cat)
            ax_index +=1
        fig.show()


# In[66]:


states = ['California', 'Washington', 'Mississippi', 'Arizona', 'Texas']
state_data_viewer(states)


# We can see the states and categories where sales and profits are strong or low from the data visualization shown above. By offering discounts in a preferred range, we can make improvements in those areas and ensure that both the business and the consumer are profitable. In this case, the superstore is losing money by offering discounts on its goods, but it can't cease. The majority of the steep discounts are offered during holidays, end-of-season, and clearance sales, which are essential for the retailer to create room in their warehouses for new inventory. Additionally, the business benefits in the future by gaining more loyal customers as a result of its minor losses. As a result, the modest losses caused by discounts play a crucial role in the operations of the firm.

# In[ ]:




