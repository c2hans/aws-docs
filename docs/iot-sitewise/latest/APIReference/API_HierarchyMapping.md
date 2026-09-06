---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_HierarchyMapping.html
---

# HierarchyMapping
<a name="API_HierarchyMapping"></a>

Maps a hierarchy from an interface asset model to a hierarchy in the asset model where the interface is applied.

## Contents
<a name="API_HierarchyMapping_Contents"></a>

 ** assetModelHierarchyId **   <a name="iotsitewise-Type-HierarchyMapping-assetModelHierarchyId"></a>
The ID of the hierarchy in the asset model where the interface is applied.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** interfaceAssetModelHierarchyId **   <a name="iotsitewise-Type-HierarchyMapping-interfaceAssetModelHierarchyId"></a>
The ID of the hierarchy in the interface asset model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## See Also
<a name="API_HierarchyMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/HierarchyMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/HierarchyMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/HierarchyMapping)
