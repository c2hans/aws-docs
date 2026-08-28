---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DynamoDBTarget.html
---

# DynamoDBTarget
<a name="API_DynamoDBTarget"></a>

Specifies an Amazon DynamoDB table to crawl.

## Contents
<a name="API_DynamoDBTarget_Contents"></a>

 ** Path **   <a name="Glue-Type-DynamoDBTarget-Path"></a>
The name of the DynamoDB table to crawl.
Type: String
Required: No

 ** scanAll **   <a name="Glue-Type-DynamoDBTarget-scanAll"></a>
Indicates whether to scan all the records, or to sample rows from the table. Scanning all the records can take a long time when the table is not a high throughput table.
A value of `true` means to scan all records, while a value of `false` means to sample the records. If no value is specified, the value defaults to `true`.
Type: Boolean
Required: No

 ** scanRate **   <a name="Glue-Type-DynamoDBTarget-scanRate"></a>
The percentage of the configured read capacity units to use by the AWS Glue crawler. Read capacity units is a term defined by DynamoDB, and is a numeric value that acts as rate limiter for the number of reads that can be performed on that table per second.
The valid values are null or a value between 0.1 to 1.5. A null value is used when user does not provide a value, and defaults to 0.5 of the configured Read Capacity Unit (for provisioned tables), or 0.25 of the max configured Read Capacity Unit (for tables using on-demand mode).
Type: Double
Required: No

## See Also
<a name="API_DynamoDBTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DynamoDBTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DynamoDBTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DynamoDBTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
