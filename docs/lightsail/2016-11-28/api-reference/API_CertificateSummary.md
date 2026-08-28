---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CertificateSummary.html
---

# CertificateSummary
<a name="API_CertificateSummary"></a>

Describes an Amazon Lightsail SSL/TLS certificate.

## Contents
<a name="API_CertificateSummary_Contents"></a>

 ** certificateArn **   <a name="Lightsail-Type-CertificateSummary-certificateArn"></a>
The Amazon Resource Name (ARN) of the certificate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** certificateDetail **   <a name="Lightsail-Type-CertificateSummary-certificateDetail"></a>
An object that describes a certificate in detail.
Type: [Certificate](API_Certificate.md) object
Required: No

 ** certificateName **   <a name="Lightsail-Type-CertificateSummary-certificateName"></a>
The name of the certificate.
Type: String
Required: No

 ** domainName **   <a name="Lightsail-Type-CertificateSummary-domainName"></a>
The domain name of the certificate.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-CertificateSummary-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_CertificateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CertificateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CertificateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CertificateSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
