---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ValidationException.html
---

# ValidationException
<a name="API_ValidationException"></a>

The resource passed is invalid.

HTTP Status Code returned: 400

## Contents
<a name="API_ValidationException_Contents"></a>

 ** message **   <a name="ManagedBlockchainQueryAPIReference-Type-ValidationException-message"></a>
The container for the exception message.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** reason **   <a name="ManagedBlockchainQueryAPIReference-Type-ValidationException-reason"></a>
The container for the reason for the exception
Type: String
Valid Values: `unknownOperation | cannotParse | fieldValidationFailed | other`
Required: Yes

 ** fieldList **   <a name="ManagedBlockchainQueryAPIReference-Type-ValidationException-fieldList"></a>
The container for the `fieldList` of the exception.
Type: Array of [ValidationExceptionField](API_ValidationExceptionField.md) objects
Required: No

## See Also
<a name="API_ValidationException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/ValidationException)
