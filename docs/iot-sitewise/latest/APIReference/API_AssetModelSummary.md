---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetModelSummary.html
---

# AssetModelSummary
<a name="API_AssetModelSummary"></a>

Contains a summary of an asset model.

## Contents
<a name="API_AssetModelSummary_Contents"></a>

 ** arn **   <a name="iotsitewise-Type-AssetModelSummary-arn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the asset model, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

 ** creationDate **   <a name="iotsitewise-Type-AssetModelSummary-creationDate"></a>
The date the asset model was created, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** description **   <a name="iotsitewise-Type-AssetModelSummary-description"></a>
The asset model description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** id **   <a name="iotsitewise-Type-AssetModelSummary-id"></a>
The ID of the asset model (used with AWS IoT SiteWise API operations).
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** lastUpdateDate **   <a name="iotsitewise-Type-AssetModelSummary-lastUpdateDate"></a>
The date the asset model was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** name **   <a name="iotsitewise-Type-AssetModelSummary-name"></a>
The name of the asset model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** status **   <a name="iotsitewise-Type-AssetModelSummary-status"></a>
The current status of the asset model.
Type: [AssetModelStatus](API_AssetModelStatus.md) object
Required: Yes

 ** assetModelType **   <a name="iotsitewise-Type-AssetModelSummary-assetModelType"></a>
The type of asset model.
+  **ASSET\_MODEL** – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.
+  **COMPONENT\_MODEL** – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model.
Type: String
Valid Values: `ASSET_MODEL | COMPONENT_MODEL | INTERFACE`
Required: No

 ** externalId **   <a name="iotsitewise-Type-AssetModelSummary-externalId"></a>
The external ID of the asset model. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** version **   <a name="iotsitewise-Type-AssetModelSummary-version"></a>
The version number of the asset model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`
Required: No

## See Also
<a name="API_AssetModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetModelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetModelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetModelSummary)
