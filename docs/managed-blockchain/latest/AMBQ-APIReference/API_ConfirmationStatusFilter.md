---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ConfirmationStatusFilter.html
---

# ConfirmationStatusFilter
<a name="API_ConfirmationStatusFilter"></a>

The container for the `ConfirmationStatusFilter` that filters for the [*finality*](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality) of the results.

## Contents
<a name="API_ConfirmationStatusFilter_Contents"></a>

 ** include **   <a name="ManagedBlockchainQueryAPIReference-Type-ConfirmationStatusFilter-include"></a>
The container to determine whether to list results that have only reached [*finality*](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality). Transactions that have reached finality are always part of the response.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `FINAL | NONFINAL`
Required: Yes

## See Also
<a name="API_ConfirmationStatusFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/ConfirmationStatusFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/ConfirmationStatusFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/ConfirmationStatusFilter)
