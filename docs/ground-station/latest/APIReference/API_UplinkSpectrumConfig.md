---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UplinkSpectrumConfig.html
---

# UplinkSpectrumConfig
<a name="API_UplinkSpectrumConfig"></a>

Information about the uplink spectral `Config`.

## Contents
<a name="API_UplinkSpectrumConfig_Contents"></a>

 ** centerFrequency **   <a name="groundstation-Type-UplinkSpectrumConfig-centerFrequency"></a>
Center frequency of an uplink spectral `Config`. Valid values are between 2025 to 2120 MHz.
Type: [Frequency](API_Frequency.md) object
Required: Yes

 ** polarization **   <a name="groundstation-Type-UplinkSpectrumConfig-polarization"></a>
Polarization of an uplink spectral `Config`. Capturing both `"RIGHT_HAND"` and `"LEFT_HAND"` polarization requires two separate configs.
Type: String
Valid Values: `RIGHT_HAND | LEFT_HAND | NONE`
Required: No

## See Also
<a name="API_UplinkSpectrumConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/UplinkSpectrumConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/UplinkSpectrumConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/UplinkSpectrumConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
