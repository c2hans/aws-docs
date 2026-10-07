---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_FilterSpecification.html
---

# FilterSpecification
<a name="API_FilterSpecification"></a>

Contains the filter criteria used to limit which items are included in an export. If you don't include this parameter, all items and attributes are exported.

## Contents
<a name="API_FilterSpecification_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ExpressionAttributeNames **   <a name="DDB-Type-FilterSpecification-ExpressionAttributeNames"></a>
One or more substitution tokens for attribute names in an expression. For more information, see [Expression Attribute Names](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeNames.html) in the Amazon DynamoDB Developer Guide.
Type: String to string map
Value Length Constraints: Maximum length of 65535.
Required: No

 ** ExpressionAttributeValues **   <a name="DDB-Type-FilterSpecification-ExpressionAttributeValues"></a>
One or more values that can be substituted in an expression. For more information, see [Expression Attribute Values](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeValues.html) in the Amazon DynamoDB Developer Guide.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Required: No

 ** FilterExpression **   <a name="DDB-Type-FilterSpecification-FilterExpression"></a>
A condition that filters which items are included in the export. This parameter uses the same syntax as `FilterExpression` in `Query` and `Scan`. If you don't provide `KeyConditionExpression`, this expression can also reference key attributes. If you don't specify this parameter, all items are included in the export.
Type: String
Required: No

 ** KeyConditionExpression **   <a name="DDB-Type-FilterSpecification-KeyConditionExpression"></a>
A condition expression that filters items by key values. The expression must test equality on a single partition key value and can optionally compare a sort key value. This parameter uses the same syntax as `KeyConditionExpression` in `Query`. When you provide this parameter, `FilterExpression` can only reference non-key attributes. If you don't specify this parameter, all items are eligible for export.
Type: String
Required: No

 ** ProjectionExpression **   <a name="DDB-Type-FilterSpecification-ProjectionExpression"></a>
The attributes you want to retrieve for items included in the export. Separate attribute names in the expression with commas. If you don't specify this parameter, all attributes are returned.
Type: String
Required: No

## See Also
<a name="API_FilterSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/FilterSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/FilterSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/FilterSpecification)
