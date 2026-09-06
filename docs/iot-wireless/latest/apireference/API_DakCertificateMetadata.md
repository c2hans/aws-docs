---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DakCertificateMetadata.html
---

# DakCertificateMetadata
<a name="API_DakCertificateMetadata"></a>

The device attestation key (DAK) information.

## Contents
<a name="API_DakCertificateMetadata_Contents"></a>

 ** CertificateId **   <a name="iotwireless-Type-DakCertificateMetadata-CertificateId"></a>
The certificate ID for the DAK.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** ApId **   <a name="iotwireless-Type-DakCertificateMetadata-ApId"></a>
The advertised product ID (APID) that's used for pre-production and production applications.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** DeviceTypeId **   <a name="iotwireless-Type-DakCertificateMetadata-DeviceTypeId"></a>
The device type ID that's used for prototyping applications.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** FactorySupport **   <a name="iotwireless-Type-DakCertificateMetadata-FactorySupport"></a>
Whether factory support has been enabled.
Type: Boolean
Required: No

 ** MaxAllowedSignature **   <a name="iotwireless-Type-DakCertificateMetadata-MaxAllowedSignature"></a>
The maximum number of signatures that the DAK can sign. A value of `-1` indicates that there's no device limit.
Type: Integer
Required: No

## See Also
<a name="API_DakCertificateMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/DakCertificateMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/DakCertificateMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/DakCertificateMetadata)
