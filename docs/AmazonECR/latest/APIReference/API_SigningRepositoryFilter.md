---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_SigningRepositoryFilter.html
---

# SigningRepositoryFilter
<a name="API_SigningRepositoryFilter"></a>

A repository filter used to determine which repositories have their images automatically signed on push. Each filter consists of a filter type and filter value.

## Contents
<a name="API_SigningRepositoryFilter_Contents"></a>

 ** filter **   <a name="ECR-Type-SigningRepositoryFilter-filter"></a>
The filter value used to match repository names. When using `WILDCARD_MATCH`, the `*` character matches any sequence of characters.
Examples:
+  `myapp/*` - Matches all repositories starting with `myapp/`
+  `*/production` - Matches all repositories ending with `/production`
+  `*prod*` - Matches all repositories containing `prod`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^(?:[a-z0-9*]+(?:[._-][a-z0-9*]+)*/)*[a-z0-9*]+(?:[._-][a-z0-9*]+)*$`
Required: Yes

 ** filterType **   <a name="ECR-Type-SigningRepositoryFilter-filterType"></a>
The type of filter to apply. Currently, only `WILDCARD_MATCH` is supported, which uses wildcard patterns to match repository names.
Type: String
Valid Values: `WILDCARD_MATCH`
Required: Yes

## See Also
<a name="API_SigningRepositoryFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/SigningRepositoryFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/SigningRepositoryFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/SigningRepositoryFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
