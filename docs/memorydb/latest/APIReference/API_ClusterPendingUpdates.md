---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ClusterPendingUpdates.html
---

# ClusterPendingUpdates
<a name="API_ClusterPendingUpdates"></a>

A list of updates being applied to the cluster

## Contents
<a name="API_ClusterPendingUpdates_Contents"></a>

 ** ACLs **   <a name="MemoryDB-Type-ClusterPendingUpdates-ACLs"></a>
A list of ACLs associated with the cluster that are being updated
Type: [ACLsUpdateStatus](API_ACLsUpdateStatus.md) object
Required: No

 ** Resharding **   <a name="MemoryDB-Type-ClusterPendingUpdates-Resharding"></a>
The status of an online resharding operation.
Type: [ReshardingStatus](API_ReshardingStatus.md) object
Required: No

 ** ServiceUpdates **   <a name="MemoryDB-Type-ClusterPendingUpdates-ServiceUpdates"></a>
A list of service updates being applied to the cluster
Type: Array of [PendingModifiedServiceUpdate](API_PendingModifiedServiceUpdate.md) objects
Required: No

## See Also
<a name="API_ClusterPendingUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/ClusterPendingUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/ClusterPendingUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/ClusterPendingUpdates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
