---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_FPorts.html
---

# FPorts
<a name="API_FPorts"></a>

List of FPort assigned for different LoRaWAN application packages to use

## Contents
<a name="API_FPorts_Contents"></a>

 ** Applications **   <a name="iotwireless-Type-FPorts-Applications"></a>
Optional LoRaWAN application information, which can be used for geolocation.
Type: Array of [ApplicationConfig](API_ApplicationConfig.md) objects
Required: No

 ** ClockSync **   <a name="iotwireless-Type-FPorts-ClockSync"></a>
The Fport value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 223.
Required: No

 ** Fuota **   <a name="iotwireless-Type-FPorts-Fuota"></a>
The Fport value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 223.
Required: No

 ** Multicast **   <a name="iotwireless-Type-FPorts-Multicast"></a>
The Fport value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 223.
Required: No

 ** Positioning **   <a name="iotwireless-Type-FPorts-Positioning"></a>
FPort values for the GNSS, stream, and ClockSync functions of the positioning information.
Type: [Positioning](API_Positioning.md) object
Required: No

## See Also
<a name="API_FPorts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/FPorts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/FPorts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/FPorts)
