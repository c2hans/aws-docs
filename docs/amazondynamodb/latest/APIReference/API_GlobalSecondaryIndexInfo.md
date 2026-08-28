---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalSecondaryIndexInfo.html
---

# GlobalSecondaryIndexInfo
<a name="API_GlobalSecondaryIndexInfo"></a>

Represents the properties of a global secondary index for the table when the backup was created.

## Contents
<a name="API_GlobalSecondaryIndexInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IndexName **   <a name="DDB-Type-GlobalSecondaryIndexInfo-IndexName"></a>
The name of the global secondary index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** KeySchema **   <a name="DDB-Type-GlobalSecondaryIndexInfo-KeySchema"></a>
The complete key schema for a global secondary index, which consists of one or more pairs of attribute names and key types:
+  `HASH` - partition key
+  `RANGE` - sort key
The partition key of an item is also known as its *hash attribute*. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.
The sort key of an item is also known as its *range attribute*. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.
Type: Array of [KeySchemaElement](API_KeySchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** OnDemandThroughput **   <a name="DDB-Type-GlobalSecondaryIndexInfo-OnDemandThroughput"></a>
Sets the maximum number of read and write units for the specified on-demand table. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.
Type: [OnDemandThroughput](API_OnDemandThroughput.md) object
Required: No

 ** Projection **   <a name="DDB-Type-GlobalSecondaryIndexInfo-Projection"></a>
Represents attributes that are copied (projected) from the table into the global secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.
Type: [Projection](API_Projection.md) object
Required: No

 ** ProvisionedThroughput **   <a name="DDB-Type-GlobalSecondaryIndexInfo-ProvisionedThroughput"></a>
Represents the provisioned throughput settings for the specified global secondary index.
Type: [ProvisionedThroughput](API_ProvisionedThroughput.md) object
Required: No

## See Also
<a name="API_GlobalSecondaryIndexInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/GlobalSecondaryIndexInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/GlobalSecondaryIndexInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/GlobalSecondaryIndexInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
