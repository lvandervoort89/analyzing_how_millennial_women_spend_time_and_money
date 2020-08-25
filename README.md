# Analyzing how millennial women spend their time and money via the Refinery29 Money Diaries

## **Objective:**  
Analyze how millennial women spend their time and money using NLP. Build a recommender that takes in user input and selects 3 Refinery29 Money Diaries that are similar to the user.

## **Approach:**
Use Natural Language Processing (NLP) to explore how millennial women spend their time and money. Identify topics for all diarists. Perform clustering on the age and salary metadata of diarists and then do additional topic modeling on each of these clusters.  Finally, create a Streamlit app that takes a users age, salary, and mini diary entry from the previous day, clusters them to the original diarists, and then based on the assigned cluster, performs cosine similarity on the mini diary the user submits. The app then recommends 3 money diaries for the user to read that are most similar.

## **Featured Techniques:**
- BeautifulSoup and Selenium web scraping
- Natural Language Processing (NLP)
- Non-negative Matrix Factorization (NMF)
- K-means clustering
- Streamlit

## **Data:**
476 money diaries were scraped from the Refinery29 website. Diaries were from January 18, 2019-June 3, 2020.
1. Diarist age, salary and location were cleaned and used as metadata.
2. Diarist 7 day entries were used as text data. All numbers, characters, and stop words were removed.

## **Results Summary:**
*Top topics (all diarists)*: Friends/socializing, Cooking/food, Work, Dogs, Self-care, Family, Husband, Baby

*Top topics by cluster*:
Cluster 1: Early 20s, entry-level earners
- Self-care, Purchases, Dogs/pets, Food, Fitness, Travel, Work, Family

Cluster 2: Late 20s, average earners
- Home routines, Dogs, Husband, Baby/mom, Work, Friends/socializing

Cluster 3: Late 20s, high earners
- Dating, Parties, Food, Home, Fitness, Work

Cluster 4: Mid 30s, average
- Work, Kid routines, Family, Adult routines, Pets, Food

Cluster 5: Mid 30s, high earners  
- Family routines, Work, Parenting, Self-care, Family
