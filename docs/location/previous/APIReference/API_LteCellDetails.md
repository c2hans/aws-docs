---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_LteCellDetails.html
---

# LteCellDetails
<a name="API_LteCellDetails"></a>

Details about the Long-Term Evolution (LTE) network.

## Contents
<a name="API_LteCellDetails_Contents"></a>

 ** CellId **   <a name="location-Type-LteCellDetails-CellId"></a>
The E-UTRAN Cell Identifier (ECI).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 268435455.
Required: Yes

 ** Mcc **   <a name="location-Type-LteCellDetails-Mcc"></a>
The Mobile Country Code (MCC).
Type: Integer
Valid Range: Minimum value of 200. Maximum value of 999.
Required: Yes

 ** Mnc **   <a name="location-Type-LteCellDetails-Mnc"></a>
The Mobile Network Code (MNC)
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 999.
Required: Yes

 ** LocalId **   <a name="location-Type-LteCellDetails-LocalId"></a>
The LTE local identification information (local ID).
Type: [LteLocalId](API_LteLocalId.md) object
Required: No

 ** NetworkMeasurements **   <a name="location-Type-LteCellDetails-NetworkMeasurements"></a>
The network measurements.
Type: Array of [LteNetworkMeasurements](API_LteNetworkMeasurements.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** NrCapable **   <a name="location-Type-LteCellDetails-NrCapable"></a>
Indicates whether the LTE object is capable of supporting NR (new radio).
Type: Boolean
Required: No

 ** Rsrp **   <a name="location-Type-LteCellDetails-Rsrp"></a>
Signal power of the reference signal received, measured in decibel-milliwatts (dBm).
Type: Integer
Valid Range: Minimum value of -140. Maximum value of -44.
Required: No

 ** Rsrq **   <a name="location-Type-LteCellDetails-Rsrq"></a>
Signal quality of the reference Signal received, measured in decibels (dB).
Type: Float
Valid Range: Minimum value of -19.5. Maximum value of -3.
Required: No

 ** Tac **   <a name="location-Type-LteCellDetails-Tac"></a>
LTE Tracking Area Code (TAC).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** TimingAdvance **   <a name="location-Type-LteCellDetails-TimingAdvance"></a>
Timing Advance (TA).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1282.
Required: No

## See Also
<a name="API_LteCellDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/LteCellDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/LteCellDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/LteCellDetails)
