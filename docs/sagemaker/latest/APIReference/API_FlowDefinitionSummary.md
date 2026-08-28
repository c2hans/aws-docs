---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FlowDefinitionSummary.html
---

# FlowDefinitionSummary
<a name="API_FlowDefinitionSummary"></a>

Contains summary information about the flow definition.

## Contents
<a name="API_FlowDefinitionSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-FlowDefinitionSummary-CreationTime"></a>
The timestamp when SageMaker created the flow definition.
Type: Timestamp
Required: Yes

 ** FlowDefinitionArn **   <a name="sagemaker-Type-FlowDefinitionSummary-FlowDefinitionArn"></a>
The Amazon Resource Name (ARN) of the flow definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:flow-definition/.*`
Required: Yes

 ** FlowDefinitionName **   <a name="sagemaker-Type-FlowDefinitionSummary-FlowDefinitionName"></a>
The name of the flow definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9](-*[a-z0-9]){0,62}`
Required: Yes

 ** FlowDefinitionStatus **   <a name="sagemaker-Type-FlowDefinitionSummary-FlowDefinitionStatus"></a>
The status of the flow definition. Valid values:
Type: String
Valid Values: `Initializing | Active | Failed | Deleting`
Required: Yes

 ** FailureReason **   <a name="sagemaker-Type-FlowDefinitionSummary-FailureReason"></a>
The reason why the flow definition creation failed. A failure reason is returned only when the flow definition status is `Failed`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_FlowDefinitionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/FlowDefinitionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/FlowDefinitionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/FlowDefinitionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
