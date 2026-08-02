---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ServiceQuotaExceededException.html
---

# ServiceQuotaExceededException
<a name="API_ServiceQuotaExceededException"></a>

The service quota has been exceeded for this resource.

HTTP Status Code returned: 402

## Contents
<a name="API_ServiceQuotaExceededException_Contents"></a>

 ** message **   <a name="ManagedBlockchainQueryAPIReference-Type-ServiceQuotaExceededException-message"></a>
The container for the exception message.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** quotaCode **   <a name="ManagedBlockchainQueryAPIReference-Type-ServiceQuotaExceededException-quotaCode"></a>
The container for the `quotaCode`.
Type: String
Required: Yes

 ** resourceId **   <a name="ManagedBlockchainQueryAPIReference-Type-ServiceQuotaExceededException-resourceId"></a>
The `resourceId` of the resource that caused the exception.
Type: String
Required: Yes

 ** resourceType **   <a name="ManagedBlockchainQueryAPIReference-Type-ServiceQuotaExceededException-resourceType"></a>
The `resourceType` of the resource that caused the exception.
Type: String
Valid Values: `collection`
Required: Yes

 ** serviceCode **   <a name="ManagedBlockchainQueryAPIReference-Type-ServiceQuotaExceededException-serviceCode"></a>
The container for the `serviceCode`.
Type: String
Required: Yes

## See Also
<a name="API_ServiceQuotaExceededException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/ServiceQuotaExceededException)
