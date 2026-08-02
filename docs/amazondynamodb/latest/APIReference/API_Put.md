---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Put.html
---

# Put
<a name="API_Put"></a>

Represents a request to perform a `PutItem` operation.

## Contents
<a name="API_Put_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Item **   <a name="DDB-Type-Put-Item"></a>
A map of attribute name to attribute values, representing the primary key of the item to be written by `PutItem`. All of the table's primary key attributes must be specified, and their data types must match those of the table's key schema. If any attributes are present in the item that are part of an index key schema for the table, their types must match the index key schema.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: Yes

 ** TableName **   <a name="DDB-Type-Put-TableName"></a>
Name of the table in which to write the item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ConditionExpression **   <a name="DDB-Type-Put-ConditionExpression"></a>
A condition that must be satisfied in order for a conditional update to succeed.
Type: String
Required: No

 ** ExpressionAttributeNames **   <a name="DDB-Type-Put-ExpressionAttributeNames"></a>
One or more substitution tokens for attribute names in an expression.
Type: String to string map
Value Length Constraints: Maximum length of 65535.
Required: No

 ** ExpressionAttributeValues **   <a name="DDB-Type-Put-ExpressionAttributeValues"></a>
One or more values that can be substituted in an expression.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Required: No

 ** ReturnValuesOnConditionCheckFailure **   <a name="DDB-Type-Put-ReturnValuesOnConditionCheckFailure"></a>
Use `ReturnValuesOnConditionCheckFailure` to get the item attributes if the `Put` condition fails. For `ReturnValuesOnConditionCheckFailure`, the valid values are: NONE and ALL\_OLD.
Type: String
Valid Values: `ALL_OLD | NONE`
Required: No

## See Also
<a name="API_Put_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/Put)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/Put)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/Put)
