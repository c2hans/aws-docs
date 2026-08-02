---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_LineItemAssetInformation.html
---

# LineItemAssetInformation
<a name="API_LineItemAssetInformation"></a>

 Information about a line item asset.

## Contents
<a name="API_LineItemAssetInformation_Contents"></a>

 ** AssetId **   <a name="outposts-Type-LineItemAssetInformation-AssetId"></a>
 The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(\w+)$`
Required: No

 ** MacAddressList **   <a name="outposts-Type-LineItemAssetInformation-MacAddressList"></a>
 The MAC addresses of the asset.
Type: Array of strings
Length Constraints: Fixed length of 17.
Pattern: `^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$`
Required: No

## See Also
<a name="API_LineItemAssetInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/LineItemAssetInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/LineItemAssetInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/LineItemAssetInformation)
