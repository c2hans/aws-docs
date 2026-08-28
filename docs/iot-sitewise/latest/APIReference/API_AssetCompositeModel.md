---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetCompositeModel.html
---

# AssetCompositeModel
<a name="API_AssetCompositeModel"></a>

Contains information about a composite model in an asset. This object contains the asset's properties that you define in the composite model.

## Contents
<a name="API_AssetCompositeModel_Contents"></a>

 ** name **   <a name="iotsitewise-Type-AssetCompositeModel-name"></a>
The name of the composite model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** properties **   <a name="iotsitewise-Type-AssetCompositeModel-properties"></a>
The asset properties that this composite model defines.
Type: Array of [AssetProperty](API_AssetProperty.md) objects
Required: Yes

 ** type **   <a name="iotsitewise-Type-AssetCompositeModel-type"></a>
The type of the composite model. For alarm composite models, this type is `AWS/ALARM`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** description **   <a name="iotsitewise-Type-AssetCompositeModel-description"></a>
The description of the composite model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** externalId **   <a name="iotsitewise-Type-AssetCompositeModel-externalId"></a>
The external ID of the asset composite model. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** id **   <a name="iotsitewise-Type-AssetCompositeModel-id"></a>
 The ID of the asset composite model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

## See Also
<a name="API_AssetCompositeModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetCompositeModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetCompositeModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetCompositeModel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
