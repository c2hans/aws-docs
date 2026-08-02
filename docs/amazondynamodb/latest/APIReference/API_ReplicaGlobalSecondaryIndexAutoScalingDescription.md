---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaGlobalSecondaryIndexAutoScalingDescription.html
---

# ReplicaGlobalSecondaryIndexAutoScalingDescription
<a name="API_ReplicaGlobalSecondaryIndexAutoScalingDescription"></a>

Represents the auto scaling configuration for a replica global secondary index.

## Contents
<a name="API_ReplicaGlobalSecondaryIndexAutoScalingDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IndexName **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexAutoScalingDescription-IndexName"></a>
The name of the global secondary index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** IndexStatus **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexAutoScalingDescription-IndexStatus"></a>
The current state of the replica global secondary index:
+  `CREATING` - The index is being created.
+  `UPDATING` - The table/index configuration is being updated. The table/index remains available for data operations when `UPDATING`
+  `DELETING` - The index is being deleted.
+  `ACTIVE` - The index is ready for use.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE`
Required: No

 ** ProvisionedReadCapacityAutoScalingSettings **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexAutoScalingDescription-ProvisionedReadCapacityAutoScalingSettings"></a>
Represents the auto scaling settings for a global table or global secondary index.
Type: [AutoScalingSettingsDescription](API_AutoScalingSettingsDescription.md) object
Required: No

 ** ProvisionedWriteCapacityAutoScalingSettings **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexAutoScalingDescription-ProvisionedWriteCapacityAutoScalingSettings"></a>
Represents the auto scaling settings for a global table or global secondary index.
Type: [AutoScalingSettingsDescription](API_AutoScalingSettingsDescription.md) object
Required: No

## See Also
<a name="API_ReplicaGlobalSecondaryIndexAutoScalingDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexAutoScalingDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexAutoScalingDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexAutoScalingDescription)
