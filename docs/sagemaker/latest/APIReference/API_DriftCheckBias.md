---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DriftCheckBias.html
---

# DriftCheckBias
<a name="API_DriftCheckBias"></a>

Represents the drift check bias baselines that can be used when the model monitor is set using the model package.

## Contents
<a name="API_DriftCheckBias_Contents"></a>

 ** ConfigFile **   <a name="sagemaker-Type-DriftCheckBias-ConfigFile"></a>
The bias config file for a model.
Type: [FileSource](API_FileSource.md) object
Required: No

 ** PostTrainingConstraints **   <a name="sagemaker-Type-DriftCheckBias-PostTrainingConstraints"></a>
The post-training constraints.
Type: [MetricsSource](API_MetricsSource.md) object
Required: No

 ** PreTrainingConstraints **   <a name="sagemaker-Type-DriftCheckBias-PreTrainingConstraints"></a>
The pre-training constraints.
Type: [MetricsSource](API_MetricsSource.md) object
Required: No

## See Also
<a name="API_DriftCheckBias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DriftCheckBias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DriftCheckBias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DriftCheckBias)
