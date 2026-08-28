---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.ImportCSV.html
---

# Importing sample data from a CSV file
<a name="workbench.Modeler.ImportCSV"></a>

If you have preexisting sample data in a CSV file, you can import it into NoSQL Workbench. This enables you to quickly populate your model with sample data without having to enter it line by line.

The column names in the CSV file must match the attribute names in your data model, but they do not need to be in the same order. For example, if your data model has attributes called `LoginAlias`, `FirstName`, and `LastName`, your CSV columns could be `LastName`, `FirstName`, and `LoginAlias`.

You can import up to 150 rows at a time from a CSV file.

**To import data from a CSV file into NoSQL Workbench**

1. To import CSV data to a **Table**, first choose the table name in the resource panel, and then choose the additional actions (three-dot icon) in the main content toolbar.

1. Choose **Import sample data**.

1. Choose your CSV file and choose **Open**. The CSV data appends to your table.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
