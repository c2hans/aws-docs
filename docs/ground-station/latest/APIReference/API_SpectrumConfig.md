---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_SpectrumConfig.html
---

# SpectrumConfig
<a name="API_SpectrumConfig"></a>

Object that describes a spectral `Config`.

## Contents
<a name="API_SpectrumConfig_Contents"></a>

 ** bandwidth **   <a name="groundstation-Type-SpectrumConfig-bandwidth"></a>
Bandwidth of a spectral `Config`. AWS Ground Station currently has the following bandwidth limitations:
+ For `AntennaDownlinkDemodDecodeconfig`, valid values are between 125 kHz to 650 MHz.
+ For `AntennaDownlinkconfig` valid values are between 10 kHz to 54 MHz.
+ For `AntennaUplinkConfig`, valid values are between 10 kHz to 54 MHz.
Type: [FrequencyBandwidth](API_FrequencyBandwidth.md) object
Required: Yes

 ** centerFrequency **   <a name="groundstation-Type-SpectrumConfig-centerFrequency"></a>
Center frequency of a spectral `Config`. Valid values are between 2200 to 2300 MHz and 7750 to 8400 MHz for downlink and 2025 to 2120 MHz for uplink.
Type: [Frequency](API_Frequency.md) object
Required: Yes

 ** polarization **   <a name="groundstation-Type-SpectrumConfig-polarization"></a>
Polarization of a spectral `Config`. Capturing both `"RIGHT_HAND"` and `"LEFT_HAND"` polarization requires two separate configs.
Type: String
Valid Values: `RIGHT_HAND | LEFT_HAND | NONE`
Required: No

## See Also
<a name="API_SpectrumConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/SpectrumConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/SpectrumConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/SpectrumConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
