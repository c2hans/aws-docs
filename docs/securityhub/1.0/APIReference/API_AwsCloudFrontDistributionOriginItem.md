---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCloudFrontDistributionOriginItem.html
---

# AwsCloudFrontDistributionOriginItem
<a name="API_AwsCloudFrontDistributionOriginItem"></a>

A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), or other server from which CloudFront gets your files.

## Contents
<a name="API_AwsCloudFrontDistributionOriginItem_Contents"></a>

 ** CustomOriginConfig **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginItem-CustomOriginConfig"></a>
An origin that is not an Amazon S3 bucket, with one exception. If the Amazon S3 bucket is configured with static website hosting, use this attribute. If the Amazon S3 bucket is not configured with static website hosting, use the `S3OriginConfig` type instead.
Type: [AwsCloudFrontDistributionOriginCustomOriginConfig](API_AwsCloudFrontDistributionOriginCustomOriginConfig.md) object
Required: No

 ** DomainName **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginItem-DomainName"></a>
Amazon S3 origins: The DNS name of the S3 bucket from which you want CloudFront to get objects for this origin.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Id **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginItem-Id"></a>
A unique identifier for the origin or origin group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OriginPath **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginItem-OriginPath"></a>
An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin.
Type: String
Pattern: `.*\S.*`
Required: No

 ** S3OriginConfig **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginItem-S3OriginConfig"></a>
An origin that is an S3 bucket that is not configured with static website hosting.
Type: [AwsCloudFrontDistributionOriginS3OriginConfig](API_AwsCloudFrontDistributionOriginS3OriginConfig.md) object
Required: No

## See Also
<a name="API_AwsCloudFrontDistributionOriginItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCloudFrontDistributionOriginItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCloudFrontDistributionOriginItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCloudFrontDistributionOriginItem)
