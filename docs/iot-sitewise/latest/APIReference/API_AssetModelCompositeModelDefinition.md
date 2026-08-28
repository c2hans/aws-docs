---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetModelCompositeModelDefinition.html
---

# AssetModelCompositeModelDefinition
<a name="API_AssetModelCompositeModelDefinition"></a>

Contains a composite model definition in an asset model. This composite model definition is applied to all assets created from the asset model.

## Contents
<a name="API_AssetModelCompositeModelDefinition_Contents"></a>

 ** name **   <a name="iotsitewise-Type-AssetModelCompositeModelDefinition-name"></a>
The name of the composite model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** type **   <a name="iotsitewise-Type-AssetModelCompositeModelDefinition-type"></a>
The type of the composite model. For alarm composite models, this type is `AWS/ALARM`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** description **   <a name="iotsitewise-Type-AssetModelCompositeModelDefinition-description"></a>
The description of the composite model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** externalId **   <a name="iotsitewise-Type-AssetModelCompositeModelDefinition-externalId"></a>
An external ID to assign to the composite model. The external ID must be unique among composite models within this asset model. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** id **   <a name="iotsitewise-Type-AssetModelCompositeModelDefinition-id"></a>
The ID to assign to the composite model, if desired. AWS IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** properties **   <a name="iotsitewise-Type-AssetModelCompositeModelDefinition-properties"></a>
The asset property definitions for this composite model.
Type: Array of [AssetModelPropertyDefinition](API_AssetModelPropertyDefinition.md) objects
Required: No

## See Also
<a name="API_AssetModelCompositeModelDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetModelCompositeModelDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetModelCompositeModelDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetModelCompositeModelDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
