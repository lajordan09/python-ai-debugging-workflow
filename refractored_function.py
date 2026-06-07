def export_customer_data(self, output_file: str, file_format: str = "csv") -> bool:
    """Export customer data in the specified format (csv or json)."""
    if not self.customers:
        logger.error("No customer data available to export")
        return False

    try:
        if file_format == "csv":
            # Determine fieldnames from the first valid customer record
            first_record = next(
                (v for v in self.customers.values() if isinstance(v, dict)), None
            )
            if first_record is None:
                logger.error("No valid customer records to export")
                return False

            fieldnames = ["customer_id"] + list(first_record.keys())

            with open(output_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for customer_id, data in self.customers.items():
                    if not isinstance(data, dict):
                        logger.warning(
                            "Skipping non-dict customer record for id %r: %r",
                            customer_id,
                            data,
                        )
                        continue
                    row = {"customer_id": customer_id, **data}
                    writer.writerow(row)

        elif file_format == "json":
            # Build a clean, serializable dict of only valid customer records
            clean_customers = {}
            for customer_id, data in self.customers.items():
                if not isinstance(data, dict):
                    logger.warning(
                        "Skipping non-dict customer record for id %r: %r",
                        customer_id,
                        data,
                    )
                    continue
                clean_customers[customer_id] = data

            if not clean_customers:
                logger.error("No valid customer records to export to JSON")
                return False

            with open(output_file, "w") as file:
                json.dump(clean_customers, file, indent=2)

        else:
            logger.error("Unsupported format: %s", file_format)
            return False

        logger.info("Exported customer data to %s", output_file)
        return True

    except (OSError, TypeError, ValueError) as e:
        logger.error("Error exporting data: %s", e)
        return False
