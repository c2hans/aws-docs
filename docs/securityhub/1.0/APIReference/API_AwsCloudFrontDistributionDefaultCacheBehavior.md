---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCloudFrontDistributionDefaultCacheBehavior.html
---

# AwsCloudFrontDistributionDefaultCacheBehavior
<a name="API_AwsCloudFrontDistributionDefaultCacheBehavior"></a>

Contains information about the default cache configuration for the CloudFront distribution.

## Contents
<a name="API_AwsCloudFrontDistributionDefaultCacheBehavior_Contents"></a>

 ** ViewerProtocolPolicy **   <a name="securityhub-Type-AwsCloudFrontDistributionDefaultCacheBehavior-ViewerProtocolPolicy"></a>
The protocol that viewers can use to access the files in an origin. You can specify the following options:
+  `allow-all` - Viewers can use HTTP or HTTPS.
+  `redirect-to-https` - CloudFront responds to HTTP requests with an HTTP status code of 301 (Moved Permanently) and the HTTPS URL. The viewer then uses the new URL to resubmit.
+  `https-only` - CloudFront responds to HTTP request with an HTTP status code of 403 (Forbidden).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCloudFrontDistributionDefaultCacheBehavior_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCloudFrontDistributionDefaultCacheBehavior)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCloudFrontDistributionDefaultCacheBehavior)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCloudFrontDistributionDefaultCacheBehavior)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
