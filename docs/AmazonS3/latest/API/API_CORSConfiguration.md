---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_CORSConfiguration.html
---

# CORSConfiguration
<a name="API_CORSConfiguration"></a>

Describes the cross-origin access configuration for objects in an Amazon S3 bucket. For more information, see [Enabling Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) in the *Amazon S3 User Guide*.

## Contents
<a name="API_CORSConfiguration_Contents"></a>

 ** CORSRules **   <a name="AmazonS3-Type-CORSConfiguration-CORSRules"></a>
A set of origins and methods (cross-origin access that you want to allow). You can add up to 100 rules to the configuration.
Type: Array of [CORSRule](API_CORSRule.md) data types
Required: Yes

## See Also
<a name="API_CORSConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CORSConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CORSConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CORSConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
