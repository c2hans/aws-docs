---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Update.html
---

# Update
<a name="API_Update"></a>

Represents a request to perform an `UpdateItem` operation.

## Contents
<a name="API_Update_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="DDB-Type-Update-Key"></a>
The primary key of the item to be updated. Each element consists of an attribute name and a value for that attribute.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: Yes

 ** TableName **   <a name="DDB-Type-Update-TableName"></a>
Name of the table for the `UpdateItem` request. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** UpdateExpression **   <a name="DDB-Type-Update-UpdateExpression"></a>
An expression that defines one or more attributes to be updated, the action to be performed on them, and new value(s) for them.
Type: String
Required: Yes

 ** ConditionExpression **   <a name="DDB-Type-Update-ConditionExpression"></a>
A condition that must be satisfied in order for a conditional update to succeed.
Type: String
Required: No

 ** ExpressionAttributeNames **   <a name="DDB-Type-Update-ExpressionAttributeNames"></a>
One or more substitution tokens for attribute names in an expression.
Type: String to string map
Value Length Constraints: Maximum length of 65535.
Required: No

 ** ExpressionAttributeValues **   <a name="DDB-Type-Update-ExpressionAttributeValues"></a>
One or more values that can be substituted in an expression.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Required: No

 ** ReturnValuesOnConditionCheckFailure **   <a name="DDB-Type-Update-ReturnValuesOnConditionCheckFailure"></a>
Use `ReturnValuesOnConditionCheckFailure` to get the item attributes if the `Update` condition fails. For `ReturnValuesOnConditionCheckFailure`, the valid values are: NONE and ALL\_OLD.
Type: String
Valid Values: `ALL_OLD | NONE`
Required: No

## See Also
<a name="API_Update_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/Update)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/Update)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/Update)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
