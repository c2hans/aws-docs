---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaSettingsDescription.html
---

# ReplicaSettingsDescription
<a name="API_ReplicaSettingsDescription"></a>

Represents the properties of a replica.

## Contents
<a name="API_ReplicaSettingsDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RegionName **   <a name="DDB-Type-ReplicaSettingsDescription-RegionName"></a>
The Region name of the replica.
Type: String
Required: Yes

 ** ReplicaBillingModeSummary **   <a name="DDB-Type-ReplicaSettingsDescription-ReplicaBillingModeSummary"></a>
The read/write capacity mode of the replica.
Type: [BillingModeSummary](API_BillingModeSummary.md) object
Required: No

 ** ReplicaGlobalSecondaryIndexSettings **   <a name="DDB-Type-ReplicaSettingsDescription-ReplicaGlobalSecondaryIndexSettings"></a>
Replica global secondary index settings for the global table.
Type: Array of [ReplicaGlobalSecondaryIndexSettingsDescription](API_ReplicaGlobalSecondaryIndexSettingsDescription.md) objects
Required: No

 ** ReplicaProvisionedReadCapacityAutoScalingSettings **   <a name="DDB-Type-ReplicaSettingsDescription-ReplicaProvisionedReadCapacityAutoScalingSettings"></a>
Auto scaling settings for a global table replica's read capacity units.
Type: [AutoScalingSettingsDescription](API_AutoScalingSettingsDescription.md) object
Required: No

 ** ReplicaProvisionedReadCapacityUnits **   <a name="DDB-Type-ReplicaSettingsDescription-ReplicaProvisionedReadCapacityUnits"></a>
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException`. For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput) in the *Amazon DynamoDB Developer Guide*.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** ReplicaProvisionedWriteCapacityAutoScalingSettings **   <a name="DDB-Type-ReplicaSettingsDescription-ReplicaProvisionedWriteCapacityAutoScalingSettings"></a>
Auto scaling settings for a global table replica's write capacity units.
Type: [AutoScalingSettingsDescription](API_AutoScalingSettingsDescription.md) object
Required: No

 ** ReplicaProvisionedWriteCapacityUnits **   <a name="DDB-Type-ReplicaSettingsDescription-ReplicaProvisionedWriteCapacityUnits"></a>
The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException`. For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput) in the *Amazon DynamoDB Developer Guide*.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** ReplicaStatus **   <a name="DDB-Type-ReplicaSettingsDescription-ReplicaStatus"></a>
The current state of the Region:
+  `CREATING` - The Region is being created.
+  `UPDATING` - The Region is being updated.
+  `DELETING` - The Region is being deleted.
+  `ACTIVE` - The Region is ready for use.
Type: String
Valid Values: `CREATING | CREATION_FAILED | UPDATING | DELETING | ACTIVE | REGION_DISABLED | INACCESSIBLE_ENCRYPTION_CREDENTIALS | ARCHIVING | ARCHIVED | REPLICATION_NOT_AUTHORIZED`
Required: No

 ** ReplicaTableClassSummary **   <a name="DDB-Type-ReplicaSettingsDescription-ReplicaTableClassSummary"></a>
Contains details of the table class.
Type: [TableClassSummary](API_TableClassSummary.md) object
Required: No

## See Also
<a name="API_ReplicaSettingsDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ReplicaSettingsDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ReplicaSettingsDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ReplicaSettingsDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
