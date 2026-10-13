---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LoraConfig.html
---

# LoraConfig
<a name="API_LoraConfig"></a>

The Low-Rank Adaptation (LoRA) configuration for a training session, including the rank and alpha parameters.

## Contents
<a name="API_LoraConfig_Contents"></a>

 ** Alpha **   <a name="sagemaker-Type-LoraConfig-Alpha"></a>
The Low-Rank Adaptation (LoRA) scaling factor.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** Rank **   <a name="sagemaker-Type-LoraConfig-Rank"></a>
The rank of the Low-Rank Adaptation (LoRA) adapter matrices.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 256.
Required: Yes

## See Also
<a name="API_LoraConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LoraConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LoraConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LoraConfig)
