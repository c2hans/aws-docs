---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_JobSummary.html
---

# JobSummary
<a name="API_JobSummary"></a>

Provides summary information about a job, returned by the `ListJobs` operation. Use `DescribeJob` to get full details for a specific job.

## Contents
<a name="API_JobSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-JobSummary-CreationTime"></a>
The date and time that the job was created.
Type: Timestamp
Required: Yes

 ** JobArn **   <a name="sagemaker-Type-JobSummary-JobArn"></a>
The Amazon Resource Name (ARN) of the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:(aws[a-z\-]*):sagemaker:[a-z0-9\-]+:[0-9]{12}:job/[a-zA-Z0-9]+/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** JobCategory **   <a name="sagemaker-Type-JobSummary-JobCategory"></a>
The category of the job.
Type: String
Valid Values: `AgentRFT | AgentRFTEvaluation`
Required: Yes

 ** JobName **   <a name="sagemaker-Type-JobSummary-JobName"></a>
The name of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** JobSecondaryStatus **   <a name="sagemaker-Type-JobSummary-JobSecondaryStatus"></a>
The secondary status of the job, providing more granular information about the job's progress. Secondary statuses may change between releases.
Type: String
Valid Values: `Starting | Downloading | Training | Uploading | Stopping | Stopped | MaxRuntimeExceeded | Interrupted | Failed | Completed | Restarting | Pending | Evaluating | Deleting | DeleteFailed`
Required: Yes

 ** JobStatus **   <a name="sagemaker-Type-JobSummary-JobStatus"></a>
The current status of the job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting | DeleteFailed`
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-JobSummary-LastModifiedTime"></a>
The date and time that the job was last modified.
Type: Timestamp
Required: Yes

 ** EndTime **   <a name="sagemaker-Type-JobSummary-EndTime"></a>
The date and time that the job ended.
Type: Timestamp
Required: No

## See Also
<a name="API_JobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/JobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/JobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/JobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
