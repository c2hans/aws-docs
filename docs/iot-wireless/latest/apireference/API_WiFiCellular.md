---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_WiFiCellular.html
---

# WiFiCellular
<a name="API_WiFiCellular"></a>

Configuration for WiFi and cellular location payloads. Contains the confidence level that determines the size of the uncertainty radius in the position estimate.

## Contents
<a name="API_WiFiCellular_Contents"></a>

 ** ConfidencePercent **   <a name="iotwireless-Type-WiFiCellular-ConfidencePercent"></a>
The confidence level for WiFi and cellular position estimates, expressed as a percentage. This value determines the size of the confidence area or uncertainty radius for the estimated position. A higher confidence level produces a larger uncertainty radius, while a lower confidence level produces a smaller, more precise radius.
Valid range: 50 to 99 inclusive. If not specified, the default value of 68 is used, which corresponds to approximately one standard deviation of the normal distribution.
Type: Integer
Valid Range: Minimum value of 50. Maximum value of 99.
Required: No

## See Also
<a name="API_WiFiCellular_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/WiFiCellular)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/WiFiCellular)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/WiFiCellular)
