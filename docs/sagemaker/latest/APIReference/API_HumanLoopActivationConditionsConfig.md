---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HumanLoopActivationConditionsConfig.html
---

# HumanLoopActivationConditionsConfig
<a name="API_HumanLoopActivationConditionsConfig"></a>

Defines under what conditions SageMaker creates a human loop. Used within [CreateFlowDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateFlowDefinition.html). See [HumanLoopActivationConditionsConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HumanLoopActivationConditionsConfig.html) for the required format of activation conditions.

## Contents
<a name="API_HumanLoopActivationConditionsConfig_Contents"></a>

 ** HumanLoopActivationConditions **   <a name="sagemaker-Type-HumanLoopActivationConditionsConfig-HumanLoopActivationConditions"></a>
JSON expressing use-case specific conditions declaratively. If any condition is matched, atomic tasks are created against the configured work team. The set of conditions is different for Rekognition and Textract. For more information about how to structure the JSON, see [JSON Schema for Human Loop Activation Conditions in Amazon Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-human-fallback-conditions-json-schema.html) in the *Amazon SageMaker Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Required: Yes

## See Also
<a name="API_HumanLoopActivationConditionsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HumanLoopActivationConditionsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HumanLoopActivationConditionsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HumanLoopActivationConditionsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
