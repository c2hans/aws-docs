---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_KeyGroup.html
---

# KeyGroup
<a name="API_KeyGroup"></a>

A key group.

A key group contains a list of public keys that you can use with [CloudFront signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html).

## Contents
<a name="API_KeyGroup_Contents"></a>

 ** Id **   <a name="cloudfront-Type-KeyGroup-Id"></a>
The identifier for the key group.
Type: String
Required: Yes

 ** KeyGroupConfig **   <a name="cloudfront-Type-KeyGroup-KeyGroupConfig"></a>
The key group configuration.
Type: [KeyGroupConfig](API_KeyGroupConfig.md) object
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-KeyGroup-LastModifiedTime"></a>
The date and time when the key group was last modified.
Type: Timestamp
Required: Yes

## See Also
<a name="API_KeyGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/KeyGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/KeyGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/KeyGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
