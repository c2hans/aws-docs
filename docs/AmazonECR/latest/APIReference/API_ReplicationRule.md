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

 ** deleteReplication **   <a name="ECR-Type-ReplicationRule-deleteReplication"></a>
The delete replication settings for the replication rule. When delete replication is enabled, the service replicates image deletions and image tag removals from the source registry to the replication destinations. If you do not specify this parameter, the service does not replicate image deletions or image tag removals for the replication rule.
Type: [DeleteReplication](API_DeleteReplication.md) object
Required: No

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
