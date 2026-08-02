---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_FilterByAssetModel.html
---

# FilterByAssetModel
<a name="API_FilterByAssetModel"></a>

Filter by asset model.

## Contents
<a name="API_FilterByAssetModel_Contents"></a>

 ** assetModelExternalId **   <a name="tm-Type-FilterByAssetModel-assetModelExternalId"></a>
The external-Id property of an asset model.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `.*[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+.*`
Required: No

 ** assetModelId **   <a name="tm-Type-FilterByAssetModel-assetModelId"></a>
The asset model Id.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** includeAssets **   <a name="tm-Type-FilterByAssetModel-includeAssets"></a>
Set to true to include all assets that use the specified asset model.
Type: Boolean
Required: No

 ** includeOffspring **   <a name="tm-Type-FilterByAssetModel-includeOffspring"></a>
Set to true to include all associated asset models in the hierarchy of the specified asset model.
Type: Boolean
Required: No

## See Also
<a name="API_FilterByAssetModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/FilterByAssetModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/FilterByAssetModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/FilterByAssetModel)
