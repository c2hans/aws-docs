---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchStatementRequest.html
---

# BatchStatementRequest
<a name="API_BatchStatementRequest"></a>

 A PartiQL batch statement request.

## Contents
<a name="API_BatchStatementRequest_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Statement **   <a name="DDB-Type-BatchStatementRequest-Statement"></a>
 A valid PartiQL statement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** ConsistentRead **   <a name="DDB-Type-BatchStatementRequest-ConsistentRead"></a>
 The read consistency of the PartiQL batch request.
Type: Boolean
Required: No

 ** Parameters **   <a name="DDB-Type-BatchStatementRequest-Parameters"></a>
 The parameters associated with a PartiQL statement in the batch request.
Type: Array of [AttributeValue](API_AttributeValue.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** ReturnValuesOnConditionCheckFailure **   <a name="DDB-Type-BatchStatementRequest-ReturnValuesOnConditionCheckFailure"></a>
An optional parameter that returns the item attributes for a PartiQL batch request operation that failed a condition check.
There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.
Type: String
Valid Values: `ALL_OLD | NONE`
Required: No

## See Also
<a name="API_BatchStatementRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/BatchStatementRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/BatchStatementRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/BatchStatementRequest)
