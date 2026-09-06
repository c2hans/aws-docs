---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_EnrollmentFlagsV3.html
---

# EnrollmentFlagsV3
<a name="API_EnrollmentFlagsV3"></a>

Template configurations for v3 template schema.

## Contents
<a name="API_EnrollmentFlagsV3_Contents"></a>

 ** EnableKeyReuseOnNtTokenKeysetStorageFull **   <a name="PcaConnectorAd-Type-EnrollmentFlagsV3-EnableKeyReuseOnNtTokenKeysetStorageFull"></a>
Allow renewal using the same key.
Type: Boolean
Required: No

 ** IncludeSymmetricAlgorithms **   <a name="PcaConnectorAd-Type-EnrollmentFlagsV3-IncludeSymmetricAlgorithms"></a>
Include symmetric algorithms allowed by the subject.
Type: Boolean
Required: No

 ** NoSecurityExtension **   <a name="PcaConnectorAd-Type-EnrollmentFlagsV3-NoSecurityExtension"></a>
This flag instructs the CA to not include the security extension szOID\_NTDS\_CA\_SECURITY\_EXT (OID:1.3.6.1.4.1.311.25.2), as specified in [MS-WCCE] sections 2.2.2.7.7.4 and 3.2.2.6.2.1.4.5.9, in the issued certificate. This addresses a Windows Kerberos elevation-of-privilege vulnerability.
Type: Boolean
Required: No

 ** RemoveInvalidCertificateFromPersonalStore **   <a name="PcaConnectorAd-Type-EnrollmentFlagsV3-RemoveInvalidCertificateFromPersonalStore"></a>
Delete expired or revoked certificates instead of archiving them.
Type: Boolean
Required: No

 ** UserInteractionRequired **   <a name="PcaConnectorAd-Type-EnrollmentFlagsV3-UserInteractionRequired"></a>
Require user interaction when the subject is enrolled and the private key associated with the certificate is used.
Type: Boolean
Required: No

## See Also
<a name="API_EnrollmentFlagsV3_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/EnrollmentFlagsV3)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/EnrollmentFlagsV3)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/EnrollmentFlagsV3)
