---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_LteNetworkMeasurements.html
---

# LteNetworkMeasurements
<a name="API_LteNetworkMeasurements"></a>

LTE network measurements.

## Contents
<a name="API_LteNetworkMeasurements_Contents"></a>

 ** CellId **   <a name="location-Type-LteNetworkMeasurements-CellId"></a>
E-UTRAN Cell Identifier (ECI).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 268435455.
Required: Yes

 ** Earfcn **   <a name="location-Type-LteNetworkMeasurements-Earfcn"></a>
E-UTRA (Evolved Universal Terrestrial Radio Access) absolute radio frequency channel number (EARFCN).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 262143.
Required: Yes

 ** Pci **   <a name="location-Type-LteNetworkMeasurements-Pci"></a>
Physical Cell ID (PCI).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 503.
Required: Yes

 ** Rsrp **   <a name="location-Type-LteNetworkMeasurements-Rsrp"></a>
Signal power of the reference signal received, measured in dBm (decibel-milliwatts).
Type: Integer
Valid Range: Minimum value of -140. Maximum value of -44.
Required: No

 ** Rsrq **   <a name="location-Type-LteNetworkMeasurements-Rsrq"></a>
Signal quality of the reference Signal received, measured in decibels (dB).
Type: Float
Valid Range: Minimum value of -19.5. Maximum value of -3.
Required: No

## See Also
<a name="API_LteNetworkMeasurements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/LteNetworkMeasurements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/LteNetworkMeasurements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/LteNetworkMeasurements)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
