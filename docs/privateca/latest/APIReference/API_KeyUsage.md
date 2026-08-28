---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_KeyUsage.html
---

# KeyUsage
<a name="API_KeyUsage"></a>

Defines one or more purposes for which the key contained in the certificate can be used. Default value for each option is false.

## Contents
<a name="API_KeyUsage_Contents"></a>

 ** CRLSign **   <a name="privateca-Type-KeyUsage-CRLSign"></a>
Key can be used to sign CRLs.
Type: Boolean
Required: No

 ** DataEncipherment **   <a name="privateca-Type-KeyUsage-DataEncipherment"></a>
Key can be used to decipher data.
Type: Boolean
Required: No

 ** DecipherOnly **   <a name="privateca-Type-KeyUsage-DecipherOnly"></a>
Key can be used only to decipher data.
Type: Boolean
Required: No

 ** DigitalSignature **   <a name="privateca-Type-KeyUsage-DigitalSignature"></a>
 Key can be used for digital signing.
Type: Boolean
Required: No

 ** EncipherOnly **   <a name="privateca-Type-KeyUsage-EncipherOnly"></a>
Key can be used only to encipher data.
Type: Boolean
Required: No

 ** KeyAgreement **   <a name="privateca-Type-KeyUsage-KeyAgreement"></a>
Key can be used in a key-agreement protocol.
Type: Boolean
Required: No

 ** KeyCertSign **   <a name="privateca-Type-KeyUsage-KeyCertSign"></a>
Key can be used to sign certificates.
Type: Boolean
Required: No

 ** KeyEncipherment **   <a name="privateca-Type-KeyUsage-KeyEncipherment"></a>
Key can be used to encipher data.
Type: Boolean
Required: No

 ** NonRepudiation **   <a name="privateca-Type-KeyUsage-NonRepudiation"></a>
Key can be used for non-repudiation.
Type: Boolean
Required: No

## See Also
<a name="API_KeyUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/KeyUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/KeyUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/KeyUsage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
