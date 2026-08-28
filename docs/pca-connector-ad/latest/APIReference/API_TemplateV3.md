---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TemplateV3.html
---

# TemplateV3
<a name="API_TemplateV3"></a>

v3 template schema that uses Key Storage Providers.

## Contents
<a name="API_TemplateV3_Contents"></a>

 ** CertificateValidity **   <a name="PcaConnectorAd-Type-TemplateV3-CertificateValidity"></a>
Certificate validity describes the validity and renewal periods of a certificate.
Type: [CertificateValidity](API_CertificateValidity.md) object
Required: Yes

 ** EnrollmentFlags **   <a name="PcaConnectorAd-Type-TemplateV3-EnrollmentFlags"></a>
Enrollment flags describe the enrollment settings for certificates such as using the existing private key and deleting expired or revoked certificates.
Type: [EnrollmentFlagsV3](API_EnrollmentFlagsV3.md) object
Required: Yes

 ** Extensions **   <a name="PcaConnectorAd-Type-TemplateV3-Extensions"></a>
Extensions describe the key usage extensions and application policies for a template.
Type: [ExtensionsV3](API_ExtensionsV3.md) object
Required: Yes

 ** GeneralFlags **   <a name="PcaConnectorAd-Type-TemplateV3-GeneralFlags"></a>
General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.
Type: [GeneralFlagsV3](API_GeneralFlagsV3.md) object
Required: Yes

 ** HashAlgorithm **   <a name="PcaConnectorAd-Type-TemplateV3-HashAlgorithm"></a>
Specifies the hash algorithm used to hash the private key.
Type: String
Valid Values: `SHA256 | SHA384 | SHA512`
Required: Yes

 ** PrivateKeyAttributes **   <a name="PcaConnectorAd-Type-TemplateV3-PrivateKeyAttributes"></a>
Private key attributes allow you to specify the algorithm, minimal key length, key spec, key usage, and cryptographic providers for the private key of a certificate for v3 templates. V3 templates allow you to use Key Storage Providers.
Type: [PrivateKeyAttributesV3](API_PrivateKeyAttributesV3.md) object
Required: Yes

 ** PrivateKeyFlags **   <a name="PcaConnectorAd-Type-TemplateV3-PrivateKeyFlags"></a>
Private key flags for v3 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, and if an alternate signature algorithm should be used.
Type: [PrivateKeyFlagsV3](API_PrivateKeyFlagsV3.md) object
Required: Yes

 ** SubjectNameFlags **   <a name="PcaConnectorAd-Type-TemplateV3-SubjectNameFlags"></a>
Subject name flags describe the subject name and subject alternate name that is included in a certificate.
Type: [SubjectNameFlagsV3](API_SubjectNameFlagsV3.md) object
Required: Yes

 ** SupersededTemplates **   <a name="PcaConnectorAd-Type-TemplateV3-SupersededTemplates"></a>
List of templates in Active Directory that are superseded by this template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^\s+$)((?![\x5c'\x2b,;<=>#\x22])([\x20-\x7E]))+`
Required: No

## See Also
<a name="API_TemplateV3_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/TemplateV3)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/TemplateV3)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/TemplateV3)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
