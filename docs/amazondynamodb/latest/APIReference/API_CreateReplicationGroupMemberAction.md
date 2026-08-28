---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateReplicationGroupMemberAction.html
---

# CreateReplicationGroupMemberAction
<a name="API_CreateReplicationGroupMemberAction"></a>

Represents a replica to be created.

## Contents
<a name="API_CreateReplicationGroupMemberAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RegionName **   <a name="DDB-Type-CreateReplicationGroupMemberAction-RegionName"></a>
The Region where the new replica will be created.
Type: String
Required: Yes

 ** GlobalSecondaryIndexes **   <a name="DDB-Type-CreateReplicationGroupMemberAction-GlobalSecondaryIndexes"></a>
Replica-specific global secondary index settings.
Type: Array of [ReplicaGlobalSecondaryIndex](API_ReplicaGlobalSecondaryIndex.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** KMSMasterKeyId **   <a name="DDB-Type-CreateReplicationGroupMemberAction-KMSMasterKeyId"></a>
The AWS KMS key that should be used for AWS KMS encryption in the new replica. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB KMS key `alias/aws/dynamodb`.
Type: String
Required: No

 ** OnDemandThroughputOverride **   <a name="DDB-Type-CreateReplicationGroupMemberAction-OnDemandThroughputOverride"></a>
The maximum on-demand throughput settings for the specified replica table being created. You can only modify `MaxReadRequestUnits`, because you can't modify `MaxWriteRequestUnits` for individual replica tables.
Type: [OnDemandThroughputOverride](API_OnDemandThroughputOverride.md) object
Required: No

 ** ProvisionedThroughputOverride **   <a name="DDB-Type-CreateReplicationGroupMemberAction-ProvisionedThroughputOverride"></a>
Replica-specific provisioned throughput. If not specified, uses the source table's provisioned throughput settings.
Type: [ProvisionedThroughputOverride](API_ProvisionedThroughputOverride.md) object
Required: No

 ** TableClassOverride **   <a name="DDB-Type-CreateReplicationGroupMemberAction-TableClassOverride"></a>
Replica-specific table class. If not specified, uses the source table's table class.
Type: String
Valid Values: `STANDARD | STANDARD_INFREQUENT_ACCESS`
Required: No

## See Also
<a name="API_CreateReplicationGroupMemberAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/CreateReplicationGroupMemberAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/CreateReplicationGroupMemberAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/CreateReplicationGroupMemberAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
