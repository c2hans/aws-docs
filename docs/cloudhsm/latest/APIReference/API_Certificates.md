---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_Certificates.html
---

# Certificates
<a name="API_Certificates"></a>

Contains one or more certificates or a certificate signing request (CSR).

## Contents
<a name="API_Certificates_Contents"></a>

 ** AwsHardwareCertificate **   <a name="CloudHSMV2-Type-Certificates-AwsHardwareCertificate"></a>
The HSM hardware certificate issued (signed) by AWS CloudHSM.
Type: String
Length Constraints: Maximum length of 20000.
Pattern: `[a-zA-Z0-9+-/=\s]*`
Required: No

 ** ClusterCertificate **   <a name="CloudHSMV2-Type-Certificates-ClusterCertificate"></a>
The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster's owner.
Type: String
Length Constraints: Maximum length of 20000.
Pattern: `[a-zA-Z0-9+-/=\s]*`
Required: No

 ** ClusterCsr **   <a name="CloudHSMV2-Type-Certificates-ClusterCsr"></a>
The cluster's certificate signing request (CSR). The CSR exists only when the cluster's state is `UNINITIALIZED`.
Type: String
Length Constraints: Maximum length of 20000.
Pattern: `[a-zA-Z0-9+-/=\s]*`
Required: No

 ** HsmCertificate **   <a name="CloudHSMV2-Type-Certificates-HsmCertificate"></a>
The HSM certificate issued (signed) by the HSM hardware.
Type: String
Length Constraints: Maximum length of 20000.
Pattern: `[a-zA-Z0-9+-/=\s]*`
Required: No

 ** ManufacturerHardwareCertificate **   <a name="CloudHSMV2-Type-Certificates-ManufacturerHardwareCertificate"></a>
The HSM hardware certificate issued (signed) by the hardware manufacturer.
Type: String
Length Constraints: Maximum length of 20000.
Pattern: `[a-zA-Z0-9+-/=\s]*`
Required: No

## See Also
<a name="API_Certificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/Certificates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/Certificates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/Certificates)
