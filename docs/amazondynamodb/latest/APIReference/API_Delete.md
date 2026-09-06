---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Delete.html
---

# Delete
<a name="API_Delete"></a>

Represents a request to perform a `DeleteItem` operation.

## Contents
<a name="API_Delete_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="DDB-Type-Delete-Key"></a>
The primary key of the item to be deleted. Each element consists of an attribute name and a value for that attribute.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: Yes

 ** TableName **   <a name="DDB-Type-Delete-TableName"></a>
Name of the table in which the item to be deleted resides. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ConditionExpression **   <a name="DDB-Type-Delete-ConditionExpression"></a>
A condition that must be satisfied in order for a conditional delete to succeed.
Type: String
Required: No

 ** ExpressionAttributeNames **   <a name="DDB-Type-Delete-ExpressionAttributeNames"></a>
One or more substitution tokens for attribute names in an expression.
Type: String to string map
Value Length Constraints: Maximum length of 65535.
Required: No

 ** ExpressionAttributeValues **   <a name="DDB-Type-Delete-ExpressionAttributeValues"></a>
One or more values that can be substituted in an expression.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Required: No

 ** ReturnValuesOnConditionCheckFailure **   <a name="DDB-Type-Delete-ReturnValuesOnConditionCheckFailure"></a>
Use `ReturnValuesOnConditionCheckFailure` to get the item attributes if the `Delete` condition fails. For `ReturnValuesOnConditionCheckFailure`, the valid values are: NONE and ALL\_OLD.
Type: String
Valid Values: `ALL_OLD | NONE`
Required: No

## See Also
<a name="API_Delete_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/Delete)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/Delete)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/Delete)
