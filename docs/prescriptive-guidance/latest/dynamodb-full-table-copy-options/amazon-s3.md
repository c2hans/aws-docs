---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/amazon-s3.html
---

# Using DynamoDB with Amazon S3 to export and import table data
<a name="amazon-s3"></a>

Amazon DynamoDB supports exporting table data to Amazon S3 using the Export to S3 feature. You can export data in DynamoDB JSON and Amazon Ion formats. Exported data is compressed and can be encrypted by using an Amazon S3 key or an AWS Key Management Service (AWS KMS) key. Exporting a table does not consume read capacity on the table, and it has no impact on table performance and availability during the export. You can export to an S3 bucket within the account or to a different account, even in a different AWS Region. Point-in-time recovery (PITR) should be activated on the source table before you perform an export to Amazon S3.

Amazon DynamoDB recently added support to import table data directly from Amazon S3 by using the Import from S3 feature. Previously, after you exported table data using Export to S3, you had to rely on extract, transform, and load (ETL) tools to parse the table data in the S3 bucket, infer the schema, and load or copy to the target DynamoDB table. This was a cumbersome process and didn't provide flexibility when table data structure changed over time. Also, the use of ETL tools such as AWS Glue incurred additional charges for infrastructure and for write capacity consumed during the import.

The Import from S3 feature doesn't consume write capacity on the target table, and it supports different data formats, including DynamoDB JSON, Amazon Ion, and comma-separated values (CSV). Data can also be in uncompressed or compressed (gzip or zstd) format.

You can perform import and export by using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the DynamoDB API.

The following diagram shows the data moving from DynamoDB in the source account to an S3 bucket in the target account and then to the target account's DynamoDB instance.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/images/guide-img/b39c4f99-8119-4c72-9813-d6420f64f36c/images/fdae5ba6-f050-4e24-be45-5b81bea9135a.png)

At a high level, the following steps are required to export and import DynamoDB table from one account to another using Amazon S3:

1. Create an S3 bucket in the target account and attach the S3 bucket policy to allow access from the source account.

1. In the source account, on the DynamoDB console, choose **Export to S3**, select the source DynamoDB table, and specify the S3 bucket in the target account. For more information, see the [DynamoDB documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataExport_Requesting.html).

1. In the target account, on the DynamoDB console, choose **Import from S3**, and specify the S3 bucket in the target account. For more information, see the [DynamoDB documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataImport.Requesting.html).

## Advantages
<a name="advantages.73f6b537-3ab3-58bd-a076-41a4b06b3db3"></a>
+ It's a serverless solution.
+ The solution works for large datasets, up to terabytes.
+ It doesn't consume any provisioned capacity on the source and destination tables.
+ There is no impact on the performance or availability of the source table.

## Drawbacks
<a name="drawbacks.0137f024-5171-551c-9dee-695a26bccf43"></a>
+ Import into existing tables is not currently supported by this feature. The import process creates a new table.
