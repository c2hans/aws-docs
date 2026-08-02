---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Get.html
---

# Get
<a name="API_Get"></a>

Specifies an item and related attribute values to retrieve in a `TransactGetItem` object.

## Contents
<a name="API_Get_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="DDB-Type-Get-Key"></a>
A map of attribute names to `AttributeValue` objects that specifies the primary key of the item to retrieve.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: Yes

 ** TableName **   <a name="DDB-Type-Get-TableName"></a>
The name of the table from which to retrieve the specified item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ExpressionAttributeNames **   <a name="DDB-Type-Get-ExpressionAttributeNames"></a>
One or more substitution tokens for attribute names in the ProjectionExpression parameter.
Type: String to string map
Value Length Constraints: Maximum length of 65535.
Required: No

 ** ProjectionExpression **   <a name="DDB-Type-Get-ProjectionExpression"></a>
A string that identifies one or more attributes of the specified item to retrieve from the table. The attributes in the expression must be separated by commas. If no attribute names are specified, then all attributes of the specified item are returned. If any of the requested attributes are not found, they do not appear in the result.
Type: String
Required: No

## See Also
<a name="API_Get_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/Get)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/Get)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/Get)
