---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SearchResultItem.html
---

# SearchResultItem
<a name="API_SearchResultItem"></a>

A single result from a `SearchVectors` operation.

## Contents
<a name="API_SearchResultItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Item **   <a name="DDB-Type-SearchResultItem-Item"></a>
A map of attribute names to `AttributeValue` objects, representing the projected attributes of the item returned by the vector search.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: No

 ** Score **   <a name="DDB-Type-SearchResultItem-Score"></a>
The similarity score for this item relative to the search vector. The interpretation depends on the distance function configured for the vector index.
Type: Double
Required: No

## See Also
<a name="API_SearchResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/SearchResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/SearchResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/SearchResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
