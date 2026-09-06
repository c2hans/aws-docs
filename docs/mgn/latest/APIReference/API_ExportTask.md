---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ExportTask.html
---

# ExportTask
<a name="API_ExportTask"></a>

Export task.

## Contents
<a name="API_ExportTask_Contents"></a>

 ** arn **   <a name="mgn-Type-ExportTask-arn"></a>
ExportTask arn.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** creationDateTime **   <a name="mgn-Type-ExportTask-creationDateTime"></a>
Export task creation datetime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** endDateTime **   <a name="mgn-Type-ExportTask-endDateTime"></a>
Export task end datetime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** exportID **   <a name="mgn-Type-ExportTask-exportID"></a>
Export task id.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `export-[0-9a-zA-Z]{17}`
Required: No

 ** progressPercentage **   <a name="mgn-Type-ExportTask-progressPercentage"></a>
Export task progress percentage.
Type: Float
Required: No

 ** s3Bucket **   <a name="mgn-Type-ExportTask-s3Bucket"></a>
Export task s3 bucket.
Type: String
Pattern: `[a-zA-Z0-9.\-_]{1,255}`
Required: No

 ** s3BucketOwner **   <a name="mgn-Type-ExportTask-s3BucketOwner"></a>
Export task s3 bucket owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** s3Key **   <a name="mgn-Type-ExportTask-s3Key"></a>
Export task s3 key.
Type: String
Pattern: `[^\x00]{1,1020}\.csv`
Required: No

 ** status **   <a name="mgn-Type-ExportTask-status"></a>
Export task status.
Type: String
Valid Values: `PENDING | STARTED | FAILED | SUCCEEDED`
Required: No

 ** summary **   <a name="mgn-Type-ExportTask-summary"></a>
Export task summary.
Type: [ExportTaskSummary](API_ExportTaskSummary.md) object
Required: No

 ** tags **   <a name="mgn-Type-ExportTask-tags"></a>
Export task tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_ExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ExportTask)
