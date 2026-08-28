---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_StreamingDistributionSummary.html
---

# StreamingDistributionSummary
<a name="API_StreamingDistributionSummary"></a>

A summary of the information for a CloudFront streaming distribution.

## Contents
<a name="API_StreamingDistributionSummary_Contents"></a>

 ** Aliases **   <a name="cloudfront-Type-StreamingDistributionSummary-Aliases"></a>
A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.
Type: [Aliases](API_Aliases.md) object
Required: Yes

 ** ARN **   <a name="cloudfront-Type-StreamingDistributionSummary-ARN"></a>
The ARN (Amazon Resource Name) for the streaming distribution. For example: `arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5`, where `123456789012` is your AWS account ID.
Type: String
Required: Yes

 ** Comment **   <a name="cloudfront-Type-StreamingDistributionSummary-Comment"></a>
The comment originally specified when this distribution was created.
Type: String
Required: Yes

 ** DomainName **   <a name="cloudfront-Type-StreamingDistributionSummary-DomainName"></a>
The domain name corresponding to the distribution, for example, `d111111abcdef8.cloudfront.net`.
Type: String
Required: Yes

 ** Enabled **   <a name="cloudfront-Type-StreamingDistributionSummary-Enabled"></a>
Whether the distribution is enabled to accept end user requests for content.
Type: Boolean
Required: Yes

 ** Id **   <a name="cloudfront-Type-StreamingDistributionSummary-Id"></a>
The identifier for the distribution, for example, `EDFDVBD632BHDS5`.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-StreamingDistributionSummary-LastModifiedTime"></a>
The date and time the distribution was last modified.
Type: Timestamp
Required: Yes

 ** PriceClass **   <a name="cloudfront-Type-StreamingDistributionSummary-PriceClass"></a>
A complex type that contains information about price class for this streaming distribution.
Type: String
Valid Values: `PriceClass_100 | PriceClass_200 | PriceClass_All | None`
Required: Yes

 ** S3Origin **   <a name="cloudfront-Type-StreamingDistributionSummary-S3Origin"></a>
A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.
Type: [S3Origin](API_S3Origin.md) object
Required: Yes

 ** Status **   <a name="cloudfront-Type-StreamingDistributionSummary-Status"></a>
Indicates the current status of the distribution. When the status is `Deployed`, the distribution's information is fully propagated throughout the Amazon CloudFront system.
Type: String
Required: Yes

 ** TrustedSigners **   <a name="cloudfront-Type-StreamingDistributionSummary-TrustedSigners"></a>
A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the `PathPattern` for this cache behavior, specify `true` for `Enabled`, and specify the applicable values for `Quantity` and `Items`.If you don't want to require signed URLs in requests for objects that match `PathPattern`, specify `false` for `Enabled` and `0` for `Quantity`. Omit `Items`. To add, change, or remove one or more trusted signers, change `Enabled` to `true` (if it's currently `false`), change `Quantity` as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
For more information, see [Serving Private Content through CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide*.
Type: [TrustedSigners](API_TrustedSigners.md) object
Required: Yes

## See Also
<a name="API_StreamingDistributionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/StreamingDistributionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/StreamingDistributionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/StreamingDistributionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
