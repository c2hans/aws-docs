---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketWebsiteConfiguration.html
---

# AwsS3BucketWebsiteConfiguration
<a name="API_AwsS3BucketWebsiteConfiguration"></a>

Website parameters for the S3 bucket.

## Contents
<a name="API_AwsS3BucketWebsiteConfiguration_Contents"></a>

 ** ErrorDocument **   <a name="securityhub-Type-AwsS3BucketWebsiteConfiguration-ErrorDocument"></a>
The name of the error document for the website.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IndexDocumentSuffix **   <a name="securityhub-Type-AwsS3BucketWebsiteConfiguration-IndexDocumentSuffix"></a>
The name of the index document for the website.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RedirectAllRequestsTo **   <a name="securityhub-Type-AwsS3BucketWebsiteConfiguration-RedirectAllRequestsTo"></a>
The redirect behavior for requests to the website.
Type: [AwsS3BucketWebsiteConfigurationRedirectTo](API_AwsS3BucketWebsiteConfigurationRedirectTo.md) object
Required: No

 ** RoutingRules **   <a name="securityhub-Type-AwsS3BucketWebsiteConfiguration-RoutingRules"></a>
The rules for applying redirects for requests to the website.
Type: Array of [AwsS3BucketWebsiteConfigurationRoutingRule](API_AwsS3BucketWebsiteConfigurationRoutingRule.md) objects
Required: No

## See Also
<a name="API_AwsS3BucketWebsiteConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketWebsiteConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketWebsiteConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketWebsiteConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
