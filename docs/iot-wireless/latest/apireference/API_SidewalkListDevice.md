---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SidewalkListDevice.html
---

# SidewalkListDevice
<a name="API_SidewalkListDevice"></a>

Sidewalk object used by list functions.

## Contents
<a name="API_SidewalkListDevice_Contents"></a>

 ** AmazonId **   <a name="iotwireless-Type-SidewalkListDevice-AmazonId"></a>
The Sidewalk Amazon ID.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** DeviceCertificates **   <a name="iotwireless-Type-SidewalkListDevice-DeviceCertificates"></a>
The sidewalk device certificates for Ed25519 and P256r1.
Type: Array of [CertificateList](API_CertificateList.md) objects
Required: No

 ** DeviceProfileId **   <a name="iotwireless-Type-SidewalkListDevice-DeviceProfileId"></a>
Sidewalk object used by list functions.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Positioning **   <a name="iotwireless-Type-SidewalkListDevice-Positioning"></a>
The Positioning object of the Sidewalk device.
Type: [SidewalkPositioning](API_SidewalkPositioning.md) object
Required: No

 ** SidewalkId **   <a name="iotwireless-Type-SidewalkListDevice-SidewalkId"></a>
The sidewalk device identification.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** SidewalkManufacturingSn **   <a name="iotwireless-Type-SidewalkListDevice-SidewalkManufacturingSn"></a>
The Sidewalk manufacturing series number.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** Status **   <a name="iotwireless-Type-SidewalkListDevice-Status"></a>
The status of the Sidewalk devices, such as provisioned or registered.
Type: String
Valid Values: `PROVISIONED | REGISTERED | ACTIVATED | UNKNOWN`
Required: No

## See Also
<a name="API_SidewalkListDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/SidewalkListDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/SidewalkListDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/SidewalkListDevice)
