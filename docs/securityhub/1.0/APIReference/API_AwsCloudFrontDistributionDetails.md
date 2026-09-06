---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCloudFrontDistributionDetails.html
---

# AwsCloudFrontDistributionDetails
<a name="API_AwsCloudFrontDistributionDetails"></a>

A CloudFront distribution configuration.

## Contents
<a name="API_AwsCloudFrontDistributionDetails_Contents"></a>

 ** CacheBehaviors **   <a name="securityhub-Type-AwsCloudFrontDistributionDetails-CacheBehaviors"></a>
Provides information about the cache configuration for the distribution.
Type: [AwsCloudFrontDistributionCacheBehaviors](API_AwsCloudFrontDistributionCacheBehaviors.md) object
Required: No

 ** DefaultCacheBehavior **   <a name="securityhub-Type-AwsCloudFrontDistributionDetails-DefaultCacheBehavior"></a>
The default cache behavior for the configuration.
Type: [AwsCloudFrontDistributionDefaultCacheBehavior](API_AwsCloudFrontDistributionDefaultCacheBehavior.md) object
Required: No

 ** DefaultRootObject **   <a name="securityhub-Type-AwsCloudFrontDistributionDetails-DefaultRootObject"></a>
The object that CloudFront sends in response to requests from the origin (for example, index.html) when a viewer requests the root URL for the distribution (http://www.example.com) instead of an object in your distribution (http://www.example.com/product-description.html).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DomainName **   <a name="securityhub-Type-AwsCloudFrontDistributionDetails-DomainName"></a>
The domain name corresponding to the distribution.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ETag **   <a name="securityhub-Type-AwsCloudFrontDistributionDetails-ETag"></a>
The entity tag is a hash of the object.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastModifiedTime **   <a name="securityhub-Type-AwsCloudFrontDistributionDetails-LastModifiedTime"></a>
Indicates when that the distribution was last modified.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Logging **   <a name="securityhub-Type-AwsCloudFrontDistributionDetails-Logging"></a>
A complex type that controls whether access logs are written for the distribution.
Type: [AwsCloudFrontDistributionLogging](API_AwsCloudFrontDistributionLogging.md) object
Required: No

 ** OriginGroups **   <a name="securityhub-Type-AwsCloudFrontDistributionDetails-OriginGroups"></a>
Provides information about the origin groups in the distribution.
Type: [AwsCloudFrontDistributionOriginGroups](API_AwsCloudFrontDistributionOriginGroups.md) object
Required: No

 ** Origins **   <a name="securityhub-Type-AwsCloudFrontDistributionDetails-Origins"></a>
A complex type that contains information about origins for this distribution.
Type: [AwsCloudFrontDistributionOrigins](API_AwsCloudFrontDistributionOrigins.md) object
Required: No

 ** Status **   <a name="securityhub-Type-AwsCloudFrontDistributionDetails-Status"></a>
Indicates the current status of the distribution.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ViewerCertificate **   <a name="securityhub-Type-AwsCloudFrontDistributionDetails-ViewerCertificate"></a>
Provides information about the TLS/SSL configuration that the distribution uses to communicate with viewers.
Type: [AwsCloudFrontDistributionViewerCertificate](API_AwsCloudFrontDistributionViewerCertificate.md) object
Required: No

 ** WebAclId **   <a name="securityhub-Type-AwsCloudFrontDistributionDetails-WebAclId"></a>
A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCloudFrontDistributionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCloudFrontDistributionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCloudFrontDistributionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCloudFrontDistributionDetails)
