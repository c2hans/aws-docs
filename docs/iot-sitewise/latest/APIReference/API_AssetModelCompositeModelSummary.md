---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetModelCompositeModelSummary.html
---

# AssetModelCompositeModelSummary
<a name="API_AssetModelCompositeModelSummary"></a>

Contains a summary of the composite model.

## Contents
<a name="API_AssetModelCompositeModelSummary_Contents"></a>

 ** id **   <a name="iotsitewise-Type-AssetModelCompositeModelSummary-id"></a>
The ID of the composite model that this summary describes..
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** name **   <a name="iotsitewise-Type-AssetModelCompositeModelSummary-name"></a>
The name of the composite model that this summary describes..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** type **   <a name="iotsitewise-Type-AssetModelCompositeModelSummary-type"></a>
The composite model type. Valid values are `AWS/ALARM`, `CUSTOM`, or ` AWS/L4E_ANOMALY`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** description **   <a name="iotsitewise-Type-AssetModelCompositeModelSummary-description"></a>
The description of the composite model that this summary describes..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** externalId **   <a name="iotsitewise-Type-AssetModelCompositeModelSummary-externalId"></a>
The external ID of a composite model on this asset model. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** path **   <a name="iotsitewise-Type-AssetModelCompositeModelSummary-path"></a>
The path that includes all the pieces that make up the composite model.
Type: Array of [AssetModelCompositeModelPathSegment](API_AssetModelCompositeModelPathSegment.md) objects
Required: No

## See Also
<a name="API_AssetModelCompositeModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetModelCompositeModelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetModelCompositeModelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetModelCompositeModelSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
