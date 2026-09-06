---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LoRaWANServiceProfile.html
---

# LoRaWANServiceProfile
<a name="API_LoRaWANServiceProfile"></a>

LoRaWANServiceProfile object.

## Contents
<a name="API_LoRaWANServiceProfile_Contents"></a>

 ** AddGwMetadata **   <a name="iotwireless-Type-LoRaWANServiceProfile-AddGwMetadata"></a>
The AddGWMetaData value.
Type: Boolean
Required: No

 ** DrMax **   <a name="iotwireless-Type-LoRaWANServiceProfile-DrMax"></a>
The DrMax value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** DrMin **   <a name="iotwireless-Type-LoRaWANServiceProfile-DrMin"></a>
The DrMin value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** NbTransMax **   <a name="iotwireless-Type-LoRaWANServiceProfile-NbTransMax"></a>
The maximum number of transmissions.
Default: `3`
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** NbTransMin **   <a name="iotwireless-Type-LoRaWANServiceProfile-NbTransMin"></a>
The minimum number of transmissions.
Default: `0`
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** PrAllowed **   <a name="iotwireless-Type-LoRaWANServiceProfile-PrAllowed"></a>
The PRAllowed value that describes whether passive roaming is allowed.
Type: Boolean
Required: No

 ** RaAllowed **   <a name="iotwireless-Type-LoRaWANServiceProfile-RaAllowed"></a>
The RAAllowed value that describes whether roaming activation is allowed.
Type: Boolean
Required: No

 ** TxPowerIndexMax **   <a name="iotwireless-Type-LoRaWANServiceProfile-TxPowerIndexMax"></a>
The Transmit Power Index maximum.
Default: `15`
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** TxPowerIndexMin **   <a name="iotwireless-Type-LoRaWANServiceProfile-TxPowerIndexMin"></a>
The Transmit Power Index minimum.
Default: `0`
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

## See Also
<a name="API_LoRaWANServiceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LoRaWANServiceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LoRaWANServiceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LoRaWANServiceProfile)
