---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_InferenceResourceConfig.html
---

# InferenceResourceConfig
<a name="API_InferenceResourceConfig"></a>

Defines the resources used to perform model inference.

## Contents
<a name="API_InferenceResourceConfig_Contents"></a>

 ** instanceType **   <a name="API-Type-InferenceResourceConfig-instanceType"></a>
The type of instance that is used to perform model inference.
Type: String
Valid Values: `ml.r7i.48xlarge | ml.r6i.16xlarge | ml.m6i.xlarge | ml.m5.4xlarge | ml.p2.xlarge | ml.m4.16xlarge | ml.r7i.16xlarge | ml.m7i.xlarge | ml.m6i.12xlarge | ml.r7i.8xlarge | ml.r7i.large | ml.m7i.12xlarge | ml.m6i.24xlarge | ml.m7i.24xlarge | ml.r6i.8xlarge | ml.r6i.large | ml.g5.2xlarge | ml.m5.large | ml.m7i.48xlarge | ml.m6i.16xlarge | ml.p2.16xlarge | ml.g5.4xlarge | ml.m7i.16xlarge | ml.c4.2xlarge | ml.c5.2xlarge | ml.c6i.32xlarge | ml.c4.4xlarge | ml.g5.8xlarge | ml.c6i.xlarge | ml.c5.4xlarge | ml.g4dn.xlarge | ml.c7i.xlarge | ml.c6i.12xlarge | ml.g4dn.12xlarge | ml.c7i.12xlarge | ml.c6i.24xlarge | ml.g4dn.2xlarge | ml.c7i.24xlarge | ml.c7i.2xlarge | ml.c4.8xlarge | ml.c6i.2xlarge | ml.g4dn.4xlarge | ml.c7i.48xlarge | ml.c7i.4xlarge | ml.c6i.16xlarge | ml.c5.9xlarge | ml.g4dn.16xlarge | ml.c7i.16xlarge | ml.c6i.4xlarge | ml.c5.xlarge | ml.c4.xlarge | ml.g4dn.8xlarge | ml.c7i.8xlarge | ml.c7i.large | ml.g5.xlarge | ml.c6i.8xlarge | ml.c6i.large | ml.g5.12xlarge | ml.g5.24xlarge | ml.m7i.2xlarge | ml.c5.18xlarge | ml.g5.48xlarge | ml.m6i.2xlarge | ml.g5.16xlarge | ml.m7i.4xlarge | ml.r6i.32xlarge | ml.m6i.4xlarge | ml.m5.xlarge | ml.m4.10xlarge | ml.r6i.xlarge | ml.m5.12xlarge | ml.m4.xlarge | ml.r7i.2xlarge | ml.r7i.xlarge | ml.r6i.12xlarge | ml.m5.24xlarge | ml.r7i.12xlarge | ml.m7i.8xlarge | ml.m7i.large | ml.r6i.24xlarge | ml.r6i.2xlarge | ml.m4.2xlarge | ml.r7i.24xlarge | ml.r7i.4xlarge | ml.m6i.8xlarge | ml.m6i.large | ml.m5.2xlarge | ml.p2.8xlarge | ml.r6i.4xlarge | ml.m6i.32xlarge | ml.m4.4xlarge | ml.p3.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge`
Required: Yes

 ** instanceCount **   <a name="API-Type-InferenceResourceConfig-instanceCount"></a>
The number of instances to use.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

## See Also
<a name="API_InferenceResourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/InferenceResourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/InferenceResourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/InferenceResourceConfig)
