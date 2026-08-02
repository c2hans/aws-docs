---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ThrottlingException.html
---

# ThrottlingException
<a name="API_ThrottlingException"></a>

The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is when you create resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources, if possible.

HTTP Status Code returned: 429

## Contents
<a name="API_ThrottlingException_Contents"></a>

 ** message **   <a name="ManagedBlockchainQueryAPIReference-Type-ThrottlingException-message"></a>
The container for the exception message.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** quotaCode **   <a name="ManagedBlockchainQueryAPIReference-Type-ThrottlingException-quotaCode"></a>
The container for the `quotaCode`.
Type: String
Required: Yes

 ** serviceCode **   <a name="ManagedBlockchainQueryAPIReference-Type-ThrottlingException-serviceCode"></a>
The container for the `serviceCode`.
Type: String
Required: Yes

 ** Retry-After **   <a name="ManagedBlockchainQueryAPIReference-Type-ThrottlingException-retryAfterSeconds"></a>
The container of the `retryAfterSeconds` value.
Type: Integer
Required: No

## See Also
<a name="API_ThrottlingException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/ThrottlingException)
