---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ParameterizedStatement.html
---

# ParameterizedStatement
<a name="API_ParameterizedStatement"></a>

 Represents a PartiQL statement that uses parameters.

## Contents
<a name="API_ParameterizedStatement_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Statement **   <a name="DDB-Type-ParameterizedStatement-Statement"></a>
 A PartiQL statement that uses parameters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** Parameters **   <a name="DDB-Type-ParameterizedStatement-Parameters"></a>
 The parameter values.
Type: Array of [AttributeValue](API_AttributeValue.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** ReturnValuesOnConditionCheckFailure **   <a name="DDB-Type-ParameterizedStatement-ReturnValuesOnConditionCheckFailure"></a>
An optional parameter that returns the item attributes for a PartiQL `ParameterizedStatement` operation that failed a condition check.
There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.
Type: String
Valid Values: `ALL_OLD | NONE`
Required: No

## See Also
<a name="API_ParameterizedStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ParameterizedStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ParameterizedStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ParameterizedStatement)
