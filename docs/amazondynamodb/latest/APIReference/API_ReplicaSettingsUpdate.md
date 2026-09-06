---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaSettingsUpdate.html
---

# ReplicaSettingsUpdate
<a name="API_ReplicaSettingsUpdate"></a>

Represents the settings for a global table in a Region that will be modified.

## Contents
<a name="API_ReplicaSettingsUpdate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RegionName **   <a name="DDB-Type-ReplicaSettingsUpdate-RegionName"></a>
The Region of the replica to be added.
Type: String
Required: Yes

 ** ReplicaGlobalSecondaryIndexSettingsUpdate **   <a name="DDB-Type-ReplicaSettingsUpdate-ReplicaGlobalSecondaryIndexSettingsUpdate"></a>
Represents the settings of a global secondary index for a global table that will be modified.
Type: Array of [ReplicaGlobalSecondaryIndexSettingsUpdate](API_ReplicaGlobalSecondaryIndexSettingsUpdate.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate **   <a name="DDB-Type-ReplicaSettingsUpdate-ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate"></a>
Auto scaling settings for managing a global table replica's read capacity units.
Type: [AutoScalingSettingsUpdate](API_AutoScalingSettingsUpdate.md) object
Required: No

 ** ReplicaProvisionedReadCapacityUnits **   <a name="DDB-Type-ReplicaSettingsUpdate-ReplicaProvisionedReadCapacityUnits"></a>
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException`. For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput) in the *Amazon DynamoDB Developer Guide*.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** ReplicaTableClass **   <a name="DDB-Type-ReplicaSettingsUpdate-ReplicaTableClass"></a>
Replica-specific table class. If not specified, uses the source table's table class.
Type: String
Valid Values: `STANDARD | STANDARD_INFREQUENT_ACCESS`
Required: No

## See Also
<a name="API_ReplicaSettingsUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ReplicaSettingsUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ReplicaSettingsUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ReplicaSettingsUpdate)
