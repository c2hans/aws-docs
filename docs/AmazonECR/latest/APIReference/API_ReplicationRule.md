---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ReplicationRule.html
---

# ReplicationRule
<a name="API_ReplicationRule"></a>

An array of objects representing the replication destinations and repository filters for a replication configuration.

## Contents
<a name="API_ReplicationRule_Contents"></a>

 ** destinations **   <a name="ECR-Type-ReplicationRule-destinations"></a>
An array of objects representing the destination for a replication rule.
Type: Array of [ReplicationDestination](API_ReplicationDestination.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** repositoryFilters **   <a name="ECR-Type-ReplicationRule-repositoryFilters"></a>
An array of objects representing the filters for a replication rule. Specifying a repository filter for a replication rule provides a method for controlling which repositories in a private registry are replicated.
Type: Array of [RepositoryFilter](API_RepositoryFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_ReplicationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ReplicationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ReplicationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ReplicationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
