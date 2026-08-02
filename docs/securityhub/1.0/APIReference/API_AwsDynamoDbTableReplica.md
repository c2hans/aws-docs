---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDynamoDbTableReplica.html
---

# AwsDynamoDbTableReplica
<a name="API_AwsDynamoDbTableReplica"></a>

Information about a replica of a DynamoDB table.

## Contents
<a name="API_AwsDynamoDbTableReplica_Contents"></a>

 ** GlobalSecondaryIndexes **   <a name="securityhub-Type-AwsDynamoDbTableReplica-GlobalSecondaryIndexes"></a>
List of global secondary indexes for the replica.
Type: Array of [AwsDynamoDbTableReplicaGlobalSecondaryIndex](API_AwsDynamoDbTableReplicaGlobalSecondaryIndex.md) objects
Required: No

 ** KmsMasterKeyId **   <a name="securityhub-Type-AwsDynamoDbTableReplica-KmsMasterKeyId"></a>
The identifier of the AWS KMS key that will be used for AWS KMS encryption for the replica.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProvisionedThroughputOverride **   <a name="securityhub-Type-AwsDynamoDbTableReplica-ProvisionedThroughputOverride"></a>
Replica-specific configuration for the provisioned throughput.
Type: [AwsDynamoDbTableProvisionedThroughputOverride](API_AwsDynamoDbTableProvisionedThroughputOverride.md) object
Required: No

 ** RegionName **   <a name="securityhub-Type-AwsDynamoDbTableReplica-RegionName"></a>
The name of the Region where the replica is located.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReplicaStatus **   <a name="securityhub-Type-AwsDynamoDbTableReplica-ReplicaStatus"></a>
The current status of the replica. Valid values are as follows:
+  `ACTIVE`
+  `CREATING`
+  `CREATION_FAILED`
+  `DELETING`
+  `UPDATING`
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReplicaStatusDescription **   <a name="securityhub-Type-AwsDynamoDbTableReplica-ReplicaStatusDescription"></a>
Detailed information about the replica status.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsDynamoDbTableReplica_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDynamoDbTableReplica)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDynamoDbTableReplica)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDynamoDbTableReplica)
