---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_InputS3Configuration.html
---

# InputS3Configuration
<a name="API_InputS3Configuration"></a>

Contains the Amazon S3 location and format settings for bulk operation input. The `S3Bucket` and `InputFormat` fields are required.

## Contents
<a name="API_InputS3Configuration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InputFormat **   <a name="DDB-Type-InputS3Configuration-InputFormat"></a>
The format of the input objects. `DYNAMODB_JSON` uses JSON Lines, with one JSON record per line. `ION` uses a sequence of Ion structs.
Type: String
Valid Values: `DYNAMODB_JSON | ION`
Required: Yes

 ** S3Bucket **   <a name="DDB-Type-InputS3Configuration-S3Bucket"></a>
The name of the Amazon S3 bucket that contains the input objects.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[a-z0-9A-Z]+[\.\-\w]*[a-z0-9A-Z]+$`
Required: Yes

 ** InputCompressionType **   <a name="DDB-Type-InputS3Configuration-InputCompressionType"></a>
The compression type of the input objects. Valid values are `GZIP`, `ZSTD`, and `NONE`. If you don't specify a value, DynamoDB uses `NONE`.
Type: String
Valid Values: `GZIP | ZSTD | NONE`
Required: No

 ** S3BucketOwner **   <a name="DDB-Type-InputS3Configuration-S3BucketOwner"></a>
The AWS account ID of the input bucket owner. If you omit this value, DynamoDB uses the AWS account ID of the requester.
 `S3BucketOwner` is required when the bucket is owned by another AWS account.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** S3KeyPrefix **   <a name="DDB-Type-InputS3Configuration-S3KeyPrefix"></a>
An optional key prefix that limits the input to matching objects in the Amazon S3 bucket.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_InputS3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/InputS3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/InputS3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/InputS3Configuration)
