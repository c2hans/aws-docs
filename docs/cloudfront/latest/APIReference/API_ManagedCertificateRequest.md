---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ManagedCertificateRequest.html
---

# ManagedCertificateRequest
<a name="API_ManagedCertificateRequest"></a>

An object that represents the request for the Amazon CloudFront managed ACM certificate.

## Contents
<a name="API_ManagedCertificateRequest_Contents"></a>

 ** ValidationTokenHost **   <a name="cloudfront-Type-ManagedCertificateRequest-ValidationTokenHost"></a>
Specify how the HTTP validation token will be served when requesting the CloudFront managed ACM certificate.
+ For `cloudfront`, CloudFront will automatically serve the validation token. Choose this mode if you can point the domain's DNS to CloudFront immediately.
+ For `self-hosted`, you serve the validation token from your existing infrastructure. Choose this mode when you need to maintain current traffic flow while your certificate is being issued. You can place the validation token at the well-known path on your existing web server, wait for ACM to validate and issue the certificate, and then update your DNS to point to CloudFront.
Type: String
Valid Values: `cloudfront | self-hosted`
Required: Yes

 ** CertificateTransparencyLoggingPreference **   <a name="cloudfront-Type-ManagedCertificateRequest-CertificateTransparencyLoggingPreference"></a>
You can opt out of certificate transparency logging by specifying the `disabled` option. Opt in by specifying `enabled`. For more information, see [Certificate Transparency Logging ](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency) in the * AWS Certificate Manager User Guide*.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** PrimaryDomainName **   <a name="cloudfront-Type-ManagedCertificateRequest-PrimaryDomainName"></a>
The primary domain name associated with the CloudFront managed ACM certificate.
Type: String
Required: No

## See Also
<a name="API_ManagedCertificateRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ManagedCertificateRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ManagedCertificateRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ManagedCertificateRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
