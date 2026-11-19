---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ContextStoreSyncState.html
---

# ContextStoreSyncState

The synchronization state of a firewall's context sets with its context store. This indicates whether the resource identifiers in the firewall's context sets resolve to resources that the context store records.

## Contents
<a name="API_ContextStoreSyncState_Contents"></a>

 ** StatusMessage **   <a name="networkfirewall-Type-ContextStoreSyncState-StatusMessage"></a>
A message that provides additional information about the synchronization status, particularly when the status is not `FULLY_RESOLVED`.
Type: String
Required: No

 ** SyncStatus **   <a name="networkfirewall-Type-ContextStoreSyncState-SyncStatus"></a>
The synchronization status of the firewall's context sets. Valid values:
+  `SYNCING` - The firewall is applying the latest context store data.
+  `FULLY_RESOLVED` - All resource identifiers in the firewall's context sets resolve to resources in the context store.
+  `PARTIALLY_RESOLVED` - Some resource identifiers in the firewall's context sets don't resolve to resources in the context store.
+  `SYNC_FAILED` - The firewall couldn't sync with the context store. For details, see `StatusMessage`.
Type: String
Valid Values: `SYNCING | PARTIALLY_RESOLVED | FULLY_RESOLVED | SYNC_FAILED | UNRESOLVED`
Required: No

## See Also
<a name="API_ContextStoreSyncState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ContextStoreSyncState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ContextStoreSyncState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ContextStoreSyncState)
