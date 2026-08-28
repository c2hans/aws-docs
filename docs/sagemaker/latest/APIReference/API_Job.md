---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Job.html
---

# Job
<a name="API_Job"></a>

The properties of a job returned by the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

## Contents
<a name="API_Job_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-Job-CreationTime"></a>
The date and time that the job was created.
Type: Timestamp
Required: No

 ** EndTime **   <a name="sagemaker-Type-Job-EndTime"></a>
The date and time that the job ended.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="sagemaker-Type-Job-FailureReason"></a>
If the job failed, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** JobArn **   <a name="sagemaker-Type-Job-JobArn"></a>
The Amazon Resource Name (ARN) of the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:(aws[a-z\-]*):sagemaker:[a-z0-9\-]+:[0-9]{12}:job/[a-zA-Z0-9]+/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** JobCategory **   <a name="sagemaker-Type-Job-JobCategory"></a>
The category of the job.
Type: String
Valid Values: `AgentRFT | AgentRFTEvaluation`
Required: No

 ** JobConfigDocument **   <a name="sagemaker-Type-Job-JobConfigDocument"></a>
The JSON configuration document for the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: No

 ** JobConfigSchemaVersion **   <a name="sagemaker-Type-Job-JobConfigSchemaVersion"></a>
The schema version used for the job configuration document.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 16.
Pattern: `\d+\.\d+\.\d+`
Required: No

 ** JobName **   <a name="sagemaker-Type-Job-JobName"></a>
The name of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** JobStatus **   <a name="sagemaker-Type-Job-JobStatus"></a>
The current status of the job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting | DeleteFailed`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-Job-LastModifiedTime"></a>
The date and time that the job was last modified.
Type: Timestamp
Required: No

 ** RoleArn **   <a name="sagemaker-Type-Job-RoleArn"></a>
The ARN of the IAM role associated with the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** SecondaryStatus **   <a name="sagemaker-Type-Job-SecondaryStatus"></a>
The detailed secondary status of the job, providing more granular information about the job's progress.
Type: String
Valid Values: `Starting | Downloading | Training | Uploading | Stopping | Stopped | MaxRuntimeExceeded | Interrupted | Failed | Completed | Restarting | Pending | Evaluating | Deleting | DeleteFailed`
Required: No

 ** SecondaryStatusTransitions **   <a name="sagemaker-Type-Job-SecondaryStatusTransitions"></a>
A list of secondary status transitions for the job, with timestamps and optional status messages.
Type: Array of [JobSecondaryStatusTransition](API_JobSecondaryStatusTransition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Tags **   <a name="sagemaker-Type-Job-Tags"></a>
The tags associated with the job.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_Job_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Job)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Job)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Job)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
