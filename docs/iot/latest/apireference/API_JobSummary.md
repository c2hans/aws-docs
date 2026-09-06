---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_JobSummary.html
---

# JobSummary
<a name="API_JobSummary"></a>

The job summary.

## Contents
<a name="API_JobSummary_Contents"></a>

 ** completedAt **   <a name="iot-Type-JobSummary-completedAt"></a>
The time, in seconds since the epoch, when the job completed.
Type: Timestamp
Required: No

 ** createdAt **   <a name="iot-Type-JobSummary-createdAt"></a>
The time, in seconds since the epoch, when the job was created.
Type: Timestamp
Required: No

 ** isConcurrent **   <a name="iot-Type-JobSummary-isConcurrent"></a>
Indicates whether a job is concurrent. Will be true when a job is rolling out new job executions or canceling previously created executions, otherwise false.
Type: Boolean
Required: No

 ** jobArn **   <a name="iot-Type-JobSummary-jobArn"></a>
The job ARN.
Type: String
Required: No

 ** jobId **   <a name="iot-Type-JobSummary-jobId"></a>
The unique identifier you assigned to this job when it was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** lastUpdatedAt **   <a name="iot-Type-JobSummary-lastUpdatedAt"></a>
The time, in seconds since the epoch, when the job was last updated.
Type: Timestamp
Required: No

 ** status **   <a name="iot-Type-JobSummary-status"></a>
The job summary status.
Type: String
Valid Values: `IN_PROGRESS | CANCELED | COMPLETED | DELETION_IN_PROGRESS | SCHEDULED`
Required: No

 ** targetSelection **   <a name="iot-Type-JobSummary-targetSelection"></a>
Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.
We recommend that you use continuous jobs instead of snapshot jobs for dynamic thing group targets. By using continuous jobs, devices that join the group receive the job execution even after the job has been created.
Type: String
Valid Values: `CONTINUOUS | SNAPSHOT`
Required: No

 ** thingGroupId **   <a name="iot-Type-JobSummary-thingGroupId"></a>
The ID of the thing group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

## See Also
<a name="API_JobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/JobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/JobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/JobSummary)
