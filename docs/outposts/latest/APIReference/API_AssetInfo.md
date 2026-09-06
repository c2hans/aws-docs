---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_AssetInfo.html
---

# AssetInfo
<a name="API_AssetInfo"></a>

 Information about hardware assets.

## Contents
<a name="API_AssetInfo_Contents"></a>

 ** AssetId **   <a name="outposts-Type-AssetInfo-AssetId"></a>
 The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(\w+)$`
Required: No

 ** AssetLocation **   <a name="outposts-Type-AssetInfo-AssetLocation"></a>
 The position of an asset in a rack.
Type: [AssetLocation](API_AssetLocation.md) object
Required: No

 ** AssetType **   <a name="outposts-Type-AssetInfo-AssetType"></a>
 The type of the asset.
Type: String
Valid Values: `COMPUTE | STORAGE | POWERSHELF | SWITCH | NETWORKING`
Required: No

 ** ComputeAttributes **   <a name="outposts-Type-AssetInfo-ComputeAttributes"></a>
 Information about compute hardware assets.
Type: [ComputeAttributes](API_ComputeAttributes.md) object
Required: No

 ** RackId **   <a name="outposts-Type-AssetInfo-RackId"></a>
 The rack ID of the asset.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 20.
Pattern: `^[\S \n]+$`
Required: No

## See Also
<a name="API_AssetInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/AssetInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/AssetInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/AssetInfo)
