---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/dynamodb-tables.html
---

# Working with Amazon DynamoDB tables the AWS Toolkit for JetBrains
<a name="dynamodb-tables"></a>

The primary resource of Amazon DynamoDB is a data-base table. The following sections describe how to work with DynamoDB tables from the AWS Toolkit for JetBrains.

## Viewing a DynamoDB table
<a name="dynamodb-overview-view-table"></a>

To view a DynamoDB table, complete the following steps:

1. Navigate to the **Explorer** tab in the AWS Toolkit for JetBrains.

1. Expand the **DynamoDB** node.

1. From your list of DynamoDB resources, double-click a table to view it in the **Editor** window.

**Note**
The first time you view table data, an initial scan with a max-result limit of 50 items is retrieved.

## Setting the max-result limit
<a name="dynamodb-table-results"></a>

To change the default limit of retrieved table entries, compete the following steps:

1. From the AWS Explorer, double-click a table to view it in the JetBrains **Editor** window.

1. From the table view, choose the **Settings icon**, located in the upper-right hand corner of your **Editor** window.

1. Hover over the **Max Results** option to view a list of available max-result values.

## Scanning a DynamoDB table
<a name="dynamodb-table-scan"></a>

To scan a DynamoDB table, complete the following steps:

**Note**
This scan generates a **PartiQL query** and requires that you have the correct AWS Identity and Access Management (AWS IAM) policies in place. To learn more about the PartiQL security policy requirements, see the [IAM security policies with PartiQL for DynamoDB](https://docs.aws.amazon.com/) topic in the *Amazon DynamoDB Developer Guide*.

1. From the AWS Explorer, double-click a table to view it in the JetBrains **Editor** window.

1. From the table view, expand the **Scan** header.

1. Select the **Table/ Index** you want to scan from the drop-down menu.

1. Choose **Run** to proceed with the scan, the scan is complete when the table data is returned in the **Editor** window.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
