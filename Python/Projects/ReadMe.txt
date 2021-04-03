The  projects that you see here are called are more serious programs that I have made in generally
4 - 20 hours. Below I will detail what they do,in order of their creation date, note that as they get updated they will do more as 
not all work is completed in one coding session.

Covid-Data-Analysis-Interface   -    Created (19/03/2021) 
___________________________________________________________
The file 'Covid-Data-Analysis-Interface.py' file is the file for this program.
At the moment this program imports a csv file found at : https://covid.ourworldindata.org/data/owid-covid-data.csv , the csv file contains all kinds of
data about Covid-19.The is some commented out code that needs to be run for this python file to work properly, the code creates a series of folders and
subfolders, the main folders being 'Countries' and 'Regions' and the subfolders in these main folders represent various Countries and Regions.
The program also creates an interface, this interface allows users to open a window to all the Countries found in the csv file, all
the regions found in the csv file or a window that default is all the regions and countries in the csv file. In these subwindows one can select a specific
country/region (the all window works for all regions and countries at the same time), for any region/country selected, a user can create various 
charts that portray different things about Covid statistics for that particular location. The charts that can be created are total cases for location
over time, total cases per million people for location over time, positive rate over time for location, total deaths over time for location and
total vaccinations per hundred people over time for a location. These charts are then saved into the subfolder for the location.
The all window allows a user to make any of these charts, however the chart is made for and saved to every location/subfolder.
The 'Test.py' file is just a file I used to store the chart-making logic in initially. It is not needed at all.
The program must be run from the main folder, i.e.  the 'Covid-Data-Analysis-Interface' folder.


