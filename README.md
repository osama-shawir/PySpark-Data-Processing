[![CI](https://github.com/osama-shawir/PySpark-Data-Processing/actions/workflows/cicd.yml/badge.svg)](https://github.com/osama-shawir/PySpark-Data-Processing/actions/workflows/cicd.yml)

# NYC Taxi Trip Data Processing with PySpark

This project uses PySpark to process and analyze the New York City Taxi Trip Duration dataset. The dataset contains information about taxi trips in New York City, including the pickup and dropoff times, the trip duration, and other related data.

## Project Overview

The project performs the following steps:

1. **Data Loading**: The dataset is loaded from a CSV file into a PySpark DataFrame.

2. **Data Exploration**: The first few rows of the dataset are displayed and the schema is printed to the console.

    ![Firstrows](media/(641).png)

    ![Explore](media/(644).png)

3. **Data Transformation**: The `pickup_datetime` and `dropoff_datetime` columns, which are initially in string format, are converted to Unix timestamp format.

4. **Data Analysis**: The actual trip duration in minutes is calculated based on the pickup and dropoff times, and compared with the `trip_duration` column in the dataset.

5. **Result Saving**: The results, including the trip ID, the original trip duration, and the calculated actual duration, are saved to a new CSV file.

## Output

The output of the project is a CSV file named `nyc_taxi_durations.csv`. Each row in the file corresponds to a taxi trip and contains the following columns:

- `id`: The ID of the taxi trip.
- `trip_duration`: The original trip duration from the dataset, in seconds.
- `actual_duration`: The actual trip duration calculated based on the pickup and dropoff times, in minutes.

    ![Output](media/(643).png)

## Running the Project

To run the project, you need to have PySpark installed and a SparkSession initialized.
After setting up, you can run the project by executing the Python script in your development environment.
