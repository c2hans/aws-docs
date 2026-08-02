---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Import.html
---

# Import
<a name="API_Import"></a>

An import job to move data from CloudTrail Event Data Store to CloudWatch.

## Contents
<a name="API_Import_Contents"></a>

 ** creationTime **   <a name="CWL-Type-Import-creationTime"></a>
The timestamp when the import task was created, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** errorMessage **   <a name="CWL-Type-Import-errorMessage"></a>
Error message related to any failed imports
Type: String
Required: No

 ** importDestinationArn **   <a name="CWL-Type-Import-importDestinationArn"></a>
The ARN of the managed CloudWatch Logs log group where the events are being imported to.
Type: String
Required: No

 ** importFilter **   <a name="CWL-Type-Import-importFilter"></a>
The filter criteria used for this import task.
Type: [ImportFilter](API_ImportFilter.md) object
Required: No

 ** importId **   <a name="CWL-Type-Import-importId"></a>
The unique identifier of the import task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\-a-zA-Z0-9]+`
Required: No

 ** importSourceArn **   <a name="CWL-Type-Import-importSourceArn"></a>
The ARN of the CloudTrail Lake Event Data Store being imported from.
Type: String
Required: No

 ** importStatistics **   <a name="CWL-Type-Import-importStatistics"></a>
Statistics about the import progress
Type: [ImportStatistics](API_ImportStatistics.md) object
Required: No

 ** importStatus **   <a name="CWL-Type-Import-importStatus"></a>
The current status of the import task. Valid values are IN\_PROGRESS, CANCELLED, COMPLETED and FAILED.
Type: String
Valid Values: `IN_PROGRESS | CANCELLED | COMPLETED | FAILED`
Required: No

 ** lastUpdatedTime **   <a name="CWL-Type-Import-lastUpdatedTime"></a>
The timestamp when the import task was last updated, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_Import_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/Import)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/Import)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/Import)
