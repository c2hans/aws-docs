---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCloudFrontDistributionCacheBehavior.html
---

# AwsCloudFrontDistributionCacheBehavior
<a name="API_AwsCloudFrontDistributionCacheBehavior"></a>

Information about a cache behavior for the distribution.

## Contents
<a name="API_AwsCloudFrontDistributionCacheBehavior_Contents"></a>

 ** ViewerProtocolPolicy **   <a name="securityhub-Type-AwsCloudFrontDistributionCacheBehavior-ViewerProtocolPolicy"></a>
The protocol that viewers can use to access the files in an origin. You can specify the following options:
+  `allow-all` - Viewers can use HTTP or HTTPS.
+  `redirect-to-https` - CloudFront responds to HTTP requests with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL. The viewer then uses the new URL to resubmit.
+  `https-only` - CloudFront responds to HTTP request with an HTTP status code of 403 (Forbidden).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCloudFrontDistributionCacheBehavior_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCloudFrontDistributionCacheBehavior)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCloudFrontDistributionCacheBehavior)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCloudFrontDistributionCacheBehavior)
