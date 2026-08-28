---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ManagedCertificateDetails.html
---

# ManagedCertificateDetails
<a name="API_ManagedCertificateDetails"></a>

Contains details about the CloudFront managed ACM certificate.

## Contents
<a name="API_ManagedCertificateDetails_Contents"></a>

 ** CertificateArn **   <a name="cloudfront-Type-ManagedCertificateDetails-CertificateArn"></a>
The ARN of the CloudFront managed ACM certificate.
Type: String
Required: No

 ** CertificateStatus **   <a name="cloudfront-Type-ManagedCertificateDetails-CertificateStatus"></a>
The status of the CloudFront managed ACM certificate.
Your distribution tenant will be updated with the latest certificate status. When calling the [UpdateDistributionTenant](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistributionTenant.html) operation, use the latest value for the `ETag`.
Type: String
Valid Values: `pending-validation | issued | inactive | expired | validation-timed-out | revoked | failed`
Required: No

 ** ValidationTokenDetails **   <a name="cloudfront-Type-ManagedCertificateDetails-ValidationTokenDetails"></a>
Contains details about the validation token of the specified CloudFront managed ACM certificate.
Type: Array of [ValidationTokenDetail](API_ValidationTokenDetail.md) objects
Required: No

 ** ValidationTokenHost **   <a name="cloudfront-Type-ManagedCertificateDetails-ValidationTokenHost"></a>
Contains details about the validation token host of the specified CloudFront managed ACM certificate.
+ For `cloudfront`, CloudFront will automatically serve the validation token. Choose this mode if you can point the domain's DNS to CloudFront immediately.
+ For `self-hosted`, you serve the validation token from your existing infrastructure. Choose this mode when you need to maintain current traffic flow while your certificate is being issued. You can place the validation token at the well-known path on your existing web server, wait for ACM to validate and issue the certificate, and then update your DNS to point to CloudFront.
This setting only affects the initial certificate request. Once the DNS points to CloudFront, all future certificate renewals are automatically handled through CloudFront.
Type: String
Valid Values: `cloudfront | self-hosted`
Required: No

## See Also
<a name="API_ManagedCertificateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ManagedCertificateDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ManagedCertificateDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ManagedCertificateDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
