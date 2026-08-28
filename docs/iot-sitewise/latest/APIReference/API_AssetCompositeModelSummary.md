---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetCompositeModelSummary.html
---

# AssetCompositeModelSummary
<a name="API_AssetCompositeModelSummary"></a>

Contains a summary of the composite model for a specific asset.

## Contents
<a name="API_AssetCompositeModelSummary_Contents"></a>

 ** description **   <a name="iotsitewise-Type-AssetCompositeModelSummary-description"></a>
A description of the composite model that this summary describes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** id **   <a name="iotsitewise-Type-AssetCompositeModelSummary-id"></a>
The ID of the composite model that this summary describes.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** name **   <a name="iotsitewise-Type-AssetCompositeModelSummary-name"></a>
The name of the composite model that this summary describes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** path **   <a name="iotsitewise-Type-AssetCompositeModelSummary-path"></a>
The path that includes all the components of the asset model for the asset.
Type: Array of [AssetCompositeModelPathSegment](API_AssetCompositeModelPathSegment.md) objects
Required: Yes

 ** type **   <a name="iotsitewise-Type-AssetCompositeModelSummary-type"></a>
The type of asset model.
+  **ASSET\_MODEL** – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.
+  **COMPONENT\_MODEL** – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** externalId **   <a name="iotsitewise-Type-AssetCompositeModelSummary-externalId"></a>
An external ID to assign to the asset model.
If the composite model is a derived composite model, or one nested inside a component model, you can only set the external ID using `UpdateAssetModelCompositeModel` and specifying the derived ID of the model or property from the created model it's a part of.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

## See Also
<a name="API_AssetCompositeModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetCompositeModelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetCompositeModelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetCompositeModelSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
