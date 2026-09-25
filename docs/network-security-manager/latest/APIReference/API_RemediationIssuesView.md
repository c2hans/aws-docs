---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_RemediationIssuesView.html
---

# RemediationIssuesView
<a name="API_RemediationIssuesView"></a>

Remediation issue details for a resource, or a marker indicating that the details are not visible. Exactly one member is set.

## Contents
<a name="API_RemediationIssuesView_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** issues **   <a name="networksecuritymanager-Type-RemediationIssuesView-issues"></a>
The remediation issues, keyed by firewall type.
Type: String to [RemediationIssueDetails](API_RemediationIssueDetails.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Valid Keys: `WAF | SHIELD_ADVANCED`
Required: No

 ** notVisible **   <a name="networksecuritymanager-Type-RemediationIssuesView-notVisible"></a>
Indicates that the details are not visible because of cross-account restrictions.
Type: [NotVisibleMarker](API_NotVisibleMarker.md) object
Required: No

## See Also
<a name="API_RemediationIssuesView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/RemediationIssuesView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/RemediationIssuesView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/RemediationIssuesView)
