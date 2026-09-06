---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EdgeModelSummary.html
---

# EdgeModelSummary
<a name="API_EdgeModelSummary"></a>

Summary of model on edge device.

## Contents
<a name="API_EdgeModelSummary_Contents"></a>

 ** ModelName **   <a name="sagemaker-Type-EdgeModelSummary-ModelName"></a>
The name of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelVersion **   <a name="sagemaker-Type-EdgeModelSummary-ModelVersion"></a>
The version model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\ \_\.]+`
Required: Yes

## See Also
<a name="API_EdgeModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EdgeModelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EdgeModelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EdgeModelSummary)
