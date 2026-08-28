---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_StreamingDistribution.html
---

# StreamingDistribution
<a name="API_StreamingDistribution"></a>

A streaming distribution tells CloudFront where you want RTMP content to be delivered from, and the details about how to track and manage content delivery.

## Contents
<a name="API_StreamingDistribution_Contents"></a>

 ** ActiveTrustedSigners **   <a name="cloudfront-Type-StreamingDistribution-ActiveTrustedSigners"></a>
A complex type that lists the AWS accounts, if any, that you included in the `TrustedSigners` complex type for this distribution. These are the accounts that you want to allow to create signed URLs for private content.
The `Signer` complex type lists the AWS account number of the trusted signer or `self` if the signer is the AWS account that created the distribution. The `Signer` element also includes the IDs of any active CloudFront key pairs that are associated with the trusted signer's AWS account. If no `KeyPairId` element appears for a `Signer`, that signer can't create signed URLs.
For more information, see [Serving Private Content through CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide*.
Type: [ActiveTrustedSigners](API_ActiveTrustedSigners.md) object
Required: Yes

 ** ARN **   <a name="cloudfront-Type-StreamingDistribution-ARN"></a>
The ARN (Amazon Resource Name) for the distribution. For example: `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`, where `123456789012` is your AWS account ID.
Type: String
Required: Yes

 ** DomainName **   <a name="cloudfront-Type-StreamingDistribution-DomainName"></a>
The domain name that corresponds to the streaming distribution, for example, `s5c39gqb8ow64r.cloudfront.net`.
Type: String
Required: Yes

 ** Id **   <a name="cloudfront-Type-StreamingDistribution-Id"></a>
The identifier for the RTMP distribution. For example: `EGTXBD79EXAMPLE`.
Type: String
Required: Yes

 ** Status **   <a name="cloudfront-Type-StreamingDistribution-Status"></a>
The current status of the RTMP distribution. When the status is `Deployed`, the distribution's information is propagated to all CloudFront edge locations.
Type: String
Required: Yes

 ** StreamingDistributionConfig **   <a name="cloudfront-Type-StreamingDistribution-StreamingDistributionConfig"></a>
The current configuration information for the RTMP distribution.
Type: [StreamingDistributionConfig](API_StreamingDistributionConfig.md) object
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-StreamingDistribution-LastModifiedTime"></a>
The date and time that the distribution was last modified.
Type: Timestamp
Required: No

## See Also
<a name="API_StreamingDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/StreamingDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/StreamingDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/StreamingDistribution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
