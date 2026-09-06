---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaAutoScalingUpdate.html
---

# ReplicaAutoScalingUpdate
<a name="API_ReplicaAutoScalingUpdate"></a>

Represents the auto scaling settings of a replica that will be modified.

## Contents
<a name="API_ReplicaAutoScalingUpdate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RegionName **   <a name="DDB-Type-ReplicaAutoScalingUpdate-RegionName"></a>
The Region where the replica exists.
Type: String
Required: Yes

 ** ReplicaGlobalSecondaryIndexUpdates **   <a name="DDB-Type-ReplicaAutoScalingUpdate-ReplicaGlobalSecondaryIndexUpdates"></a>
Represents the auto scaling settings of global secondary indexes that will be modified.
Type: Array of [ReplicaGlobalSecondaryIndexAutoScalingUpdate](API_ReplicaGlobalSecondaryIndexAutoScalingUpdate.md) objects
Required: No

 ** ReplicaProvisionedReadCapacityAutoScalingUpdate **   <a name="DDB-Type-ReplicaAutoScalingUpdate-ReplicaProvisionedReadCapacityAutoScalingUpdate"></a>
Represents the auto scaling settings to be modified for a global table or global secondary index.
Type: [AutoScalingSettingsUpdate](API_AutoScalingSettingsUpdate.md) object
Required: No

## See Also
<a name="API_ReplicaAutoScalingUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ReplicaAutoScalingUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ReplicaAutoScalingUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ReplicaAutoScalingUpdate)
