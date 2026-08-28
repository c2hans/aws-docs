---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyErrorEntry.html
---

# BatchPutAssetPropertyErrorEntry
<a name="API_BatchPutAssetPropertyErrorEntry"></a>

Contains error information for asset property value entries that are associated with the [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html) API.

## Contents
<a name="API_BatchPutAssetPropertyErrorEntry_Contents"></a>

 ** entryId **   <a name="iotsitewise-Type-BatchPutAssetPropertyErrorEntry-entryId"></a>
The ID of the failed entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** errors **   <a name="iotsitewise-Type-BatchPutAssetPropertyErrorEntry-errors"></a>
The list of update property value errors.
Type: Array of [BatchPutAssetPropertyError](API_BatchPutAssetPropertyError.md) objects
Required: Yes

## See Also
<a name="API_BatchPutAssetPropertyErrorEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchPutAssetPropertyErrorEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchPutAssetPropertyErrorEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchPutAssetPropertyErrorEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
