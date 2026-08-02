---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelMetadataFilter.html
---

# ModelMetadataFilter
<a name="API_ModelMetadataFilter"></a>

Part of the search expression. You can specify the name and value (domain, task, framework, framework version, task, and model).

## Contents
<a name="API_ModelMetadataFilter_Contents"></a>

 ** Name **   <a name="sagemaker-Type-ModelMetadataFilter-Name"></a>
The name of the of the model to filter by.
Type: String
Valid Values: `Domain | Framework | Task | FrameworkVersion`
Required: Yes

 ** Value **   <a name="sagemaker-Type-ModelMetadataFilter-Value"></a>
The value to filter the model metadata.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_ModelMetadataFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelMetadataFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelMetadataFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelMetadataFilter)
