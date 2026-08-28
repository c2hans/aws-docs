---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCloudFrontDistributionLogging.html
---

# AwsCloudFrontDistributionLogging
<a name="API_AwsCloudFrontDistributionLogging"></a>

A complex type that controls whether access logs are written for the CloudFront distribution.

## Contents
<a name="API_AwsCloudFrontDistributionLogging_Contents"></a>

 ** Bucket **   <a name="securityhub-Type-AwsCloudFrontDistributionLogging-Bucket"></a>
The S3 bucket to store the access logs in.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Enabled **   <a name="securityhub-Type-AwsCloudFrontDistributionLogging-Enabled"></a>
With this field, you can enable or disable the selected distribution.
Type: Boolean
Required: No

 ** IncludeCookies **   <a name="securityhub-Type-AwsCloudFrontDistributionLogging-IncludeCookies"></a>
Specifies whether you want CloudFront to include cookies in access logs.
Type: Boolean
Required: No

 ** Prefix **   <a name="securityhub-Type-AwsCloudFrontDistributionLogging-Prefix"></a>
An optional string that you want CloudFront to use as a prefix to the access log filenames for this distribution.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCloudFrontDistributionLogging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCloudFrontDistributionLogging)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCloudFrontDistributionLogging)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCloudFrontDistributionLogging)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
