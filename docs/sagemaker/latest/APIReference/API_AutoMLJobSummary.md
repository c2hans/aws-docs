---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobSummary.html
---

# AutoMLJobSummary
<a name="API_AutoMLJobSummary"></a>

Provides a summary about an AutoML job.

## Contents
<a name="API_AutoMLJobSummary_Contents"></a>

 ** AutoMLJobArn **   <a name="sagemaker-Type-AutoMLJobSummary-AutoMLJobArn"></a>
The ARN of the AutoML job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:automl-job/.*`
Required: Yes

 ** AutoMLJobName **   <a name="sagemaker-Type-AutoMLJobSummary-AutoMLJobName"></a>
The name of the AutoML job you are requesting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

 ** AutoMLJobSecondaryStatus **   <a name="sagemaker-Type-AutoMLJobSummary-AutoMLJobSecondaryStatus"></a>
The secondary status of the AutoML job.
Type: String
Valid Values: `Starting | MaxCandidatesReached | Failed | Stopped | MaxAutoMLJobRuntimeReached | Stopping | CandidateDefinitionsGenerated | Completed | ExplainabilityError | DeployingModel | ModelDeploymentError | GeneratingModelInsightsReport | ModelInsightsError | AnalyzingData | FeatureEngineering | ModelTuning | GeneratingExplainabilityReport | TrainingModels | PreTraining`
Required: Yes

 ** AutoMLJobStatus **   <a name="sagemaker-Type-AutoMLJobSummary-AutoMLJobStatus"></a>
The status of the AutoML job.
Type: String
Valid Values: `Completed | InProgress | Failed | Stopped | Stopping`
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-AutoMLJobSummary-CreationTime"></a>
When the AutoML job was created.
Type: Timestamp
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-AutoMLJobSummary-LastModifiedTime"></a>
When the AutoML job was last modified.
Type: Timestamp
Required: Yes

 ** EndTime **   <a name="sagemaker-Type-AutoMLJobSummary-EndTime"></a>
The end time of an AutoML job.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="sagemaker-Type-AutoMLJobSummary-FailureReason"></a>
The failure reason of an AutoML job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** PartialFailureReasons **   <a name="sagemaker-Type-AutoMLJobSummary-PartialFailureReasons"></a>
The list of reasons for partial failures within an AutoML job.
Type: Array of [AutoMLPartialFailureReason](API_AutoMLPartialFailureReason.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_AutoMLJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
