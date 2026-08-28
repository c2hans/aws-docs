---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelVariantConfigSummary.html
---

# ModelVariantConfigSummary
<a name="API_ModelVariantConfigSummary"></a>

Summary of the deployment configuration of a model.

## Contents
<a name="API_ModelVariantConfigSummary_Contents"></a>

 ** InfrastructureConfig **   <a name="sagemaker-Type-ModelVariantConfigSummary-InfrastructureConfig"></a>
The configuration of the infrastructure that the model has been deployed to.
Type: [ModelInfrastructureConfig](API_ModelInfrastructureConfig.md) object
Required: Yes

 ** ModelName **   <a name="sagemaker-Type-ModelVariantConfigSummary-ModelName"></a>
The name of the Amazon SageMaker Model entity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

 ** Status **   <a name="sagemaker-Type-ModelVariantConfigSummary-Status"></a>
The status of deployment for the model variant on the hosted inference endpoint.
+  `Creating` - Amazon SageMaker is preparing the model variant on the hosted inference endpoint.
+  `InService` - The model variant is running on the hosted inference endpoint.
+  `Updating` - Amazon SageMaker is updating the model variant on the hosted inference endpoint.
+  `Deleting` - Amazon SageMaker is deleting the model variant on the hosted inference endpoint.
+  `Deleted` - The model variant has been deleted on the hosted inference endpoint. This can only happen after stopping the experiment.
Type: String
Valid Values: `Creating | Updating | InService | Deleting | Deleted`
Required: Yes

 ** VariantName **   <a name="sagemaker-Type-ModelVariantConfigSummary-VariantName"></a>
The name of the variant.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

## See Also
<a name="API_ModelVariantConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelVariantConfigSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelVariantConfigSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelVariantConfigSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
