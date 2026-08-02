---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ResourceNotFoundException.html
---

# ResourceNotFoundException
<a name="API_ResourceNotFoundException"></a>

The resource was not found.

HTTP Status Code returned: 404

## Contents
<a name="API_ResourceNotFoundException_Contents"></a>

 ** message **   <a name="ManagedBlockchainQueryAPIReference-Type-ResourceNotFoundException-message"></a>
The container for the exception message.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** resourceId **   <a name="ManagedBlockchainQueryAPIReference-Type-ResourceNotFoundException-resourceId"></a>
The `resourceId` of the resource that caused the exception.
Type: String
Required: Yes

 ** resourceType **   <a name="ManagedBlockchainQueryAPIReference-Type-ResourceNotFoundException-resourceType"></a>
The `resourceType` of the resource that caused the exception.
Type: String
Valid Values: `collection`
Required: Yes

## See Also
<a name="API_ResourceNotFoundException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/ResourceNotFoundException)
