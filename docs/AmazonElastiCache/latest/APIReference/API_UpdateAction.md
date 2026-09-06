---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_UpdateAction.html
---

# UpdateAction
<a name="API_UpdateAction"></a>

The status of the service update for a specific replication group

## Contents
<a name="API_UpdateAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CacheClusterId **
The ID of the cache cluster
Type: String
Required: No

 ** CacheNodeUpdateStatus.CacheNodeUpdateStatus.N **
The status of the service update on the cache node
Type: Array of [CacheNodeUpdateStatus](API_CacheNodeUpdateStatus.md) objects
Required: No

 ** Engine **
The Elasticache engine to which the update applies. Either Valkey, Redis OSS or Memcached.
Type: String
Required: No

 ** EstimatedUpdateTime **
The estimated length of time for the update to complete
Type: String
Required: No

 ** NodeGroupUpdateStatus.NodeGroupUpdateStatus.N **
The status of the service update on the node group
Type: Array of [NodeGroupUpdateStatus](API_NodeGroupUpdateStatus.md) objects
Required: No

 ** NodesUpdated **
The progress of the service update on the replication group
Type: String
Required: No

 ** ReplicationGroupId **
The ID of the replication group
Type: String
Required: No

 ** ServiceUpdateName **
The unique ID of the service update
Type: String
Required: No

 ** ServiceUpdateRecommendedApplyByDate **
The recommended date to apply the service update to ensure compliance. For information on compliance, see [Self-Service Security Updates for Compliance](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/elasticache-compliance.html#elasticache-compliance-self-service).
Type: Timestamp
Required: No

 ** ServiceUpdateReleaseDate **
The date the update is first available
Type: Timestamp
Required: No

 ** ServiceUpdateSeverity **
The severity of the service update
Type: String
Valid Values: `critical | important | medium | low`
Required: No

 ** ServiceUpdateStatus **
The status of the service update
Type: String
Valid Values: `available | cancelled | expired`
Required: No

 ** ServiceUpdateType **
Reflects the nature of the service update
Type: String
Valid Values: `security-update`
Required: No

 ** SlaMet **
If yes, all nodes in the replication group have been updated by the recommended apply-by date. If no, at least one node in the replication group have not been updated by the recommended apply-by date. If N/A, the replication group was created after the recommended apply-by date.
Type: String
Valid Values: `yes | no | n/a`
Required: No

 ** UpdateActionAvailableDate **
The date that the service update is available to a replication group
Type: Timestamp
Required: No

 ** UpdateActionStatus **
The status of the update action
Type: String
Valid Values: `not-applied | waiting-to-start | in-progress | stopping | stopped | complete | scheduling | scheduled | not-applicable`
Required: No

 ** UpdateActionStatusModifiedDate **
The date when the UpdateActionStatus was last modified
Type: Timestamp
Required: No

## See Also
<a name="API_UpdateAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/UpdateAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/UpdateAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/UpdateAction)
