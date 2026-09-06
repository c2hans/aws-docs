---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetModelHierarchyDefinition.html
---

# AssetModelHierarchyDefinition
<a name="API_AssetModelHierarchyDefinition"></a>

Contains an asset model hierarchy used in asset model creation. An asset model hierarchy determines the kind (or type) of asset that can belong to a hierarchy.

## Contents
<a name="API_AssetModelHierarchyDefinition_Contents"></a>

 ** childAssetModelId **   <a name="iotsitewise-Type-AssetModelHierarchyDefinition-childAssetModelId"></a>
The ID of an asset model for this hierarchy. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** name **   <a name="iotsitewise-Type-AssetModelHierarchyDefinition-name"></a>
The name of the asset model hierarchy definition (as specified in the [CreateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html) or [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) API operation).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** externalId **   <a name="iotsitewise-Type-AssetModelHierarchyDefinition-externalId"></a>
An external ID to assign to the asset model hierarchy. The external ID must be unique among asset model hierarchies within this asset model. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** id **   <a name="iotsitewise-Type-AssetModelHierarchyDefinition-id"></a>
The ID to assign to the asset model hierarchy, if desired. AWS IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

## See Also
<a name="API_AssetModelHierarchyDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetModelHierarchyDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetModelHierarchyDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetModelHierarchyDefinition)
