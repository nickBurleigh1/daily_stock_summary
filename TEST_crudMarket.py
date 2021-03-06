from crudMarket import create_document, read_document, update_document, delete_document
import unittest

testDocument = {
      "Ticker" : "TEST_NO_ACTION",
      "Profit Margin" : 0.137,
      "Institutional Ownership" : 0.847,
      "EPS growth past 5 years" : 0.158,
      "Total Debt/Equity" : 0.56,
      "Current Ratio" : 3,
      "Return on Assets" : 0.089,
      "Sector" : "Healthcare",
      "P/S" : 2.54,
      "Change from Open" : -0.0148,
      "Performance (YTD)" : 0.2605,
      "Performance (Week)" : 0.0031,
      "Quick Ratio" : 2.3,
      "Insider Transactions" : -0.1352,
      "P/B" : 3.63,
      "EPS growth quarter over quarter" : -0.29,
      "Payout Ratio" : 0.162,
      "Performance (Quarter)" : 0.0928,
      "Forward P/E" : 16.11,
      "P/E" : 19.1,
      "200-Day Simple Moving Average" : 0.1062,
      "Shares Outstanding" : 339,
      "Earnings Date" : "2013-11-14T21:30:00Z",
      "52-Week High" : -0.0544,
      "P/Cash" : 7.45,
      "Change" : -0.0148,
      "Analyst Recom" : 1.6,
      "Volatility (Week)" : 0.0177,
      "Country" : "USA",
      "Return on Equity" : 0.182,
      "50-Day Low" : 0.0728,
      "Price" : 50.44,
      "50-Day High" : -0.0544,
      "Return on Investment" : 0.163,
      "Shares Float" : 330.21,
      "Dividend Yield" : 0.0094,
      "EPS growth next 5 years" : 0.0843,
      "Industry" : "Medical Laboratories & Research",
      "Beta" : 1.5,
      "Sales growth quarter over quarter" : -0.041,
      "Operating Margin" : 0.187,
      "EPS (ttm)" : 2.68,
      "PEG" : 2.27,
      "Float Short" : 0.008,
      "52-Week Low" : 0.4378,
      "Average True Range" : 0.86,
      "EPS growth next year" : 0.1194,
      "Sales growth past 5 years" : 0.048,
      "Company" : "Agilent Technologies Inc.",
      "Gap" : 0,
      "Relative Volume" : 0.79,
      "Volatility (Month)" : 0.0168,
      "Market Cap" : 17356.8,
      "Volume" : 1847978,
      "Gross Margin" : 0.512,
      "Short Ratio" : 1.03,
      "Performance (Half Year)" : 0.1439,
      "Relative Strength Index (14)" : 46.51,
      "Insider Ownership" : 0.001,
      "20-Day Simple Moving Average" : -0.0172,
      "Performance (Month)" : 0.0063,
      "P/Free Cash Flow" : 19.63,
      "Institutional Transactions" : -0.0074,
      "Performance (Year)" : 0.4242,
      "LT Debt/Equity" : 0.56,
      "Average Volume" : 2569.36,
      "EPS growth this year" : 0.147,
      "50-Day Simple Moving Average" : -0.0055
    }  


class TestCrudFunctions(unittest.TestCase):
    
  def test_create_document(self):
    self.assertNotEqual(create_document(testDocument), None)
    self.assertRaises(read_document("TEST_NO_ACTION"))
    delete_document("TEST_NO_ACTION")
    
  def test_read_document(self):
    create_document(testDocument)
    self.assertTrue(read_document("TEST_NO_ACTION"))
    self.assertRaises(read_document(123))
    delete_document("TEST_NO_ACTION")

  def test_update_document(self):
    self.assertRaises(update_document("TEST_NO_ACTION", "PEG", 1.5))
    delete_document("TEST_NO_ACTION")
    
  def test_delete_document(self):
    delete_document("TEST_NO_ACTION")
    self.assertEqual(read_document("TEST_NO_ACTION"), None)




if __name__ == '__main__':
    unittest.main()