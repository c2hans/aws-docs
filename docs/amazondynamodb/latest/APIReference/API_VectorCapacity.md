---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_VectorCapacity.html
---

# VectorCapacity
<a name="API_VectorCapacity"></a>

The consumed capacity for vector index operations, including vector search request bytes and vector write request bytes.

## Contents
<a name="API_VectorCapacity_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** VectorSearchRequestBytes **   <a name="DDB-Type-VectorCapacity-VectorSearchRequestBytes"></a>
The number of vector search request bytes consumed by a `SearchVectors` operation.
Type: Double
Required: No

 ** VectorWriteRequestBytes **   <a name="DDB-Type-VectorCapacity-VectorWriteRequestBytes"></a>
The number of vector write request bytes consumed when writing to a vector index. Reported for write operations that modify attributes indexed by a vector index.
Type: Double
Required: No

## See Also
<a name="API_VectorCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/VectorCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/VectorCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/VectorCapacity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
