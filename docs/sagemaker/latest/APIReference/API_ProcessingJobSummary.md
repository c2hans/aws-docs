---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProcessingJobSummary.html
---

# ProcessingJobSummary
<a name="API_ProcessingJobSummary"></a>

Summary of information about a processing job.

## Contents
<a name="API_ProcessingJobSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-ProcessingJobSummary-CreationTime"></a>
The time at which the processing job was created.
Type: Timestamp
Required: Yes

 ** ProcessingJobArn **   <a name="sagemaker-Type-ProcessingJobSummary-ProcessingJobArn"></a>
The Amazon Resource Name (ARN) of the processing job..
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:processing-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ProcessingJobName **   <a name="sagemaker-Type-ProcessingJobSummary-ProcessingJobName"></a>
The name of the processing job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ProcessingJobStatus **   <a name="sagemaker-Type-ProcessingJobSummary-ProcessingJobStatus"></a>
The status of the processing job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`
Required: Yes

 ** ExitMessage **   <a name="sagemaker-Type-ProcessingJobSummary-ExitMessage"></a>
An optional string, up to one KB in size, that contains metadata from the processing container when the processing job exits.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** FailureReason **   <a name="sagemaker-Type-ProcessingJobSummary-FailureReason"></a>
A string, up to one KB in size, that contains the reason a processing job failed, if it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-ProcessingJobSummary-LastModifiedTime"></a>
A timestamp that indicates the last time the processing job was modified.
Type: Timestamp
Required: No

 ** ProcessingEndTime **   <a name="sagemaker-Type-ProcessingJobSummary-ProcessingEndTime"></a>
The time at which the processing job completed.
Type: Timestamp
Required: No

## See Also
<a name="API_ProcessingJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProcessingJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProcessingJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProcessingJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
