---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationUsage.html
---

# BulkOperationUsage
<a name="API_BulkOperationUsage"></a>

Contains the bytes used during a bulk operation, including a breakdown for the table and its indexes.

## Contents
<a name="API_BulkOperationUsage_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BulkPutBytes **   <a name="DDB-Type-BulkOperationUsage-BulkPutBytes"></a>
The total number of bulk put bytes used by the operation. This value excludes bulk put vector bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** GlobalSecondaryIndexes **   <a name="DDB-Type-BulkOperationUsage-GlobalSecondaryIndexes"></a>
The bulk put bytes used on each global secondary index affected by the operation, keyed by index name.
Type: String to [BulkOperationBytes](API_BulkOperationBytes.md) object map
Key Length Constraints: Minimum length of 3. Maximum length of 255.
Key Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** LocalSecondaryIndexes **   <a name="DDB-Type-BulkOperationUsage-LocalSecondaryIndexes"></a>
The bulk put bytes used on each local secondary index affected by the operation, keyed by index name.
Type: String to [BulkOperationBytes](API_BulkOperationBytes.md) object map
Key Length Constraints: Minimum length of 3. Maximum length of 255.
Key Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** Table **   <a name="DDB-Type-BulkOperationUsage-Table"></a>
The number of bulk put bytes for the table, excluding its indexes.
Type: [BulkOperationBytes](API_BulkOperationBytes.md) object
Required: No

 ** TableName **   <a name="DDB-Type-BulkOperationUsage-TableName"></a>
The name or ARN of the table associated with the reported usage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** VectorIndexes **   <a name="DDB-Type-BulkOperationUsage-VectorIndexes"></a>
The bulk put vector bytes used on each vector index affected by the operation, keyed by index name.
Type: String to [BulkOperationVectorBytes](API_BulkOperationVectorBytes.md) object map
Key Length Constraints: Minimum length of 3. Maximum length of 255.
Key Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_BulkOperationUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/BulkOperationUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/BulkOperationUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/BulkOperationUsage)
