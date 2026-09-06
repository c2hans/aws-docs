---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ImportBatch.html
---

# ImportBatch
<a name="API_ImportBatch"></a>

A collection of events being imported to CloudWatch

## Contents
<a name="API_ImportBatch_Contents"></a>

 ** batchId **   <a name="CWL-Type-ImportBatch-batchId"></a>
The unique identifier of the import batch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** status **   <a name="CWL-Type-ImportBatch-status"></a>
The current status of the import batch. Valid values are IN\_PROGRESS, CANCELLED, COMPLETED and FAILED.
Type: String
Valid Values: `IN_PROGRESS | CANCELLED | COMPLETED | FAILED`
Required: Yes

 ** errorMessage **   <a name="CWL-Type-ImportBatch-errorMessage"></a>
The error message if the batch failed to import. Only present when status is FAILED.
Type: String
Required: No

## See Also
<a name="API_ImportBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ImportBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ImportBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ImportBatch)
