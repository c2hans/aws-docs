---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListFilteredTransactionEventsSort.html
---

# ListFilteredTransactionEventsSort
<a name="API_ListFilteredTransactionEventsSort"></a>

Lists all the transaction events for an address on the blockchain.

**Note**
This operation is only supported on the Bitcoin blockchain networks.

## Contents
<a name="API_ListFilteredTransactionEventsSort_Contents"></a>

 ** sortBy **   <a name="ManagedBlockchainQueryAPIReference-Type-ListFilteredTransactionEventsSort-sortBy"></a>
The container for determining how the results will be sorted.
Type: String
Valid Values: `blockchainInstant`
Required: No

 ** sortOrder **   <a name="ManagedBlockchainQueryAPIReference-Type-ListFilteredTransactionEventsSort-sortOrder"></a>
The container for the *sort order* for `ListFilteredTransactionEvents`. The `SortOrder` field only accepts the values `ASCENDING` and `DESCENDING`. Not providing `SortOrder` will default to `ASCENDING`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## See Also
<a name="API_ListFilteredTransactionEventsSort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-query-2023-05-04/ListFilteredTransactionEventsSort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-query-2023-05-04/ListFilteredTransactionEventsSort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-query-2023-05-04/ListFilteredTransactionEventsSort)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
