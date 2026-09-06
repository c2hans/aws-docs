---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DistributionSummary.html
---

# DistributionSummary
<a name="API_DistributionSummary"></a>

A summary of the information about a CloudFront distribution.

## Contents
<a name="API_DistributionSummary_Contents"></a>

 ** Aliases **   <a name="cloudfront-Type-DistributionSummary-Aliases"></a>
A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
Type: [Aliases](API_Aliases.md) object
Required: Yes

 ** ARN **   <a name="cloudfront-Type-DistributionSummary-ARN"></a>
The ARN (Amazon Resource Name) for the distribution. For example: `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`, where `123456789012` is your AWS account ID.
Type: String
Required: Yes

 ** CacheBehaviors **   <a name="cloudfront-Type-DistributionSummary-CacheBehaviors"></a>
A complex type that contains zero or more `CacheBehavior` elements.
Type: [CacheBehaviors](API_CacheBehaviors.md) object
Required: Yes

 ** Comment **   <a name="cloudfront-Type-DistributionSummary-Comment"></a>
The comment originally specified when this distribution was created.
Type: String
Required: Yes

 ** CustomErrorResponses **   <a name="cloudfront-Type-DistributionSummary-CustomErrorResponses"></a>
A complex type that contains zero or more `CustomErrorResponses` elements.
Type: [CustomErrorResponses](API_CustomErrorResponses.md) object
Required: Yes

 ** DefaultCacheBehavior **   <a name="cloudfront-Type-DistributionSummary-DefaultCacheBehavior"></a>
A complex type that describes the default cache behavior if you don't specify a `CacheBehavior` element or if files don't match any of the values of `PathPattern` in `CacheBehavior` elements. You must create exactly one default cache behavior.
Type: [DefaultCacheBehavior](API_DefaultCacheBehavior.md) object
Required: Yes

 ** DomainName **   <a name="cloudfront-Type-DistributionSummary-DomainName"></a>
The domain name that corresponds to the distribution, for example, `d111111abcdef8.cloudfront.net`.
Type: String
Required: Yes

 ** Enabled **   <a name="cloudfront-Type-DistributionSummary-Enabled"></a>
Whether the distribution is enabled to accept user requests for content.
Type: Boolean
Required: Yes

 ** HttpVersion **   <a name="cloudfront-Type-DistributionSummary-HttpVersion"></a>
Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is `http2`. Viewers that don't support `HTTP/2` will automatically use an earlier version.
Type: String
Valid Values: `http1.1 | http2 | http3 | http2and3`
Required: Yes

 ** Id **   <a name="cloudfront-Type-DistributionSummary-Id"></a>
The identifier for the distribution. For example: `EDFDVBD632BHDS5`.
Type: String
Required: Yes

 ** IsIPV6Enabled **   <a name="cloudfront-Type-DistributionSummary-IsIPV6Enabled"></a>
Whether CloudFront responds to IPv6 DNS requests with an IPv6 address for your distribution.
Type: Boolean
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-DistributionSummary-LastModifiedTime"></a>
The date and time the distribution was last modified.
Type: Timestamp
Required: Yes

 ** Origins **   <a name="cloudfront-Type-DistributionSummary-Origins"></a>
A complex type that contains information about origins for this distribution.
Type: [Origins](API_Origins.md) object
Required: Yes

 ** PriceClass **   <a name="cloudfront-Type-DistributionSummary-PriceClass"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
A complex type that contains information about price class for this streaming distribution.
Type: String
Valid Values: `PriceClass_100 | PriceClass_200 | PriceClass_All | None`
Required: Yes

 ** Restrictions **   <a name="cloudfront-Type-DistributionSummary-Restrictions"></a>
A complex type that identifies ways in which you want to restrict distribution of your content.
Type: [Restrictions](API_Restrictions.md) object
Required: Yes

 ** Staging **   <a name="cloudfront-Type-DistributionSummary-Staging"></a>
A Boolean that indicates whether this is a staging distribution. When this value is `true`, this is a staging distribution. When this value is `false`, this is not a staging distribution.
Type: Boolean
Required: Yes

 ** Status **   <a name="cloudfront-Type-DistributionSummary-Status"></a>
The current status of the distribution. When the status is `Deployed`, the distribution's information is propagated to all CloudFront edge locations.
Type: String
Required: Yes

 ** ViewerCertificate **   <a name="cloudfront-Type-DistributionSummary-ViewerCertificate"></a>
A complex type that determines the distribution's SSL/TLS configuration for communicating with viewers.
Type: [ViewerCertificate](API_ViewerCertificate.md) object
Required: Yes

 ** WebACLId **   <a name="cloudfront-Type-DistributionSummary-WebACLId"></a>
The Web ACL Id (if any) associated with the distribution.
Type: String
Required: Yes

 ** AliasICPRecordals **   <a name="cloudfront-Type-DistributionSummary-AliasICPRecordals"></a>
 AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they've added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.
For more information about ICP recordals, see [ Signup, Accounts, and Credentials](https://docs.amazonaws.cn/en_us/aws/latest/userguide/accounts-and-credentials.html) in *Getting Started with AWS services in China*.
Type: Array of [AliasICPRecordal](API_AliasICPRecordal.md) objects
Required: No

 ** AnycastIpListId **   <a name="cloudfront-Type-DistributionSummary-AnycastIpListId"></a>
ID of the Anycast static IP list that is associated with the distribution.
Type: String
Required: No

 ** ConnectionFunctionAssociation **   <a name="cloudfront-Type-DistributionSummary-ConnectionFunctionAssociation"></a>
The distribution's connection function association.
Type: [ConnectionFunctionAssociation](API_ConnectionFunctionAssociation.md) object
Required: No

 ** ConnectionMode **   <a name="cloudfront-Type-DistributionSummary-ConnectionMode"></a>
This field specifies whether the connection mode is through a standard distribution (direct) or a multi-tenant distribution with distribution tenants (tenant-only).
Type: String
Valid Values: `direct | tenant-only`
Required: No

 ** ETag **   <a name="cloudfront-Type-DistributionSummary-ETag"></a>
The current version of the distribution.
Type: String
Required: No

 ** OriginGroups **   <a name="cloudfront-Type-DistributionSummary-OriginGroups"></a>
A complex type that contains information about origin groups for this distribution.
Type: [OriginGroups](API_OriginGroups.md) object
Required: No

 ** ViewerMtlsConfig **   <a name="cloudfront-Type-DistributionSummary-ViewerMtlsConfig"></a>
The distribution's viewer mTLS configuration.
Type: [ViewerMtlsConfig](API_ViewerMtlsConfig.md) object
Required: No

## See Also
<a name="API_DistributionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DistributionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DistributionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DistributionSummary)
