---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_AcceleratorConfig.html
---

# AcceleratorConfig

The accelerator resource settings for a Lambda execution environment, including the amount of accelerator memory to allocate. To use an accelerator, the function must also have a capacity provider configuration (`CapacityProviderConfig`) for Lambda Managed Instances.

## Contents
<a name="API_AcceleratorConfig_Contents"></a>

 ** AcceleratorMemorySize **   <a name="lambda-Type-AcceleratorConfig-AcceleratorMemorySize"></a>
The minimum amount of memory (in GB) of each accelerator device exposed to the execution environment. Lambda might allocate more, depending on the accelerator instance types available. Valid values: 3, 6, 12, 16, 24, 48.
Type: Integer
Required: Yes

## See Also
<a name="API_AcceleratorConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/AcceleratorConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/AcceleratorConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/AcceleratorConfig)
