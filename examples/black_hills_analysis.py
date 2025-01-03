"""
Example analysis of vegetation changes in the Black Hills region.
"""

from geode.analysis import NDVIAnalyzer

def main():
    # Define the Black Hills region
    polygon_coords = [
        [-103.43004786118804, 43.23971521107963],
        [-103.01352665709838, 44.073250174728756],
        [-103.3313537175783, 44.405415780543436],
        [-104.62471529429507, 44.748492362200224],
        [-104.29514388295235, 43.90269371474301],
        [-103.43004786118804, 43.23971521107963]
    ]
    
    # Initialize analyzer
    analyzer = NDVIAnalyzer(polygon_coords)
    
    # Run analysis
    print("\nAnalyzing NDVI changes...")
    changes = analyzer.analyze_changes(2018, 2023, n_points=10)
    
    # Generate visualizations and report
    print("\nGenerating visualizations...")
    analyzer.create_visualizations(changes, output_dir='output')
    
    print("\nAnalysis complete! Check the output directory for:")
    print("1. ndvi_analysis.png - Statistical plots")
    print("2. ndvi_map.html - Interactive map")
    print("3. ndvi_statistics.txt - Detailed analysis")

if __name__ == "__main__":
    main()