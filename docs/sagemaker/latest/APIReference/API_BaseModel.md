---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BaseModel.html
---

# BaseModel
<a name="API_BaseModel"></a>

Identifies the foundation model that was used as the starting point for model customization.

## Contents
<a name="API_BaseModel_Contents"></a>

 ** HubContentName **   <a name="sagemaker-Type-BaseModel-HubContentName"></a>
 The hub content name of the base model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** HubContentVersion **   <a name="sagemaker-Type-BaseModel-HubContentVersion"></a>
 The hub content version of the base model.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: No

 ** RecipeName **   <a name="sagemaker-Type-BaseModel-RecipeName"></a>
 The recipe name of the base model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_BaseModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BaseModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BaseModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BaseModel)
