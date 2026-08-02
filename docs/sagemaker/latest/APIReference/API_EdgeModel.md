---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EdgeModel.html
---

# EdgeModel
<a name="API_EdgeModel"></a>

The model on the edge device.

## Contents
<a name="API_EdgeModel_Contents"></a>

 ** ModelName **   <a name="sagemaker-Type-EdgeModel-ModelName"></a>
The name of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelVersion **   <a name="sagemaker-Type-EdgeModel-ModelVersion"></a>
The model version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\ \_\.]+`
Required: Yes

 ** LatestInference **   <a name="sagemaker-Type-EdgeModel-LatestInference"></a>
The timestamp of the last inference that was made.
Type: Timestamp
Required: No

 ** LatestSampleTime **   <a name="sagemaker-Type-EdgeModel-LatestSampleTime"></a>
The timestamp of the last data sample taken.
Type: Timestamp
Required: No

## See Also
<a name="API_EdgeModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EdgeModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EdgeModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EdgeModel)
