# dstamatis
geog3050/dstamatis - Dionysios Stamatis
The aim of this project is to harness geospatial programming techniques to integrate two key datasets: the Global Aridity Index and Potential Evapotranspiration Database (Zomer, et al., 2022) and the WorldClim 2 climate surfaces (Fick & Hijmans, 2017). These datasets will be utilized to generate comprehensive maps encompassing temperature, precipitation, and effective rainfall. Finally, modern effective rainfall will be calculated for 2023. The overarching objective is to employ these mapped variables to support cave studies, particularly in calculating effective rainfall for selected cave systems. Effective rainfall, defined as the disparity between precipitation and potential evapotranspirationv(PET), holds significance in understanding water infiltration patterns within cave environments. To calculate modern effective rainfall you will need temperature and precipitation data from weather stations. For example in this project, two weather stations with data for Perryville, Missouri were used. 

Data Requirements:
1. Global Aridity Index and Potential Evapotranspiration Database (Version 3): This dataset provides essential information regarding potential evapotranspiration and aridity index on a global scale. The data will serve as a fundamental component in assessing water availability and climatic conditions.

Zomer, R.J., Xu, J., & Trabucco, A. (2022). Version 3 of the Global Aridity Index and Potential Evapotranspiration Database. Scientific Data, 9(1), 409. [DOI: 10.1038/s41597-022-01493-1](https://doi.org/10.1038/s41597-022-01493-1)

WorldClim 2 Climate Surfaces: The WorldClim 2 dataset offers high-resolution climate data, including temperature and precipitation variables. These data layers are crucial for understanding the climatic context of the study area and for calculating effective rainfall.

Fick, S.E., & Hijmans, R.J. (2017). WorldClim 2: new 1-km spatial resolution climate surfaces for global land areas. International Journal of Climatology, 37(12), 4302-4315. [DOI:10.1002/joc.5086](https://doi.org/10.1002/joc.5086)

Data from Proximal Stations: Temperature and precipitation data will be derived from proximal stations to calculate modern PET and effective rainfall. Specifically stations:
KMOPERRY49 (37.69°N,	-89.87°W)
PERRYVILLE WATER PLT, MO (37.73°N,-89.92°W)

Methods:
PET Calculation: PyETo is a Python library for calculating reference crop evapotranspiration (ETo), sometimes referred to as potential evapotranspiration (PET). The library provides numerous functions for estimating missing meteorological data. For estimating ETo/PET the Thornthwaite (Thornthwaite, 1948) method will be implemented.

Effective Rainfall Calculation: This will be done in Excel by subtracting potential evapotranspiration from precipitation values. This calculation will provide insights into the actual water input available for infiltration into the selected cave systems.
