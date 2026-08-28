---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_ASN1Subject.html
---

# ASN1Subject
<a name="API_ASN1Subject"></a>

Contains information about the certificate subject. The `Subject` field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The `Subject `must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.

## Contents
<a name="API_ASN1Subject_Contents"></a>

 ** CommonName **   <a name="privateca-Type-ASN1Subject-CommonName"></a>
For CA and end-entity certificates in a private PKI, the common name (CN) can be any string within the length limit.
Note: In publicly trusted certificates, the common name must be a fully qualified domain name (FQDN) associated with the certificate subject.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** Country **   <a name="privateca-Type-ASN1Subject-Country"></a>
Two-digit code that specifies the country in which the certificate subject located.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Za-z]{2}`
Required: No

 ** CustomAttributes **   <a name="privateca-Type-ASN1Subject-CustomAttributes"></a>

Contains a sequence of one or more X.500 relative distinguished names (RDNs), each of which consists of an object identifier (OID) and a value. For more information, see NIST’s definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier).
Custom attributes cannot be used in combination with standard attributes.
Type: Array of [CustomAttribute](API_CustomAttribute.md) objects
Array Members: Minimum number of 1 item. Maximum number of 150 items.
Required: No

 ** DistinguishedNameQualifier **   <a name="privateca-Type-ASN1Subject-DistinguishedNameQualifier"></a>
Disambiguating information for the certificate subject.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9'()+-.?:/= ]*`
Required: No

 ** GenerationQualifier **   <a name="privateca-Type-ASN1Subject-GenerationQualifier"></a>
Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3.
Required: No

 ** GivenName **   <a name="privateca-Type-ASN1Subject-GivenName"></a>
First name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Required: No

 ** Initials **   <a name="privateca-Type-ASN1Subject-Initials"></a>
Concatenation that typically contains the first letter of the **GivenName**, the first letter of the middle name if one exists, and the first letter of the **Surname**.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5.
Required: No

 ** Locality **   <a name="privateca-Type-ASN1Subject-Locality"></a>
The locality (such as a city or town) in which the certificate subject is located.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** Organization **   <a name="privateca-Type-ASN1Subject-Organization"></a>
Legal name of the organization with which the certificate subject is affiliated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** OrganizationalUnit **   <a name="privateca-Type-ASN1Subject-OrganizationalUnit"></a>
A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** Pseudonym **   <a name="privateca-Type-ASN1Subject-Pseudonym"></a>
Typically a shortened version of a longer **GivenName**. For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** SerialNumber **   <a name="privateca-Type-ASN1Subject-SerialNumber"></a>
The certificate serial number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9'()+-.?:/= ]*`
Required: No

 ** State **   <a name="privateca-Type-ASN1Subject-State"></a>
State in which the subject of the certificate is located.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** Surname **   <a name="privateca-Type-ASN1Subject-Surname"></a>
Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Required: No

 ** Title **   <a name="privateca-Type-ASN1Subject-Title"></a>
A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

## See Also
<a name="API_ASN1Subject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/ASN1Subject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/ASN1Subject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/ASN1Subject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
