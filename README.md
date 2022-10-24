# CityDivvyBikes
Case study project for Google Data Analytics, consists on reading the data from https://divvy-tripdata.s3.amazonaws.com/index.html.

The idea is cleaning, processing, analyzing and visualizing the data of the last 12 months of bikes rides (202110 to 202210) to get an idea to improve the business related
to the cyclists membership. The company wants to increase the number of cyclists taking an annual membership instead of a casual riders.

I have uploaded a draft trying to import the data and aggregated it on a few csv files, imported it to SQL and also calculated and introduced
a few key variables like ride time in minutes, the day of the week where a certain ride started, new columns for pivot tables regarding month-day values

There is still work to do but its an ongoing project to showcase some of my skills, currently I have used Pandas and Numpy for data manipulation,
[Tableau](https://public.tableau.com/views/test_16661905807670/Dashboard13?:language=en-US&:display_count=n&:origin=viz_share_link) for quick visualization 
and sqlalchemy for importing it to my own PostgreSQL installation, also there is the usage of dotenv to create a few personal variables for login.

The funcLocal folder has the functions regarding the project and the DataSource shows how the files should be put in the directory to be able to read them
(should be extracted from the very data page source which can't be redistributed here)

It's a little rough on the edges but its a work in progress, it's not on a finished stage. There is a quick todo.txt file which has some of the ideas I want to implement
