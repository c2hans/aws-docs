---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValueHistoryErrorEntry.html
---

# BatchGetAssetPropertyValueHistoryErrorEntry
<a name="API_BatchGetAssetPropertyValueHistoryErrorEntry"></a>

A list of the errors (if any) associated with the batch request. Each error entry contains the `entryId` of the entry that failed.

## Contents
<a name="API_BatchGetAssetPropertyValueHistoryErrorEntry_Contents"></a>

 ** entryId **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistoryErrorEntry-entryId"></a>
The ID of the entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** errorCode **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistoryErrorEntry-errorCode"></a>
The error code.
Type: String
Valid Values: `ResourceNotFoundException | InvalidRequestException | AccessDeniedException`
Required: Yes

 ** errorMessage **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistoryErrorEntry-errorMessage"></a>
The associated error message.
Type: String
Required: Yes

## See Also
<a name="API_BatchGetAssetPropertyValueHistoryErrorEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistoryErrorEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistoryErrorEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistoryErrorEntry)
