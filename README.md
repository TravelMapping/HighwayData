# HighwayData

This repository is for raw data used by the Travel Mapping project.

Please help us improve our data by reporting any problems you notice with the data in [the project forum](http://tm.teresco.org/forum).

In general, the project's data is in plain text files in two formats: CSV using semicolon separators, and WPT or "waypoint" files.  WPT files are required to contain only plain ASCII text.  Some CSV files can include non-ASCII characters, but should always use a UTF-8 encoding when such characters are used.

The project's data is organized herein as follows:

Several CSV files at the top level are used to describe some project-wide information.

* `continents.csv`, `countries.csv`, `regions.csv`, and `regions_countries_continents.csv` are used to define the lists, names, abbreviations, and hierarchies for the geographic entities and governmental subdivisions used by the project.

* `datacheckfps.csv` contains a list of false positives that will be detected in the "datacheck" list of possible errors in the data.  Entries listed here will be shown only in the "crossed off" list on the datacheck error page.

* `systems.csv` contains a list of the highway systems included in the project.

* `systemupdates.csv` lists the system-level changes being made to the project, such as highway system activations.

* `updates.csv` lists the highway-level changes being made to routes in active systems within the project that could affect users.  Minor changes such as point relabelings or recenterings that do not require users to make any changes to their list files are not included here. Please keep this file sorted by region (ascending) and the by date (descending) within each region.

The `chm_final` directory contains an archive of the version of the project's data that was imported from the Clinched Highway Mapping project as a starting point for Travel Mapping.  It remains for historical interest only and is not used by Travel Mapping.

The `boundaries` directory contains descriptions of shorelines and borders that can be used to render certain types of maps.  Travel Mapping does not currently use these.

The `graphs` directory contains CSV files that guide the creation of some of the graphs generated for use by the [METAL project](http://courses.teresco.org/metal/).

The `hwy_data` directory contains all of the information about which routes are in each system and the points that make up each route.

Most directories within `hwy_data` are names of countries or regions.  Each country or region's directory will have one or more subdirectories, one for each highway system that includes at least one route in that country or region.  Within those directories are WPT files that list the waypoints of a route.  Each line in a WPT file has two parts: one or more labels (only the first of which will be considered primary) and an OpenStreetMap-style URL that includes the latitude and longitude of the point.

There is also a special directory inside `hwy_data`.  

* The `_systems` directory contains two CSV files for each highway system listed in the top-level `systems.csv` file.  For a hypothetical system called "usaza", the file `usaza.csv` would contain a list of highways within the system, and the file `usaza_con.csv` would contain a list of "connected" routes.  For example, I-90 is made up of WPT files in the usai system under regions `WA`, `ID`, `MT`, `SD`, `MN`, `WI`, `IL`, `IN`, `OH`, `PA`, `NY`, and `MA`, so its entry in `usai_con.csv` describes which files make up the entire route and in which order they come.
