# -------------------------------------------------------------------
# Created by Jhordanne Jones. 
# xarray_linear_trend.py function was made with the help of Gemini AI
# -------------------------------------------------------------------

import xarray as xr
import numpy as np
import pymannkendall as mk

''' Calculate linear trend using Mann-Kendall test on xarray data. 
    Input: xarray DataArray with time as one of the dimensions.
    Output: xarray Dataset with trend and p-value for each grid point.'''
def calculate_spatial_trend(chunk):
    # Create an empty DataArray to store the trend values
    trend = xr.zeros_like(chunk.isel(year=0))
    p_value = xr.zeros_like(chunk.isel(year=0))

    # Loop through each grid point
    for lat in chunk.latitude:
        for lon in chunk.longitude:
            # Extract time series for the current grid point
            y = chunk.sel(latitude=lat, longitude=lon).values

            # Check if the time series has enough data points for trend calculation
            # Modified condition to require at least 2 valid data points
            if len(y) > 20 and not np.all(np.isnan(y)) and np.sum(~np.isnan(y)) >= 20 and np.divide(np.sum(np.isnan(y)), len(y)) < 0.1:
                # Run the Mann-Kendall trend calculation and hypothesis test
                mk_result = mk.original_test(y)

                # Store the trend (slope) and p-value
                trend.loc[dict(latitude=lat, longitude=lon)] = mk_result.slope
                p_value.loc[dict(latitude=lat, longitude=lon)] = mk_result.p
            else:
                # Handle cases with insufficient data (e.g., set trend and p-value to NaN)
                trend.loc[dict(latitude=lat, longitude=lon)] = 0
                p_value.loc[dict(latitude=lat, longitude=lon)] = np.nan

    ds = xr.Dataset({'trend': trend, 'p_value': p_value})
    return ds

''' Apply calculate_spatial_trend func on a given xarray DataArray.
    Input: xarray DataArray with time as one of the dimensions,
           months to consider, year range, and chunk sizes for Dask.
    Output: xarray Dataset with trend and p-value for each grid point.'''
def linear_trend_analysis(da, months=[5, 6, 7], year_range=(1979, 2024), chunk_sizes={'latitude': 10, 'longitude': 10}):
    seasonal_da = da.sel(time=da.time.dt.month.isin(months)).groupby('time.year').mean('time')
    seasonal_da = seasonal_da.sel(year=slice(year_range[0], year_range[1]))
    dask_da = seasonal_da.chunk(chunk_sizes)

    array1 = dask_da.isel(year=0)
    array2 = dask_da.isel(year=0)
    template = xr.Dataset({'trend': array1, 'p_value': array2})

    trend_results = dask_da.map_blocks(calculate_spatial_trend, template=template).compute()
    return trend_results