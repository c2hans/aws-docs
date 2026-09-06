---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetHierarchyInfo.html
---

# AssetHierarchyInfo
<a name="API_AssetHierarchyInfo"></a>

Contains information about a parent asset and a child asset that are related through an asset hierarchy.

## Contents
<a name="API_AssetHierarchyInfo_Contents"></a>

 ** childAssetId **   <a name="iotsitewise-Type-AssetHierarchyInfo-childAssetId"></a>
The ID of the child asset in this asset relationship.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** parentAssetId **   <a name="iotsitewise-Type-AssetHierarchyInfo-parentAssetId"></a>
The ID of the parent asset in this asset relationship.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

## See Also
<a name="API_AssetHierarchyInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetHierarchyInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetHierarchyInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetHierarchyInfo)
