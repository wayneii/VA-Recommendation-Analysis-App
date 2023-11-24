# VA-Recommendation-Analysis-App
This application provides tools to the Center for Women Veterans (CWV) to be able to assess previous recommendations and make future recommendations.

# Tools in the Application
1. Visual representation of top themes by year (the user selects year(s))
- This is created by utilizing the Hugging Face API to convert text to embeddings and then a Kmeans clustering algorithm is used to capture semantic meaning. 
2.	List of Reoccuring Recommendations (what’s still left on the table)
-	This is done using cosine similarity
3.	Search functionality 
- search for specific phrases, pulls up specific recommendations that match phrases
