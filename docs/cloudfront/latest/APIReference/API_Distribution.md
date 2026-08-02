---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_Distribution.html
---

# Distribution
<a name="API_Distribution"></a>

A distribution tells CloudFront where you want content to be delivered from, and the details about how to track and manage content delivery.

## Contents
<a name="API_Distribution_Contents"></a>

 ** ARN **   <a name="cloudfront-Type-Distribution-ARN"></a>
The distribution's Amazon Resource Name (ARN).
Type: String
Required: Yes

 ** DistributionConfig **   <a name="cloudfront-Type-Distribution-DistributionConfig"></a>
The distribution's configuration.
Type: [DistributionConfig](API_DistributionConfig.md) object
Required: Yes

 ** DomainName **   <a name="cloudfront-Type-Distribution-DomainName"></a>
The distribution's CloudFront domain name. For example: `d111111abcdef8.cloudfront.net`.
Type: String
Required: Yes

 ** Id **   <a name="cloudfront-Type-Distribution-Id"></a>
The distribution's identifier. For example: `E1U5RQF7T870K0`.
Type: String
Required: Yes

 ** InProgressInvalidationBatches **   <a name="cloudfront-Type-Distribution-InProgressInvalidationBatches"></a>
The number of invalidation batches currently in progress.
Type: Integer
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-Distribution-LastModifiedTime"></a>
The date and time when the distribution was last modified.
Type: Timestamp
Required: Yes

 ** Status **   <a name="cloudfront-Type-Distribution-Status"></a>
The distribution's status. When the status is `Deployed`, the distribution's information is fully propagated to all CloudFront edge locations.
Type: String
Required: Yes

 ** ActiveTrustedKeyGroups **   <a name="cloudfront-Type-Distribution-ActiveTrustedKeyGroups"></a>
This field contains a list of key groups and the public keys in each key group that CloudFront can use to verify the signatures of signed URLs or signed cookies.
Type: [ActiveTrustedKeyGroups](API_ActiveTrustedKeyGroups.md) object
Required: No

 ** ActiveTrustedSigners **   <a name="cloudfront-Type-Distribution-ActiveTrustedSigners"></a>
We recommend using `TrustedKeyGroups` instead of `TrustedSigners`.
This field contains a list of AWS account IDs and the active CloudFront key pairs in each account that CloudFront can use to verify the signatures of signed URLs or signed cookies.
Type: [ActiveTrustedSigners](API_ActiveTrustedSigners.md) object
Required: No

 ** AliasICPRecordals **   <a name="cloudfront-Type-Distribution-AliasICPRecordals"></a>
 AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they've added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.
For more information about ICP recordals, see [ Signup, Accounts, and Credentials](https://docs.amazonaws.cn/en_us/aws/latest/userguide/accounts-and-credentials.html) in *Getting Started with AWS services in China*.
Type: Array of [AliasICPRecordal](API_AliasICPRecordal.md) objects
Required: No

## See Also
<a name="API_Distribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Distribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Distribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Distribution)
