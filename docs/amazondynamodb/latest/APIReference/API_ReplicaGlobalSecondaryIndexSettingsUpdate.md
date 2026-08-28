---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaGlobalSecondaryIndexSettingsUpdate.html
---

# ReplicaGlobalSecondaryIndexSettingsUpdate
<a name="API_ReplicaGlobalSecondaryIndexSettingsUpdate"></a>

Represents the settings of a global secondary index for a global table that will be modified.

## Contents
<a name="API_ReplicaGlobalSecondaryIndexSettingsUpdate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IndexName **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexSettingsUpdate-IndexName"></a>
The name of the global secondary index. The name must be unique among all other indexes on this table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** ProvisionedReadCapacityAutoScalingSettingsUpdate **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexSettingsUpdate-ProvisionedReadCapacityAutoScalingSettingsUpdate"></a>
Auto scaling settings for managing a global secondary index replica's read capacity units.
Type: [AutoScalingSettingsUpdate](API_AutoScalingSettingsUpdate.md) object
Required: No

 ** ProvisionedReadCapacityUnits **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexSettingsUpdate-ProvisionedReadCapacityUnits"></a>
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException`.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ReplicaGlobalSecondaryIndexSettingsUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexSettingsUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexSettingsUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexSettingsUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
