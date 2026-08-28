---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaGlobalSecondaryIndexDescription.html
---

# ReplicaGlobalSecondaryIndexDescription
<a name="API_ReplicaGlobalSecondaryIndexDescription"></a>

Represents the properties of a replica global secondary index.

## Contents
<a name="API_ReplicaGlobalSecondaryIndexDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IndexName **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexDescription-IndexName"></a>
The name of the global secondary index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** OnDemandThroughputOverride **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexDescription-OnDemandThroughputOverride"></a>
Overrides the maximum on-demand throughput for the specified global secondary index in the specified replica table.
Type: [OnDemandThroughputOverride](API_OnDemandThroughputOverride.md) object
Required: No

 ** ProvisionedThroughputOverride **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexDescription-ProvisionedThroughputOverride"></a>
If not described, uses the source table GSI's read capacity settings.
Type: [ProvisionedThroughputOverride](API_ProvisionedThroughputOverride.md) object
Required: No

 ** WarmThroughput **   <a name="DDB-Type-ReplicaGlobalSecondaryIndexDescription-WarmThroughput"></a>
Represents the warm throughput of the global secondary index for this replica.
Type: [GlobalSecondaryIndexWarmThroughputDescription](API_GlobalSecondaryIndexWarmThroughputDescription.md) object
Required: No

## See Also
<a name="API_ReplicaGlobalSecondaryIndexDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ReplicaGlobalSecondaryIndexDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
