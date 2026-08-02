---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIDatasetConfig.html
---

# AIDatasetConfig
<a name="API_AIDatasetConfig"></a>

The dataset configuration for an AI workload. This is a union type — specify one of the members.

## Contents
<a name="API_AIDatasetConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** InputDataConfig **   <a name="sagemaker-Type-AIDatasetConfig-InputDataConfig"></a>
An array of input data channel configurations for the workload.
Type: Array of [AIWorkloadInputDataConfig](API_AIWorkloadInputDataConfig.md) objects
Required: No

## See Also
<a name="API_AIDatasetConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIDatasetConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIDatasetConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIDatasetConfig)
