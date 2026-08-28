---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_OcspConfiguration.html
---

# OcspConfiguration
<a name="API_OcspConfiguration"></a>

Contains information to enable and configure Online Certificate Status Protocol (OCSP) for validating certificate revocation status.

When you revoke a certificate, OCSP responses may take up to 60 minutes to reflect the new status.

## Contents
<a name="API_OcspConfiguration_Contents"></a>

 ** Enabled **   <a name="privateca-Type-OcspConfiguration-Enabled"></a>
Flag enabling use of the Online Certificate Status Protocol (OCSP) for validating certificate revocation status.
Type: Boolean
Required: Yes

 ** OcspCustomCname **   <a name="privateca-Type-OcspConfiguration-OcspCustomCname"></a>
By default, AWS Private CA injects an AWS domain into certificates being validated by the Online Certificate Status Protocol (OCSP). A customer can alternatively use this object to define a CNAME specifying a customized OCSP domain.
The content of a Canonical Name (CNAME) record must conform to [RFC2396](https://www.ietf.org/rfc/rfc2396.txt) restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as "http://" or "https://".
For more information, see [Customizing Online Certificate Status Protocol (OCSP) ](https://docs.aws.amazon.com/privateca/latest/userguide/ocsp-customize.html) in the * AWS Private Certificate Authority User Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 253.
Pattern: `[-a-zA-Z0-9;/?:@&=+$,%_.!~*()']*`
Required: No

## See Also
<a name="API_OcspConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/OcspConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/OcspConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/OcspConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
