---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TransferData.html
---

# TransferData
<a name="API_TransferData"></a>

Data used to transfer a certificate to an AWS account.

## Contents
<a name="API_TransferData_Contents"></a>

 ** acceptDate **   <a name="iot-Type-TransferData-acceptDate"></a>
The date the transfer was accepted.
Type: Timestamp
Required: No

 ** rejectDate **   <a name="iot-Type-TransferData-rejectDate"></a>
The date the transfer was rejected.
Type: Timestamp
Required: No

 ** rejectReason **   <a name="iot-Type-TransferData-rejectReason"></a>
The reason why the transfer was rejected.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

 ** transferDate **   <a name="iot-Type-TransferData-transferDate"></a>
The date the transfer took place.
Type: Timestamp
Required: No

 ** transferMessage **   <a name="iot-Type-TransferData-transferMessage"></a>
The transfer message.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_TransferData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TransferData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TransferData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TransferData)
