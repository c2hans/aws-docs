---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SidewalkDevice.html
---

# SidewalkDevice
<a name="API_SidewalkDevice"></a>

Sidewalk device object.

## Contents
<a name="API_SidewalkDevice_Contents"></a>

 ** AmazonId **   <a name="iotwireless-Type-SidewalkDevice-AmazonId"></a>
The Sidewalk Amazon ID.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** CertificateId **   <a name="iotwireless-Type-SidewalkDevice-CertificateId"></a>
The ID of the Sidewalk device profile.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** DeviceCertificates **   <a name="iotwireless-Type-SidewalkDevice-DeviceCertificates"></a>
The sidewalk device certificates for Ed25519 and P256r1.
Type: Array of [CertificateList](API_CertificateList.md) objects
Required: No

 ** DeviceProfileId **   <a name="iotwireless-Type-SidewalkDevice-DeviceProfileId"></a>
The ID of the Sidewalk device profile.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Positioning **   <a name="iotwireless-Type-SidewalkDevice-Positioning"></a>
The Positioning object of the Sidewalk device.
Type: [SidewalkPositioning](API_SidewalkPositioning.md) object
Required: No

 ** PrivateKeys **   <a name="iotwireless-Type-SidewalkDevice-PrivateKeys"></a>
The Sidewalk device private keys that will be used for onboarding the device.
Type: Array of [CertificateList](API_CertificateList.md) objects
Required: No

 ** SidewalkId **   <a name="iotwireless-Type-SidewalkDevice-SidewalkId"></a>
The sidewalk device identification.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** SidewalkManufacturingSn **   <a name="iotwireless-Type-SidewalkDevice-SidewalkManufacturingSn"></a>
The Sidewalk manufacturing series number.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** Status **   <a name="iotwireless-Type-SidewalkDevice-Status"></a>
The Sidewalk device status, such as provisioned or registered.
Type: String
Valid Values: `PROVISIONED | REGISTERED | ACTIVATED | UNKNOWN`
Required: No

## See Also
<a name="API_SidewalkDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/SidewalkDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/SidewalkDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/SidewalkDevice)
