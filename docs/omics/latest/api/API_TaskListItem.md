---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_TaskListItem.html
---

# TaskListItem
<a name="API_TaskListItem"></a>

A workflow run task.

## Contents
<a name="API_TaskListItem_Contents"></a>

 ** cacheHit **   <a name="omics-Type-TaskListItem-cacheHit"></a>
Set to true if AWS HealthOmics found a matching entry in the run cache for this task.
Type: Boolean
Required: No

 ** cacheS3Uri **   <a name="omics-Type-TaskListItem-cacheS3Uri"></a>
The S3 URI of the cache location.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])(/(.{0,1024}))?`
Required: No

 ** cpus **   <a name="omics-Type-TaskListItem-cpus"></a>
The task's CPU count.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** creationTime **   <a name="omics-Type-TaskListItem-creationTime"></a>
When the task was created.
Type: Timestamp
Required: No

 ** gpus **   <a name="omics-Type-TaskListItem-gpus"></a>
 The number of Graphics Processing Units (GPU) specified for the task.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** instanceType **   <a name="omics-Type-TaskListItem-instanceType"></a>
 The instance type for a task.
Type: String
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** memory **   <a name="omics-Type-TaskListItem-memory"></a>
The task's memory use in gigabyes.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** name **   <a name="omics-Type-TaskListItem-name"></a>
The task's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** startTime **   <a name="omics-Type-TaskListItem-startTime"></a>
When the task started.
Type: Timestamp
Required: No

 ** status **   <a name="omics-Type-TaskListItem-status"></a>
The task's status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PENDING | STARTING | RUNNING | STOPPING | COMPLETED | CANCELLED | FAILED`
Required: No

 ** stopTime **   <a name="omics-Type-TaskListItem-stopTime"></a>
When the task stopped.
Type: Timestamp
Required: No

 ** taskId **   <a name="omics-Type-TaskListItem-taskId"></a>
The task's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** uuid **   <a name="omics-Type-TaskListItem-uuid"></a>
The universally unique identifier (UUID) for the workflow task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## See Also
<a name="API_TaskListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/TaskListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/TaskListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/TaskListItem)
