---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AttributeValue.html
---

# AttributeValue
<a name="API_AttributeValue"></a>

Represents the data for an attribute.

Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.

For more information, see [Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes) in the *Amazon DynamoDB Developer Guide*.

## Contents
<a name="API_AttributeValue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** B **   <a name="DDB-Type-AttributeValue-B"></a>
An attribute of type Binary. For example:
 `"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"`
Type: Base64-encoded binary data object
Required: No

 ** BOOL **   <a name="DDB-Type-AttributeValue-BOOL"></a>
An attribute of type Boolean. For example:
 `"BOOL": true`
Type: Boolean
Required: No

 ** BS **   <a name="DDB-Type-AttributeValue-BS"></a>
An attribute of type Binary Set. For example:
 `"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]`
Type: Array of Base64-encoded binary data objects
Required: No

 ** L **   <a name="DDB-Type-AttributeValue-L"></a>
An attribute of type List. For example:
 `"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N": "3.14159"}]`
Type: Array of [AttributeValue](#API_AttributeValue) objects
Required: No

 ** M **   <a name="DDB-Type-AttributeValue-M"></a>
An attribute of type Map. For example:
 `"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}`
Type: String to [AttributeValue](#API_AttributeValue) object map
Key Length Constraints: Maximum length of 65535.
Required: No

 ** N **   <a name="DDB-Type-AttributeValue-N"></a>
An attribute of type Number. For example:
 `"N": "123.45"`
Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
Type: String
Required: No

 ** NS **   <a name="DDB-Type-AttributeValue-NS"></a>
An attribute of type Number Set. For example:
 `"NS": ["42.2", "-19", "7.5", "3.14"]`
Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
Type: Array of strings
Required: No

 ** NULL **   <a name="DDB-Type-AttributeValue-NULL"></a>
An attribute of type Null. For example:
 `"NULL": true`
Type: Boolean
Required: No

 ** S **   <a name="DDB-Type-AttributeValue-S"></a>
An attribute of type String. For example:
 `"S": "Hello"`
Type: String
Required: No

 ** SS **   <a name="DDB-Type-AttributeValue-SS"></a>
An attribute of type String Set. For example:
 `"SS": ["Giraffe", "Hippo" ,"Zebra"]`
Type: Array of strings
Required: No

## See Also
<a name="API_AttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/AttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/AttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/AttributeValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
