---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CollectionConfiguration.html
---

# CollectionConfiguration
<a name="API_CollectionConfiguration"></a>

Configuration information for the Amazon SageMaker Debugger output tensor collections.

## Contents
<a name="API_CollectionConfiguration_Contents"></a>

 ** CollectionName **   <a name="sagemaker-Type-CollectionConfiguration-CollectionName"></a>
The name of the tensor collection. The name must be unique relative to other rule configuration names.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** CollectionParameters **   <a name="sagemaker-Type-CollectionConfiguration-CollectionParameters"></a>
Parameter values for the tensor collection. The allowed parameters are `"name"`, `"include_regex"`, `"reduction_config"`, `"save_config"`, `"tensor_names"`, and `"save_histogram"`.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`
Required: No

## See Also
<a name="API_CollectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CollectionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CollectionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CollectionConfiguration)
