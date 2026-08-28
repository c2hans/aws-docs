---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/RedshiftforDynamoDB-zero-etl-deleting.html
---

# Deleting DynamoDB zero-ETL integrations with Amazon Redshift
<a name="RedshiftforDynamoDB-zero-etl-deleting"></a>

 When you delete a zero-ETL integration, your data isn't deleted from DynamoDB or Amazon Redshift, but DynamoDB stops sending data from your source table to the Amazon Redshift target.

**To delete a zero-ETL integration**

1.  Sign in to the AWS Management Console and open the Amazon DynamoDB console at [https://console.aws.amazon.com/dynamodbv2](https://console.aws.amazon.com/dynamodbv2).

1.  In the DynamoDB console, choose **Integrations**.

1.  In the **Zero-ETL integration** pane, select the zero-ETL integration you want to delete.

1.  Choose **Manage**. This will take you to the integration details page.

1.  To confirm the deletion, choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
