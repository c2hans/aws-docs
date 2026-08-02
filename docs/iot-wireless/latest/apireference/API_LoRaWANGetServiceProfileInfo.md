---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LoRaWANGetServiceProfileInfo.html
---

# LoRaWANGetServiceProfileInfo
<a name="API_LoRaWANGetServiceProfileInfo"></a>

LoRaWANGetServiceProfileInfo object.

## Contents
<a name="API_LoRaWANGetServiceProfileInfo_Contents"></a>

 ** AddGwMetadata **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-AddGwMetadata"></a>
The AddGWMetaData value.
Type: Boolean
Required: No

 ** ChannelMask **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-ChannelMask"></a>
The ChannelMask value.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** DevStatusReqFreq **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-DevStatusReqFreq"></a>
The DevStatusReqFreq value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** DlBucketSize **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-DlBucketSize"></a>
The DLBucketSize value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** DlRate **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-DlRate"></a>
The DLRate value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** DlRatePolicy **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-DlRatePolicy"></a>
The DLRatePolicy value.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** DrMax **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-DrMax"></a>
The DRMax value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** DrMin **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-DrMin"></a>
The DRMin value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** HrAllowed **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-HrAllowed"></a>
The HRAllowed value that describes whether handover roaming is allowed.
Type: Boolean
Required: No

 ** MinGwDiversity **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-MinGwDiversity"></a>
The MinGwDiversity value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** NbTransMax **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-NbTransMax"></a>
The maximum number of transmissions.
Default: `3`
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** NbTransMin **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-NbTransMin"></a>
The minimum number of transmissions.
Default: `0`
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** NwkGeoLoc **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-NwkGeoLoc"></a>
The NwkGeoLoc value.
Type: Boolean
Required: No

 ** PrAllowed **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-PrAllowed"></a>
The PRAllowed value that describes whether passive roaming is allowed.
Type: Boolean
Required: No

 ** RaAllowed **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-RaAllowed"></a>
The RAAllowed value that describes whether roaming activation is allowed.
Type: Boolean
Required: No

 ** ReportDevStatusBattery **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-ReportDevStatusBattery"></a>
The ReportDevStatusBattery value.
Type: Boolean
Required: No

 ** ReportDevStatusMargin **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-ReportDevStatusMargin"></a>
The ReportDevStatusMargin value.
Type: Boolean
Required: No

 ** TargetPer **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-TargetPer"></a>
The TargetPER value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** TxPowerIndexMax **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-TxPowerIndexMax"></a>
The Transmit Power Index maximum value.
Default: `15`
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** TxPowerIndexMin **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-TxPowerIndexMin"></a>
The Transmit Power Index minimum value.
Default: `0`
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** UlBucketSize **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-UlBucketSize"></a>
The ULBucketSize value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** UlRate **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-UlRate"></a>
The ULRate value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** UlRatePolicy **   <a name="iotwireless-Type-LoRaWANGetServiceProfileInfo-UlRatePolicy"></a>
The ULRatePolicy value.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_LoRaWANGetServiceProfileInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LoRaWANGetServiceProfileInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LoRaWANGetServiceProfileInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LoRaWANGetServiceProfileInfo)
