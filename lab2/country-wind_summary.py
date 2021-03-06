# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# country-wind_summary.py
# Created on: 2014-10-11 11:00:30.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")


# Local variables:
in_countries = "H:\\esm296-4f\\labs\\lab2\\raw\\ne_10m_admin_0_countries.shp"
s_0_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_0.tif"
s_120_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_120.tif"
s_150_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_150.tif"
s_180_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_180.tif"
s_210_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_210.tif"
s_240_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_240.tif"
s_270_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_270.tif"
s_30_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_30.tif"
s_300_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_300.tif"
s_330_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_330.tif"
s_360_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_360.tif"
s_60_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_60.tif"
s_90_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_90.tif"
s_avg_tif = "H:\\esm296-4f\\labs\\lab2\\out\\s_avg.tif"
out_countries = "H:\\esm296-4f\\labs\\lab2\\lab2.gdb\\countries"
s_countries = "H:\\esm296-4f\\labs\\lab2\\lab2.gdb\\s_countries"

# Process: Copy Features
arcpy.CopyFeatures_management(in_countries, out_countries, "", "0", "0", "0")

# Process: Cell Statistics
arcpy.gp.CellStatistics_sa("H:\\esm296-4f\\labs\\lab2\\out\\s_0.tif;H:\\esm296-4f\\labs\\lab2\\out\\s_120.tif;H:\\esm296-4f\\labs\\lab2\\out\\s_150.tif;H:\\esm296-4f\\labs\\lab2\\out\\s_180.tif;H:\\esm296-4f\\labs\\lab2\\out\\s_210.tif;H:\\esm296-4f\\labs\\lab2\\out\\s_240.tif;H:\\esm296-4f\\labs\\lab2\\out\\s_270.tif;H:\\esm296-4f\\labs\\lab2\\out\\s_30.tif;H:\\esm296-4f\\labs\\lab2\\out\\s_300.tif;H:\\esm296-4f\\labs\\lab2\\out\\s_330.tif;H:\\esm296-4f\\labs\\lab2\\out\\s_360.tif;H:\\esm296-4f\\labs\\lab2\\out\\s_60.tif;H:\\esm296-4f\\labs\\lab2\\out\\s_90.tif", s_avg_tif, "MEAN", "DATA")

# Process: Zonal Statistics as Table
arcpy.gp.ZonalStatisticsAsTable_sa(out_countries, "NAME", s_avg_tif, s_countries, "DATA", "MIN_MAX_MEAN")

# Process: Join Field
arcpy.JoinField_management(out_countries, "NAME", s_countries, "NAME", "Min;Max;Mean")

