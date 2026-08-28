---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ViewerCertificate.html
---

# ViewerCertificate
<a name="API_ViewerCertificate"></a>

A complex type that determines the distribution's SSL/TLS configuration for communicating with viewers.

If the distribution doesn't use `Aliases` (also known as alternate domain names or CNAMEs)—that is, if the distribution uses the CloudFront domain name such as `d111111abcdef8.cloudfront.net`—set `CloudFrontDefaultCertificate` to `true` and leave all other fields empty.

If the distribution uses `Aliases` (alternate domain names or CNAMEs), use the fields in this type to specify the following settings:
+ Which viewers the distribution accepts HTTPS connections from: only viewers that support [server name indication (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication) (recommended), or all viewers including those that don't support SNI.
  + To accept HTTPS connections from only viewers that support SNI, set `SSLSupportMethod` to `sni-only`. This is recommended. Most browsers and clients support SNI. (In CloudFormation, the field name is `SslSupportMethod`. Note the different capitalization.)
  + To accept HTTPS connections from all viewers, including those that don't support SNI, set `SSLSupportMethod` to `vip`. This is not recommended, and results in additional monthly charges from CloudFront. (In CloudFormation, the field name is `SslSupportMethod`. Note the different capitalization.)
+ The minimum SSL/TLS protocol version that the distribution can use to communicate with viewers. To specify a minimum version, choose a value for `MinimumProtocolVersion`. For more information, see [Security Policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValues-security-policy) in the *Amazon CloudFront Developer Guide*.
+ The location of the SSL/TLS certificate, [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) (recommended) or [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html). You specify the location by setting a value in one of the following fields (not both):
  +  `ACMCertificateArn` (In CloudFormation, this field name is `AcmCertificateArn`. Note the different capitalization.)
  +  `IAMCertificateId` (In CloudFormation, this field name is `IamCertificateId`. Note the different capitalization.)

All distributions support HTTPS connections from viewers. To require viewers to use HTTPS only, or to redirect them from HTTP to HTTPS, use `ViewerProtocolPolicy` in the `CacheBehavior` or `DefaultCacheBehavior`. To specify how CloudFront should use SSL/TLS to communicate with your custom origin, use `CustomOriginConfig`.

For more information, see [Using HTTPS with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) and [ Using Alternate Domain Names and HTTPS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-alternate-domain-names.html) in the *Amazon CloudFront Developer Guide*.

## Contents
<a name="API_ViewerCertificate_Contents"></a>

 ** ACMCertificateArn **   <a name="cloudfront-Type-ViewerCertificate-ACMCertificateArn"></a>
In CloudFormation, this field name is `AcmCertificateArn`. Note the different capitalization.
If the distribution uses `Aliases` (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html), provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (`us-east-1`).
If you specify an ACM certificate ARN, you must also specify values for `MinimumProtocolVersion` and `SSLSupportMethod`. (In CloudFormation, the field name is `SslSupportMethod`. Note the different capitalization.)
Type: String
Required: No

 ** Certificate **   <a name="cloudfront-Type-ViewerCertificate-Certificate"></a>
This field is deprecated. Use one of the following fields instead:
+  `ACMCertificateArn` (In CloudFormation, this field name is `AcmCertificateArn`. Note the different capitalization.)
+  `IAMCertificateId` (In CloudFormation, this field name is `IamCertificateId`. Note the different capitalization.)
+  `CloudFrontDefaultCertificate`
Type: String
Required: No

 ** CertificateSource **   <a name="cloudfront-Type-ViewerCertificate-CertificateSource"></a>
This field is deprecated. Use one of the following fields instead:
+  `ACMCertificateArn` (In CloudFormation, this field name is `AcmCertificateArn`. Note the different capitalization.)
+  `IAMCertificateId` (In CloudFormation, this field name is `IamCertificateId`. Note the different capitalization.)
+  `CloudFrontDefaultCertificate`
Type: String
Valid Values: `cloudfront | iam | acm`
Required: No

 ** CloudFrontDefaultCertificate **   <a name="cloudfront-Type-ViewerCertificate-CloudFrontDefaultCertificate"></a>
If the distribution uses the CloudFront domain name such as `d111111abcdef8.cloudfront.net`, set this field to `true`.
If the distribution uses `Aliases` (alternate domain names or CNAMEs), set this field to `false` and specify values for the following fields:
+  `ACMCertificateArn` or `IAMCertificateId` (specify a value for one, not both)

  In CloudFormation, these field names are `AcmCertificateArn` and `IamCertificateId`. Note the different capitalization.
+  `MinimumProtocolVersion`
+  `SSLSupportMethod` (In CloudFormation, this field name is `SslSupportMethod`. Note the different capitalization.)
Type: Boolean
Required: No

 ** IAMCertificateId **   <a name="cloudfront-Type-ViewerCertificate-IAMCertificateId"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
In CloudFormation, this field name is `IamCertificateId`. Note the different capitalization.
If the distribution uses `Aliases` (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html), provide the ID of the IAM certificate.
If you specify an IAM certificate ID, you must also specify values for `MinimumProtocolVersion` and `SSLSupportMethod`. (In CloudFormation, the field name is `SslSupportMethod`. Note the different capitalization.)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: No

 ** MinimumProtocolVersion **   <a name="cloudfront-Type-ViewerCertificate-MinimumProtocolVersion"></a>
If the distribution uses `Aliases` (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:
+ The minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.
+ The ciphers that CloudFront can use to encrypt the content that it returns to viewers.
For more information, see [Security Policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValues-security-policy) and [Supported Protocols and Ciphers Between Viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html#secure-connections-supported-ciphers) in the *Amazon CloudFront Developer Guide*.
On the CloudFront console, this setting is called **Security Policy**.
When you're using SNI only (you set `SSLSupportMethod` to `sni-only`), you must specify `TLSv1` or higher. (In CloudFormation, the field name is `SslSupportMethod`. Note the different capitalization.)
If the distribution uses the CloudFront domain name such as `d111111abcdef8.cloudfront.net` (you set `CloudFrontDefaultCertificate` to `true`), CloudFront automatically sets the security policy to `TLSv1` regardless of the value that you set here.
Type: String
Valid Values: `SSLv3 | TLSv1 | TLSv1_2016 | TLSv1.1_2016 | TLSv1.2_2018 | TLSv1.2_2019 | TLSv1.2_2021 | TLSv1.3_2025 | TLSv1.2_2025`
Required: No

 ** SSLSupportMethod **   <a name="cloudfront-Type-ViewerCertificate-SSLSupportMethod"></a>
In CloudFormation, this field name is `SslSupportMethod`. Note the different capitalization.
If the distribution uses `Aliases` (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.
+  `sni-only` – The distribution accepts HTTPS connections from only viewers that support [server name indication (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication). This is recommended. Most browsers and clients support SNI.
+  `vip` – The distribution accepts HTTPS connections from all viewers including those that don't support SNI. This is not recommended, and results in additional monthly charges from CloudFront.
+  `static-ip` - Do not specify this value unless your distribution has been enabled for this feature by the CloudFront team. If you have a use case that requires static IP addresses for a distribution, contact CloudFront through the [Support Center](https://console.aws.amazon.com/support/home).
If the distribution uses the CloudFront domain name such as `d111111abcdef8.cloudfront.net`, don't set a value for this field.
Type: String
Valid Values: `sni-only | vip | static-ip`
Required: No

## See Also
<a name="API_ViewerCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ViewerCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ViewerCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ViewerCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
