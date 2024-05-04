# dstamatis
geog3050/dstamatis - Dionysios Stamatis

Dionysios Stamatis - Reconstructing Temperature and moisture patterns using stalagmites from Crevice Cave, Missouri

Dionysios Stamatis holds a BSc in Geology and an MSc in Geosciences from the University of Patras, Greece. Currently a second-year PhD student in the Earth and Environmental Science Department at the University of Iowa, USA, his research focuses on unraveling temperature and precipitation patterns during past Interglacials. To achieve this, he employs a range of analytical techniques, including measuring δ18O, δ13C, δ44Ca, trace elements, Dual-Clumped Isotopes, and TEX86 in speleothems. His aim is to illuminate the hydroclimate dynamics of the Midcontinental USA during periods resembling projected future climate conditions.

Dionysios Stamatis
151 Westside Drive, Iowa City, IA 52246, USA • tel: (+1) 952-297-5609 • dionysios-stamatis@uiowa.edu
EDUCATION
University of Iowa, USA    				                                                                08/2022 - 05/2027
•	PhD in Geosciences 
o	Current Grade: 3.41/4 
o	Thesis: Reconstructing Temperature and moisture patterns using stalagmites from Crevice Cave, Missouri

University of Patras, Greece				                                                                09/2019 - 12/2021
•	MSc in Geosciences and the Environment (2-year degree; 90 ECTS)
o	Grade: 9.27/10 (Distinction)
o	Thesis: Paleoenvironmental evolution of Lousoi lake during the Holocene, Northern Peloponnese, Greece (Grade: 10/10)

University of Patras, Greece				                                                               10/2015 - 12/2019
•	BSc in Geology (4-year degree; 240 ECTS)                                                                                     
o	Grade: 7.34/10 (graduated 9th out of a class of 180 students)
o	Specialization: Sedimentology, Geochemistry and Micropaleontology
o	Thesis: Sedimentological and Geochemical study of Upper Holocene of lake
Vouliagmeni, Corinth gulf, Greece (Grade: 10/10)

Christian-Albrechts University, Kiel, Germany                                                                                 11/2020 - 12/2020
•	Erasmus exchange student at the Institute of Geosciences at the Faculty of Mathematics and Natural Sciences

RESEARCH EXPERIENCE
Lab Assistant, Sedimentology Lab, Patras, Greece 		                                                               10/2018 - 10/2021
•	Assisted in drilling expeditions of the Sedimentology lab, preparation, and analysis of the samples  
Reasearch Assistant, Sedimentology Lab, Patras, Greece 		                                                  09/2018 - 09/2019
•	Assisted in the sampling, sedimentological, geochemical and magnetic susceptibility analysis of a varved record as part of a team of undergraduate students
WORK EXPERIENCE
Engineering Geologist, GaiaComm Ltd., Greece 		                                                               11/2021 – 06/2022

PUBLICATIONS
•	Dionysios Stamatis, Alexandros Emmanouilidis, Alessia Masi, Adam Izdebski, and Pavlos Avramidis, “Holocene hydroclimatic changes of Northern Peloponnese, Greece, inferred from karst lake systems” (Water)

SKILLS 
•	Programming	 	R, MATLAB, Python
•	Software Tools		ArcGIS Pro, QGIS, ImageJ, Tinytag Explorer, Hoboware
•	Statistics                         Bayesian statistics

VOLUNTEERING
•	Hellenic Red Cross, Samaritan/Rescuer, 2015-2020

LANGUAGES
•	English (fluent), Greek (native)




Project

Introduction:

The aim of this project is to harness geospatial programming techniques to integrate two key datasets: the Global Aridity Index and Potential Evapotranspiration Database (Zomer, et al., 2022) and the WorldClim 2 climate surfaces (Fick & Hijmans, 2017). These datasets will be utilized to generate comprehensive maps encompassing temperature, precipitation, and effective rainfall. Finally, modern effective rainfall will be calculated for 2023. The overarching objective is to employ these mapped variables to support cave studies, particularly in calculating effective rainfall for selected cave systems. Effective rainfall, defined as the disparity between precipitation and potential evapotranspirationv(PET), holds significance in understanding water infiltration patterns within cave environments. To calculate modern effective rainfall you will need temperature and precipitation data from weather stations. For example in this project, two weather stations with data for Perryville, Missouri were used. 

Data Requirements:

Global Aridity Index and Potential Evapotranspiration Database (Version 3): This dataset provides essential information regarding potential evapotranspiration and aridity index on a global scale. The data will serve as a fundamental component in assessing water availability and climatic conditions.

Zomer, R.J., Xu, J., & Trabucco, A. (2022). Version 3 of the Global Aridity Index and Potential Evapotranspiration Database. Scientific Data, 9(1), 409. [DOI: 10.1038/s41597-022-01493-1](https://doi.org/10.1038/s41597-022-01493-1)

WorldClim 2 Climate Surfaces: The WorldClim 2 dataset offers high-resolution climate data, including temperature and precipitation variables. These data layers are crucial for understanding the climatic context of the study area and for calculating effective rainfall.

Fick, S.E., & Hijmans, R.J. (2017). WorldClim 2: new 1-km spatial resolution climate surfaces for global land areas. International Journal of Climatology, 37(12), 4302-4315. [DOI:10.1002/joc.5086](https://doi.org/10.1002/joc.5086)

Data from Proximal Stations: Temperature and precipitation data will be derived from proximal stations to calculate modern PET and effective rainfall. Specifically stations:
KMOPERRY49 (37.69°N,	-89.87°W)
PERRYVILLE WATER PLT, MO (37.73°N,-89.92°W)

Methods:

PET Calculation: PyETo is a Python library for calculating reference crop evapotranspiration (ETo), sometimes referred to as potential evapotranspiration (PET). The library provides numerous functions for estimating missing meteorological data. For estimating ETo/PET the Thornthwaite (Thornthwaite, 1948) method will be implemented.

Effective Rainfall Calculation: This will be done in Excel by subtracting potential evapotranspiration from precipitation values. This calculation will provide insights into the actual water input available for infiltration into the selected cave systems.


Step by Step:

First of all, we will calculate annual PET.

Here's a step-by-step guide based on the Thornthwaite (1948) equation example for estimating monthly Potential Evapotranspiration (PET) in 2023 for Perryville, Missouri from the first weather station KMOPERRY49 (latitude 37.69 degrees N):

1. **Convert Latitude to Radians**:
   - Convert the latitude from degrees to radians using the `deg2rad` function.

2. **Calculate Monthly Mean Daylight Hours**:
   - Use the `monthly_mean_daylight_hours` function to calculate the mean daylight hours for each month of the year based on the converted latitude and the year (2023 in this case).

3. **Collect Monthly Mean Temperature Data**:
   - Prepare a list of monthly mean temperatures in degrees Celsius for Perryville in 2023.

4. **Apply Thornthwaite Equation**:
   - Utilize the `thornthwaite` function, providing the monthly mean temperatures and the calculated mean daylight hours for each month as inputs. This function will compute the PET for each month.

By following these steps, you can estimate monthly PET using the Thornthwaite equation for a specific location based on mean monthly temperature and daylight hours. 

Now that we have PET we can subtract it from precipitation to find the effective rainfall.

For the next step we need to download annual ET0 and Precipitation for the period 1970-2000 from the global datasets. After the files are downloaded the user should open the jupyter notebook in ArcGIS Pro and follow the procedure outlined in there. Below a short step by step guide is provided:

**Set up Environment and Licenses**:

Import necessary modules from arcpy.
Check out Spatial Analyst and Image Analyst extensions licenses.

**Set Analysis Environments**:

Set the workspace to the appropriate geodatabase.
Enable overwriting output.

**Import Data into Geodatabase**:

Convert raster and shapefile data to the geodatabase.
Import CSV file as point data using XYTableToPoint tool.

**Project Feature Classes**:

Project point and polygon feature classes to a desired coordinate system (NAD 1983 UTM Zone 15N).

**Project Raster Data**:

Project raster data (Annual_ET0 and Annual_Prec) to the desired coordinate system (NAD 1983 UTM Zone 15N).

**Select and Clip Raster Data**:

Select a specific county (Perry county in Missouri) using a SQL query.
Clip the projected rasters to the extent of the selected county.

**Perform Raster Operations**:

Perform raster calculation (subtraction) to find the difference between two rasters (AnPrec_Perry and AnET0_Perry).
Save the output raster.

**Create Points and Project Coordinates**:

Define points using coordinates.
Create point geometries and project them to the desired coordinate system (NAD 1983 UTM Zone 15N).
Print the projected coordinates.

**Set Extent and Perform Interpolation**:

Set the extent environment.
Perform IDW interpolation on the point data.
Save the interpolated result.

**Compute Raster Difference**:

Perform raster calculation (subtraction) to find the difference between two rasters (outMinus and outIDW).
Save the output raster.
