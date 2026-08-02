---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_AttemptDetail.html
---

# AttemptDetail
<a name="API_AttemptDetail"></a>

An object that represents a job attempt.

## Contents
<a name="API_AttemptDetail_Contents"></a>

 ** container **   <a name="Batch-Type-AttemptDetail-container"></a>
The details for the container in this job attempt.
Type: [AttemptContainerDetail](API_AttemptContainerDetail.md) object
Required: No

 ** startedAt **   <a name="Batch-Type-AttemptDetail-startedAt"></a>
The Unix timestamp (in milliseconds) for when the attempt was started (when the attempt transitioned from the `STARTING` state to the `RUNNING` state).
Type: Long
Required: No

 ** statusReason **   <a name="Batch-Type-AttemptDetail-statusReason"></a>
A short, human-readable string to provide additional details for the current status of the job attempt.
Type: String
Required: No

 ** stoppedAt **   <a name="Batch-Type-AttemptDetail-stoppedAt"></a>
The Unix timestamp (in milliseconds) for when the attempt was stopped (when the attempt transitioned from the `RUNNING` state to a terminal state, such as `SUCCEEDED` or `FAILED`).
Type: Long
Required: No

 ** taskProperties **   <a name="Batch-Type-AttemptDetail-taskProperties"></a>
The properties for a task definition that describes the container and volume definitions of an Amazon ECS task.
Type: Array of [AttemptEcsTaskDetails](API_AttemptEcsTaskDetails.md) objects
Required: No

## See Also
<a name="API_AttemptDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/AttemptDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/AttemptDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/AttemptDetail)
