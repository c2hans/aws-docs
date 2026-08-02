---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_WiFiAccessPoint.html
---

# WiFiAccessPoint
<a name="API_WiFiAccessPoint"></a>

Wi-Fi access point.

## Contents
<a name="API_WiFiAccessPoint_Contents"></a>

 ** MacAddress **   <a name="iotwireless-Type-WiFiAccessPoint-MacAddress"></a>
Wi-Fi MAC Address.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 17.
Pattern: `^([0-9A-Fa-f]{2}[:-]?){5}([0-9A-Fa-f]{2})$`
Required: Yes

 ** Rss **   <a name="iotwireless-Type-WiFiAccessPoint-Rss"></a>
Received signal strength (dBm) of the WLAN measurement data.
Type: Integer
Valid Range: Minimum value of -128. Maximum value of 0.
Required: Yes

## See Also
<a name="API_WiFiAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/WiFiAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/WiFiAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/WiFiAccessPoint)
