---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ConflictingAlias.html
---

# ConflictingAlias
<a name="API_ConflictingAlias"></a>

An alias (also called a CNAME) and the CloudFront standard distribution and AWS account ID that it's associated with. The standard distribution and account IDs are partially hidden, which allows you to identify the standard distributions and accounts that you own, and helps to protect the information of ones that you don't own.

## Contents
<a name="API_ConflictingAlias_Contents"></a>

 ** AccountId **   <a name="cloudfront-Type-ConflictingAlias-AccountId"></a>
The (partially hidden) ID of the AWS account that owns the standard distribution that's associated with the alias.
Type: String
Required: No

 ** Alias **   <a name="cloudfront-Type-ConflictingAlias-Alias"></a>
An alias (also called a CNAME).
Type: String
Required: No

 ** DistributionId **   <a name="cloudfront-Type-ConflictingAlias-DistributionId"></a>
The (partially hidden) ID of the CloudFront standard distribution associated with the alias.
Type: String
Required: No

## See Also
<a name="API_ConflictingAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ConflictingAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ConflictingAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ConflictingAlias)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
