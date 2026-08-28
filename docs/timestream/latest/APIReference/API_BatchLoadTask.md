---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_BatchLoadTask.html
---

# BatchLoadTask
<a name="API_BatchLoadTask"></a>

Details about a batch load task.

## Contents
<a name="API_BatchLoadTask_Contents"></a>

 ** CreationTime **   <a name="timestream-Type-BatchLoadTask-CreationTime"></a>
The time when the Timestream batch load task was created.
Type: Timestamp
Required: No

 ** DatabaseName **   <a name="timestream-Type-BatchLoadTask-DatabaseName"></a>
Database name for the database into which a batch load task loads data.
Type: String
Required: No

 ** LastUpdatedTime **   <a name="timestream-Type-BatchLoadTask-LastUpdatedTime"></a>
The time when the Timestream batch load task was last updated.
Type: Timestamp
Required: No

 ** ResumableUntil **   <a name="timestream-Type-BatchLoadTask-ResumableUntil"></a>

Type: Timestamp
Required: No

 ** TableName **   <a name="timestream-Type-BatchLoadTask-TableName"></a>
Table name for the table into which a batch load task loads data.
Type: String
Required: No

 ** TaskId **   <a name="timestream-Type-BatchLoadTask-TaskId"></a>
The ID of the batch load task.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[A-Z0-9]+`
Required: No

 ** TaskStatus **   <a name="timestream-Type-BatchLoadTask-TaskStatus"></a>
Status of the batch load task.
Type: String
Valid Values: `CREATED | IN_PROGRESS | FAILED | SUCCEEDED | PROGRESS_STOPPED | PENDING_RESUME`
Required: No

## See Also
<a name="API_BatchLoadTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/BatchLoadTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/BatchLoadTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/BatchLoadTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
