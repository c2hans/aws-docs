---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SidewalkSendDataToDevice.html
---

# SidewalkSendDataToDevice
<a name="API_SidewalkSendDataToDevice"></a>

Information about a Sidewalk router.

## Contents
<a name="API_SidewalkSendDataToDevice_Contents"></a>

 ** AckModeRetryDurationSecs **   <a name="iotwireless-Type-SidewalkSendDataToDevice-AckModeRetryDurationSecs"></a>
The duration of time in seconds to retry sending the ACK.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.
Required: No

 ** MessageType **   <a name="iotwireless-Type-SidewalkSendDataToDevice-MessageType"></a>
Sidewalk device message type. Default value is `CUSTOM_COMMAND_ID_NOTIFY`.
Type: String
Valid Values: `CUSTOM_COMMAND_ID_NOTIFY | CUSTOM_COMMAND_ID_GET | CUSTOM_COMMAND_ID_SET | CUSTOM_COMMAND_ID_RESP`
Required: No

 ** Seq **   <a name="iotwireless-Type-SidewalkSendDataToDevice-Seq"></a>
The sequence number.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 16383.
Required: No

## See Also
<a name="API_SidewalkSendDataToDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/SidewalkSendDataToDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/SidewalkSendDataToDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/SidewalkSendDataToDevice)
