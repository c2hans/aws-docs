---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_DestinationConfig.html
---

# DestinationConfig
<a name="API_iot-secure-tunneling_DestinationConfig"></a>

The destination configuration. You can not use `DestinationConfig` with source `clientMode`.

## Contents
<a name="API_iot-secure-tunneling_DestinationConfig_Contents"></a>

 ** services **   <a name="iot-Type-iot-secure-tunneling_DestinationConfig-services"></a>
A list of service names that identify the target application. The AWS IoT client running on the destination device reads this value and uses it to look up a port or an IP address and a port. The AWS IoT client instantiates the local proxy, which uses this information to connect to the destination application.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

 ** thingName **   <a name="iot-Type-iot-secure-tunneling_DestinationConfig-thingName"></a>
The name of the IoT thing to which you want to connect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

## See Also
<a name="API_iot-secure-tunneling_DestinationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsecuretunneling-2018-10-05/DestinationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsecuretunneling-2018-10-05/DestinationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsecuretunneling-2018-10-05/DestinationConfig)
