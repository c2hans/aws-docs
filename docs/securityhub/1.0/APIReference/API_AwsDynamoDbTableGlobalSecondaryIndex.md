---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDynamoDbTableGlobalSecondaryIndex.html
---

# AwsDynamoDbTableGlobalSecondaryIndex
<a name="API_AwsDynamoDbTableGlobalSecondaryIndex"></a>

Information abut a global secondary index for the table.

## Contents
<a name="API_AwsDynamoDbTableGlobalSecondaryIndex_Contents"></a>

 ** Backfilling **   <a name="securityhub-Type-AwsDynamoDbTableGlobalSecondaryIndex-Backfilling"></a>
Whether the index is currently backfilling.
Type: Boolean
Required: No

 ** IndexArn **   <a name="securityhub-Type-AwsDynamoDbTableGlobalSecondaryIndex-IndexArn"></a>
The ARN of the index.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IndexName **   <a name="securityhub-Type-AwsDynamoDbTableGlobalSecondaryIndex-IndexName"></a>
The name of the index.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IndexSizeBytes **   <a name="securityhub-Type-AwsDynamoDbTableGlobalSecondaryIndex-IndexSizeBytes"></a>
The total size in bytes of the index.
Type: Long
Required: No

 ** IndexStatus **   <a name="securityhub-Type-AwsDynamoDbTableGlobalSecondaryIndex-IndexStatus"></a>
The current status of the index.
+  `ACTIVE`
+  `CREATING`
+  `DELETING`
+  `UPDATING`
Type: String
Pattern: `.*\S.*`
Required: No

 ** ItemCount **   <a name="securityhub-Type-AwsDynamoDbTableGlobalSecondaryIndex-ItemCount"></a>
The number of items in the index.
Type: Integer
Required: No

 ** KeySchema **   <a name="securityhub-Type-AwsDynamoDbTableGlobalSecondaryIndex-KeySchema"></a>
The key schema for the index.
Type: Array of [AwsDynamoDbTableKeySchema](API_AwsDynamoDbTableKeySchema.md) objects
Required: No

 ** Projection **   <a name="securityhub-Type-AwsDynamoDbTableGlobalSecondaryIndex-Projection"></a>
Attributes that are copied from the table into an index.
Type: [AwsDynamoDbTableProjection](API_AwsDynamoDbTableProjection.md) object
Required: No

 ** ProvisionedThroughput **   <a name="securityhub-Type-AwsDynamoDbTableGlobalSecondaryIndex-ProvisionedThroughput"></a>
Information about the provisioned throughput settings for the indexes.
Type: [AwsDynamoDbTableProvisionedThroughput](API_AwsDynamoDbTableProvisionedThroughput.md) object
Required: No

## See Also
<a name="API_AwsDynamoDbTableGlobalSecondaryIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDynamoDbTableGlobalSecondaryIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDynamoDbTableGlobalSecondaryIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDynamoDbTableGlobalSecondaryIndex)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
