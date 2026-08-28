---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/connect-odbc-excel.html
---

# Connect to Amazon DocumentDB from Microsoft Excel
<a name="connect-odbc-excel"></a>

1. Ensure that the Amazon DocumentDB driver has been correctly installed and configured. For more information, see [Setting up the Amazon DocumentDB ODBC driver in Windows](connect-odbc-setup-windows.md).

1. Launch Microsoft Excel.

1. Navigate to **Data** > **Get Data** > **From Other Sources**.

1. Choose **From ODBC**:
![The Get Data dropdown shows the From Other Sources submenu. The From ODBC option is selected.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/excel-odbc-1.png)

1. Select the data source from the **Data source name (DSN)** drop down menu that is associated with Amazon DocumentDB:
![The Data source name dropdown with the DocumentDB DSN option selected.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/excel-odbc-dsn-select-1.png)

1. Choose the collection from which you want to load data into Excel:
![The Navigator interface with the salaries table selected and a preview of its data.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/excel-odbc-collect-1.png)

1. Load data into Excel:
![Excel spreadsheet showing five rows of data from the selected salaries table.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/excel-data-load-1.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
