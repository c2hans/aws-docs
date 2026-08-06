---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateVectorIndexAction.html
---

# CreateVectorIndexAction
<a name="API_CreateVectorIndexAction"></a>

A new vector index to be added to a table.

## Contents
<a name="API_CreateVectorIndexAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Dimensions **   <a name="DDB-Type-CreateVectorIndexAction-Dimensions"></a>
The number of dimensions in each vector.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** DistanceFunction **   <a name="DDB-Type-CreateVectorIndexAction-DistanceFunction"></a>
The distance function used to calculate similarity. Valid values: `COSINE`, `EUCLIDEAN`, `DOT_PRODUCT`.
Type: String
Valid Values: `COSINE | DOT_PRODUCT | EUCLIDEAN`
Required: Yes

 ** IndexName **   <a name="DDB-Type-CreateVectorIndexAction-IndexName"></a>
The name of the vector index. Must be unique within the table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** Projection **   <a name="DDB-Type-CreateVectorIndexAction-Projection"></a>
Specifies attributes that are copied (projected) from the table into the vector index.
Type: [Projection](API_Projection.md) object
Required: Yes

 ** VectorAttribute **   <a name="DDB-Type-CreateVectorIndexAction-VectorAttribute"></a>
The attribute that contains vector embeddings. If multiple vector indexes reference the same attribute, they must all use the same number of dimensions.
Type: [VectorAttributeDefinition](API_VectorAttributeDefinition.md) object
Required: Yes

 ** SearchSchema **   <a name="DDB-Type-CreateVectorIndexAction-SearchSchema"></a>
The partition key and inline filter attribute definitions for the vector index.
Type: Array of [SearchSchemaElement](API_SearchSchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_CreateVectorIndexAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/CreateVectorIndexAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/CreateVectorIndexAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/CreateVectorIndexAction)
