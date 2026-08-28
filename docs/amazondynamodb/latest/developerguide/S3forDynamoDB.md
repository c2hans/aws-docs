---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3forDynamoDB.html
---

# Integrating DynamoDB with Amazon S3
<a name="S3forDynamoDB"></a>

Amazon DynamoDB import and export capabilities provide a simple and efficient way to move data between Amazon S3 and DynamoDB tables without writing any code.

DynamoDB import and export features help you move, transform, and copy DynamoDB table accounts. You can import from your S3 sources, and you can export your DynamoDB table data to Amazon S3 and use AWS services such as Athena, Amazon SageMaker AI, and AWS Lake Formation to analyze your data and extract actionable insights. You can also import data directly into new DynamoDB tables to build new applications with single-digit millisecond performance at scale, facilitate data sharing between tables and accounts, and simplify your disaster recovery and business continuity plans.

**Topics**
+ [Import from Amazon S3](S3DataImport.HowItWorks.md)
+ [Export to Amazon S3](S3DataExport.HowItWorks.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
