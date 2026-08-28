---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDynamoDbTableReplicaGlobalSecondaryIndex.html
---

# AwsDynamoDbTableReplicaGlobalSecondaryIndex
<a name="API_AwsDynamoDbTableReplicaGlobalSecondaryIndex"></a>

Information about a global secondary index for a DynamoDB table replica.

## Contents
<a name="API_AwsDynamoDbTableReplicaGlobalSecondaryIndex_Contents"></a>

 ** IndexName **   <a name="securityhub-Type-AwsDynamoDbTableReplicaGlobalSecondaryIndex-IndexName"></a>
The name of the index.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProvisionedThroughputOverride **   <a name="securityhub-Type-AwsDynamoDbTableReplicaGlobalSecondaryIndex-ProvisionedThroughputOverride"></a>
Replica-specific configuration for the provisioned throughput for the index.
Type: [AwsDynamoDbTableProvisionedThroughputOverride](API_AwsDynamoDbTableProvisionedThroughputOverride.md) object
Required: No

## See Also
<a name="API_AwsDynamoDbTableReplicaGlobalSecondaryIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDynamoDbTableReplicaGlobalSecondaryIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDynamoDbTableReplicaGlobalSecondaryIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDynamoDbTableReplicaGlobalSecondaryIndex)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
