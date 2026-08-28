---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DomainConflict.html
---

# DomainConflict
<a name="API_DomainConflict"></a>

Contains information about the domain conflict. Use this information to determine the affected domain, the related resource, and the affected AWS account.

## Contents
<a name="API_DomainConflict_Contents"></a>

 ** AccountId **   <a name="cloudfront-Type-DomainConflict-AccountId"></a>
The ID of the AWS account for the domain conflict.
Type: String
Required: Yes

 ** Domain **   <a name="cloudfront-Type-DomainConflict-Domain"></a>
The domain used to find existing conflicts for domain configurations.
Type: String
Required: Yes

 ** ResourceId **   <a name="cloudfront-Type-DomainConflict-ResourceId"></a>
The ID of the resource that has a domain conflict.
Type: String
Required: Yes

 ** ResourceType **   <a name="cloudfront-Type-DomainConflict-ResourceType"></a>
The CloudFront resource type that has a domain conflict.
Type: String
Valid Values: `distribution | distribution-tenant`
Required: Yes

## See Also
<a name="API_DomainConflict_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DomainConflict)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DomainConflict)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DomainConflict)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
