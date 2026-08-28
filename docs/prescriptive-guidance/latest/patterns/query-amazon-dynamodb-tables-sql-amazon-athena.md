---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/query-amazon-dynamodb-tables-sql-amazon-athena.html
---

# Query Amazon DynamoDB tables with SQL by using Amazon Athena
<a name="query-amazon-dynamodb-tables-sql-amazon-athena"></a>

*Gavin Perrie, Ajit Ambike, and Brad Yates, Amazon Web Services*

## Summary
<a name="query-amazon-dynamodb-tables-sql-amazon-athena-summary"></a>

If your data includes sources other than Amazon Simple Storage Service (Amazon S3), you can use federated queries to access those relational, non-relational, object, or custom data sources. This pattern shows how to configure federated query access through Amazon Athena to Amazon DynamoDB by using an SQL data source connector.

Using this pattern you can do the following:
+ Query DynamoDB tables by using SQL.
+ Run federated SQL queries in Athena and join DynamoDB tables with other supported data sources.

## Prerequisites and limitations
<a name="query-amazon-dynamodb-tables-sql-amazon-athena-prereqs"></a>

**Prerequisites**
+ A DynamoDB table.
+ An Athena workgroup set to use Athena engine version 2. For instructions, see the [Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/engine-versions-changing.html).
+ An S3 bucket where the `AthenaDynamoDBConnector` AWS Lambda function can spill the data. The S3 bucket and the Lambda function must be in the same AWS Region.

If this is your first time accessing Athena, you will need an additional S3 bucket to use as the query result location. For instructions, see the [Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/querying.html#query-results-specify-location-console).

**Limitations**
+ Write operations such as [INSERT INTO](https://docs.aws.amazon.com/athena/latest/ug/insert-into.html) are not supported.** **

**Product versions**
+ [Athena Query Federation releases on GitHub](https://github.com/awslabs/aws-athena-query-federation/releases)

## Architecture
<a name="query-amazon-dynamodb-tables-sql-amazon-athena-architecture"></a>

**Target architecture**

The following diagram shows the connection flow after the pattern is established. The user connects to Amazon Athena to provide the query. Athena passes the query and target to the DynamoDB data source connector Lambda function, which retrieves and returns the data to Athena. If large amounts of data are returned, Athena stores the temporary results in the spill bucket before packaging and returning the complete dataset.

![Workflow from users to Athena to Lambda, which connects to the S3 bucket and to the DynamoDB table.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/9d1ee529-36f3-4c7e-a2e7-05b76e09a3d8/images/e50a00cf-a55a-4def-81d5-4d2755dc9a97.png)

## Tools
<a name="query-amazon-dynamodb-tables-sql-amazon-athena-tools"></a>

**AWS services**
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon Simple Storage Service (Amazon S3) by using standard SQL. This pattern uses [Amazon Athena DynamoDB Connector](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-dynamodb), a tool built using the Amazon Athena Query Federation SDK and installed as an AWS Lambda application through the AWS Serverless Application Repository.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Code repository**

The code for this pattern is available in the GitHub [Athena Query Federation](https://github.com/awslabs/aws-athena-query-federation/releases) repository.

## Epics
<a name="query-amazon-dynamodb-tables-sql-amazon-athena-epics"></a>

### Set up and test the DynamoDB data source connector
<a name="set-up-and-test-the-ddb-data-source-connector"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the AthenaDynamoDBConnector application. | To deploy AthenaDynamoDBConnecter, do the following:1. Sign in to the AWS Management Console, and choose the AWS Region that you're using for the DynamoDB table and the spill bucket.<br />2. Open the **Serverless Application Repository** at https://console.aws.amazon.com/serverlessrepo/.<br />3. In the navigation pane, choose **Available Applications**.<br />4. For AWS Identity and Access Management (IAM) access, under the search bar, select the **Show apps that create custom IAM roles or resource policies** check box.<br />5. Search for and select **AthenaDynamoDBConnector**, and ensure that the author listed is **Amazon Athena Federation**.<br />6. In **Application Settings**, enter the following values:**SpillBucket** ‒ Location that the function can spill data to.**AthenaCatalogName** ‒ The name of the Lambda function that will be created. The name will also be used as the **Data Source Name** in Athena.<br />7. Select the check box to acknowledge the creation of IAM roles and policies.<br />8. Choose **Deploy**. | AWS DevOps |
| Create a data source for Athena. | To create the data source, do the following:1. Open the Athena console at <br />https://console.aws.amazon.com/athena/.<br />2. Expand the navigation pane, and choose **Data sources**.<br />3. Choose **Create data source**.<br />4. Choose **Amazon DynamoDB**.<br />5. Enter the **Data Source Name**.<br />6. Select the Lambda function that you created.<br />7. Review the details, and choose **Create data source**. | AWS DevOps |
| Use Athena to query the DynamoDB table. | To query the DynamoDB table, do the following:1. On the Athena console, expand the navigation pane, and choose **Query editor**.<br />2. On the **Data source** dropdown list, choose the data source that you created.<br />3. Confirm that the DynamoDB tables are listed under **Tables**.<br />4. Run the query. | App developer |

## Troubleshooting
<a name="query-amazon-dynamodb-tables-sql-amazon-athena-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Query fails with `GENERIC_INTERNAL_ERROR: The bucket is in this region: <region>`*.* | Make sure that the Athena spill bucket and Lambda function are created in the same AWS Region. |
| The newly created data source isn't visible on the Athena console. | Athena data catalogs are regional. Ensure the `AthenaDynamoDBConnector` has been deployed in the Region where you are trying to use Athena. |
| You're unable to run the query against the newly created data source. | Check that the **Query Result Location** has been set. |

## Related resources
<a name="query-amazon-dynamodb-tables-sql-amazon-athena-resources"></a>
+ [Amazon Athena DynamoDB Connector](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-dynamodb)
+ [Amazon Athena Federated Query](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
