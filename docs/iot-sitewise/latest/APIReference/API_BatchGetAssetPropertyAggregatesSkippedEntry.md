---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregatesSkippedEntry.html
---

# BatchGetAssetPropertyAggregatesSkippedEntry
<a name="API_BatchGetAssetPropertyAggregatesSkippedEntry"></a>

Contains information for an entry that has been processed by the previous [BatchGetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html) request.

## Contents
<a name="API_BatchGetAssetPropertyAggregatesSkippedEntry_Contents"></a>

 ** completionStatus **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesSkippedEntry-completionStatus"></a>
The completion status of each entry that is associated with the [BatchGetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html) API.
Type: String
Valid Values: `SUCCESS | ERROR`
Required: Yes

 ** entryId **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesSkippedEntry-entryId"></a>
The ID of the entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** errorInfo **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesSkippedEntry-errorInfo"></a>
The error information, such as the error code and the timestamp.
Type: [BatchGetAssetPropertyAggregatesErrorInfo](API_BatchGetAssetPropertyAggregatesErrorInfo.md) object
Required: No

## See Also
<a name="API_BatchGetAssetPropertyAggregatesSkippedEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregatesSkippedEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregatesSkippedEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregatesSkippedEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
