---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SearchSchemaElement.html
---

# SearchSchemaElement
<a name="API_SearchSchemaElement"></a>

An element in the search schema of a vector index.

## Contents
<a name="API_SearchSchemaElement_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AttributeName **   <a name="DDB-Type-SearchSchemaElement-AttributeName"></a>
The name of the attribute.
Type: String
Length Constraints: Maximum length of 65535.
Required: Yes

 ** SearchSchemaElementType **   <a name="DDB-Type-SearchSchemaElement-SearchSchemaElementType"></a>
The role of the attribute in the search schema. Valid values:
+  `HASH` - A partition key that partitions the vector index for independent scaling. When specified, you must provide this attribute's value in the `SearchConditionExpression`.
+  `INLINE_FILTER` - An attribute projected into the vector index for filtering at the storage layer during search. Inline filters are optional in the `SearchConditionExpression`.
Type: String
Valid Values: `HASH | INLINE_FILTER`
Required: Yes

## See Also
<a name="API_SearchSchemaElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/SearchSchemaElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/SearchSchemaElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/SearchSchemaElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
