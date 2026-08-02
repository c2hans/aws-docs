---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaGlobalSecondaryIndexAutoScalingUpdate.html
---

# ReplicaGlobalSecondaryIndexAutoScalingUpdate
<a name="API_ReplicaGlobalSecondaryIndexAutoScalingUpdate"></a>

Represents the auto scaling settings of a global secondary index for a replica that will be modified.

## Contents
<a name="API_ReplicaGlobalSecondaryIndexAutoScalingUpdate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IndexName **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexAutoScalingUpdate-IndexName"></a>
The name of the global secondary index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** ProvisionedReadCapacityAutoScalingUpdate **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexAutoScalingUpdate-ProvisionedReadCapacityAutoScalingUpdate"></a>
Represents the auto scaling settings to be modified for a global table or global secondary index.
Type: [AutoScalingSettingsUpdate](API_AutoScalingSettingsUpdate.md) object
Required: No

## See Also
<a name="API_ReplicaGlobalSecondaryIndexAutoScalingUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexAutoScalingUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexAutoScalingUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexAutoScalingUpdate)
