---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValueErrorEntry.html
---

# BatchGetAssetPropertyValueErrorEntry
<a name="API_BatchGetAssetPropertyValueErrorEntry"></a>

Contains error information for an asset property value entry that is associated with the [BatchGetAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValue.html) API.

## Contents
<a name="API_BatchGetAssetPropertyValueErrorEntry_Contents"></a>

 ** entryId **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueErrorEntry-entryId"></a>
The ID of the entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** errorCode **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueErrorEntry-errorCode"></a>
The error code.
Type: String
Valid Values: `ResourceNotFoundException | InvalidRequestException | AccessDeniedException`
Required: Yes

 ** errorMessage **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueErrorEntry-errorMessage"></a>
The associated error message.
Type: String
Required: Yes

## See Also
<a name="API_BatchGetAssetPropertyValueErrorEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchGetAssetPropertyValueErrorEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchGetAssetPropertyValueErrorEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchGetAssetPropertyValueErrorEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
