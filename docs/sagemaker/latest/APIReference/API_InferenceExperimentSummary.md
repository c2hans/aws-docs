---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceExperimentSummary.html
---

# InferenceExperimentSummary
<a name="API_InferenceExperimentSummary"></a>

Lists a summary of properties of an inference experiment.

## Contents
<a name="API_InferenceExperimentSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-InferenceExperimentSummary-CreationTime"></a>
The timestamp at which the inference experiment was created.
Type: Timestamp
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-InferenceExperimentSummary-LastModifiedTime"></a>
The timestamp when you last modified the inference experiment.
Type: Timestamp
Required: Yes

 ** Name **   <a name="sagemaker-Type-InferenceExperimentSummary-Name"></a>
The name of the inference experiment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

 ** Status **   <a name="sagemaker-Type-InferenceExperimentSummary-Status"></a>
The status of the inference experiment.
Type: String
Valid Values: `Creating | Created | Updating | Running | Starting | Stopping | Completed | Cancelled`
Required: Yes

 ** Type **   <a name="sagemaker-Type-InferenceExperimentSummary-Type"></a>
The type of the inference experiment.
Type: String
Valid Values: `ShadowMode`
Required: Yes

 ** CompletionTime **   <a name="sagemaker-Type-InferenceExperimentSummary-CompletionTime"></a>
The timestamp at which the inference experiment was completed.
Type: Timestamp
Required: No

 ** Description **   <a name="sagemaker-Type-InferenceExperimentSummary-Description"></a>
The description of the inference experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** RoleArn **   <a name="sagemaker-Type-InferenceExperimentSummary-RoleArn"></a>
 The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** Schedule **   <a name="sagemaker-Type-InferenceExperimentSummary-Schedule"></a>
The duration for which the inference experiment ran or will run.
The maximum duration that you can set for an inference experiment is 30 days.
Type: [InferenceExperimentSchedule](API_InferenceExperimentSchedule.md) object
Required: No

 ** StatusReason **   <a name="sagemaker-Type-InferenceExperimentSummary-StatusReason"></a>
The error message for the inference experiment status result.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_InferenceExperimentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceExperimentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceExperimentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceExperimentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
