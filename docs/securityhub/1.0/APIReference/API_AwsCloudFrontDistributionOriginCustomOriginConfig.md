---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCloudFrontDistributionOriginCustomOriginConfig.html
---

# AwsCloudFrontDistributionOriginCustomOriginConfig
<a name="API_AwsCloudFrontDistributionOriginCustomOriginConfig"></a>

A custom origin. A custom origin is any origin that is not an Amazon S3 bucket, with one exception. An Amazon S3 bucket that is [configured with static website hosting](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) is a custom origin.

## Contents
<a name="API_AwsCloudFrontDistributionOriginCustomOriginConfig_Contents"></a>

 ** HttpPort **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginCustomOriginConfig-HttpPort"></a>
The HTTP port that CloudFront uses to connect to the origin.
Type: Integer
Required: No

 ** HttpsPort **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginCustomOriginConfig-HttpsPort"></a>
The HTTPS port that CloudFront uses to connect to the origin.
Type: Integer
Required: No

 ** OriginKeepaliveTimeout **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginCustomOriginConfig-OriginKeepaliveTimeout"></a>
Specifies how long, in seconds, CloudFront persists its connection to the origin.
Type: Integer
Required: No

 ** OriginProtocolPolicy **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginCustomOriginConfig-OriginProtocolPolicy"></a>
Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OriginReadTimeout **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginCustomOriginConfig-OriginReadTimeout"></a>
Specifies how long, in seconds, CloudFront waits for a response from the origin.
Type: Integer
Required: No

 ** OriginSslProtocols **   <a name="securityhub-Type-AwsCloudFrontDistributionOriginCustomOriginConfig-OriginSslProtocols"></a>
Specifies the minimum SSL/TLS protocol that CloudFront uses when connecting to your origin over HTTPS.
Type: [AwsCloudFrontDistributionOriginSslProtocols](API_AwsCloudFrontDistributionOriginSslProtocols.md) object
Required: No

## See Also
<a name="API_AwsCloudFrontDistributionOriginCustomOriginConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCloudFrontDistributionOriginCustomOriginConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCloudFrontDistributionOriginCustomOriginConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCloudFrontDistributionOriginCustomOriginConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
