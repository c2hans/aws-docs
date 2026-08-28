---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_KeyUsage.html
---

# KeyUsage
<a name="API_KeyUsage"></a>

The Key Usage X.509 v3 extension defines the purpose of the public key contained in the certificate.

## Contents
<a name="API_KeyUsage_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="ACM-Type-KeyUsage-Name"></a>
A string value that contains a Key Usage extension name.
Type: String
Valid Values: `DIGITAL_SIGNATURE | NON_REPUDIATION | KEY_ENCIPHERMENT | DATA_ENCIPHERMENT | KEY_AGREEMENT | CERTIFICATE_SIGNING | CRL_SIGNING | ENCIPHER_ONLY | DECIPHER_ONLY | ANY | CUSTOM`
Required: No

## See Also
<a name="API_KeyUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/KeyUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/KeyUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/KeyUsage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
