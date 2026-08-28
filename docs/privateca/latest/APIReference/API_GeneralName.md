---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_GeneralName.html
---

# GeneralName
<a name="API_GeneralName"></a>

Describes an ASN.1 X.400 `GeneralName` as defined in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280). Only one of the following naming options should be provided. Providing more than one option results in an `InvalidArgsException` error.

## Contents
<a name="API_GeneralName_Contents"></a>

 ** DirectoryName **   <a name="privateca-Type-GeneralName-DirectoryName"></a>
Contains information about the certificate subject. The `Subject` field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The `Subject `must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.
Type: [ASN1Subject](API_ASN1Subject.md) object
Required: No

 ** DnsName **   <a name="privateca-Type-GeneralName-DnsName"></a>
Represents `GeneralName` as a DNS name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 253.
Required: No

 ** EdiPartyName **   <a name="privateca-Type-GeneralName-EdiPartyName"></a>
Represents `GeneralName` as an `EdiPartyName` object.
Type: [EdiPartyName](API_EdiPartyName.md) object
Required: No

 ** IpAddress **   <a name="privateca-Type-GeneralName-IpAddress"></a>
Represents `GeneralName` as an IPv4 or IPv6 address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 39.
Required: No

 ** OtherName **   <a name="privateca-Type-GeneralName-OtherName"></a>
Represents `GeneralName` using an `OtherName` object.
Type: [OtherName](API_OtherName.md) object
Required: No

 ** RegisteredId **   <a name="privateca-Type-GeneralName-RegisteredId"></a>
 Represents `GeneralName` as an object identifier (OID).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
Required: No

 ** Rfc822Name **   <a name="privateca-Type-GeneralName-Rfc822Name"></a>
Represents `GeneralName` as an [RFC 822](https://datatracker.ietf.org/doc/html/rfc822) email address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** UniformResourceIdentifier **   <a name="privateca-Type-GeneralName-UniformResourceIdentifier"></a>
Represents `GeneralName` as a URI.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 253.
Required: No

## See Also
<a name="API_GeneralName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/GeneralName)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/GeneralName)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/GeneralName)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
