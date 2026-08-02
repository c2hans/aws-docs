---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_FrequencyBandwidth.html
---

# FrequencyBandwidth
<a name="API_FrequencyBandwidth"></a>

Object that describes the frequency bandwidth.

## Contents
<a name="API_FrequencyBandwidth_Contents"></a>

 ** units **   <a name="groundstation-Type-FrequencyBandwidth-units"></a>
Frequency bandwidth units.
Type: String
Valid Values: `GHz | MHz | kHz`
Required: Yes

 ** value **   <a name="groundstation-Type-FrequencyBandwidth-value"></a>
Frequency bandwidth value. AWS Ground Station currently has the following bandwidth limitations:
+ For `AntennaDownlinkDemodDecodeconfig`, valid values are between 125 kHz to 650 MHz.
+ For `AntennaDownlinkconfig`, valid values are between 10 kHz to 54 MHz.
+ For `AntennaUplinkConfig`, valid values are between 10 kHz to 54 MHz.
Type: Double
Required: Yes

## See Also
<a name="API_FrequencyBandwidth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/FrequencyBandwidth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/FrequencyBandwidth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/FrequencyBandwidth)
