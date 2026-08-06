---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ImportSummary.html
---

# ImportSummary
<a name="API_ImportSummary"></a>

 Summary information about the source file for the import.

## Contents
<a name="API_ImportSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CloudWatchLogGroupArn **   <a name="DDB-Type-ImportSummary-CloudWatchLogGroupArn"></a>
 The Amazon Resource Number (ARN) of the Cloudwatch Log Group associated with this import task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** EndTime **   <a name="DDB-Type-ImportSummary-EndTime"></a>
 The time at which this import task ended.
Type: Timestamp
Required: No

 ** ImportArn **   <a name="DDB-Type-ImportSummary-ImportArn"></a>
 The Amazon Resource Number (ARN) corresponding to the import request.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: No

 ** ImportStatus **   <a name="DDB-Type-ImportSummary-ImportStatus"></a>
 The status of the import operation.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | CANCELLING | CANCELLED | FAILED`
Required: No

 ** InputFormat **   <a name="DDB-Type-ImportSummary-InputFormat"></a>
 The format of the source data. Valid values are `CSV`, `DYNAMODB_JSON` or `ION`.
Type: String
Valid Values: `DYNAMODB_JSON | ION | CSV`
Required: No

 ** S3BucketSource **   <a name="DDB-Type-ImportSummary-S3BucketSource"></a>
 The path and S3 bucket of the source file that is being imported. This includes the S3Bucket (required), S3KeyPrefix (optional) and S3BucketOwner (optional if the bucket is owned by the requester).
Type: [S3BucketSource](API_S3BucketSource.md) object
Required: No

 ** StartTime **   <a name="DDB-Type-ImportSummary-StartTime"></a>
 The time at which this import task began.
Type: Timestamp
Required: No

 ** TableArn **   <a name="DDB-Type-ImportSummary-TableArn"></a>
 The Amazon Resource Number (ARN) of the table being imported into.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ImportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ImportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ImportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ImportSummary)
