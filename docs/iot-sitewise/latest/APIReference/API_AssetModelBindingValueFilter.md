---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetModelBindingValueFilter.html
---

# AssetModelBindingValueFilter
<a name="API_AssetModelBindingValueFilter"></a>

A filter used to match data bindings based on a specific asset model. This filter identifies all computation models referencing a particular asset model in their data bindings.

## Contents
<a name="API_AssetModelBindingValueFilter_Contents"></a>

 ** assetModelId **   <a name="iotsitewise-Type-AssetModelBindingValueFilter-assetModelId"></a>
The ID of the asset model to filter data bindings by. Only data bindings referemncing this specific asset model are matched.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## See Also
<a name="API_AssetModelBindingValueFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetModelBindingValueFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetModelBindingValueFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetModelBindingValueFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
