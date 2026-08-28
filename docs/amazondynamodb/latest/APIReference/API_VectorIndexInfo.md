---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_VectorIndexInfo.html
---

# VectorIndexInfo
<a name="API_VectorIndexInfo"></a>

Contains the configuration of a vector index as it existed at the time a backup was created.

## Contents
<a name="API_VectorIndexInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Dimensions **   <a name="DDB-Type-VectorIndexInfo-Dimensions"></a>
The number of dimensions in each vector.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** DistanceFunction **   <a name="DDB-Type-VectorIndexInfo-DistanceFunction"></a>
The distance function used to calculate similarity between vectors.
Type: String
Valid Values: `COSINE | DOT_PRODUCT | EUCLIDEAN`
Required: No

 ** IndexName **   <a name="DDB-Type-VectorIndexInfo-IndexName"></a>
The name of the vector index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** Projection **   <a name="DDB-Type-VectorIndexInfo-Projection"></a>
Specifies attributes that are copied (projected) from the table into the vector index.
Type: [Projection](API_Projection.md) object
Required: No

 ** SearchSchema **   <a name="DDB-Type-VectorIndexInfo-SearchSchema"></a>
The search schema that defines partition key and inline filter attributes for the vector index.
Type: Array of [SearchSchemaElement](API_SearchSchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** VectorAttribute **   <a name="DDB-Type-VectorIndexInfo-VectorAttribute"></a>
The vector attribute configuration for the index.
Type: [VectorAttributeDefinition](API_VectorAttributeDefinition.md) object
Required: No

## See Also
<a name="API_VectorIndexInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/VectorIndexInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/VectorIndexInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/VectorIndexInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
