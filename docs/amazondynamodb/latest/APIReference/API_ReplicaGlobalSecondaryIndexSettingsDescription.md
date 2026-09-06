---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaGlobalSecondaryIndexSettingsDescription.html
---

# ReplicaGlobalSecondaryIndexSettingsDescription
<a name="API_ReplicaGlobalSecondaryIndexSettingsDescription"></a>

Represents the properties of a global secondary index.

## Contents
<a name="API_ReplicaGlobalSecondaryIndexSettingsDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IndexName **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexSettingsDescription-IndexName"></a>
The name of the global secondary index. The name must be unique among all other indexes on this table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** IndexStatus **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexSettingsDescription-IndexStatus"></a>
 The current status of the global secondary index:
+  `CREATING` - The global secondary index is being created.
+  `UPDATING` - The global secondary index is being updated.
+  `DELETING` - The global secondary index is being deleted.
+  `ACTIVE` - The global secondary index is ready for use.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE`
Required: No

 ** ProvisionedReadCapacityAutoScalingSettings **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexSettingsDescription-ProvisionedReadCapacityAutoScalingSettings"></a>
Auto scaling settings for a global secondary index replica's read capacity units.
Type: [AutoScalingSettingsDescription](API_AutoScalingSettingsDescription.md) object
Required: No

 ** ProvisionedReadCapacityUnits **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexSettingsDescription-ProvisionedReadCapacityUnits"></a>
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException`.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** ProvisionedWriteCapacityAutoScalingSettings **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexSettingsDescription-ProvisionedWriteCapacityAutoScalingSettings"></a>
Auto scaling settings for a global secondary index replica's write capacity units.
Type: [AutoScalingSettingsDescription](API_AutoScalingSettingsDescription.md) object
Required: No

 ** ProvisionedWriteCapacityUnits **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexSettingsDescription-ProvisionedWriteCapacityUnits"></a>
The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException`.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ReplicaGlobalSecondaryIndexSettingsDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexSettingsDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexSettingsDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexSettingsDescription)
