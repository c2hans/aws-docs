---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DesiredWeightAndCapacity.html
---

# DesiredWeightAndCapacity
<a name="API_DesiredWeightAndCapacity"></a>

Specifies weight and capacity values for a production variant.

## Contents
<a name="API_DesiredWeightAndCapacity_Contents"></a>

 ** VariantName **   <a name="sagemaker-Type-DesiredWeightAndCapacity-VariantName"></a>
The name of the variant to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** DesiredInstanceCount **   <a name="sagemaker-Type-DesiredWeightAndCapacity-DesiredInstanceCount"></a>
The variant's capacity.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** DesiredWeight **   <a name="sagemaker-Type-DesiredWeightAndCapacity-DesiredWeight"></a>
The variant's weight.
Type: Float
Valid Range: Minimum value of 0.
Required: No

 ** ServerlessUpdateConfig **   <a name="sagemaker-Type-DesiredWeightAndCapacity-ServerlessUpdateConfig"></a>
Specifies the serverless update concurrency configuration for an endpoint variant.
Type: [ProductionVariantServerlessUpdateConfig](API_ProductionVariantServerlessUpdateConfig.md) object
Required: No

## See Also
<a name="API_DesiredWeightAndCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DesiredWeightAndCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DesiredWeightAndCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DesiredWeightAndCapacity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
