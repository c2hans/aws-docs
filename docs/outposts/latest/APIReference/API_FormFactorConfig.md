---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_FormFactorConfig.html
---

# FormFactorConfig
<a name="API_FormFactorConfig"></a>

A supported form factor and Outpost generation configuration for an instance type.

## Contents
<a name="API_FormFactorConfig_Contents"></a>

 ** FormFactor **   <a name="outposts-Type-FormFactorConfig-FormFactor"></a>
The form factor. Valid values are `RACK` for rack-based Outposts and `SERVER` for server-based Outposts.
Type: String
Valid Values: `RACK | SERVER`
Required: No

 ** OutpostGeneration **   <a name="outposts-Type-FormFactorConfig-OutpostGeneration"></a>
The Outpost generation. Valid values are `GENERATION_1` for first-generation rack deployments and `GENERATION_2` for second-generation rack deployments. This value is not set for server form factors.
Type: String
Valid Values: `GENERATION_2 | GENERATION_1`
Required: No

## See Also
<a name="API_FormFactorConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/FormFactorConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/FormFactorConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/FormFactorConfig)
