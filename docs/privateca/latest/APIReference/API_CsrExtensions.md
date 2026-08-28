---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_CsrExtensions.html
---

# CsrExtensions
<a name="API_CsrExtensions"></a>

Describes the certificate extensions to be added to the certificate signing request (CSR).

## Contents
<a name="API_CsrExtensions_Contents"></a>

 ** KeyUsage **   <a name="privateca-Type-CsrExtensions-KeyUsage"></a>
Indicates the purpose of the certificate and of the key contained in the certificate.
Type: [KeyUsage](API_KeyUsage.md) object
Required: No

 ** SubjectInformationAccess **   <a name="privateca-Type-CsrExtensions-SubjectInformationAccess"></a>
For CA certificates, provides a path to additional information pertaining to the CA, such as revocation and policy. For more information, see [Subject Information Access](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.2.2) in RFC 5280.
Type: Array of [AccessDescription](API_AccessDescription.md) objects
Required: No

## See Also
<a name="API_CsrExtensions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/CsrExtensions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/CsrExtensions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/CsrExtensions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
