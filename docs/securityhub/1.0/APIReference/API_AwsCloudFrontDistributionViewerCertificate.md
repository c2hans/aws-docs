---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCloudFrontDistributionViewerCertificate.html
---

# AwsCloudFrontDistributionViewerCertificate
<a name="API_AwsCloudFrontDistributionViewerCertificate"></a>

Provides information about the TLS/SSL configuration that the CloudFront distribution uses to communicate with viewers.

## Contents
<a name="API_AwsCloudFrontDistributionViewerCertificate_Contents"></a>

 ** AcmCertificateArn **   <a name="securityhub-Type-AwsCloudFrontDistributionViewerCertificate-AcmCertificateArn"></a>
The ARN of the ACM certificate. Used if the certificate is stored in ACM. If you provide an ACM certificate ARN, you must also provide `MinimumCertificateVersion` and `SslSupportMethod`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Certificate **   <a name="securityhub-Type-AwsCloudFrontDistributionViewerCertificate-Certificate"></a>
The identifier of the certificate. Note that in CloudFront, this attribute is deprecated.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CertificateSource **   <a name="securityhub-Type-AwsCloudFrontDistributionViewerCertificate-CertificateSource"></a>
The source of the certificate identified by `Certificate`. Note that in CloudFront, this attribute is deprecated.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CloudFrontDefaultCertificate **   <a name="securityhub-Type-AwsCloudFrontDistributionViewerCertificate-CloudFrontDefaultCertificate"></a>
Whether the distribution uses the CloudFront domain name. If set to `false`, then you provide either `AcmCertificateArn` or `IamCertificateId`.
Type: Boolean
Required: No

 ** IamCertificateId **   <a name="securityhub-Type-AwsCloudFrontDistributionViewerCertificate-IamCertificateId"></a>
The identifier of the IAM certificate. Used if the certificate is stored in IAM. If you provide `IamCertificateId`, then you also must provide `MinimumProtocolVersion` and `SslSupportMethod`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MinimumProtocolVersion **   <a name="securityhub-Type-AwsCloudFrontDistributionViewerCertificate-MinimumProtocolVersion"></a>
The security policy that CloudFront uses for HTTPS connections with viewers. If `SslSupportMethod` is `sni-only`, then `MinimumProtocolVersion` must be `TLSv1` or higher.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SslSupportMethod **   <a name="securityhub-Type-AwsCloudFrontDistributionViewerCertificate-SslSupportMethod"></a>
The viewers that the distribution accepts HTTPS connections from.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCloudFrontDistributionViewerCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCloudFrontDistributionViewerCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCloudFrontDistributionViewerCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCloudFrontDistributionViewerCertificate)
