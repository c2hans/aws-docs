---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_OutOfSyncReasonsView.html
---

# OutOfSyncReasonsView
<a name="API_OutOfSyncReasonsView"></a>

The out-of-sync reasons for a resource, or a marker indicating that the details are not visible. Exactly one member is set.

## Contents
<a name="API_OutOfSyncReasonsView_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** notVisible **   <a name="networksecuritymanager-Type-OutOfSyncReasonsView-notVisible"></a>
Indicates that the details are not visible because of cross-account restrictions.
Type: [NotVisibleMarker](API_NotVisibleMarker.md) object
Required: No

 ** reasons **   <a name="networksecuritymanager-Type-OutOfSyncReasonsView-reasons"></a>
The out-of-sync reasons, keyed by firewall type.
Type: String to [FirewallSyncReason](API_FirewallSyncReason.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Valid Keys: `WAF | SHIELD_ADVANCED`
Required: No

## See Also
<a name="API_OutOfSyncReasonsView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/OutOfSyncReasonsView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/OutOfSyncReasonsView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/OutOfSyncReasonsView)
