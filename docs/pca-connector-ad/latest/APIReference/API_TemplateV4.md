---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TemplateV4.html
---

# TemplateV4
<a name="API_TemplateV4"></a>

v4 template schema that can use either Legacy Cryptographic Providers or Key Storage Providers.

## Contents
<a name="API_TemplateV4_Contents"></a>

 ** CertificateValidity **   <a name="PcaConnectorAd-Type-TemplateV4-CertificateValidity"></a>
Certificate validity describes the validity and renewal periods of a certificate.
Type: [CertificateValidity](API_CertificateValidity.md) object
Required: Yes

 ** EnrollmentFlags **   <a name="PcaConnectorAd-Type-TemplateV4-EnrollmentFlags"></a>
Enrollment flags describe the enrollment settings for certificates using the existing private key and deleting expired or revoked certificates.
Type: [EnrollmentFlagsV4](API_EnrollmentFlagsV4.md) object
Required: Yes

 ** Extensions **   <a name="PcaConnectorAd-Type-TemplateV4-Extensions"></a>
Extensions describe the key usage extensions and application policies for a template.
Type: [ExtensionsV4](API_ExtensionsV4.md) object
Required: Yes

 ** GeneralFlags **   <a name="PcaConnectorAd-Type-TemplateV4-GeneralFlags"></a>
General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.
Type: [GeneralFlagsV4](API_GeneralFlagsV4.md) object
Required: Yes

 ** PrivateKeyAttributes **   <a name="PcaConnectorAd-Type-TemplateV4-PrivateKeyAttributes"></a>
Private key attributes allow you to specify the minimal key length, key spec, key usage, and cryptographic providers for the private key of a certificate for v4 templates. V4 templates allow you to use either Key Storage Providers or Legacy Cryptographic Service Providers. You specify the cryptography provider category in private key flags.
Type: [PrivateKeyAttributesV4](API_PrivateKeyAttributesV4.md) object
Required: Yes

 ** PrivateKeyFlags **   <a name="PcaConnectorAd-Type-TemplateV4-PrivateKeyFlags"></a>
Private key flags for v4 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, if an alternate signature algorithm should be used, and if certificates are renewed using the same private key.
Type: [PrivateKeyFlagsV4](API_PrivateKeyFlagsV4.md) object
Required: Yes

 ** SubjectNameFlags **   <a name="PcaConnectorAd-Type-TemplateV4-SubjectNameFlags"></a>
Subject name flags describe the subject name and subject alternate name that is included in a certificate.
Type: [SubjectNameFlagsV4](API_SubjectNameFlagsV4.md) object
Required: Yes

 ** HashAlgorithm **   <a name="PcaConnectorAd-Type-TemplateV4-HashAlgorithm"></a>
Specifies the hash algorithm used to hash the private key. Hash algorithm can only be specified when using Key Storage Providers.
Type: String
Valid Values: `SHA256 | SHA384 | SHA512`
Required: No

 ** SupersededTemplates **   <a name="PcaConnectorAd-Type-TemplateV4-SupersededTemplates"></a>
List of templates in Active Directory that are superseded by this template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^\s+$)((?![\x5c'\x2b,;<=>#\x22])([\x20-\x7E]))+`
Required: No

## See Also
<a name="API_TemplateV4_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/TemplateV4)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/TemplateV4)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/TemplateV4)
