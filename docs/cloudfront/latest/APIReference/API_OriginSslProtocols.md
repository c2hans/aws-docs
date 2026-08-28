---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_OriginSslProtocols.html
---

# OriginSslProtocols
<a name="API_OriginSslProtocols"></a>

A complex type that contains information about the SSL/TLS protocols that CloudFront can use when establishing an HTTPS connection with your origin.

## Contents
<a name="API_OriginSslProtocols_Contents"></a>

 ** Items **   <a name="cloudfront-Type-OriginSslProtocols-Items"></a>
A list that contains allowed SSL/TLS protocols for this distribution.
Type: Array of strings
Valid Values: `SSLv3 | TLSv1 | TLSv1.1 | TLSv1.2`
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-OriginSslProtocols-Quantity"></a>
The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
Type: Integer
Required: Yes

## See Also
<a name="API_OriginSslProtocols_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginSslProtocols)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginSslProtocols)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginSslProtocols)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
