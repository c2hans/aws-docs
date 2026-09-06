---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchStatementError.html
---

# BatchStatementError
<a name="API_BatchStatementError"></a>

 An error associated with a statement in a PartiQL batch that was run.

## Contents
<a name="API_BatchStatementError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Code **   <a name="DDB-Type-BatchStatementError-Code"></a>
 The error code associated with the failed PartiQL batch statement.
Type: String
Valid Values: `ConditionalCheckFailed | ItemCollectionSizeLimitExceeded | RequestLimitExceeded | ValidationError | ProvisionedThroughputExceeded | TransactionConflict | ThrottlingError | InternalServerError | ResourceNotFound | AccessDenied | DuplicateItem`
Required: No

 ** Item **   <a name="DDB-Type-BatchStatementError-Item"></a>
The item which caused the condition check to fail. This will be set if ReturnValuesOnConditionCheckFailure is specified as `ALL_OLD`.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: No

 ** Message **   <a name="DDB-Type-BatchStatementError-Message"></a>
 The error message associated with the PartiQL batch response.
Type: String
Required: No

## See Also
<a name="API_BatchStatementError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/BatchStatementError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/BatchStatementError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/BatchStatementError)
