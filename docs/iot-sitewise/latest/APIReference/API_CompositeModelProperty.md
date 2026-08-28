---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CompositeModelProperty.html
---

# CompositeModelProperty
<a name="API_CompositeModelProperty"></a>

Contains information about a composite model property on an asset.

## Contents
<a name="API_CompositeModelProperty_Contents"></a>

 ** assetProperty **   <a name="iotsitewise-Type-CompositeModelProperty-assetProperty"></a>
Contains asset property information.
Type: [Property](API_Property.md) object
Required: Yes

 ** name **   <a name="iotsitewise-Type-CompositeModelProperty-name"></a>
The name of the property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** type **   <a name="iotsitewise-Type-CompositeModelProperty-type"></a>
The type of the composite model that defines this property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** externalId **   <a name="iotsitewise-Type-CompositeModelProperty-externalId"></a>
The external ID of the composite model that contains the property. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** id **   <a name="iotsitewise-Type-CompositeModelProperty-id"></a>
 The ID of the composite model that contains the property.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

## See Also
<a name="API_CompositeModelProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CompositeModelProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CompositeModelProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CompositeModelProperty)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
