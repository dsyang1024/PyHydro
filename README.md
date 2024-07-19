# PyHydro
Python based Hydrology analysis tool sets


# Flow Duration Curve (FDC) Function Documentation

The `FDC` function within the `PyHydro.py` script is designed to generate a Flow Duration Curve (FDC) plot from a given set of streamflow data. An FDC is a graphical representation that shows the percentage of time specified flows are equaled or exceeded over a given period. It is a crucial tool in hydrology for water resource planning and management.

## Function Overview

The `FDC` function takes a list of streamflow data, along with optional title and unit parameters, and generates an FDC plot. The function uses logarithmic scaling for the y-axis to accommodate the wide range of streamflow values typically encountered in hydrological datasets.

### Key Features

- **Logarithmic Y-Axis**: Enhances the readability of the plot across a broad range of streamflow values.
- **Customizable Plot Appearance**: Allows for customization of the plot title and the unit of streamflow measurement.
- **Sorted Streamflow Data**: Automatically sorts the input streamflow data in descending order as required for FDC plotting.

### Arguments

- `streamflow` (numerical list): A list of streamflow data points. This list should contain numerical values representing streamflow measurements.
- `title` (str, optional): The title of the plot. Defaults to an empty string (`''`), resulting in no title being displayed.
- `unit` (str, optional): The unit of measurement for the streamflow data. Defaults to cubic feet per second (`ft^3/sec`).

### Detailed Implementation

1. **Import Dependencies**: Imports `numpy` for numerical operations and `matplotlib.pyplot` for plotting.
2. **Font Configuration**: Sets the font family to "Times New Roman" for a classic, readable appearance.
3. **Data Sorting**: Sorts the input streamflow data in descending order to prepare for FDC plotting.
4. **Exceedance Probability Calculation**: Calculates the exceedance probability for each streamflow value. This calculation determines the percentage of time each flow rate is equaled or exceeded.
5. **Plot Creation**: Generates the FDC plot with logarithmic scaling on the y-axis, custom labels, and axis limits.

### Usage Notes

- The script requires the `numpy` and `matplotlib` libraries. Ensure these dependencies are installed in your Python environment.
- The function is designed to work with a list of numerical streamflow values. Ensure your data is correctly formatted before passing it to the function.

### Example Usage

```python
streamflow_data = [100, 200, 300, 400, 500]  # Example streamflow data
FDC(streamflow_data, title='Sample FDC Plot', unit='m^3/s')
```

***
# Water Quality Boxplot Function Documentation

The `boxplot` function within the `PyHydro.py` script is designed to generate boxplots for water quality data. Boxplots are statistical visualizations that summarize the distribution of data through their quartiles, highlighting the median, the upper and lower quartiles, and potential outliers. This function is particularly useful for analyzing the variability and central tendency of water quality parameters over time.

## Function Overview

The `boxplot` function takes a pandas DataFrame containing water quality data, along with optional parameters for unit and criteria, to generate boxplots. The function supports generating boxplots for all data points collectively, or categorized by monthly, annual, or seasonal criteria, although the current implementation only covers the 'all' criteria.

### Key Features

- **Customizable Unit of Measurement**: Allows specifying the unit for water quality data, with a default of milligrams per liter (mg/L).
- **Flexible Criteria Selection**: Intended to support different criteria for boxplot generation, such as monthly, annual, or seasonal, with the current implementation focusing on the 'all' criteria.
- **High-Resolution Output**: Saves the generated boxplots as high-resolution PNG files.

### Arguments

- `wq_data` (pandas DataFrame): The primary input for the function. This DataFrame must have its index set to dates (in `yyyy-mm-dd` format) and contain columns for different water quality parameters.
- `unit` (str, optional): Specifies the unit of measurement for the water quality data. Defaults to `mg/L`.
- `criteria` (str, optional): Determines the criteria for which the boxplot is generated (`all`, `monthly`, `annual`, `seasonal`). The default is `'all'`.

### Detailed Implementation

1. **Import Dependencies**: Imports `matplotlib.pyplot` for plotting.
2. **Font Configuration**: Sets the font family to "Times New Roman" for a classic, readable appearance.
3. **Boxplot Generation**: Currently, the function generates a boxplot for each parameter in the DataFrame when the criteria is set to 'all'. It iterates through each column, creates a figure, and plots a boxplot for the water quality parameter.
4. **Labeling and Saving**: Labels the y-axis with the concentration and unit, applies a tight layout for neat presentation, enables grid lines for better readability, and saves the plot as a high-resolution PNG file named after the parameter with '_Boxplot.png' suffix.
5. **Cleanup**: Clears the figure after saving to free up memory.

### Usage Notes

- The script requires the `matplotlib` library. Ensure this dependency is installed in your Python environment.
- The function is designed to work with a pandas DataFrame indexed by date, with columns representing different water quality parameters.

### Example Usage

```python
import pandas as pd
# Assuming `data` is a pandas DataFrame with the required structure
boxplot(data, unit='mg/L', criteria='all')
```

***
# PyHydro Script Documentation

The `PyHydro.py` script is designed for hydrological data analysis, with a focus on generating hydrographs. A hydrograph is a graphical representation of the flow rate of water (streamflow) and precipitation over time. This script specifically provides functionality to plot hydrographs using streamflow and precipitation data.

## Functionality Overview

The core of this script is a function that creates a hydrograph from a given pandas DataFrame. The DataFrame should contain streamflow and precipitation data, indexed by date. The function plots both sets of data on a dual-axis graph, with precipitation data inverted to visually emphasize its impact on streamflow.

### Key Features

- **Dual-Axis Plotting**: Utilizes matplotlib to plot both precipitation and streamflow data on a shared x-axis (date) but separate y-axes.
- **Customizable Appearance**: Allows for customization of the plot title and the unit of streamflow measurement.
- **High-Resolution Output**: Saves the generated hydrograph as a high-resolution PNG file.

### Function Arguments

- `sp_df` (pandas DataFrame): The primary input for the function. This DataFrame must have its index set to dates (in `yyyy-mm-dd` format) and contain two columns: one for streamflow and another for precipitation data.
- `title` (str): An optional argument that specifies the title of the hydrograph. If not provided, the plot will have no title.
- `unit` (str): An optional argument that allows specifying the unit of measurement for streamflow data. The default unit is cubic feet per second (`ft^3/sec`).

### Detailed Implementation

1. **Font Configuration**: Sets the font family to "Times New Roman" for a classic, readable appearance.
2. **Subplot Creation**: Generates a figure with two subplots (one for precipitation and one for streamflow) with shared x-axis and custom height ratios.
3. **Precipitation Plotting**: Currently plots precipitation data as a line graph. A TODO note suggests changing this to a bar graph for better visualization.
4. **Streamflow Plotting**: Plots streamflow data as a line graph on the second subplot.
5. **Axis Labeling and Adjustment**: Configures y-axis labels for both precipitation and streamflow, inverts the y-axis for precipitation, and sets a common x-axis label (Date).
6. **Grid and Title Configuration**: Optionally adds a title to the plot and enables grid lines for better readability.
7. **Output Generation**: Saves the plot as a high-resolution PNG file named `Hydrograph.png` and then clears the figure to free up memory.

### Usage Notes

- The script requires the `matplotlib` library for plotting. Ensure this dependency is installed in your Python environment.
- The function is designed to be flexible with the input DataFrame structure, requiring only specific column names (`precip` and `streamflow`) and a date-indexed DataFrame.
- The TODO comment indicates a planned enhancement to improve the visualization of precipitation data by plotting it as a bar graph instead of a line graph.

### Example Usage

```python
import pandas as pd
# Assuming `data` is a pandas DataFrame with the required structure
plot_hydrograph(data, title='Sample Hydrograph', unit='m^3/s')
```