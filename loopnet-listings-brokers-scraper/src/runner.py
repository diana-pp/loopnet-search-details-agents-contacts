thonimport json
import logging
from extractors.property_scraper import PropertyScraper
from extractors.broker_scraper import BrokerScraper
from outputs.exporters import Exporter

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Starting LoopNet Listings + Brokers Scraper...")

    property_scraper = PropertyScraper()
    broker_scraper = BrokerScraper()
    exporter = Exporter()

    # Scraping properties and brokers
    property_data = property_scraper.scrape()
    broker_data = broker_scraper.scrape()

    # Exporting results
    exporter.export(property_data, 'sample_output.json')
    exporter.export(broker_data, 'sample_output.json', append=True)

    logging.info("Scraping completed successfully!")

if __name__ == "__main__":
    main()