import unittest
import tempfile
import os
from process_data import DataProcessor

class TestExportCustomerData(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for test files
        self.temp_dir = tempfile.TemporaryDirectory()
        self.customer_file = os.path.join(self.temp_dir.name, "customers.csv")
        self.transaction_file = os.path.join(self.temp_dir.name, "transactions.csv")

        # Write clean customer data
        with open(self.customer_file, "w") as f:
            f.write(
                "customer_id,name,email,join_date\n"
                "C001,John Smith,john@example.com,2023-01-01\n"
                "C002,Jane Doe,jane@example.com,2023-02-01\n"
            )

        # Write transactions INCLUDING a malformed row
        # This simulates the real-world corruption that originally caused JSON export to fail
        with open(self.transaction_file, "w") as f:
            f.write(
                "transaction_id,customer_id,amount,date,category\n"
                "T001,C001,100.00,2024-01-10,electronics\n"
                "T002,C002,50.00,2024-01-11,books\n"
                # Malformed row: customer_id is actually a field name
                "T003,name,75.00,2024-01-12,clothing\n"
            )

    def tearDown(self):
        # Clean up temporary directory
        self.temp_dir.cleanup()

    def test_export_customer_data_json_success_after_fix(self):
        processor = DataProcessor(self.customer_file)

        # Load customers
        self.assertTrue(processor.load_data())

        # Process transactions (this will introduce a malformed entry)
        self.assertTrue(processor.process_transactions(self.transaction_file))

        # Attempt JSON export — should now SUCCEED after refactor
        output_file = os.path.join(self.temp_dir.name, "export.json")
        result = processor.export_customer_data(output_file, "json")

        # EXPECT SUCCESS after the fix
        self.assertTrue(
            result,
            "JSON export should succeed after handling malformed customer entry safely"
        )

        # Confirm file was actually created
        self.assertTrue(os.path.exists(output_file))

if __name__ == "__main__":
    unittest.main()
