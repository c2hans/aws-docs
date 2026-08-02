---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_FilterByAsset.html
---

# FilterByAsset
<a name="API_FilterByAsset"></a>

Filter by asset. You can include multiple filters when you export your AWS IoT SiteWise content. See [Export metadata examples](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/bulk-operations-export-filter-examples.html) in the AWS IoT SiteWise User Guide.

## Contents
<a name="API_FilterByAsset_Contents"></a>

 ** assetExternalId **   <a name="tm-Type-FilterByAsset-assetExternalId"></a>
The external-Id property of an asset.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `.*[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+.*`
Required: No

 ** assetId **   <a name="tm-Type-FilterByAsset-assetId"></a>
Filter by asset Id.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** includeAssetModel **   <a name="tm-Type-FilterByAsset-includeAssetModel"></a>
Set to true to include the asset model that the specified asset uses.
Type: Boolean
Required: No

 ** includeOffspring **   <a name="tm-Type-FilterByAsset-includeOffspring"></a>
Set to true to include all associated asset models in the hierarchy of the specified asset model.
Type: Boolean
Required: No

## See Also
<a name="API_FilterByAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/FilterByAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/FilterByAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/FilterByAsset)
