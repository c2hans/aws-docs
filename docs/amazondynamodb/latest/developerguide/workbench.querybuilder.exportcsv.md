---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.querybuilder.exportcsv.html
---

# Exporting data to a CSV file
<a name="workbench.querybuilder.exportcsv"></a>

You can export the results of a query from Operation Builder to a CSV file. This enables you to load the data into a spreadsheet or process it using your preferred programming language.

**Exporting to CSV**

1. In the Operation Builder, run an operation of your choice, such as a Scan or Query.
**Note**
You can only export results from read API operations and PartiQL statements to a CSV file. You can't export results from transaction read statements.
Currently, you can export results one page at a time to a CSV file. If there are multiple pages of results, you must export each page individually.

1. Select the items you want to export from the results.

1. In the **Actions** dropdown, choose **Export as CSV**.

1. Choose a filename and location for your CSV file and select **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
