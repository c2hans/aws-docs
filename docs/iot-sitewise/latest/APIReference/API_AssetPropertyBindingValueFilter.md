---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetPropertyBindingValueFilter.html
---

# AssetPropertyBindingValueFilter
<a name="API_AssetPropertyBindingValueFilter"></a>

A filter used to match data bindings based on a specific asset property. This filter helps identify all computation models referencing a particular property of an asset in their data bindings.

## Contents
<a name="API_AssetPropertyBindingValueFilter_Contents"></a>

 ** assetId **   <a name="iotsitewise-Type-AssetPropertyBindingValueFilter-assetId"></a>
The ID of the asset containing the property to filter by. This identifies the specific asset instance containing the property of interest.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** propertyId **   <a name="iotsitewise-Type-AssetPropertyBindingValueFilter-propertyId"></a>
The ID of the property within the asset to filter by. Only data bindings referencing this specific property of the specified asset are matched.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## See Also
<a name="API_AssetPropertyBindingValueFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetPropertyBindingValueFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetPropertyBindingValueFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetPropertyBindingValueFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
