---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_BatchLoadTaskDescription.html
---

# BatchLoadTaskDescription
<a name="API_BatchLoadTaskDescription"></a>

Details about a batch load task.

## Contents
<a name="API_BatchLoadTaskDescription_Contents"></a>

 ** CreationTime **   <a name="timestream-Type-BatchLoadTaskDescription-CreationTime"></a>
The time when the Timestream batch load task was created.
Type: Timestamp
Required: No

 ** DataModelConfiguration **   <a name="timestream-Type-BatchLoadTaskDescription-DataModelConfiguration"></a>
Data model configuration for a batch load task. This contains details about where a data model for a batch load task is stored.
Type: [DataModelConfiguration](API_DataModelConfiguration.md) object
Required: No

 ** DataSourceConfiguration **   <a name="timestream-Type-BatchLoadTaskDescription-DataSourceConfiguration"></a>
Configuration details about the data source for a batch load task.
Type: [DataSourceConfiguration](API_DataSourceConfiguration.md) object
Required: No

 ** ErrorMessage **   <a name="timestream-Type-BatchLoadTaskDescription-ErrorMessage"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** LastUpdatedTime **   <a name="timestream-Type-BatchLoadTaskDescription-LastUpdatedTime"></a>
The time when the Timestream batch load task was last updated.
Type: Timestamp
Required: No

 ** ProgressReport **   <a name="timestream-Type-BatchLoadTaskDescription-ProgressReport"></a>

Type: [BatchLoadProgressReport](API_BatchLoadProgressReport.md) object
Required: No

 ** RecordVersion **   <a name="timestream-Type-BatchLoadTaskDescription-RecordVersion"></a>

Type: Long
Required: No

 ** ReportConfiguration **   <a name="timestream-Type-BatchLoadTaskDescription-ReportConfiguration"></a>
Report configuration for a batch load task. This contains details about where error reports are stored.
Type: [ReportConfiguration](API_ReportConfiguration.md) object
Required: No

 ** ResumableUntil **   <a name="timestream-Type-BatchLoadTaskDescription-ResumableUntil"></a>

Type: Timestamp
Required: No

 ** TargetDatabaseName **   <a name="timestream-Type-BatchLoadTaskDescription-TargetDatabaseName"></a>

Type: String
Required: No

 ** TargetTableName **   <a name="timestream-Type-BatchLoadTaskDescription-TargetTableName"></a>

Type: String
Required: No

 ** TaskId **   <a name="timestream-Type-BatchLoadTaskDescription-TaskId"></a>
The ID of the batch load task.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[A-Z0-9]+`
Required: No

 ** TaskStatus **   <a name="timestream-Type-BatchLoadTaskDescription-TaskStatus"></a>
Status of the batch load task.
Type: String
Valid Values: `CREATED | IN_PROGRESS | FAILED | SUCCEEDED | PROGRESS_STOPPED | PENDING_RESUME`
Required: No

## See Also
<a name="API_BatchLoadTaskDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/BatchLoadTaskDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/BatchLoadTaskDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/BatchLoadTaskDescription)
