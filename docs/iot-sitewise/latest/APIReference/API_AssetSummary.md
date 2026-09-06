---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetSummary.html
---

# AssetSummary
<a name="API_AssetSummary"></a>

Contains a summary of an asset.

## Contents
<a name="API_AssetSummary_Contents"></a>

 ** arn **   <a name="iotsitewise-Type-AssetSummary-arn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the asset, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

 ** assetModelId **   <a name="iotsitewise-Type-AssetSummary-assetModelId"></a>
The ID of the asset model used to create this asset.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** creationDate **   <a name="iotsitewise-Type-AssetSummary-creationDate"></a>
The date the asset was created, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** hierarchies **   <a name="iotsitewise-Type-AssetSummary-hierarchies"></a>
A list of asset hierarchies that each contain a `hierarchyId`. A hierarchy specifies allowed parent/child asset relationships.
Type: Array of [AssetHierarchy](API_AssetHierarchy.md) objects
Required: Yes

 ** id **   <a name="iotsitewise-Type-AssetSummary-id"></a>
The ID of the asset, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** lastUpdateDate **   <a name="iotsitewise-Type-AssetSummary-lastUpdateDate"></a>
The date the asset was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** name **   <a name="iotsitewise-Type-AssetSummary-name"></a>
The name of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** status **   <a name="iotsitewise-Type-AssetSummary-status"></a>
The current status of the asset.
Type: [AssetStatus](API_AssetStatus.md) object
Required: Yes

 ** description **   <a name="iotsitewise-Type-AssetSummary-description"></a>
A description for the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** externalId **   <a name="iotsitewise-Type-AssetSummary-externalId"></a>
The external ID of the asset. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

## See Also
<a name="API_AssetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetSummary)
