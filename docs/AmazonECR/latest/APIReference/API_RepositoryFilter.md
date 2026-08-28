---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RepositoryFilter.html
---

# RepositoryFilter
<a name="API_RepositoryFilter"></a>

The filter settings used with image replication. Specifying a repository filter to a replication rule provides a method for controlling which repositories in a private registry are replicated. If no filters are added, the contents of all repositories are replicated.

## Contents
<a name="API_RepositoryFilter_Contents"></a>

 ** filter **   <a name="ECR-Type-RepositoryFilter-filter"></a>
The repository filter details. When the `PREFIX_MATCH` filter type is specified, this value is required and should be the repository name prefix to configure replication for.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `^(?:[a-z0-9]+(?:[._-][a-z0-9]*)*/)*[a-z0-9]*(?:[._-][a-z0-9]*)*$`
Required: Yes

 ** filterType **   <a name="ECR-Type-RepositoryFilter-filterType"></a>
The repository filter type. The only supported value is `PREFIX_MATCH`, which is a repository name prefix specified with the `filter` parameter.
Type: String
Valid Values: `PREFIX_MATCH`
Required: Yes

## See Also
<a name="API_RepositoryFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/RepositoryFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/RepositoryFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/RepositoryFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
