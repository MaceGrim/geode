# Geode

**Geo**spatial **E**nvironmental **D**ata **E**xplorer - Tools for analyzing environmental changes using satellite imagery.

## Features

- STAC API integration for satellite imagery access
- NDVI change detection and analysis
- Interactive visualization tools
- Statistical analysis of environmental changes
- Support for multiple data sources (Sentinel-2, Landsat)

## Installation

```bash
pip install geode
```

Or install from source:

```bash
git clone https://github.com/openhands/geode.git
cd geode
pip install -e .
```

## Quick Start

```python
from geode.analysis import NDVIAnalyzer

# Define area of interest
polygon = [
    [-103.430, 43.239],
    [-103.013, 44.073],
    [-103.331, 44.405],
    [-104.624, 44.748],
    [-104.295, 43.902],
    [-103.430, 43.239]
]

# Initialize analyzer
analyzer = NDVIAnalyzer(polygon)

# Run analysis
changes = analyzer.analyze_changes(2018, 2023)

# Generate visualizations
analyzer.create_visualizations(changes, output_dir='output')
```

## Example Outputs

- Interactive maps showing change patterns
- Statistical summaries and reports
- Time series analysis
- Change detection visualizations

## Documentation

For detailed documentation, visit [docs/](docs/).

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.