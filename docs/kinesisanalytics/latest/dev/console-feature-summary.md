---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/dev/console-feature-summary.html
---

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# Step 4 (Optional) Edit the Schema and SQL Code Using the Console
<a name="console-feature-summary"></a>

Following, you can find information about how to edit an inferred schema and how to edit SQL code for Amazon Kinesis Data Analytics. You do so by working with the schema editor and SQL editor that are part of the Kinesis Data Analytics console.

**Note**
To access or sample data in the console, your login user's role must have the `kinesisanalytics:GetApplicationState` permission. For more information about Kinesis Data Analytics application permissions, see [Overview of Managing Access](access-control-overview.md).

**Topics**
+ [Working with the Schema Editor](console-summary-edit-schema.md)
+ [Working with the SQL Editor](console-summary-sql-editor.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
