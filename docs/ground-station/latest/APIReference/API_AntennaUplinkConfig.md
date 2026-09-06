---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AntennaUplinkConfig.html
---

# AntennaUplinkConfig
<a name="API_AntennaUplinkConfig"></a>

Information about the uplink `Config` of an antenna.

## Contents
<a name="API_AntennaUplinkConfig_Contents"></a>

 ** spectrumConfig **   <a name="groundstation-Type-AntennaUplinkConfig-spectrumConfig"></a>
Information about the uplink spectral `Config`.
Type: [UplinkSpectrumConfig](API_UplinkSpectrumConfig.md) object
Required: Yes

 ** targetEirp **   <a name="groundstation-Type-AntennaUplinkConfig-targetEirp"></a>
EIRP of the target.
Type: [Eirp](API_Eirp.md) object
Required: Yes

 ** transmitDisabled **   <a name="groundstation-Type-AntennaUplinkConfig-transmitDisabled"></a>
Whether or not uplink transmit is disabled.
Type: Boolean
Required: No

## See Also
<a name="API_AntennaUplinkConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/AntennaUplinkConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/AntennaUplinkConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/AntennaUplinkConfig)
