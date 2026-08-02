---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TemplateV2.html
---

# TemplateV2
<a name="API_TemplateV2"></a>

v2 template schema that uses Legacy Cryptographic Providers.

## Contents
<a name="API_TemplateV2_Contents"></a>

 ** CertificateValidity **   <a name="PcaConnectorAd-Type-TemplateV2-CertificateValidity"></a>
Certificate validity describes the validity and renewal periods of a certificate.
Type: [CertificateValidity](API_CertificateValidity.md) object
Required: Yes

 ** EnrollmentFlags **   <a name="PcaConnectorAd-Type-TemplateV2-EnrollmentFlags"></a>
Enrollment flags describe the enrollment settings for certificates such as using the existing private key and deleting expired or revoked certificates.
Type: [EnrollmentFlagsV2](API_EnrollmentFlagsV2.md) object
Required: Yes

 ** Extensions **   <a name="PcaConnectorAd-Type-TemplateV2-Extensions"></a>
Extensions describe the key usage extensions and application policies for a template.
Type: [ExtensionsV2](API_ExtensionsV2.md) object
Required: Yes

 ** GeneralFlags **   <a name="PcaConnectorAd-Type-TemplateV2-GeneralFlags"></a>
General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.
Type: [GeneralFlagsV2](API_GeneralFlagsV2.md) object
Required: Yes

 ** PrivateKeyAttributes **   <a name="PcaConnectorAd-Type-TemplateV2-PrivateKeyAttributes"></a>
Private key attributes allow you to specify the minimal key length, key spec, and cryptographic providers for the private key of a certificate for v2 templates. V2 templates allow you to use Legacy Cryptographic Service Providers.
Type: [PrivateKeyAttributesV2](API_PrivateKeyAttributesV2.md) object
Required: Yes

 ** PrivateKeyFlags **   <a name="PcaConnectorAd-Type-TemplateV2-PrivateKeyFlags"></a>
Private key flags for v2 templates specify the client compatibility, if the private key can be exported, and if user input is required when using a private key.
Type: [PrivateKeyFlagsV2](API_PrivateKeyFlagsV2.md) object
Required: Yes

 ** SubjectNameFlags **   <a name="PcaConnectorAd-Type-TemplateV2-SubjectNameFlags"></a>
Subject name flags describe the subject name and subject alternate name that is included in a certificate.
Type: [SubjectNameFlagsV2](API_SubjectNameFlagsV2.md) object
Required: Yes

 ** SupersededTemplates **   <a name="PcaConnectorAd-Type-TemplateV2-SupersededTemplates"></a>
List of templates in Active Directory that are superseded by this template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^\s+$)((?![\x5c'\x2b,;<=>#\x22])([\x20-\x7E]))+`
Required: No

## See Also
<a name="API_TemplateV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/TemplateV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/TemplateV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/TemplateV2)
