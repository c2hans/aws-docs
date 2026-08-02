---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateReplicationGroupMemberAction.html
---

# UpdateReplicationGroupMemberAction
<a name="API_UpdateReplicationGroupMemberAction"></a>

Represents a replica to be modified.

## Contents
<a name="API_UpdateReplicationGroupMemberAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RegionName **   <a name="DDB-Type-UpdateReplicationGroupMemberAction-RegionName"></a>
The Region where the replica exists.
Type: String
Required: Yes

 ** GlobalSecondaryIndexes **   <a name="DDB-Type-UpdateReplicationGroupMemberAction-GlobalSecondaryIndexes"></a>
Replica-specific global secondary index settings.
Type: Array of [ReplicaGlobalSecondaryIndex](API_ReplicaGlobalSecondaryIndex.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** KMSMasterKeyId **   <a name="DDB-Type-UpdateReplicationGroupMemberAction-KMSMasterKeyId"></a>
The AWS KMS key of the replica that should be used for AWS KMS encryption. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB KMS key `alias/aws/dynamodb`.
Type: String
Required: No

 ** OnDemandThroughputOverride **   <a name="DDB-Type-UpdateReplicationGroupMemberAction-OnDemandThroughputOverride"></a>
Overrides the maximum on-demand throughput for the replica table.
Type: [OnDemandThroughputOverride](API_OnDemandThroughputOverride.md) object
Required: No

 ** ProvisionedThroughputOverride **   <a name="DDB-Type-UpdateReplicationGroupMemberAction-ProvisionedThroughputOverride"></a>
Replica-specific provisioned throughput. If not specified, uses the source table's provisioned throughput settings.
Type: [ProvisionedThroughputOverride](API_ProvisionedThroughputOverride.md) object
Required: No

 ** TableClassOverride **   <a name="DDB-Type-UpdateReplicationGroupMemberAction-TableClassOverride"></a>
Replica-specific table class. If not specified, uses the source table's table class.
Type: String
Valid Values: `STANDARD | STANDARD_INFREQUENT_ACCESS`
Required: No

## See Also
<a name="API_UpdateReplicationGroupMemberAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/UpdateReplicationGroupMemberAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/UpdateReplicationGroupMemberAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/UpdateReplicationGroupMemberAction)
