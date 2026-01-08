from data_loader import load_all_files
from analysis import seasonal_averages, station_ranges, station_stability

def main() :
      data = load_all_files()
      averages = seasonal_averages(data)
      ranges = station_ranges(data)
      stability = station_stability(data)
      

if __name__ == "__main__":
    main()