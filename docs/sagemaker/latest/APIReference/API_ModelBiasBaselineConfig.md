---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelBiasBaselineConfig.html
---

# ModelBiasBaselineConfig
<a name="API_ModelBiasBaselineConfig"></a>

The configuration for a baseline model bias job.

## Contents
<a name="API_ModelBiasBaselineConfig_Contents"></a>

 ** BaseliningJobName **   <a name="sagemaker-Type-ModelBiasBaselineConfig-BaseliningJobName"></a>
The name of the baseline model bias job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** ConstraintsResource **   <a name="sagemaker-Type-ModelBiasBaselineConfig-ConstraintsResource"></a>
The constraints resource for a monitoring job.
Type: [MonitoringConstraintsResource](API_MonitoringConstraintsResource.md) object
Required: No

## See Also
<a name="API_ModelBiasBaselineConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelBiasBaselineConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelBiasBaselineConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelBiasBaselineConfig)
