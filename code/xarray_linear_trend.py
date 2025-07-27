import xarray as xr
import numpy as np
import pymannkendall as mk

''' Calculate linear trend using Mann-Kendall test on xarray data. '''
def calculate_spatial_trend(chunk):
    trend = xr.zeros_like(chunk.isel(year=0))
    p_value = xr.zeros_like(chunk.isel(year=0))

    for lat in chunk.latitude:
        for lon in chunk.longitude:
            y = chunk.sel(latitude=lat, longitude=lon).values
            if len(y) > 20 and not np.all(np.isnan(y)) and np.sum(~np.isnan(y)) >= 20 and np.divide(np.sum(np.isnan(y)), len(y)) < 0.1:
                mk_result = mk.original_test(y)
                trend.loc[dict(latitude=lat, longitude=lon)] = mk_result.slope
                p_value.loc[dict(latitude=lat, longitude=lon)] = mk_result.p
            else:
                trend.loc[dict(latitude=lat, longitude=lon)] = 0
                p_value.loc[dict(latitude=lat, longitude=lon)] = np.nan

    ds = xr.Dataset({'trend': trend, 'p_value': p_value})
    return ds

def linear_trend_analysis(da, months=[5, 6, 7], year_range=(1979, 2024), chunk_sizes={'latitude': 10, 'longitude': 10}):
    seasonal_da = da.sel(time=da.time.dt.month.isin(months)).groupby('time.year').mean('time')
    seasonal_da = seasonal_da.sel(year=slice(year_range[0], year_range[1]))
    dask_da = seasonal_da.chunk(chunk_sizes)

    array1 = dask_da.isel(year=0)
    array2 = dask_da.isel(year=0)
    template = xr.Dataset({'trend': array1, 'p_value': array2})

    trend_results = dask_da.map_blocks(calculate_spatial_trend, template=template).compute()
    return trend_results