---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelExplainabilityBaselineConfig.html
---

# ModelExplainabilityBaselineConfig
<a name="API_ModelExplainabilityBaselineConfig"></a>

The configuration for a baseline model explainability job.

## Contents
<a name="API_ModelExplainabilityBaselineConfig_Contents"></a>

 ** BaseliningJobName **   <a name="sagemaker-Type-ModelExplainabilityBaselineConfig-BaseliningJobName"></a>
The name of the baseline model explainability job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ConstraintsResource **   <a name="sagemaker-Type-ModelExplainabilityBaselineConfig-ConstraintsResource"></a>
The constraints resource for a monitoring job.
Type: [MonitoringConstraintsResource](API_MonitoringConstraintsResource.md) object
Required: No

## See Also
<a name="API_ModelExplainabilityBaselineConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelExplainabilityBaselineConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelExplainabilityBaselineConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelExplainabilityBaselineConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
