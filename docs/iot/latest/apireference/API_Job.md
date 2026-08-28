---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_Job.html
---

# Job
<a name="API_Job"></a>

The `Job` object contains details about a job.

## Contents
<a name="API_Job_Contents"></a>

 ** abortConfig **   <a name="iot-Type-Job-abortConfig"></a>
Configuration for criteria to abort the job.
Type: [AbortConfig](API_AbortConfig.md) object
Required: No

 ** comment **   <a name="iot-Type-Job-comment"></a>
If the job was updated, describes the reason for the update.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** completedAt **   <a name="iot-Type-Job-completedAt"></a>
The time, in seconds since the epoch, when the job was completed.
Type: Timestamp
Required: No

 ** createdAt **   <a name="iot-Type-Job-createdAt"></a>
The time, in seconds since the epoch, when the job was created.
Type: Timestamp
Required: No

 ** description **   <a name="iot-Type-Job-description"></a>
A short text description of the job.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** destinationPackageVersions **   <a name="iot-Type-Job-destinationPackageVersions"></a>
The package version Amazon Resource Names (ARNs) that are installed on the device when the job successfully completes. The package version must be in either the Published or Deprecated state when the job deploys. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle).The package version must be in either the Published or Deprecated state when the job deploys. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle).
 **Note:**The following Length Constraints relates to a single ARN. Up to 25 package version ARNs are allowed.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`
Required: No

 ** documentParameters **   <a name="iot-Type-Job-documentParameters"></a>
A key-value map that pairs the patterns that need to be replaced in a managed template job document schema. You can use the description of each key as a guidance to specify the inputs during runtime when creating a job.
 `documentParameters` can only be used when creating jobs from AWS managed templates. This parameter can't be used with custom job templates or to create jobs from them.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_-]+`
Value Length Constraints: Minimum length of 1. Maximum length of 30720.
Value Pattern: `[^\p{C}]+`
Required: No

 ** forceCanceled **   <a name="iot-Type-Job-forceCanceled"></a>
Will be `true` if the job was canceled with the optional `force` parameter set to `true`.
Type: Boolean
Required: No

 ** isConcurrent **   <a name="iot-Type-Job-isConcurrent"></a>
Indicates whether a job is concurrent. Will be true when a job is rolling out new job executions or canceling previously created executions, otherwise false.
Type: Boolean
Required: No

 ** jobArn **   <a name="iot-Type-Job-jobArn"></a>
An ARN identifying the job with format "arn:aws:iot:region:account:job/jobId".
Type: String
Required: No

 ** jobExecutionsRetryConfig **   <a name="iot-Type-Job-jobExecutionsRetryConfig"></a>
The configuration for the criteria to retry the job.
Type: [JobExecutionsRetryConfig](API_JobExecutionsRetryConfig.md) object
Required: No

 ** jobExecutionsRolloutConfig **   <a name="iot-Type-Job-jobExecutionsRolloutConfig"></a>
Allows you to create a staged rollout of a job.
Type: [JobExecutionsRolloutConfig](API_JobExecutionsRolloutConfig.md) object
Required: No

 ** jobId **   <a name="iot-Type-Job-jobId"></a>
The unique identifier you assigned to this job when it was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** jobProcessDetails **   <a name="iot-Type-Job-jobProcessDetails"></a>
Details about the job process.
Type: [JobProcessDetails](API_JobProcessDetails.md) object
Required: No

 ** jobTemplateArn **   <a name="iot-Type-Job-jobTemplateArn"></a>
The ARN of the job template used to create the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`
Required: No

 ** lastUpdatedAt **   <a name="iot-Type-Job-lastUpdatedAt"></a>
The time, in seconds since the epoch, when the job was last updated.
Type: Timestamp
Required: No

 ** namespaceId **   <a name="iot-Type-Job-namespaceId"></a>
The namespace used to indicate that a job is a customer-managed job.
When you specify a value for this parameter, AWS IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.
 `$aws/things/THING_NAME/jobs/JOB_ID/notify-namespace-NAMESPACE_ID/`
The `namespaceId` feature is only supported by AWS IoT Greengrass at this time. For more information, see [Setting up AWS IoT Greengrass core devices.](https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html)
Type: String
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** presignedUrlConfig **   <a name="iot-Type-Job-presignedUrlConfig"></a>
Configuration for pre-signed S3 URLs.
Type: [PresignedUrlConfig](API_PresignedUrlConfig.md) object
Required: No

 ** reasonCode **   <a name="iot-Type-Job-reasonCode"></a>
If the job was updated, provides the reason code for the update.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\p{Upper}\p{Digit}_]+`
Required: No

 ** scheduledJobRollouts **   <a name="iot-Type-Job-scheduledJobRollouts"></a>
Displays the next seven maintenance window occurrences and their start times.
Type: Array of [ScheduledJobRollout](API_ScheduledJobRollout.md) objects
Required: No

 ** schedulingConfig **   <a name="iot-Type-Job-schedulingConfig"></a>
The configuration that allows you to schedule a job for a future date and time in addition to specifying the end behavior for each job execution.
Type: [SchedulingConfig](API_SchedulingConfig.md) object
Required: No

 ** status **   <a name="iot-Type-Job-status"></a>
The status of the job, one of `IN_PROGRESS`, `CANCELED`, `DELETION_IN_PROGRESS` or `COMPLETED`.
Type: String
Valid Values: `IN_PROGRESS | CANCELED | COMPLETED | DELETION_IN_PROGRESS | SCHEDULED`
Required: No

 ** targets **   <a name="iot-Type-Job-targets"></a>
A list of IoT things and thing groups to which the job should be sent.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Maximum length of 2048.
Required: No

 ** targetSelection **   <a name="iot-Type-Job-targetSelection"></a>
Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a device when the thing representing the device is added to a target group, even after the job was completed by all things originally in the group.
We recommend that you use continuous jobs instead of snapshot jobs for dynamic thing group targets. By using continuous jobs, devices that join the group receive the job execution even after the job has been created.
Type: String
Valid Values: `CONTINUOUS | SNAPSHOT`
Required: No

 ** timeoutConfig **   <a name="iot-Type-Job-timeoutConfig"></a>
Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to `IN_PROGRESS`. If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to `TIMED_OUT`.
Type: [TimeoutConfig](API_TimeoutConfig.md) object
Required: No

## See Also
<a name="API_Job_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/Job)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/Job)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/Job)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
