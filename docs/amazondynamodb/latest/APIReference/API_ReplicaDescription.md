---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaDescription.html
---

# ReplicaDescription
<a name="API_ReplicaDescription"></a>

Contains the details of the replica.

## Contents
<a name="API_ReplicaDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GlobalSecondaryIndexes **   <a name="DDB-Type-ReplicaDescription-GlobalSecondaryIndexes"></a>
Replica-specific global secondary index settings.
Type: Array of [ReplicaGlobalSecondaryIndexDescription](API_ReplicaGlobalSecondaryIndexDescription.md) objects
Required: No

 ** GlobalTableSettingsReplicationMode **   <a name="DDB-Type-ReplicaDescription-GlobalTableSettingsReplicationMode"></a>
Indicates one of the settings synchronization modes for the global table replica:
+  `ENABLED`: Indicates that the settings synchronization mode for the global table replica is enabled.
+  `DISABLED`: Indicates that the settings synchronization mode for the global table replica is disabled.
+  `ENABLED_WITH_OVERRIDES`: This mode is set by default for a same account global table. Indicates that certain global table settings can be overridden.
Type: String
Valid Values: `ENABLED | DISABLED | ENABLED_WITH_OVERRIDES`
Required: No

 ** KMSMasterKeyId **   <a name="DDB-Type-ReplicaDescription-KMSMasterKeyId"></a>
The AWS KMS key of the replica that will be used for AWS KMS encryption.
Type: String
Required: No

 ** OnDemandThroughputOverride **   <a name="DDB-Type-ReplicaDescription-OnDemandThroughputOverride"></a>
Overrides the maximum on-demand throughput settings for the specified replica table.
Type: [OnDemandThroughputOverride](API_OnDemandThroughputOverride.md) object
Required: No

 ** ProvisionedThroughputOverride **   <a name="DDB-Type-ReplicaDescription-ProvisionedThroughputOverride"></a>
Replica-specific provisioned throughput. If not described, uses the source table's provisioned throughput settings.
Type: [ProvisionedThroughputOverride](API_ProvisionedThroughputOverride.md) object
Required: No

 ** RegionName **   <a name="DDB-Type-ReplicaDescription-RegionName"></a>
The name of the Region.
Type: String
Required: No

 ** ReplicaArn **   <a name="DDB-Type-ReplicaDescription-ReplicaArn"></a>
The Amazon Resource Name (ARN) of the global table replica.
Type: String
Required: No

 ** ReplicaInaccessibleDateTime **   <a name="DDB-Type-ReplicaDescription-ReplicaInaccessibleDateTime"></a>
The time at which the replica was first detected as inaccessible. To determine cause of inaccessibility check the `ReplicaStatus` property.
Type: Timestamp
Required: No

 ** ReplicaStatus **   <a name="DDB-Type-ReplicaDescription-ReplicaStatus"></a>
The current state of the replica:
+  `CREATING` - The replica is being created.
+  `UPDATING` - The replica is being updated.
+  `DELETING` - The replica is being deleted.
+  `ACTIVE` - The replica is ready for use.
+  `REGION_DISABLED` - The replica is inaccessible because the AWS Region has been disabled.
**Note**
If the AWS Region remains inaccessible for more than 20 hours, DynamoDB will remove this replica from the replication group. The replica will not be deleted and replication will stop from and to this region.
+  `INACCESSIBLE_ENCRYPTION_CREDENTIALS ` - The AWS KMS key used to encrypt the table is inaccessible.
**Note**
If the AWS KMS key remains inaccessible for more than 20 hours, DynamoDB will remove this replica from the replication group. The replica will not be deleted and replication will stop from and to this region.
Type: String
Valid Values: `CREATING | CREATION_FAILED | UPDATING | DELETING | ACTIVE | REGION_DISABLED | INACCESSIBLE_ENCRYPTION_CREDENTIALS | ARCHIVING | ARCHIVED | REPLICATION_NOT_AUTHORIZED`
Required: No

 ** ReplicaStatusDescription **   <a name="DDB-Type-ReplicaDescription-ReplicaStatusDescription"></a>
Detailed information about the replica status.
Type: String
Required: No

 ** ReplicaStatusPercentProgress **   <a name="DDB-Type-ReplicaDescription-ReplicaStatusPercentProgress"></a>
Specifies the progress of a Create, Update, or Delete action on the replica as a percentage.
Type: String
Required: No

 ** ReplicaTableClassSummary **   <a name="DDB-Type-ReplicaDescription-ReplicaTableClassSummary"></a>
Contains details of the table class.
Type: [TableClassSummary](API_TableClassSummary.md) object
Required: No

 ** WarmThroughput **   <a name="DDB-Type-ReplicaDescription-WarmThroughput"></a>
Represents the warm throughput value for this replica.
Type: [TableWarmThroughputDescription](API_TableWarmThroughputDescription.md) object
Required: No

## See Also
<a name="API_ReplicaDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ReplicaDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ReplicaDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ReplicaDescription)
