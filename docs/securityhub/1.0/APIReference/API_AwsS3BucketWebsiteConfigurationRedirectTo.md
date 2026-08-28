---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketWebsiteConfigurationRedirectTo.html
---

# AwsS3BucketWebsiteConfigurationRedirectTo
<a name="API_AwsS3BucketWebsiteConfigurationRedirectTo"></a>

The redirect behavior for requests to the website.

## Contents
<a name="API_AwsS3BucketWebsiteConfigurationRedirectTo_Contents"></a>

 ** Hostname **   <a name="securityhub-Type-AwsS3BucketWebsiteConfigurationRedirectTo-Hostname"></a>
The name of the host to redirect requests to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Protocol **   <a name="securityhub-Type-AwsS3BucketWebsiteConfigurationRedirectTo-Protocol"></a>
The protocol to use when redirecting requests. By default, this field uses the same protocol as the original request. Valid values are `http` or `https`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsS3BucketWebsiteConfigurationRedirectTo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketWebsiteConfigurationRedirectTo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketWebsiteConfigurationRedirectTo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketWebsiteConfigurationRedirectTo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
