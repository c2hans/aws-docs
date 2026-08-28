---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/amazon-sagemaker-lakehouse-for-DynamoDB-zero-etl-getting-started.html
---

# Creating a DynamoDB zero-ETL integration with Amazon SageMaker Lakehouse
<a name="amazon-sagemaker-lakehouse-for-DynamoDB-zero-etl-getting-started"></a>

After completing integration prerequisites, you can create, modify, or delete the zero-ETL integration following the guidance below:

## Creating an integration
<a name="amazon-sagemaker-lakehouse-for-DynamoDB-zero-etl-getting-started-creating"></a>

**To create an integration**

1. Sign in to the AWS Management Console and open the Amazon DynamoDB console at [https://console.aws.amazon.com/dynamodbv2](https://console.aws.amazon.com/dynamodbv2).

1. In the navigation pane, choose **Integrations**.

1. Select **Create zero-ETL integration with Amazon SageMaker Lakehouse**, and then choose **Next**.

1. To create an integration, see [Creating an integration](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-common-integration-tasks.html#zero-etl-creating).

1. To modify an integration, see [Modifying an integration](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-common-integration-tasks.html#zero-etl-modifying).

1. To delete an integration, see [Deleting an integration](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-common-integration-tasks.html#zero-etl-deleting).

1. To set up a cross-account integration, see [Setting up cross-account integration](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-prerequisites.html#zero-etl-setup-cross-account-integration).

## Enabling compaction on target Amazon S3 tables
<a name="amazon-sagemaker-lakehouse-for-DynamoDB-zero-etl-enabling-compaction"></a>

You can enable compaction to improve query performance in Amazon Athena.

First, complete the prerequisite setup for compaction resources, including configuring the necessary IAM role. Refer to the Lake Formation documentation for detailed IAM role configuration steps. See, [Optimizing tables for compaction](https://docs.aws.amazon.com/lake-formation/latest/dg/data-compaction.html).

To enable compaction on the AWS Glue table created during integration, follow the Lake Formation compaction enabling process. This will help optimize your table's performance and query efficiency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
