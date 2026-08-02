---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValueErrorInfo.html
---

# BatchGetAssetPropertyValueErrorInfo
<a name="API_BatchGetAssetPropertyValueErrorInfo"></a>

The error information, such as the error code and the timestamp.

## Contents
<a name="API_BatchGetAssetPropertyValueErrorInfo_Contents"></a>

 ** errorCode **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueErrorInfo-errorCode"></a>
The error code.
Type: String
Valid Values: `ResourceNotFoundException | InvalidRequestException | AccessDeniedException`
Required: Yes

 ** errorTimestamp **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueErrorInfo-errorTimestamp"></a>
The date the error occurred, in Unix epoch time.
Type: Timestamp
Required: Yes

## See Also
<a name="API_BatchGetAssetPropertyValueErrorInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchGetAssetPropertyValueErrorInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchGetAssetPropertyValueErrorInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchGetAssetPropertyValueErrorInfo)
