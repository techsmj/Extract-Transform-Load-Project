#Food for Thought - Extract-Transform-Load-Project

#Team: Tolani, Joy, Andrea, Manuel

#Data Sources:

#http://www.allrecipes.com/recipes/84/Healthy-recipes/
#https://fdc.nal.usda.gov/download-datasets.html

#Data Cleanup & Analysis: Extract and Transform

#The notebook “Final_recipes_pulled_into_pandas” outlines the first step in this study: web scraping the Allrecipes.com website for healthy recipes. As part of the scraping process, we extract the recipe title, recipe link, and ingredients using Selenium, Beautiful Soup, PyMongo, and MongoDB. The results are then transformed to a DataFrame using Pandas. Please refer to the “Final_recipes_pulled_into_pandas” notebook for specific comments about the code.

#The notebook “recipes_csv” outlines the next steps in this study:
#●	Using Pandas to clean and join recipes with ingredients and add to MongoDB collection.
#●	Extract FoodData Central dataset and clean data using Pandas 
#●	Convert datasets to json format and export to MongoDB using terminal

#Recipe title and ingredient data were joined using Pandas and the combined DataFrame was organized by removing id columns added by MongoDB. Additionally, the scraped data contained unnecessary symbols and letters (“, b, ‘, / , etc.) Using Pandas, the data was exported as a csv, then reimported as a new DataFrame (“recipes_df”). Unnecessary columns were again removed, leaving just the recipe title and ingredients.

#The USDA FoodData Central download site provides nutritional information in the form of Excel files. Using Pandas’ read_excel Method, a food DataFrame was created. 8790 ingredients were imported, and columns without complete nutritional information were removed. The data was further refined into a dictionary format by converting to a json format.


#Data Cleanup & Analysis: Load

#With the cleanup of data completed, the datasets were loaded into the non-relational database, MongoDB utilizing the terminal in VSCode. We chose to use this database due to the variance of ways to quantify recipe ingredients. Instead of trying to resolve this issue in this one week project, we took advantage of the NoSQL approach and imported ingredients as is. 

#MongoDB: allrecipes_etl1
#Collections:
#collection = db.recipes
#collection2= db.ingredients
