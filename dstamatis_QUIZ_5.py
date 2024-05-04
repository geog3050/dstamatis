import arcpy
import os

# Set up the workspace
folder = r'C:/Users/sdion/Desktop/Geospatial Programming/airports'
arcpy.env.workspace = folder

# Input feature class
fc = 'airports.shp'

# Output buffer shapefile
output_buffer_fc = os.path.join(arcpy.env.workspace, 'buffer_airports.shp')

# Define fields
fields = ['FEATURE', 'TOT_ENP', 'SHAPE@']

# Create a new feature class for the buffer
arcpy.CreateFeatureclass_management(arcpy.env.workspace, os.path.basename(output_buffer_fc), "POLYGON", spatial_reference=arcpy.Describe(fc).spatialReference)

# Add fields to the new feature class
arcpy.AddField_management(output_buffer_fc, "FEATURE", "TEXT")
arcpy.AddField_management(output_buffer_fc, "TOT_ENP", "LONG")

# Open an insert cursor for the new feature class
with arcpy.da.InsertCursor(output_buffer_fc, ['FEATURE', 'TOT_ENP', 'SHAPE@']) as cursor_out:
    # Open a search cursor for the input feature class
    with arcpy.da.SearchCursor(fc, fields) as cursor_in:
        for row in cursor_in:
            # Check if the feature is either "airport" or "seaplane base"
            if row[0] in ["airport", "seaplane base"]:
                # Determine the buffer distance based on the feature type and enplanements
                if row[0] == "airport" and row[1] > 10000:
                    buffer_distance = 15000
                elif row[0] == "airport" and row[1] <= 10000:
                    buffer_distance = 10000
                elif row[0] == "seaplane base" and row[1] > 1000:
                    buffer_distance = 7500
                else:
                    # No buffer needed for facilities with minimal activity
                    continue
                
                # Create buffer polygon
                buffer_geometry = row[2].buffer(buffer_distance)
                
                # Insert new feature into the buffer shapefile
                cursor_out.insertRow([row[0], row[1], buffer_geometry])

print("Buffer creation completed.")
