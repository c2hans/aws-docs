---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_VectorIndexDescription.html
---

# VectorIndexDescription
<a name="API_VectorIndexDescription"></a>

Contains the current state and configuration of a vector index, including its status, size, item count, and the settings specified when the index was created.

## Contents
<a name="API_VectorIndexDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Backfilling **   <a name="DDB-Type-VectorIndexDescription-Backfilling"></a>
Specifies whether the index is currently backfilling. `SearchVectors` returns a `ValidationException` while the index is backfilling; it does not return partial results. This field is reported for an index added with `UpdateTable`, and is absent for an index created as part of `CreateTable`. Wait until this field is not `true` before you search.
Type: Boolean
Required: No

 ** Dimensions **   <a name="DDB-Type-VectorIndexDescription-Dimensions"></a>
The number of dimensions in each vector.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** DistanceFunction **   <a name="DDB-Type-VectorIndexDescription-DistanceFunction"></a>
The distance function used to calculate similarity between vectors.
Type: String
Valid Values: `COSINE | DOT_PRODUCT | EUCLIDEAN`
Required: No

 ** IndexArn **   <a name="DDB-Type-VectorIndexDescription-IndexArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the vector index.
Type: String
Required: No

 ** IndexName **   <a name="DDB-Type-VectorIndexDescription-IndexName"></a>
The name of the vector index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** IndexSizeBytes **   <a name="DDB-Type-VectorIndexDescription-IndexSizeBytes"></a>
The total size of the vector index, in bytes. Amazon DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
Type: Long
Required: No

 ** IndexStatus **   <a name="DDB-Type-VectorIndexDescription-IndexStatus"></a>
The current state of the vector index:
+  `CREATING` - The index is being created. This state covers both provisioning the index and backfilling existing base table data. Check the `Backfilling` field to distinguish the two.
+  `UPDATING` - The index is being updated.
+  `ACTIVE` - The index is ready for use.
+  `DELETING` - The index is being deleted.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE`
Required: No

 ** ItemCount **   <a name="DDB-Type-VectorIndexDescription-ItemCount"></a>
The number of items indexed in the vector index. Amazon DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.
Type: Long
Required: No

 ** Projection **   <a name="DDB-Type-VectorIndexDescription-Projection"></a>
Specifies attributes that are copied (projected) from the table into the vector index.
Type: [Projection](API_Projection.md) object
Required: No

 ** SearchSchema **   <a name="DDB-Type-VectorIndexDescription-SearchSchema"></a>
The search schema that defines partition key and inline filter attributes for the vector index.
Type: Array of [SearchSchemaElement](API_SearchSchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** VectorAttribute **   <a name="DDB-Type-VectorIndexDescription-VectorAttribute"></a>
The vector attribute configuration for the index.
Type: [VectorAttributeDefinition](API_VectorAttributeDefinition.md) object
Required: No

## See Also
<a name="API_VectorIndexDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/VectorIndexDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/VectorIndexDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/VectorIndexDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
