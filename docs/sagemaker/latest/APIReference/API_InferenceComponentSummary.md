---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentSummary.html
---

# InferenceComponentSummary
<a name="API_InferenceComponentSummary"></a>

A summary of the properties of an inference component.

## Contents
<a name="API_InferenceComponentSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-InferenceComponentSummary-CreationTime"></a>
The time when the inference component was created.
Type: Timestamp
Required: Yes

 ** EndpointArn **   <a name="sagemaker-Type-InferenceComponentSummary-EndpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint that hosts the inference component.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/.*`
Required: Yes

 ** EndpointName **   <a name="sagemaker-Type-InferenceComponentSummary-EndpointName"></a>
The name of the endpoint that hosts the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** InferenceComponentArn **   <a name="sagemaker-Type-InferenceComponentSummary-InferenceComponentArn"></a>
The Amazon Resource Name (ARN) of the inference component.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** InferenceComponentName **   <a name="sagemaker-Type-InferenceComponentSummary-InferenceComponentName"></a>
The name of the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-InferenceComponentSummary-LastModifiedTime"></a>
The time when the inference component was last updated.
Type: Timestamp
Required: Yes

 ** VariantName **   <a name="sagemaker-Type-InferenceComponentSummary-VariantName"></a>
The name of the production variant that hosts the inference component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** InferenceComponentStatus **   <a name="sagemaker-Type-InferenceComponentSummary-InferenceComponentStatus"></a>
The status of the inference component.
Type: String
Valid Values: `InService | Creating | Updating | Failed | Deleting`
Required: No

## See Also
<a name="API_InferenceComponentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
