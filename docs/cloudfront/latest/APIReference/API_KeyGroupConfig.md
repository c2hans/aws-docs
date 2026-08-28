---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_KeyGroupConfig.html
---

# KeyGroupConfig
<a name="API_KeyGroupConfig"></a>

A key group configuration.

A key group contains a list of public keys that you can use with [CloudFront signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html).

## Contents
<a name="API_KeyGroupConfig_Contents"></a>

 ** Items **   <a name="cloudfront-Type-KeyGroupConfig-Items"></a>
A list of the identifiers of the public keys in the key group.
Type: Array of strings
Required: Yes

 ** Name **   <a name="cloudfront-Type-KeyGroupConfig-Name"></a>
A name to identify the key group.
Type: String
Required: Yes

 ** Comment **   <a name="cloudfront-Type-KeyGroupConfig-Comment"></a>
A comment to describe the key group. The comment cannot be longer than 128 characters.
Type: String
Required: No

## See Also
<a name="API_KeyGroupConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/KeyGroupConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/KeyGroupConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/KeyGroupConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
