import pandas as pd
import numpy as np
from netCDF4 import Dataset


rootgrp = Dataset("C:\\Frankwork\\HomeWork\\DS_3\\frank_ds3.nc", "w", format="NETCDF4")
WebStatsgrp = rootgrp.createGroup("WebStats")
Num = WebStatsgrp.createDimension("Num", 5)
Which_Website = WebStatsgrp.createDimension("Which_Website", 5)
RegisterdUsers = WebStatsgrp.createDimension("RegisterdUsers", 5)
As_of_date = WebStatsgrp.createDimension("As_of_date", 5)
Link_to_Screendump = WebStatsgrp.createDimension("Link_to_Screendump", 5)
Orignial_URL = WebStatsgrp.createDimension("Orignial_URL", 5)
Reporting_date = WebStatsgrp.createDimension("Reporting_date", 5)
Num = WebStatsgrp.createVariable("Num","u2",("Num",))
Which_Website = WebStatsgrp.createVariable("Which_Website","S200",("Which_Website",))
RegisterdUsers = WebStatsgrp.createVariable("RegisterdUsers","u8",("RegisterdUsers",))
As_of_date = WebStatsgrp.createVariable("As_of_date","S200",("As_of_date",))
Link_to_Screendump = WebStatsgrp.createVariable("Link_to_Screendump","S200",("Link_to_Screendump",))
Orignial_URL = WebStatsgrp.createVariable("Orignial_URL","S200",("Orignial_URL",))
Reporting_date = WebStatsgrp.createVariable("Reporting_date","S200",("Reporting_date",))
WebStatsgrp.description = "Web Statistics"
WebStatsgrp.history = "Created By Frank on 10/24/2016"
WebStatsgrp.source = "All data are got from internet"

# For .read_csv, always use header=0 when you know row 0 is the header row
df = pd.read_csv('C:\\Frankwork\\HomeWork\\DS_3\\WebStats.csv', header=0)
print(df['No#'].values)
Num[:] = df['No#'].values
Which_Website[:] = df['Which_Website?'].values
RegisterdUsers[:] = df['RegisterdUsers'].values
As_of_date[:] = df['As_of_date'].values
Link_to_Screendump[:] = df['Link_to_Screendump'].values
Orignial_URL[:] = df['Orignial_URL'].values
Reporting_date[:] = df['Reporting_date'].values
print("RegisterdUsers =\n",RegisterdUsers[:])

Easy_2_Startgrp = rootgrp.createGroup("Easy_2_Start")
Num = Easy_2_Startgrp.createDimension("Num", 5)
Which_Website = Easy_2_Startgrp.createDimension("Which_Website", 5)
Easy_To_learn = Easy_2_Startgrp.createDimension("Easy_To_learn", 5)
Good_for_job_seeking = Easy_2_Startgrp.createDimension("Good_for_job_seeking", 5)
Link_to_Screendump = Easy_2_Startgrp.createDimension("Link_to_Screendump", 5)
Orignial_URL = Easy_2_Startgrp.createDimension("Orignial_URL", 5)
Reporting_date = Easy_2_Startgrp.createDimension("Reporting_date", 5)
Num = Easy_2_Startgrp.createVariable("Num","u2",("Num",))
Which_Website = Easy_2_Startgrp.createVariable("Which_Website","S200",("Which_Website",))
Easy_To_learn = Easy_2_Startgrp.createVariable("Easy_To_learn","S200",("Easy_To_learn",))
Good_for_job_seeking = Easy_2_Startgrp.createVariable("Good_for_job_seeking","S200",("Good_for_job_seeking",))
Link_to_Screendump = Easy_2_Startgrp.createVariable("Link_to_Screendump","S200",("Link_to_Screendump",))
Orignial_URL = Easy_2_Startgrp.createVariable("Orignial_URL","S200",("Orignial_URL",))
Reporting_date = Easy_2_Startgrp.createVariable("Reporting_date","S200",("Reporting_date",))
Easy_2_Startgrp.description = "Easy to start for beginners?"
Easy_2_Startgrp.history = "Created By Frank on 10/24/2016"
Easy_2_Startgrp.source = "All data are got from internet"

# For .read_csv, always use header=0 when you know row 0 is the header row
df = pd.read_csv('C:\\Frankwork\\HomeWork\\DS_3\\Easy_2_Start.csv', header=0)
Num[:] = df['Num'].values
Which_Website[:] = df['Which_Website'].values
Easy_To_learn[:] = df['Easy_To_learn'].values
Good_for_job_seeking[:] = df['Good_for_job_seeking'].values
Link_to_Screendump[:] = df['Link_to_Screendump'].values
Orignial_URL[:] = df['Orignial_URL'].values
Reporting_date[:] = df['Reporting_date'].values

AlexaRankinggrp = rootgrp.createGroup("AlexaRanking")
Num = AlexaRankinggrp.createDimension("Num", 5)
Which_Website = AlexaRankinggrp.createDimension("Which_Website", 5)
WorldRanking = AlexaRankinggrp.createDimension("WorldRanking", 5)
USRanking = AlexaRankinggrp.createDimension("USRanking", 5)
Link_to_Screendump = AlexaRankinggrp.createDimension("Link_to_Screendump", 5)
Orignial_URL = AlexaRankinggrp.createDimension("Orignial_URL", 5)
Reporting_date = AlexaRankinggrp.createDimension("Reporting_date", 5)
Num = AlexaRankinggrp.createVariable("Num","u2",("Num",))
Which_Website = AlexaRankinggrp.createVariable("Which_Website","S200",("Which_Website",))
WorldRanking = AlexaRankinggrp.createVariable("WorldRanking","u8",("WorldRanking",))
USRanking = AlexaRankinggrp.createVariable("USRanking","u8",("USRanking",))
Link_to_Screendump = AlexaRankinggrp.createVariable("Link_to_Screendump","S200",("Link_to_Screendump",))
Orignial_URL = AlexaRankinggrp.createVariable("Orignial_URL","S200",("Orignial_URL",))
Reporting_date = AlexaRankinggrp.createVariable("Reporting_date","S200",("Reporting_date",))
AlexaRankinggrp.description = "Alexa Ranking"
AlexaRankinggrp.history = "Created By Frank on 10/24/2016"
AlexaRankinggrp.source = "All data are got from internet"

# For .read_csv, always use header=0 when you know row 0 is the header row
df = pd.read_csv('C:\\Frankwork\\HomeWork\\DS_3\\AlexaRanking.csv', header=0)
print(df['Num'].values)
Num[:] = df['Num'].values
Which_Website[:] = df['Which_Website'].values
WorldRanking[:] = df['WorldRanking'].values
USRanking[:] = df['USRanking'].values
Link_to_Screendump[:] = df['Link_to_Screendump'].values
Orignial_URL[:] = df['Orignial_URL'].values
Reporting_date[:] = df['Reporting_date'].values

SearchEngineResultsgrp = rootgrp.createGroup("SearchEngineResults")
Num = SearchEngineResultsgrp.createDimension("Num", 90)
Which_Website = SearchEngineResultsgrp.createDimension("Which_Website", 90)
Keywords = SearchEngineResultsgrp.createDimension("Keywords", 90)
Which_Search_Engine = SearchEngineResultsgrp.createDimension("Which_Search_Engine", 90)
Link_to_Screendump = SearchEngineResultsgrp.createDimension("Link_to_Screendump", 90)
Orignial_URL = SearchEngineResultsgrp.createDimension("Orignial_URL", 90)
Reporting_date = SearchEngineResultsgrp.createDimension("Reporting_date", 90)
Weights_for_currentSearchEngine = SearchEngineResultsgrp.createDimension("Weights_for_currentSearchEngine", 90)
Grades_Converted_for_Ranking = SearchEngineResultsgrp.createDimension("Grades_Converted_for_Ranking", 90)
Ranking = SearchEngineResultsgrp.createDimension("Ranking", 90)
Weights_of_the_Keywords = SearchEngineResultsgrp.createDimension("Weights_of_the_Keywords", 90)
Num = SearchEngineResultsgrp.createVariable("Num","u2",("Num",))
Which_Website = SearchEngineResultsgrp.createVariable("Which_Website","S200",("Which_Website",))
Keywords = SearchEngineResultsgrp.createVariable("Keywords","S200",("Keywords",))
Which_Search_Engine = SearchEngineResultsgrp.createVariable("Which_Search_Engine","S200",("Which_Search_Engine",))
Link_to_Screendump = SearchEngineResultsgrp.createVariable("Link_to_Screendump","S200",("Link_to_Screendump",))
Orignial_URL = SearchEngineResultsgrp.createVariable("Orignial_URL","S200",("Orignial_URL",))
Reporting_date = SearchEngineResultsgrp.createVariable("Reporting_date","S200",("Reporting_date",))
Weights_for_currentSearchEngine = SearchEngineResultsgrp.createVariable("Weights_for_currentSearchEngine","u2",("Weights_for_currentSearchEngine",))
Ranking = SearchEngineResultsgrp.createVariable("Ranking","u2",("Ranking",))
Weights_of_the_Keywords = SearchEngineResultsgrp.createVariable("Weights_of_the_Keywords","u2",("Weights_of_the_Keywords",))
Grades_Converted_for_Ranking = SearchEngineResultsgrp.createVariable("Grades_Converted_for_Ranking","u2",("Grades_Converted_for_Ranking",))
SearchEngineResultsgrp.description = "Ranking by searching engines"
SearchEngineResultsgrp.history = "Created By Frank on 10/24/2016"
SearchEngineResultsgrp.source = "All data are got from internet"

# For .read_csv, always use header=0 when you know row 0 is the header row
df = pd.read_csv('C:\\Frankwork\\HomeWork\\DS_3\\SearchEngineResults.csv', header=0)
print(df['Num'].values)
Num[:] = df['Num'].values
Which_Website[:] = df['Which_Website'].values
Keywords[:] = df['Keywords'].values
Which_Search_Engine[:] = df['Which_Search_Engine'].values
Link_to_Screendump[:] = df['Link_to_Screendump'].values
Orignial_URL[:] = df['Orignial_URL'].values
Reporting_date[:] = df['Reporting_date'].values
Weights_for_currentSearchEngine[:] = df['Weights_for_currentSearchEngine'].values
Ranking[:] = df['Ranking'].values
Grades_Converted_for_Ranking[:] = df['Grades_Converted_for_Ranking'].values
Weights_of_the_Keywords[:] = df['Weights_of_the_Keywords'].values
rootgrp.close()