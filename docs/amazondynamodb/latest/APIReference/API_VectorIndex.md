---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_VectorIndex.html
---

# VectorIndex
<a name="API_VectorIndex"></a>

Contains the configuration settings for a vector index, including the index name, vector attribute, dimensions, distance function, search schema, and projection.

## Contents
<a name="API_VectorIndex_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Dimensions **   <a name="DDB-Type-VectorIndex-Dimensions"></a>
The number of dimensions in each vector.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** DistanceFunction **   <a name="DDB-Type-VectorIndex-DistanceFunction"></a>
The distance function used to calculate similarity between vectors. Valid values: `COSINE`, `EUCLIDEAN`, `DOT_PRODUCT`.
Type: String
Valid Values: `COSINE | DOT_PRODUCT | EUCLIDEAN`
Required: Yes

 ** IndexName **   <a name="DDB-Type-VectorIndex-IndexName"></a>
The name of the vector index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** Projection **   <a name="DDB-Type-VectorIndex-Projection"></a>
Specifies attributes that are copied (projected) from the table into the vector index.
Type: [Projection](API_Projection.md) object
Required: Yes

 ** VectorAttribute **   <a name="DDB-Type-VectorIndex-VectorAttribute"></a>
The vector attribute configuration for the index.
Type: [VectorAttributeDefinition](API_VectorAttributeDefinition.md) object
Required: Yes

 ** SearchSchema **   <a name="DDB-Type-VectorIndex-SearchSchema"></a>
The search schema that defines partition key and inline filter attributes for the vector index.
Type: Array of [SearchSchemaElement](API_SearchSchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_VectorIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/VectorIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/VectorIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/VectorIndex)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
