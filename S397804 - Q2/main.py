"""
Entry point for the program.
Loads data, runs analyses and writes output files.
"""
from data_loader import load_all_files
from analysis import seasonal_averages, station_ranges, station_stability
from writers import write_average_file, write_range_file, write_stability_file

def main() :
      """
      Main function to perform analysis and write results.
            Load data from temperatures/*.csv
            Compute seasonal averages, station ranges, and stability
            Write results into output files
      """
      data = load_all_files()
      averages = seasonal_averages(data)
      ranges = station_ranges(data)
      stability = station_stability(data)
      
      write_average_file(averages)
      write_range_file(ranges)
      write_stability_file(stability)

if __name__ == "__main__":
    main()