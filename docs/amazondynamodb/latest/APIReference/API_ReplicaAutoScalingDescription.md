---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaAutoScalingDescription.html
---

# ReplicaAutoScalingDescription
<a name="API_ReplicaAutoScalingDescription"></a>

Represents the auto scaling settings of the replica.

## Contents
<a name="API_ReplicaAutoScalingDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GlobalSecondaryIndexes **   <a name="DDB-Type-ReplicaAutoScalingDescription-GlobalSecondaryIndexes"></a>
Replica-specific global secondary index auto scaling settings.
Type: Array of [ReplicaGlobalSecondaryIndexAutoScalingDescription](API_ReplicaGlobalSecondaryIndexAutoScalingDescription.md) objects
Required: No

 ** RegionName **   <a name="DDB-Type-ReplicaAutoScalingDescription-RegionName"></a>
The Region where the replica exists.
Type: String
Required: No

 ** ReplicaProvisionedReadCapacityAutoScalingSettings **   <a name="DDB-Type-ReplicaAutoScalingDescription-ReplicaProvisionedReadCapacityAutoScalingSettings"></a>
Represents the auto scaling settings for a global table or global secondary index.
Type: [AutoScalingSettingsDescription](API_AutoScalingSettingsDescription.md) object
Required: No

 ** ReplicaProvisionedWriteCapacityAutoScalingSettings **   <a name="DDB-Type-ReplicaAutoScalingDescription-ReplicaProvisionedWriteCapacityAutoScalingSettings"></a>
Represents the auto scaling settings for a global table or global secondary index.
Type: [AutoScalingSettingsDescription](API_AutoScalingSettingsDescription.md) object
Required: No

 ** ReplicaStatus **   <a name="DDB-Type-ReplicaAutoScalingDescription-ReplicaStatus"></a>
The current state of the replica:
+  `CREATING` - The replica is being created.
+  `UPDATING` - The replica is being updated.
+  `DELETING` - The replica is being deleted.
+  `ACTIVE` - The replica is ready for use.
Type: String
Valid Values: `CREATING | CREATION_FAILED | UPDATING | DELETING | ACTIVE | REGION_DISABLED | INACCESSIBLE_ENCRYPTION_CREDENTIALS | ARCHIVING | ARCHIVED | REPLICATION_NOT_AUTHORIZED`
Required: No

## See Also
<a name="API_ReplicaAutoScalingDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ReplicaAutoScalingDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ReplicaAutoScalingDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ReplicaAutoScalingDescription)
