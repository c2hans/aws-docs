---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_Extensions.html
---

# Extensions
<a name="API_Extensions"></a>

Contains X.509 extension information for a certificate.

## Contents
<a name="API_Extensions_Contents"></a>

 ** CertificatePolicies **   <a name="privateca-Type-Extensions-CertificatePolicies"></a>
Contains a sequence of one or more policy information terms, each of which consists of an object identifier (OID) and optional qualifiers. For more information, see NIST's definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier).
In an end-entity certificate, these terms indicate the policy under which the certificate was issued and the purposes for which it may be used. In a CA certificate, these terms limit the set of policies for certification paths that include this certificate.
Type: Array of [PolicyInformation](API_PolicyInformation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** CustomExtensions **   <a name="privateca-Type-Extensions-CustomExtensions"></a>

Contains a sequence of one or more X.509 extensions, each of which consists of an object identifier (OID), a base64-encoded value, and the critical flag. For more information, see the [Global OID reference database.](https://oidref.com/2.5.29)
Type: Array of [CustomExtension](API_CustomExtension.md) objects
Array Members: Minimum number of 1 item. Maximum number of 150 items.
Required: No

 ** ExtendedKeyUsage **   <a name="privateca-Type-Extensions-ExtendedKeyUsage"></a>
Specifies additional purposes for which the certified public key may be used other than basic purposes indicated in the `KeyUsage` extension.
Type: Array of [ExtendedKeyUsage](API_ExtendedKeyUsage.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** KeyUsage **   <a name="privateca-Type-Extensions-KeyUsage"></a>
Defines one or more purposes for which the key contained in the certificate can be used. Default value for each option is false.
Type: [KeyUsage](API_KeyUsage.md) object
Required: No

 ** SubjectAlternativeNames **   <a name="privateca-Type-Extensions-SubjectAlternativeNames"></a>
The subject alternative name extension allows identities to be bound to the subject of the certificate. These identities may be included in addition to or in place of the identity in the subject field of the certificate.
Type: Array of [GeneralName](API_GeneralName.md) objects
Array Members: Minimum number of 1 item. Maximum number of 150 items.
Required: No

## See Also
<a name="API_Extensions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/Extensions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/Extensions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/Extensions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
