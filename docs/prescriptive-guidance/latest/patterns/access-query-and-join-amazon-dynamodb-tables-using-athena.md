---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-query-and-join-amazon-dynamodb-tables-using-athena.html
---

# Access, query, and join Amazon DynamoDB tables using Athena
<a name="access-query-and-join-amazon-dynamodb-tables-using-athena"></a>

*Moinul Al-Mamun, Amazon Web Services*

## Summary
<a name="access-query-and-join-amazon-dynamodb-tables-using-athena-summary"></a>

This pattern shows you how to set up a connection between Amazon Athena and Amazon DynamoDB by using the Amazon Athena DynamoDB connector. The connector uses an AWS Lambda function to query the data in DynamoDB. You don’t need to write any code to set up the connection. After the connection is established, you can quickly access and analyze DynamoDB tables by using [Athena Federated Query](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source.html) to run SQL commands from Athena. You can also join one or more DynamoDB tables to each other or to other data sources, such as Amazon Redshift or Amazon Aurora.

## Prerequisites and limitations
<a name="access-query-and-join-amazon-dynamodb-tables-using-athena-prereqs"></a>

**Prerequisites**
+ An active AWS account with permissions to manage DynamoDB tables, Athena Data sources, Lambda, and AWS Identity and Access Management (IAM) roles
+ An Amazon Simple Storage Service (Amazon S3) bucket where Athena can store query results
+ An S3 bucket where the Athena DynamoDB Connector can save the data in the short term
+ An AWS Region that supports [Athena engine version 2](https://docs.aws.amazon.com/athena/latest/ug/engine-versions-reference-0002.html)
+ IAM permissions to access Athena and the required S3 buckets
+ [Amazon Athena DynamoDB Connector](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-dynamodb), installed

**Limitations**

There is a cost for querying DynamoDB tables. Table sizes exceeding a few gigabytes (GBs) can incur a high cost. We recommend that you consider cost before performing any full table SCAN operation. For more information, see [Amazon DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/). To reduce costs and achieve high performance, we recommend that you always use LIMIT in your query (for example, `SELECT * FROM table1 LIMIT 10`). Also, before you perform a JOIN or GROUP BY query in a production environment, consider the size of your tables. If your tables are too large, consider alternative options such as [migrating the table to Amazon S3](https://aws.amazon.com/blogs/database/simplify-amazon-dynamodb-data-extraction-and-analysis-by-using-aws-glue-and-amazon-athena/).

## Architecture
<a name="access-query-and-join-amazon-dynamodb-tables-using-athena-architecture"></a>

The following diagram shows how a user can run a SQL query on a DynamoDB table from Athena.

![Workflow for connecting Athena and DynamoDB to run a SQL query.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e6ff94af-d208-40c7-94e4-af257755a603/images/bc8e0132-b578-463b-bf55-3c39ce359c17.png)

The diagram shows the following workflow:

1. To query a DynamoDB table, a user runs a SQL query from Athena.

1. Athena initiates a Lambda function.

1. The Lambda function queries the requested data in the DynamoDB table.

1. DynamoDB returns the requested data to the Lambda function. Then, the function transfers the query results to the user through Athena.

1. The Lambda function stores data in the S3 bucket.

**Technology stack**
+ Amazon Athena
+ Amazon DynamoDB
+ Amazon S3
+ AWS Lambda

## Tools
<a name="access-query-and-join-amazon-dynamodb-tables-using-athena-tools"></a>
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon S3 by using standard SQL.
+ [Amazon Athena DynamoDB Connector](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-dynamodb) is an AWS tool that enables Athena to connect with DynamoDB and access your tables by using SQL queries.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.

## Epics
<a name="access-query-and-join-amazon-dynamodb-tables-using-athena-epics"></a>

### Create sample DynamoDB tables
<a name="create-sample-dynamodb-tables"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the first sample table.  | 1. Sign in to the AWS Management Console and open the [DynamoDB console](https://console.aws.amazon.com/dynamodb/).<br />2. Choose **Create table**.<br />3. For **Table name**, enter **dydbtable1**.<br />4. For **Partition key**,** **enter **PK1**.<br />5. For **Sort key**, enter **SK1**.<br />6. In the **Table settings** section, choose **Customize settings**.<br />7. In the **Table class** section, choose **DynamoDB Standard**.<br />8. In the **Read/write capacity settings** section, for **Capacity mode**, choose **On-demand**.<br />9. In the **Encryption at rest** section, choose **Owned by Amazon DynamoDB**.<br />10. Choose **Create table**. | Developer |
| Insert sample data into the first table. | 1. Open the [DynamoDB console](https://console.aws.amazon.com/dynamodb/).<br />2. In the navigation pane, choose **Table**, and then choose your table in the **Name** column.<br />3. Choose **Actions**, and then choose **Create item**.<br />4. Choose **JSON view**.<br />5. In the title bar of the **Attributes** editor, turn off **View DynamoDB JSON**.<br />6. In the **Attributes** editor, enter the following sample data one by one:<pre>{<br />  "PK1": "1234",<br />  "SK1": "info",<br />  "Salary": "5000"<br /> }</pre><pre>{<br />  "PK1": "1235",<br />  "SK1": "info",<br />  "Salary": "5200"<br /> }</pre> | Developer |
| Create the second sample table.  | 1. Open the [DynamoDB console](https://console.aws.amazon.com/dynamodb/).<br />2. Choose **Create table**.<br />3. For **Table name**, enter **dydbtable2**.<br />4. For **Partition key**, enter **PK2**.<br />5. For **Sort key**, enter **SK2**.<br />6. In the **Table settings** section, choose **Customize settings**.<br />7. In the **Table class** section, choose **DynamoDB Standard**.<br />8. In the **Read/write capacity settings** section, for **Capacity mode**, choose **On-demand**.<br />9. In the **Encryption at rest** section, choose **Owned by Amazon DynamoDB**.<br />10. Choose **Create table**. | Developer |
| Insert sample data into the second table. | 1. Open the [DynamoDB console](https://console.aws.amazon.com/dynamodb/).<br />2. In the navigation pane, choose **Table**, and then choose your table in the **Name** column.<br />3. Choose **Actions**, and then choose **Create item**.<br />4. In the title bar of the **Attributes** editor, turn off **View DynamoDB JSON**.<br />5. In the **Attributes** editor, enter the following sample data one by one:<pre>{<br />  "PK2": "1234",<br /> "SK2": "bonus",<br /> "Bonus": "500"<br />}</pre><pre>{<br />  "PK2": "1235",<br /> "SK2": "bonus",<br /> "Bonus": "1000"<br />}</pre> | Developer |

### Create a data source in Athena for DynamoDB
<a name="create-a-data-source-in-athena-for-dynamodb"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the data source connector. | Create a data source for DynamoDB, and then create a Lambda function to connect to that data source.1. Sign in to the AWS Management Console and open the [Athena console](https://console.aws.amazon.com/athena/).<br />2. In the navigation pane, choose **Data sources**, and then choose **Create data source**.<br />3. Choose the **Amazon DynamoDB** data source, and then choose **Next**.<br />4. In the **Data source details** section, for **Data source name**, enter **testDynamoDB**.<br />5. In the **Connection details** section, select a Lambda function that’s already deployed or choose **Create Lambda function** if you don’t have a Lambda function to use for this pattern. **Note**: For more information on creating a Lambda function, see [Getting started with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) in the Lambda Developer Guide.<br />6. (Optional) If you choose **Create Lambda function**, then you must configure the AWS CloudFormation template that’s included by the Java application before deploying that stack. The template includes ApplicationName, SpillBucket, AthenaCatalogName, and other application settings. **Note**: After you deploy this Java-based application, the stack creates a Lambda function that enables Athena to communicate with DynamoDB. This makes your tables accessible through SQL commands.<br />7. Deploy your Lambda function.<br />8. Choose **Next**. | Developer |
| Verify that the Lambda function can access the S3 spill bucket. | 1. Open the [Lambda console](https://console.aws.amazon.com/lambda/).<br />2. In the navigation pane, choose **Functions**, and then choose the function that you created earlier.<br />3. Choose the **Configuration** tab.<br />4. In the left pane, choose **Environment variables**, and then confirm that the value for the key is `spill_bucket`.<br />5. In the left pane, choose **Permissions**, and then in the **Execution role** section, choose the attached IAM role. **Note**: You are directed to the IAM role that’s attached to your Lambda function in the IAM console.<br />6. Confirm that you have write permission on `spill_bucket` bucket.If you experience errors, see the *Additional information* section in this pattern for guidance. | Developer |

### Access DynamoDB tables from Athena
<a name="access-dynamodb-tables-from-athena"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Query the DynamoDB tables. | 1. Sign in to the AWS Management Console and open the [Athena console](https://console.aws.amazon.com/athena/).<br />2. In the navigation pane, choose **Data sources**, and then choose **Create data source**.<br />3. In the navigation pane, choose **Query editor**.<br />4. On the **Editor** tab, in the **Data** section, for **Data source**, choose your data source for **Data source**.<br />5. For **Database**, choose your database.<br />6. For Query 1, enter the following query: `SELECT * FROM dydbtable1 t1;`<br />7. Choose **Run**, and then verify the output in the table.<br />8. For Query 2, enter the following query: `SELECT * FROM dydbtable2 t2;`<br />9. Choose **Run**, and then verify the output in the table. | Developer |
| Join the two DynamoDB tables. | DynamoDB is a NoSQL data store and doesn’t support the SQL join operation. Consequently, you must perform a join operation on two DynamoDB tables:1. Choose the plus icon to create another query.<br />2. For Query 3, enter the following query:<pre>SELECT pk1, salary, bonus FROM dydbtable1 t1<br /> JOIN dydbtable2 t2 ON t1.pk1 = t2.pk2;</pre> | Developer |

## Related resources
<a name="access-query-and-join-amazon-dynamodb-tables-using-athena-resources"></a>
+ [Amazon Athena DynamoDB Connector](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-dynamodb) (AWS Labs)
+ [Query any data source with Amazon Athena’s new federated query](https://aws.amazon.com/blogs/big-data/query-any-data-source-with-amazon-athenas-new-federated-query/) (AWS Big Data Blog)
+ [Athena engine version reference](https://docs.aws.amazon.com/athena/latest/ug/engine-versions-reference.html) (Athena User Guide)
+ [Simplify Amazon DynamoDB data extraction and analysis by using AWS Glue and Amazon Athena](https://aws.amazon.com/blogs/database/simplify-amazon-dynamodb-data-extraction-and-analysis-by-using-aws-glue-and-amazon-athena/) (AWS Database Blog)

## Additional information
<a name="access-query-and-join-amazon-dynamodb-tables-using-athena-additional"></a>

If you run a query in Athena with `spill_bucket` in the `{bucket_name}/folder_name/` format, then you can receive the following error message:

```
"GENERIC_USER_ERROR: Encountered an exception[java.lang.RuntimeException] from your LambdaFunction[arn:aws:lambda:us-east-1:xxxxxx:function:testdynamodb] executed in context[retrieving meta-data] with message[You do NOT own the spill bucket with the name: s3://DOC-EXAMPLE-BUCKET/athena_dynamodb_spill_data/]
This query ran against the "default" database, unless qualified by the query. Please post the error message on our forum  or contact customer support with Query Id: [query-id]"
```

To resolve this error, update the Lambda function’s environment variable `spill_bucket` to `{bucket_name_only}`, and then update the following Lambda IAM policy for bucket write access:

```
{
             "Action": [
                 "s3:GetObject",
                 "s3:ListBucket",
                 "s3:GetBucketLocation",
                 "s3:GetObjectVersion",
                 "s3:PutObject",
                 "s3:PutObjectAcl",
                 "s3:GetLifecycleConfiguration",
                 "s3:PutLifecycleConfiguration",
                 "s3:DeleteObject"
            ],
             "Resource": [
                 "arn:aws:s3:::spill_bucket",
                 "arn:aws:s3:::spill_bucket/*"
            ],
             "Effect": "Allow"
        }
```

Alternatively, you can remove the Athena data source connector that you created earlier, and recreate it by using only `{bucket_name}` for `spill_bucket`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
