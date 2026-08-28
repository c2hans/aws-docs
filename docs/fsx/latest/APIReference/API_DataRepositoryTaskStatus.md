---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_DataRepositoryTaskStatus.html
---

# DataRepositoryTaskStatus
<a name="API_DataRepositoryTaskStatus"></a>

Provides the task status showing a running total of the total number of files to be processed, the number successfully processed, and the number of files the task failed to process.

## Contents
<a name="API_DataRepositoryTaskStatus_Contents"></a>

 ** FailedCount **   <a name="FSx-Type-DataRepositoryTaskStatus-FailedCount"></a>
A running total of the number of files that the task failed to process.
Type: Long
Required: No

 ** LastUpdatedTime **   <a name="FSx-Type-DataRepositoryTaskStatus-LastUpdatedTime"></a>
The time at which the task status was last updated.
Type: Timestamp
Required: No

 ** ReleasedCapacity **   <a name="FSx-Type-DataRepositoryTaskStatus-ReleasedCapacity"></a>
The total amount of data, in GiB, released by an Amazon File Cache AUTO\_RELEASE\_DATA task that automatically releases files from the cache.
Type: Long
Required: No

 ** SucceededCount **   <a name="FSx-Type-DataRepositoryTaskStatus-SucceededCount"></a>
A running total of the number of files that the task has successfully processed.
Type: Long
Required: No

 ** TotalCount **   <a name="FSx-Type-DataRepositoryTaskStatus-TotalCount"></a>
The total number of files that the task will process. While a task is executing, the sum of `SucceededCount` plus `FailedCount` may not equal `TotalCount`. When the task is complete, `TotalCount` equals the sum of `SucceededCount` plus `FailedCount`.
Type: Long
Required: No

## See Also
<a name="API_DataRepositoryTaskStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DataRepositoryTaskStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DataRepositoryTaskStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DataRepositoryTaskStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
