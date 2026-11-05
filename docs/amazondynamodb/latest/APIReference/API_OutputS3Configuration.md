---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OutputS3Configuration.html
---

# OutputS3Configuration
<a name="API_OutputS3Configuration"></a>

Contains the Amazon S3 location, encryption settings, and output types for a bulk operation. The `S3Bucket` and `OutputType` fields are required.

## Contents
<a name="API_OutputS3Configuration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** OutputType **   <a name="DDB-Type-OutputS3Configuration-OutputType"></a>
The following values describe the types of output that DynamoDB writes for individual input items. Include one or both values.
 `ERROR`
Reports input records or input objects that DynamoDB couldn't process. This includes malformed input and item validation failures, such as a missing or incorrectly typed primary key attribute or an item that exceeds a DynamoDB limit.
 `CONDITION_CHECK_FAILURE`
Reports the attempted item and, when present, the existing item for a write whose condition expression evaluates to false.
Type: Array of strings
Valid Values: `ERROR | CONDITION_CHECK_FAILURE`
Required: Yes

 ** S3Bucket **   <a name="DDB-Type-OutputS3Configuration-S3Bucket"></a>
The name of the Amazon S3 bucket where DynamoDB writes output records.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[a-z0-9A-Z]+[\.\-\w]*[a-z0-9A-Z]+$`
Required: No

 ** S3BucketOwner **   <a name="DDB-Type-OutputS3Configuration-S3BucketOwner"></a>
The AWS account ID of the output bucket owner. If you omit this value, DynamoDB uses the AWS account ID of the requester.
 `S3BucketOwner` is required when the bucket is owned by another AWS account.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** S3KeyPrefix **   <a name="DDB-Type-OutputS3Configuration-S3KeyPrefix"></a>
An optional key prefix under which DynamoDB writes the output records.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** S3SseAlgorithm **   <a name="DDB-Type-OutputS3Configuration-S3SseAlgorithm"></a>
The server-side encryption algorithm for the output objects. Valid values are `AES256` and `KMS`. If you don't specify a value, Amazon S3 applies the destination bucket's default encryption settings.
Type: String
Valid Values: `AES256 | KMS`
Required: No

 ** S3SseKmsKeyId **   <a name="DDB-Type-OutputS3Configuration-S3SseKmsKeyId"></a>
The identifier of the AWS KMS key that encrypts the output objects. Specify this value when `S3SseAlgorithm` is `KMS`. Don't specify it when the algorithm is `AES256`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_OutputS3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/OutputS3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/OutputS3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/OutputS3Configuration)
