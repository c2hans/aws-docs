---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregatesErrorInfo.html
---

# BatchGetAssetPropertyAggregatesErrorInfo
<a name="API_BatchGetAssetPropertyAggregatesErrorInfo"></a>

Contains the error code and the timestamp for an asset property aggregate entry that is associated with the [BatchGetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html) API.

## Contents
<a name="API_BatchGetAssetPropertyAggregatesErrorInfo_Contents"></a>

 ** errorCode **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesErrorInfo-errorCode"></a>
The error code.
Type: String
Valid Values: `ResourceNotFoundException | InvalidRequestException | AccessDeniedException`
Required: Yes

 ** errorTimestamp **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesErrorInfo-errorTimestamp"></a>
The date the error occurred, in Unix epoch time.
Type: Timestamp
Required: Yes

## See Also
<a name="API_BatchGetAssetPropertyAggregatesErrorInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregatesErrorInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregatesErrorInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregatesErrorInfo)
