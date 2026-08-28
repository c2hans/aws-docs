---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDynamoDbTableDetails.html
---

# AwsDynamoDbTableDetails
<a name="API_AwsDynamoDbTableDetails"></a>

Provides details about a DynamoDB table.

## Contents
<a name="API_AwsDynamoDbTableDetails_Contents"></a>

 ** AttributeDefinitions **   <a name="securityhub-Type-AwsDynamoDbTableDetails-AttributeDefinitions"></a>
A list of attribute definitions for the table.
Type: Array of [AwsDynamoDbTableAttributeDefinition](API_AwsDynamoDbTableAttributeDefinition.md) objects
Required: No

 ** BillingModeSummary **   <a name="securityhub-Type-AwsDynamoDbTableDetails-BillingModeSummary"></a>
Information about the billing for read/write capacity on the table.
Type: [AwsDynamoDbTableBillingModeSummary](API_AwsDynamoDbTableBillingModeSummary.md) object
Required: No

 ** CreationDateTime **   <a name="securityhub-Type-AwsDynamoDbTableDetails-CreationDateTime"></a>
Indicates when the table was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeletionProtectionEnabled **   <a name="securityhub-Type-AwsDynamoDbTableDetails-DeletionProtectionEnabled"></a>
 Indicates whether deletion protection is to be enabled (true) or disabled (false) on the table.
Type: Boolean
Required: No

 ** GlobalSecondaryIndexes **   <a name="securityhub-Type-AwsDynamoDbTableDetails-GlobalSecondaryIndexes"></a>
List of global secondary indexes for the table.
Type: Array of [AwsDynamoDbTableGlobalSecondaryIndex](API_AwsDynamoDbTableGlobalSecondaryIndex.md) objects
Required: No

 ** GlobalTableVersion **   <a name="securityhub-Type-AwsDynamoDbTableDetails-GlobalTableVersion"></a>
The version of global tables being used.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ItemCount **   <a name="securityhub-Type-AwsDynamoDbTableDetails-ItemCount"></a>
The number of items in the table.
Type: Integer
Required: No

 ** KeySchema **   <a name="securityhub-Type-AwsDynamoDbTableDetails-KeySchema"></a>
The primary key structure for the table.
Type: Array of [AwsDynamoDbTableKeySchema](API_AwsDynamoDbTableKeySchema.md) objects
Required: No

 ** LatestStreamArn **   <a name="securityhub-Type-AwsDynamoDbTableDetails-LatestStreamArn"></a>
The ARN of the latest stream for the table.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LatestStreamLabel **   <a name="securityhub-Type-AwsDynamoDbTableDetails-LatestStreamLabel"></a>
The label of the latest stream. The label is not a unique identifier.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LocalSecondaryIndexes **   <a name="securityhub-Type-AwsDynamoDbTableDetails-LocalSecondaryIndexes"></a>
The list of local secondary indexes for the table.
Type: Array of [AwsDynamoDbTableLocalSecondaryIndex](API_AwsDynamoDbTableLocalSecondaryIndex.md) objects
Required: No

 ** ProvisionedThroughput **   <a name="securityhub-Type-AwsDynamoDbTableDetails-ProvisionedThroughput"></a>
Information about the provisioned throughput for the table.
Type: [AwsDynamoDbTableProvisionedThroughput](API_AwsDynamoDbTableProvisionedThroughput.md) object
Required: No

 ** Replicas **   <a name="securityhub-Type-AwsDynamoDbTableDetails-Replicas"></a>
The list of replicas of this table.
Type: Array of [AwsDynamoDbTableReplica](API_AwsDynamoDbTableReplica.md) objects
Required: No

 ** RestoreSummary **   <a name="securityhub-Type-AwsDynamoDbTableDetails-RestoreSummary"></a>
Information about the restore for the table.
Type: [AwsDynamoDbTableRestoreSummary](API_AwsDynamoDbTableRestoreSummary.md) object
Required: No

 ** SseDescription **   <a name="securityhub-Type-AwsDynamoDbTableDetails-SseDescription"></a>
Information about the server-side encryption for the table.
Type: [AwsDynamoDbTableSseDescription](API_AwsDynamoDbTableSseDescription.md) object
Required: No

 ** StreamSpecification **   <a name="securityhub-Type-AwsDynamoDbTableDetails-StreamSpecification"></a>
The current DynamoDB Streams configuration for the table.
Type: [AwsDynamoDbTableStreamSpecification](API_AwsDynamoDbTableStreamSpecification.md) object
Required: No

 ** TableId **   <a name="securityhub-Type-AwsDynamoDbTableDetails-TableId"></a>
The identifier of the table.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TableName **   <a name="securityhub-Type-AwsDynamoDbTableDetails-TableName"></a>
The name of the table.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TableSizeBytes **   <a name="securityhub-Type-AwsDynamoDbTableDetails-TableSizeBytes"></a>
The total size of the table in bytes.
Type: Long
Required: No

 ** TableStatus **   <a name="securityhub-Type-AwsDynamoDbTableDetails-TableStatus"></a>
The current status of the table. Valid values are as follows:
+  `ACTIVE`
+  `ARCHIVED`
+  `ARCHIVING`
+  `CREATING`
+  `DELETING`
+  `INACCESSIBLE_ENCRYPTION_CREDENTIALS`
+  `UPDATING`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsDynamoDbTableDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDynamoDbTableDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDynamoDbTableDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDynamoDbTableDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
