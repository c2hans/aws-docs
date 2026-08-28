---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DDBELTConnectionOptions.html
---

# DDBELTConnectionOptions
<a name="API_DDBELTConnectionOptions"></a>

Specifies connection options for DynamoDB ELT (Extract, Load, Transform) operations. This structure contains configuration parameters for connecting to and extracting data from DynamoDB tables using the ELT connector.

## Contents
<a name="API_DDBELTConnectionOptions_Contents"></a>

 ** DynamodbTableArn **   <a name="Glue-Type-DDBELTConnectionOptions-DynamodbTableArn"></a>
The Amazon Resource Name (ARN) of the DynamoDB table to extract data from. This parameter specifies the source table for the ELT operation.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** DynamodbExport **   <a name="Glue-Type-DDBELTConnectionOptions-DynamodbExport"></a>
Specifies the export type for DynamoDB data extraction. This parameter determines how data is exported from the DynamoDB table during the ELT process.
Type: String
Valid Values: `ddb | s3`
Required: No

 ** DynamodbS3Bucket **   <a name="Glue-Type-DDBELTConnectionOptions-DynamodbS3Bucket"></a>
The name of the Amazon S3 bucket used for intermediate storage during the DynamoDB ELT process. This bucket is used to temporarily store exported DynamoDB data before it is processed by the ELT job.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** DynamodbS3BucketOwner **   <a name="Glue-Type-DDBELTConnectionOptions-DynamodbS3BucketOwner"></a>
The AWS account ID of the owner of the S3 bucket specified in `DynamodbS3Bucket`. This parameter is required when the S3 bucket is owned by a different AWS account than the one running the ELT job, enabling cross-account access to the intermediate storage bucket.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** DynamodbS3Prefix **   <a name="Glue-Type-DDBELTConnectionOptions-DynamodbS3Prefix"></a>
The S3 object key prefix for files stored in the intermediate S3 bucket during the DynamoDB ELT process. This prefix helps organize and identify the temporary files created during data extraction.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** DynamodbStsRoleArn **   <a name="Glue-Type-DDBELTConnectionOptions-DynamodbStsRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Security Token Service (STS) role to assume for accessing DynamoDB and S3 resources during the ELT operation. This role must have the necessary permissions to read from the DynamoDB table and write to the intermediate S3 bucket.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** DynamodbUnnestDDBJson **   <a name="Glue-Type-DDBELTConnectionOptions-DynamodbUnnestDDBJson"></a>
A boolean value that specifies whether to unnest DynamoDB JSON format during data extraction. When set to `true`, the connector will flatten nested JSON structures from DynamoDB items. When set to `false`, the original DynamoDB JSON structure is preserved.
Type: Boolean
Required: No

## See Also
<a name="API_DDBELTConnectionOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DDBELTConnectionOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DDBELTConnectionOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DDBELTConnectionOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
